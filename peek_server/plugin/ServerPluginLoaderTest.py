import logging

import sys
from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.trial import unittest

from .ServerPluginLoader import serverPluginLoader

logger = logging.getLogger(__name__)

PLUGIN_NOOP = "plugin_noop"


class ServerPluginLoaderTest(unittest.TestCase):
    def testLoadAll(self):
        serverPluginLoader.loadAllPlugins()

        logger.info(serverPluginLoader.listPlugins())

        for plugin in list(serverPluginLoader._loadedPlugins.values()):
            logger.info("configUrl = %s", plugin.configUrl())

        d = Deferred()
        reactor.callLater(5.0, d.callback, True)
        return d

    def testUnregister(self):
        loadedModuleBefore = set(sys.modules)

        serverPluginLoader.loadPlugin(PLUGIN_NOOP)
        self.assertTrue(PLUGIN_NOOP in sys.modules)

        serverPluginLoader.unloadPlugin(PLUGIN_NOOP)

        loadedModuleNow = set(sys.modules) - loadedModuleBefore

        # Ensure that none of the modules contain the plugin_name
        for modName in loadedModuleNow:
            self.assertFalse(PLUGIN_NOOP in modName)

    def testReRegister(self):
        serverPluginLoader.loadPlugin(PLUGIN_NOOP)
        serverPluginLoader.loadPlugin(PLUGIN_NOOP)

        for plugin in list(serverPluginLoader._loadedPlugins.values()):
            logger.info("configUrl = %s", plugin.configUrl())

        d = Deferred()
        reactor.callLater(5.0, d.callback, True)
        return d