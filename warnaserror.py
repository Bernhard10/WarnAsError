__author__ = 'Bernhard Thiel'

from nose.plugins import Plugin
import nose
import warnings

class WarnAsError(Plugin):
    enabled = False
    def options(self, parser, env):
        """
        Add options to command line.
        """
        super(WarnAsError, self).options(parser, env)
        parser.add_option("--warn-as-error", action="store_true",
                          default=False,
                          dest="enabled",
                          help="Treat warnings that occur WITHIN tests as errors.")

    def configure(self, options, conf):
        """
        Configure plugin.
        """
        super(WarnAsError, self).configure(options, conf)
        if options.enabled:
            self.enabled=True


    def prepareTestRunner(self, runner):
        """
        Treat warnings as errors.
        """
        return WaETestRunner(runner)



class WaETestRunner(object):
    def __init__(self, runner):
        self.runner=runner
    def run(self, test):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            return self.runner.run(test)


