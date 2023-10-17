# Tóm tắt về Django cơ bản

## 1. Tạo biến môi trường ảo với Anaconda

Để tạo một môi trường ảo với Anaconda, bạn sử dụng lệnh sau:

```
conda create --name venv_name python=3.8
```

Sau khi tạo xong, bạn kích hoạt môi trường ảo bằng lệnh:

```
conda activate venv_name
```

## 2. Khởi tạo dự án bằng Django Project

Để khởi tạo một dự án Django mới, bạn sử dụng lệnh sau:

```
django-admin startproject project_name
```

## 3. Tạo một Django Application

Trong một dự án Django, bạn có thể tạo nhiều ứng dụng khác nhau. Để tạo một ứng dụng mới:

```
python manage.py startapp app_name
```

## 4. URLs Mappings

Django sử dụng một hệ thống URLs để điều hướng người dùng đến các view tương ứng. Bạn có thể định nghĩa URLs này trong tệp `urls.py` của mỗi ứng dụng.

Ví dụ:

```python
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
]
```

## 5. Templates

Templates trong Django giúp bạn tạo ra các trang HTML một cách linh hoạt và tái sử dụng. Bạn có thể sử dụng ngôn ngữ mẫu của Django để truyền dữ liệu từ views đến templates.

Ví dụ:

```html
<p>{{ item.name }}</p>
```

## 6. Static Files

Các tệp tĩnh như CSS, JavaScript, hình ảnh được lưu trong thư mục `static` của mỗi ứng dụng. Để sử dụng chúng, bạn cần cấu hình settings và sử dụng `{% static 'path_to_file' %}` trong templates.
