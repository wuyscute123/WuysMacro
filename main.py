"""
Macro hỗ trợ Blade Ball Roblox với Config JSON
Tác giả: Wuys
Phiên bản: 2.0 - Hỗ trợ cấu hình và setup
"""

import sys
import ctypes
import time
import random
import threading
import platform
import json
import os
from datetime import datetime
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import pyautogui

# ==============================================
# ĐƯỜNG DẪN VÀ BIẾN TOÀN CỤC
# ==============================================

CONFIG_FILE = "bladeball_config.json"
DEFAULT_CONFIG = {
    "spam_key": "x1",  # Mouse 4 mặc định
    "curve_key": "x2",  # Mouse 5 mặc định
    "spam_cps": 20,     # CPS cho cả 3 phím
    "curve_delay": 0.05,# Delay curve
    "curve_distance": 50,# Khoảng cách curve
    "setup_completed": False  # Đã setup chưa
}

# Controller cho chuột và bàn phím
mouse_controller = MouseController()
keyboard_controller = KeyboardController()

# Biến điều khiển
spam_active = False
spam_thread = None
config = DEFAULT_CONFIG.copy()
current_setup_step = None
selected_key = None

# Mapping phím
KEY_MAPPING = {
    "x1": Button.x1,  # Mouse 4
    "x2": Button.x2,  # Mouse 5
    "mouse_left": Button.left,
    "mouse_right": Button.right,
    "mouse_middle": Button.middle,
    "f1": Key.f1, "f2": Key.f2, "f3": Key.f3, "f4": Key.f4,
    "f5": Key.f5, "f6": Key.f6, "f7": Key.f7, "f8": Key.f8,
    "f9": Key.f9, "f10": Key.f10, "f11": Key.f11, "f12": Key.f12,
    "space": Key.space,
    "ctrl": Key.ctrl, "alt": Key.alt, "shift": Key.shift,
    "tab": Key.tab, "caps_lock": Key.caps_lock,
    "k": 'k', "l": 'l', "j": 'j', "h": 'h',  # Các phím chữ cái
    "q": 'q', "w": 'w', "e": 'e', "r": 'r',
    "a": 'a', "s": 's', "d": 'd', "f": 'f', "g": 'g',
    "z": 'z', "x": 'x', "c": 'c', "v": 'v', "b": 'b',
}

# ==============================================
# KIỂM TRA WINDOWS VERSION
# ==============================================

def check_windows_version():
    """Kiểm tra phiên bản Windows, chỉ hỗ trợ Windows 10/11"""
    
    if sys.platform != "win32":
        print("❌ Lỗi: Chương trình chỉ hỗ trợ Windows")
        input("Nhấn Enter để thoát...")
        return False
    
    win_version = platform.version()
    
    try:
        major_version = int(win_version.split('.')[0])
        
        if major_version < 10:
            print("=" * 60)
            print("❌ KHÔNG HỖ TRỢ HỆ ĐIỀU HÀNH")
            print("=" * 60)
            print(f"Phiên bản Windows hiện tại: Windows {major_version}")
            print("Chương trình chỉ hỗ trợ Windows 10 và Windows 11")
            print("\nVui lòng nâng cấp lên Windows 10/11 để sử dụng.")
            print("=" * 60)
            input("Nhấn Enter để thoát...")
            return False
            
        build_number = int(win_version.split('.')[2]) if len(win_version.split('.')) > 2 else 0
        
        if major_version == 10:
            if build_number >= 22000:
                print(f"✅ Windows 11 (Build {build_number})")
            elif build_number >= 10240:
                print(f"✅ Windows 10 (Build {build_number})")
            else:
                print(f"⚠ Windows 10 bản cũ (Build {build_number})")
        return True
                
    except (ValueError, IndexError):
        print(f"⚠ Không thể xác định phiên bản Windows")
        return True
    
    return True

# ==============================================
# QUẢN LÝ CONFIG JSON
# ==============================================

def load_config():
    """Tải cấu hình từ file JSON"""
    global config
    
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                loaded_config = json.load(f)
                config.update(loaded_config)
            print(f"✅ Đã tải cấu hình từ {CONFIG_FILE}")
            return True
        except Exception as e:
            print(f"⚠ Không thể đọc config: {e}")
            print("Sử dụng cấu hình mặc định...")
    else:
        print("⚠ Không tìm thấy file config, sử dụng mặc định")
    
    return False

def save_config():
    """Lưu cấu hình vào file JSON"""
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        print(f"✅ Đã lưu cấu hình vào {CONFIG_FILE}")
        return True
    except Exception as e:
        print(f"❌ Lỗi khi lưu config: {e}")
        return False

# ==============================================
# SETUP WIZARD - THIẾT LẬP PHÍM
# ==============================================

def display_setup_menu():
    """Hiển thị menu setup"""
    print("=" * 60)
    print("         THIẾT LẬP MACRO BLADE BALL")
    print("=" * 60)
    print("Các bước setup:")
    print("1. Thiết lập phím kích hoạt SPAM macro")
    print("2. Thiết lập phím kích hoạt CURVE")
    print("3. Thiết lập CPS cho SPAM macro")
    print("4. Xác nhận và lưu cấu hình")
    print()
    print("📝 Hướng dẫn:")
    print("- Nhấn phím bạn muốn sử dụng")
    print("- Phím R: Nhập lại phím hiện tại")
    print("- Phím ESC: Hủy setup, sử dụng mặc định")
    print("=" * 60)
    print()

def get_key_name(key):
    """Chuyển đổi đối tượng key thành tên string"""
    if hasattr(key, 'name'):
        return key.name
    elif hasattr(key, 'char'):
        return key.char
    return str(key)

def setup_spam_key():
    """Thiết lập phím SPAM macro"""
    global selected_key, current_setup_step
    
    print("\n" + "=" * 40)
    print("THIẾT LẬP PHÍM SPAM MACRO")
    print("=" * 40)
    print("Phím hiện tại:", config.get('spam_key', 'x1 (Mouse 4)'))
    print("Nhấn phím bạn muốn sử dụng để kích hoạt SPAM macro")
    print("(Giữ để spam, thả để dừng)")
    print()
    print("R: Nhập lại    |    ESC: Bỏ qua (giữ mặc định)")
    print("=" * 40)
    
    current_setup_step = "spam_key"
    selected_key = None
    
    def on_key_press(key):
        global selected_key
        key_name = get_key_name(key).lower()
        
        # ESC để bỏ qua
        if key_name == 'esc':
            print("⚠ Giữ phím mặc định: x1 (Mouse 4)")
            return False
        
        # R để nhập lại (không làm gì, vẫn tiếp tục nghe)
        elif key_name == 'r':
            print("↻ Vui lòng nhấn phím mới...")
            return True
        
        # Phím hợp lệ
        print(f"✅ Đã chọn phím: {key_name}")
        config['spam_key'] = key_name
        selected_key = key_name
        return False
    
    # Lắng nghe phím
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()
    
    current_setup_step = None
    return selected_key

def setup_curve_key():
    """Thiết lập phím CURVE"""
    global selected_key, current_setup_step
    
    print("\n" + "=" * 40)
    print("THIẾT LẬP PHÍM CURVE")
    print("=" * 40)
    print("Phím hiện tại:", config.get('curve_key', 'x2 (Mouse 5)'))
    print("Nhấn phím bạn muốn sử dụng để kích hoạt CURVE")
    print("(Nhấn một lần thực hiện một curve)")
    print()
    print("R: Nhập lại    |    ESC: Bỏ qua (giữ mặc định)")
    print("=" * 40)
    
    current_setup_step = "curve_key"
    selected_key = None
    
    def on_key_press(key):
        global selected_key
        key_name = get_key_name(key).lower()
        
        if key_name == 'esc':
            print("⚠ Giữ phím mặc định: x2 (Mouse 5)")
            return False
        
        elif key_name == 'r':
            print("↻ Vui lòng nhấn phím mới...")
            return True
        
        print(f"✅ Đã chọn phím: {key_name}")
        config['curve_key'] = key_name
        selected_key = key_name
        return False
    
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()
    
    current_setup_step = None
    return selected_key

def setup_spam_cps():
    """Thiết lập CPS cho SPAM macro"""
    print("\n" + "=" * 40)
    print("THIẾT LẬP TỐC ĐỘ SPAM (CPS)")
    print("=" * 40)
    print("CPS hiện tại:", config.get('spam_cps', 20))
    print("CPS = Số lần click mỗi giây (cho cả 3 phím: Chuột trái, F, G)")
    print("Giới hạn an toàn: 5-30 CPS")
    print()
    
    while True:
        try:
            cps_input = input("Nhập CPS mong muốn (5-30): ").strip()
            
            if not cps_input:
                print("⚠ Giữ giá trị cũ:", config.get('spam_cps', 20))
                break
                
            cps = int(cps_input)
            
            if 5 <= cps <= 30:
                config['spam_cps'] = cps
                config['spam_delay'] = 1.0 / cps  # Tính delay tự động
                print(f"✅ Đã đặt CPS: {cps} (Delay: {1.0/cps:.3f}s)")
                break
            else:
                print("❌ CPS phải từ 5 đến 30!")
                
        except ValueError:
            print("❌ Vui lòng nhập số hợp lệ!")
        except KeyboardInterrupt:
            print("\n⚠ Giữ giá trị cũ")
            break
    
    return config.get('spam_cps', 20)

def setup_wizard():
    """Wizard setup đầy đủ"""
    print("\n" + "=" * 60)
    print("           WIZARD THIẾT LẬP MACRO")
    print("=" * 60)
    
    # Kiểm tra nếu đã setup
    if config.get('setup_completed', False):
        print("✅ Đã tìm thấy cấu hình trước đó!")
        print("Cấu hình hiện tại:")
        print(f"  • Phím SPAM: {config.get('spam_key')}")
        print(f"  • Phím CURVE: {config.get('curve_key')}")
        print(f"  • CPS: {config.get('spam_cps')}")
        print()
        
        choice = input("Bạn có muốn thiết lập lại? (y/n): ").lower()
        if choice != 'y':
            print("Tiếp tục với cấu hình cũ...")
            return True
    
    display_setup_menu()
    
    steps_completed = 0
    try:
        # Bước 1: Phím SPAM
        print("\n[1/3] Thiết lập phím SPAM macro")
        if setup_spam_key():
            steps_completed += 1
        
        # Bước 2: Phím CURVE
        print("\n[2/3] Thiết lập phím CURVE")
        if setup_curve_key():
            steps_completed += 1
        
        # Bước 3: CPS
        print("\n[3/3] Thiết lập CPS")
        setup_spam_cps()
        steps_completed += 1
        
        # Lưu config
        config['setup_completed'] = True
        if save_config():
            print("\n" + "=" * 60)
            print("✅ THIẾT LẬP HOÀN TẤT!")
            print("=" * 60)
            print("Cấu hình đã được lưu:")
            print(f"  • Phím SPAM: {config.get('spam_key')}")
            print(f"  • Phím CURVE: {config.get('curve_key')}")
            print(f"  • CPS: {config.get('spam_cps')}")
            print(f"  • Delay: {1.0/config.get('spam_cps', 20):.3f}s")
            print()
            print("Chương trình sẽ khởi động macro trong 3 giây...")
            time.sleep(3)
            return True
        
    except KeyboardInterrupt:
        print("\n\n⚠ Setup bị hủy, sử dụng cấu hình mặc định")
    
    return False

# ==============================================
# MACRO SPAM
# ==============================================

def spam_macro():
    """Thực hiện macro spam với CPS từ config"""
    global spam_active
    
    # Tính delay từ CPS
    delay = 1.0 / config.get('spam_cps', 20)
    
    while spam_active:
        try:
            # Click chuột trái
            mouse_controller.click(Button.left)
            
            # Nhấn phím F
            keyboard_controller.press('f')
            keyboard_controller.release('f')
            
            # Nhấn phím G  
            keyboard_controller.press('g')
            keyboard_controller.release('g')
            
            # Delay chính xác
            time.sleep(delay)
            
        except Exception as e:
            spam_active = False
            print(f"[Lỗi] Trong macro spam: {e}")
            break

# ==============================================
# MACRO CURVE
# ==============================================

def perform_curve():
    """Thực hiện macro curve một lần"""
    
    try:
        # Lưu vị trí chuột hiện tại
        original_x, original_y = pyautogui.position()
        
        # Chọn hướng curve ngẫu nhiên
        directions = ["top_left", "top_right", "top", "left", "right"]
        direction = random.choice(directions)
        
        # Khoảng cách từ config
        distance = config.get('curve_distance', 50)
        
        # Tính toán điểm đích
        if direction == "top_left":
            target_x = original_x - distance
            target_y = original_y - distance
        elif direction == "top_right":
            target_x = original_x + distance
            target_y = original_y - distance
        elif direction == "top":
            target_x = original_x
            target_y = original_y - distance
        elif direction == "left":
            target_x = original_x - distance
            target_y = original_y
        elif direction == "right":
            target_x = original_x + distance
            target_y = original_y
        
        # Thực hiện curve nhanh
        pyautogui.moveTo(target_x, target_y, duration=0)
        mouse_controller.click(Button.left)
        pyautogui.moveTo(original_x, original_y, duration=0)
        
        # Log debug (có thể tắt)
        # print(f"[Curve] {direction}")
        
    except Exception as e:
        print(f"[Lỗi] Trong macro curve: {e}")

# ==============================================
# XỬ LÝ SỰ KIỆN CHUỘT & BÀN PHÍM
# ==============================================

def is_matching_key(event_key, config_key):
    """Kiểm tra phím nhấn có khớp với phím trong config không"""
    try:
        # Lấy tên phím từ event
        if hasattr(event_key, 'name'):
            event_name = event_key.name.lower()
        elif hasattr(event_key, 'char'):
            event_name = event_key.char.lower()
        else:
            event_name = str(event_key).lower().replace("'", "")
        
        # So sánh với config
        return event_name == config_key.lower()
    except:
        return False

def on_click(x, y, button, pressed):
    """Xử lý sự kiện click chuột"""
    global spam_active, spam_thread
    
    # Nếu đang trong setup, bỏ qua
    if current_setup_step:
        return True
    
    # Kiểm tra phím SPAM
    spam_key_config = config.get('spam_key', 'x1')
    try:
        # Kiểm tra phím chuột
        if spam_key_config in ['x1', 'x2', 'left', 'right', 'middle']:
            button_mapping = {
                'x1': Button.x1,
                'x2': Button.x2,
                'left': Button.left,
                'right': Button.right,
                'middle': Button.middle
            }
            
            if spam_key_config in button_mapping and button == button_mapping[spam_key_config]:
                if pressed and not spam_active:
                    # Bắt đầu spam macro
                    spam_active = True
                    spam_thread = threading.Thread(target=spam_macro, daemon=True)
                    spam_thread.start()
                    print(f"[Spam] Đã kích hoạt (CPS: {config.get('spam_cps', 20)})")
                elif not pressed and spam_active:
                    # Dừng spam macro
                    spam_active = False
                    if spam_thread:
                        spam_thread.join(timeout=0.1)
                    print("[Spam] Đã dừng")
    except:
        pass
    
    # Kiểm tra phím CURVE (chỉ khi nhấn xuống)
    curve_key_config = config.get('curve_key', 'x2')
    try:
        if curve_key_config in ['x1', 'x2', 'left', 'right', 'middle']:
            button_mapping = {
                'x1': Button.x1,
                'x2': Button.x2,
                'left': Button.left,
                'right': Button.right,
                'middle': Button.middle
            }
            
            if curve_key_config in button_mapping and button == button_mapping[curve_key_config] and pressed:
                # Thực hiện curve trong luồng riêng
                curve_thread = threading.Thread(target=perform_curve, daemon=True)
                curve_thread.start()
    except:
        pass
    
    return True

def on_press(key):
    """Xử lý sự kiện nhấn phím"""
    global spam_active, spam_thread
    
    # Thoát chương trình khi nhấn ESC
    if hasattr(key, 'name') and key.name == 'esc':
        print("\nĐang thoát chương trình...")
        
        if spam_active:
            spam_active = False
            if spam_thread:
                spam_thread.join(timeout=0.1)
        
        return False
    
    # Nếu đang trong setup, bỏ qua
    if current_setup_step:
        return True
    
    # Kiểm tra phím SPAM (phím bàn phím)
    spam_key_config = config.get('spam_key', 'x1')
    if spam_key_config not in ['x1', 'x2', 'left', 'right', 'middle']:
        # Là phím bàn phím
        if is_matching_key(key, spam_key_config):
            if not spam_active:
                spam_active = True
                spam_thread = threading.Thread(target=spam_macro, daemon=True)
                spam_thread.start()
                print(f"[Spam] Đã kích hoạt (CPS: {config.get('spam_cps', 20)})")
    
    # Kiểm tra phím CURVE (phím bàn phím)
    curve_key_config = config.get('curve_key', 'x2')
    if curve_key_config not in ['x1', 'x2', 'left', 'right', 'middle']:
        # Là phím bàn phím
        if is_matching_key(key, curve_key_config):
            # Thực hiện curve
            curve_thread = threading.Thread(target=perform_curve, daemon=True)
            curve_thread.start()
    
    return True

def on_release(key):
    """Xử lý sự kiện thả phím"""
    global spam_active, spam_thread
    
    # Kiểm tra phím SPAM (phím bàn phím)
    spam_key_config = config.get('spam_key', 'x1')
    if spam_key_config not in ['x1', 'x2', 'left', 'right', 'middle']:
        if is_matching_key(key, spam_key_config):
            if spam_active:
                spam_active = False
                if spam_thread:
                    spam_thread.join(timeout=0.1)
                print("[Spam] Đã dừng")
    
    return True

# ==============================================
# HIỂN THỊ THÔNG TIN
# ==============================================

def display_info():
    """Hiển thị thông tin chương trình"""
    print("=" * 60)
    print("           MACRO HỖ TRỢ BLADE BALL v1.0")
    print("=" * 60)
    print("Tác giả: Wuys")
    print("GitHub: Wuyscute123")
    print("Website: http://getwuysmacro.getenjoyment.net/")
    print("Facebook: https://www.facebook.com/bbinaty.2007")
    print("Discord: xwuys")
    print()
    print("📋 CẤU HÌNH HIỆN TẠI:")
    print(f"  • Phím SPAM macro: {config.get('spam_key')}")
    print(f"  • Phím CURVE: {config.get('curve_key')}")
    print(f"  • CPS: {config.get('spam_cps')} clicks/giây")
    print(f"  • Delay curve: {config.get('curve_delay', 0.05)}s")
    print()
    print("🎮 HƯỚNG DẪN SỬ DỤNG:")
    print(f"  1. Nhấn GIỮ '{config.get('spam_key')}' để spam")
    print(f"  2. Nhấn '{config.get('curve_key')}' để curve")
    print("  3. Nhấn ESC để thoát chương trình")
    print()
    print("⚙ ĐỂ THAY ĐỔI CẤU HÌNH:")
    print("  - Xóa file 'bladeball_config.json' và chạy lại")
    print("  - Hoặc chỉnh sửa file config trực tiếp")
    print("=" * 60)
    print()

# ==============================================
# HÀM CHÍNH
# ==============================================

def main():
    """Hàm chính của chương trình"""
    
    # Kiểm tra Windows version
    if not check_windows_version():
        sys.exit(1)
    
    # Tải config
    load_config()
    
    # Chạy setup wizard nếu cần
    setup_wizard()
    
    # Hiển thị thông tin
    display_info()
    
    # Khởi tạo listener
    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    
    try:
        # Bắt đầu lắng nghe
        mouse_listener.start()
        keyboard_listener.start()
        
        print("✅ Macro đã sẵn sàng!")
        print("📌 Đang chạy nền... (Nhấn ESC để thoát)")
        print()
        
        # Giữ chương trình chạy
        while True:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n🛑 Đang dừng chương trình...")
    
    except Exception as e:
        print(f"\n[❌ Lỗi] {e}")
    
    finally:
        # Dừng tất cả
        global spam_active
        spam_active = False
        
        mouse_listener.stop()
        keyboard_listener.stop()
        
        print("=" * 60)
        print("Chương trình đã dừng.")
        print("Cảm ơn đã sử dụng!")
        print("=" * 60)

# ==============================================
# KHỞI CHẠY
# ==============================================

if __name__ == "__main__":
    # Thiết lập pyautogui
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0
    
    # Chạy chương trình
    main()