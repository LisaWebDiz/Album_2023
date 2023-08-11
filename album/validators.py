from django.core.exceptions import ValidationError


def image_validator(value):
    image_type = ['.png', '.jpeg', '.jpg']
    image_size = value.size

    if image_size > 5242880:
        raise ValidationError("Максимальный размерз изображения - 5MB")

    if not any([True if value.name.endswith(i) else False for i in image_type]):
        raise ValidationError("Изображение должно быть в формате png, jpeg или jpg")

    else:
        return value
