
# Django Models Summary

## Django Models Overview

**Django Models** là một phần trung tâm của framework Django, giúp định nghĩa cấu trúc của cơ sở dữ liệu. 
Một model là một lớp Python định nghĩa các trường và hành vi của dữ liệu mà bạn muốn lưu trữ.

**Đặc điểm chính**:

1. **Trường (Fields)**: Định nghĩa loại dữ liệu mà một cột cụ thể sẽ chứa. Ví dụ: `CharField`, `IntegerField`, `DateField`, v.v.
2. **Tùy chọn Meta**: Cung cấp các tùy chọn bổ sung cho mô hình, như tên bảng.
3. **Phương thức**: Bạn có thể định nghĩa các phương thức bổ sung để tương tác với dữ liệu của mô hình.

## Creating Models

Để tạo một model:

1. Xác định lớp con của `django.db.models.Model`.
2. Thêm các trường bạn muốn vào lớp này.
3. Sau khi tạo mô hình, chạy lệnh `python manage.py makemigrations` để tạo các migration cho mô hình.
4. Sử dụng lệnh `python manage.py migrate` để áp dụng các thay đổi này vào cơ sở dữ liệu.

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
```

## Population Scripts

Một **Population Script** là một script dùng để tự động thêm dữ liệu vào cơ sở dữ liệu. 
Điều này rất hữu ích khi bạn muốn điền dữ liệu giả vào cơ sở dữ liệu của mình để kiểm tra.

Một số điểm quan trọng:

1. Sử dụng thư viện như `Faker` để tạo dữ liệu giả.
2. Đảm bảo sử dụng `django.db.transaction.atomic()` để tạo các giao dịch cơ sở dữ liệu, giúp giảm thiểu khả năng lỗi.

## Models-Templates-Views Paradigm

Django tuân theo **MTV (Model-Template-View)**, một biến thể của **MVC (Model-View-Controller)**.

1. **Model**: Đại diện cho cơ sở dữ liệu và cung cấp cơ chế để truy cập, thêm, sửa, và xóa dữ liệu.
2. **Template**: Đại diện cho phần giao diện người dùng. Django sử dụng một hệ thống template riêng.
3. **View**: Xử lý dữ liệu từ model và truyền nó vào template. Trong Django, view có thể là một hàm hoặc một lớp.

