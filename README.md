# Giới thiệu
Một chiếc app window mà Kumo đã tìm thấy đâu đó trên mạng được sửa lại theo phong cách của anh ấy.

Source code và các file chi tiết ở trong các branch.
___
# Translate-App
App này được sử dụng để dịch các ngôn ngữ bằng googletrans trong Python.

Bạn có thể cài đặt với câu lệnh sau:
```pip install googletrans```

App sẽ sử dụng tkinter để làm GUI, bạn có thể tìm hiểu thêm tại [đây](https://tkdocs.com/tutorial/index.html)
___
## Phiên bản 1: master
Bạn có thể lựa chọn nhiều ngôn ngữ hơn, nhưng ở phiên bản này, app chỉ hỗ trợ 3 ngôn ngữ: Tiếng Việt, Tiếng Anh, Tiếng Nhật.

Nếu muốn coi các ngôn ngữ được hỗ trợ, hãy chạy file language.py để coi, sau đó sửa lại dic và combo box trong file.
___
## Phiên bản 2: update2.0
Update khả năng chọn thêm nhiều ngôn ngữ khác.

Các hàm xử lý back-end (file controller.py) được tách riêng ra với front-end (file viewer.py).
___
## Phiên bản 3: update3.0
Update thêm tính năng OCR: giúp nhận dạng các ký tự tiếng Anh từ hình ảnh.

OCR được sử dụng dựa theo Transformers trên HuggingFace. Nếu muốn tuỳ chỉnh thêm cho tiếng Việt, có thể tham khảo tại: [đây](https://github.com/DyThen-Kumo/CS519.O21.KHTN)
___
# Lưu ý
App chạy offline và sử dụng Python nên có thể sẽ hơi lâu, chỉ nên sử dụng khi không có mạng Internet.
___
# Liên hệ:
- [x] Facebook: https://www.facebook.com/dythen.kumo

- [x] Gmail: 22521333@gm.uit.edu.vn

Do mới bắt đầu, có thể app sẽ không được tối ưu, bạn có thể góp ý với Kumo theo [facebook](https://www.facebook.com/dythen.kumo).
