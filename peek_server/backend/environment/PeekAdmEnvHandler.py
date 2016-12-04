'''
Created on 09/07/2014

@author: synerty
'''

from peek_server.storage import getPeekServerOrmSession
from peek_server.storage.PeekEnv import PeekEnvServer, PeekEnvAgent, PeekEnvWorker, \
    PeekEnvClient
from vortex.handler.OrmCrudHandler import OrmCrudHandler, OrmCrudHandlerExtension

# -----------------------------------------------------------------------------
# Servers
serverListDataKey = {
    'papp': 'peek_server',
    'key': "peakadm.env.server.list.data"
}


class EnvServerListHandler(OrmCrudHandler):
    pass


envServerListHandler = EnvServerListHandler(getPeekServerOrmSession,
                                            PeekEnvServer,
                                            serverListDataKey,
                                            retreiveAll=True)


@envServerListHandler.addExtension(PeekEnvServer)
class _EnvServerListHandlerExtension(OrmCrudHandlerExtension):
    def afterUpdateCommit(self, tuple_, tuples, session, payloadFilt):
        # from peek.api.client.ClientGridHandler import clientGridHandler
        # reactor.callLater(0.0, clientGridHandler.reload)
        return True


# -----------------------------------------------------------------------------
# workers
workerListDataKey = {
    'papp': 'peek_server',
    'key': "peakadm.env.worker.list.data"
}


class EnvWorkerListHandler(OrmCrudHandler):
    pass


envWorkerListHandler = EnvWorkerListHandler(getPeekServerOrmSession,
                                            PeekEnvWorker,
                                            workerListDataKey,
                                            retreiveAll=True)


@envWorkerListHandler.addExtension(PeekEnvWorker)
class _EnvWorkerListHandlerExtension(OrmCrudHandlerExtension):
    def afterUpdateCommit(self, tuple_, tuples, session, payloadFilt):
        # from peek.api.client.ClientGridHandler import clientGridHandler
        # reactor.callLater(0.0, clientGridHandler.reload)
        return True

# -----------------------------------------------------------------------------
# agents
agentListDataKey = {
    'papp': 'peek_server',
    'key': "peakadm.env.agent.list.data"
}

class EnvAgentListHandler(OrmCrudHandler):
    pass

envAgentListHandler = EnvAgentListHandler(getPeekServerOrmSession,
                                          PeekEnvAgent,
                                          agentListDataKey,
                                          retreiveAll=True)

@envAgentListHandler.addExtension(PeekEnvAgent)
class _EnvAgentListHandlerExtension(OrmCrudHandlerExtension):
    def afterUpdateCommit(self, tuple_, tuples, session, payloadFilt):
        return True

# -----------------------------------------------------------------------------
# agents
clientListDataKey = {
    'papp': 'peek_server',
    'key': "peakadm.env.client.list.data"
}


class EnvClientListHandler(OrmCrudHandler):
    pass


envClientListHandler = EnvClientListHandler(getPeekServerOrmSession,
                                          PeekEnvClient,
                                           clientListDataKey,
                                          retreiveAll=True)


@envClientListHandler.addExtension(PeekEnvClient)
class _EnvClientListHandlerExtension(OrmCrudHandlerExtension):
    def afterUpdateCommit(self, tuple_, tuples, session, payloadFilt):
        return True