from app import always_false

def test_always_false():
    """Функция always_false должна возвращать False"""
    assert always_false() is False, "always_false() должен вернут False"
