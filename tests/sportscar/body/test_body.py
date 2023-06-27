from pytest import mark


@mark.body
class BodyTest:
    @mark.smoke
    def test_body_function_as_expected(self):
        assert True

    def test_another_part_of_body(self):
        assert False
