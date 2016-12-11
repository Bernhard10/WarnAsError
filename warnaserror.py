from nose.plugins import Plugin
import warnings

__author__ = 'Bernhard Thiel'


class WarnAsError(Plugin):
    """Treat warnings that occur DURIONG tests as errors."""
    enabled = False

    def options(self, parser, env):
        """
        Add options to command line.
        """
        super(WarnAsError, self).options(parser, env)

    def configure(self, options, conf):
        """
        Configure plugin.
        """
        super(WarnAsError, self).configure(options, conf)

    def prepareTestRunner(self, runner):
        """
        Treat warnings as errors.
        """
        return WaETestRunner(runner)


class WaETestRunner(object):

    def __init__(self, runner):
        self.runner = runner

    def run(self, test):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            return self.runner.run(test)
