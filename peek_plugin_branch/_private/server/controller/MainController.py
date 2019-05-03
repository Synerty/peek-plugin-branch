import logging

from twisted.internet.defer import Deferred
from vortex.DeferUtil import deferToThreadWrapWithLogger
from vortex.TupleAction import TupleActionABC
from vortex.TupleSelector import TupleSelector
from vortex.handler.TupleActionProcessor import TupleActionProcessorDelegateABC
from vortex.handler.TupleDataObservableHandler import TupleDataObservableHandler

from peek_plugin_branch._private.storage.BranchDetailTable import BranchDetailTable
from peek_plugin_branch._private.tuples.CreateBranchActionTuple import \
    CreateBranchActionTuple

logger = logging.getLogger(__name__)


class MainController(TupleActionProcessorDelegateABC):
    def __init__(self, dbSessionCreator, tupleObservable: TupleDataObservableHandler):
        self._dbSessionCreator = dbSessionCreator
        self._tupleObservable = tupleObservable

    def shutdown(self):
        pass

    def processTupleAction(self, tupleAction: TupleActionABC) -> Deferred:

        if isinstance(tupleAction, CreateBranchActionTuple):
            return self._processCreateBranch(tupleAction)

        raise NotImplementedError(tupleAction.tupleName())

    @deferToThreadWrapWithLogger(logger)
    def _processCreateBranch(self, action: CreateBranchActionTuple):
        try:
            # Perform update using SQLALchemy
            session = self._dbSessionCreator()
            row = (session.query(BranchDetailTable)
                   .filter(BranchDetailTable.id == action.branchDetailId)
                   .one())
            row.int1 += action.offset
            session.commit()

            logger.debug("Int changed by %u", action.offset)

            # Notify the observer of the update
            # This tuple selector must exactly match what the UI observes
            tupleSelector = TupleSelector(BranchDetailTable.tupleName(), {})
            self._tupleObservable.notifyOfTupleUpdate(tupleSelector)

        finally:
            # Always close the session after we create it
            session.close()
