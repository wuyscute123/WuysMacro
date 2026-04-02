
⚙️ Wuys Macro

> Lightweight. Stable. Built for real clash.



Wuys Macro là một project mã nguồn mở tập trung vào một mục tiêu duy nhất:

> Giữ nhịp – giữ ổn định – thắng trong clash thực tế



Macro không chạy theo CPS ảo hay spam vô nghĩa, mà tập trung vào:

Stability

Timing

Performance trong combat thật



---

🚀 Features

⚡ Engine tối ưu (SendInput-based)

🧠 Timing ổn định, giữ nhịp lâu

🔁 Spam cycle gọn (LMB + F + G)

📊 Hiệu quả ở CPS vừa phải (~60–100 CPS)

🥊 Tối ưu cho clash khoảng cách gần



---

🧬 Versions Overview

v1.0 → Reborn: nền tảng + tối ưu core

v1.1: thử nghiệm curve (đã loại bỏ)

v1.2 – Legit Mode: tăng stability + clean behavior

v1.2.1 trở xuống: sử dụng pyautogui cho input

v1.3 – Engine Update: rebuild engine (SendInput + ctypes)

v2.0 – Toe Method: dynamic timing + kiểm soát clash



---

📊 Performance

Hoạt động ổn định ở ~60 CPS

Không cần CPS quá cao

Clash hiệu quả ở ping ~50–70ms


Thực tế:

> ~200 CPS + 60 FPS đã đủ để giữ nhịp clash ổn định




---

🧪 Real Match Result

Test thực chiến:

Wuys Macro vs cheater

Điều kiện ngang nhau (mạng, thiết bị, môi trường)


Kết quả:

> 3 – 1 (BO3) → Wuys Macro thắng



Điều này cho thấy:

> Timing + stability quan trọng hơn CPS.




---

🔓 Open Source

Project hoàn toàn mã nguồn mở.

Bạn có thể:

Kiểm tra toàn bộ source

Tự build lại

Modify theo nhu cầu



---

🔐 Security & Transparency

Wuys Macro được thiết kế theo nguyên tắc:

> Ít dependency → dễ kiểm tra → minh bạch tuyệt đối




---

📦 Thư viện sử dụng (phiên bản hiện tại)

ctypes (built-in Python)
→ Gọi Windows API (SendInput)

keyboard
→ Bắt phím và điều khiển input



---

📜 Lưu ý về phiên bản cũ (Legacy)

Các phiên bản từ v1.2.1 trở xuống có sử dụng:

pyautogui


Mục đích sử dụng:

> Chỉ để gửi input (send input), không sử dụng cho bất kỳ hành vi nào khác.




---

🚫 Cam kết bảo mật

Wuys Macro KHÔNG BAO GIỜ sử dụng các thư viện hoặc cơ chế có rủi ro cao, bao gồm:

Thư viện điều khiển từ xa / backdoor

Thư viện gửi dữ liệu ra ngoài (networking)

Thư viện chạy lệnh hệ thống ẩn

Obfuscation / code che giấu hành vi

Bất kỳ cơ chế nào liên quan tới:

Data exfiltration

Background service ẩn

Crypto mining



Ví dụ các thư viện thường bị lạm dụng (và không được sử dụng trong các phiên bản hiện tại):

pynput

pyautogui (đã loại bỏ từ v1.3 trở lên)

socket

requests

subprocess



---

⚠ False Positive (VirusTotal)

Khi scan file .exe, bạn có thể thấy cảnh báo như:

trojan.tedy


Đây là false positive, do:

Hook bàn phím (keyboard)

Gọi Windows API (ctypes)

Hành vi automation giống macro

File .exe được build từ Python



---

✔ Cách kiểm tra an toàn nhất

Scan trực tiếp file main.py trên VirusTotal

Hoặc tự build từ source



---

🧠 Important

> Wuys Macro chạy hoàn toàn ở user-mode
Không gửi dữ liệu
Không có network
Không có backdoor




---

🛠 Usage

Chạy bằng Python:

python main.py

Hoặc sử dụng bản build .exe


---

🧠 Philosophy

Macro này không được tạo ra để:

Spam CPS vô hạn

Fake chỉ số


Mà để:

> Giữ nhịp – giữ ổn định – chiến thắng trong clash thực tế




---

📌 Links

Facebook: wuys nee🐧

GitHub: https://github.com/wuyscute123/WuysMacro



---

🌐 Official Website

> Website download chính thức: wuysmacro.eu.cc

---

🏁 Final

Wuys Macro không cố gắng trở thành macro mạnh nhất.

Nhưng nó được xây dựng để:

> đủ mạnh để thắng – và đủ ổn định để sống lâu trong mọi tình huống. 😏
