class TestPhrase:
    def test_phrase_len(self):
        phrase = input("Пожалуйста, введите строку короче 15 символов: ")
        print(phrase)
        limit_len = 15
        actual_len = len(phrase)
        print(actual_len)
        assert actual_len < limit_len, f"Длина строки больше чем {limit_len} символов"
