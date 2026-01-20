# 🛡️ Security & Build Disclaimer

Wuys Macro là dự án mã nguồn mở. Repository cung cấp hai cách sử dụng:

- 📦 Bản build sẵn (.exe) – tiện lợi cho người dùng phổ thông

-🛠️ Tự build từ source – được khuyến khích cho những ai muốn mức độ tin cậy cao nhất

**Nếu bạn có kiến thức kỹ thuật, việc tự build từ mã nguồn luôn là lựa chọn an toàn và minh bạch nhất.

# 🔍 VirusTotal & False Positive

Tại thời điểm phát hành Release v1.0, bản .exe build sẵn đã được kiểm tra bằng VirusTotal:

🔗 Link kiểm tra VirusTotal:
https://www.virustotal.com/gui/file/af9aca281253f784a0d913269450dfecf713a4aa1cb69c827cd64fe58c35a070/detection

Kết quả: 4 / 70 engine phát hiện

Các cảnh báo đến từ AI / heuristic / static machine learning

Không có antivirus lớn nào (Microsoft Defender, Kaspersky, Bitdefender, ESET, Avast, …) phát hiện mã độc

# Các engine đã flag:
- Bkav Pro – AI heuristic, thường false positive với macro & PyInstaller
- Malwarebytes (AI) – phát hiện dựa trên ML, không phải signature
- SecureAge – static analysis, không phân tích runtime
- SentinelOne (Static ML) – đánh dấu “Suspicious”, không kết luận malware

# 📌 Đây là false positive phổ biến với:

- Phần mềm macro / auto click
- Tool mô phỏng input
- File .exe build bằng PyInstaller và không ký số

# 📂 Minh bạch & Cam kết
Wuys Macro:
- Không inject game
- Không can thiệp bộ nhớ
- Không gửi dữ liệu
- Không có persistence
- Không keylogger

--

# Wuys Macro

Wuys Macro là một công cụ **macro hỗ trợ input** cho Roblox (Blade Ball), được tạo ra nhằm **giảm spam tay**, **ổn định thao tác** và giúp người chơi tập trung hơn vào phản xạ và quyết định trong game.

> Đây **không phải hack / cheat**.  
> Wuys Macro **không inject**, **không đọc dữ liệu game**, **không can thiệp server** — chỉ mô phỏng chuột và bàn phím hợp lệ, tương tự autoclicker hoặc macro chuột gaming.

---

## ✨ Tính năng chính

- 🔘 **Spam input thông minh**
  - Chuột trái + phím `F` + `G`
  - 20 CPS / phím
  - Kích hoạt bằng **giữ Mouse 4**, thả là dừng ngay

- 🎯 **Curve đa hướng**
  - Kích hoạt bằng **Mouse 5**
  - Curve ngẫu nhiên: trái / phải / dọc / chéo
  - Click ngay lập tức và **trả chuột về vị trí cũ**
  - Tổng delay ≤ **0.05s**

- 🧠 **Input giống người thật**
  - Delay nhỏ, không cứng
  - Không spam vô hạn
  - Người chơi vẫn là người quyết định mọi hành động

- 📢 **Loading + quảng cáo**
  - Hiển thị loading 3 giây khi khởi động
  - Random nội dung giới thiệu / disclaimer

---

## 🆚 Vì sao không dùng AHK?

Wuys Macro không hướng tới macro “cứng” như AHK truyền thống.

Khác biệt chính:
- Input **mượt và tự nhiên hơn**
- Curve **đa hướng, random**
- Macro **không điều khiển người chơi**, mà chỉ hỗ trợ thao tác

Mục tiêu là **giữ cảm giác chơi thật**, không phải auto chơi.

---

## ❓ Câu hỏi thường gặp

### Wuys Macro có chứa virus không?
Không.  
Dự án **mã nguồn mở**, bạn có thể tự kiểm tra.  
Hoàn toàn có thể quét bằng **VirusTotal** hoặc antivirus bất kỳ.

---

### Wuys Macro có clash thắng hacker không?
**50–50.**  
Không có tool nào đảm bảo thắng hack thật.  
Nhưng Wuys Macro **ăn được macro AHK kiểu cũ** và **autoclicker thông thường** nhờ input linh hoạt hơn.

---

### Dùng Wuys Macro có bị ban không?
Wuys Macro **không inject, không exploit**, chỉ mô phỏng input hợp lệ.  
Tuy nhiên, việc sử dụng vẫn phụ thuộc **luật game / server**.  
Bạn tự chịu trách nhiệm khi dùng trong môi trường cạnh tranh.

---

### Wuys Macro khác gì autoclicker?
Wuys Macro được **tối ưu riêng cho Blade Ball**:
- Có curve
- Có logic theo thao tác người chơi
- Không chỉ spam click đơn thuần

---

## 👤 Về tác giả

**Wuys** *(tên thật: Huy)* là một developer độc lập, từng phát triển nhiều dự án **Discord** và công cụ hỗ trợ cộng đồng.  
Thông thạo **Python, HTML, CSS, JavaScript**, mình tập trung xây dựng các công cụ **ổn định, minh bạch và dễ dùng**.

Wuys Macro được tạo ra để **hỗ trợ người chơi**, không thay thế kỹ năng.

---

## 🔗 Liên kết

- 🌐 Website: [GetWuysMacro Here](http://getwuysmacro.getenjoyment.net/)
- 💻 GitHub: https://github.com/wuyscute123  

---

## ⚠️ Tuyên bố miễn trừ trách nhiệm

Wuys Macro là **công cụ hỗ trợ input**.  
Tác giả **không chịu trách nhiệm** nếu bạn sử dụng sai mục đích hoặc vi phạm luật của game / server.

---

## 📜 License

Open-source.  
Bạn được phép học hỏi, chỉnh sửa và đóng góp, miễn là **tôn trọng tác giả gốc**.
