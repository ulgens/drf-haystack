import warnings


class WarningTestCaseMixin:
    """
    TestCase mixin to catch warnings
    """

    def assertWarning(self, warning, callable, *args, **kwargs):
        with warnings.catch_warnings(record=True) as warning_list:
            warnings.simplefilter(action="always")
            callable(*args, **kwargs)
            self.assertTrue(any(item.category == warning for item in warning_list))
