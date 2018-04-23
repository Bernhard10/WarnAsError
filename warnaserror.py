from nose.plugins import Plugin
import warnings

__author__ = 'Bernhard Thiel'


class WarnAsError(Plugin):
    """Treat warnings that occur DURING tests as errors."""
    enabled = False

    def options(self, parser, env):
        """
        Add options to command line.
        """
        super(WarnAsError, self).options(parser, env)

        parser.add_option(
            str('--warning-class'), action='store', dest='warning_class',
            default=None,
            help="Set the warning class to turn into an error. Default: all warnings"
        )

    def configure(self, options, conf):
        """
        Configure plugin.
        """
        super(WarnAsError, self).configure(options, conf)
        self.options = options

    def prepareTestRunner(self, runner):
        """
        Treat warnings as errors.
        """
        return WaETestRunner(runner, self.options.warning_class)


class WaETestRunner(object):

    def __init__(self, runner, warning_class=None):
        self.runner = runner
        self.warning_class = warning_class

    def run(self, test):
        warning_class = Warning
        if self.warning_class:
            if '.' in self.warning_class:
                path, obj = self.warning_class.rsplit('.', 1)
            else:
                path = 'builtins'
                obj = self.warning_class
            import importlib
            warning_class = getattr(importlib.import_module(path), obj)
        with warnings.catch_warnings():
            warnings.simplefilter("error", category=warning_class)
            return self.runner.run(test)
