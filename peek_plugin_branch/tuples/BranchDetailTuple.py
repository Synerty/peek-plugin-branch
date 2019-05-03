from datetime import datetime

from vortex.Tuple import Tuple, addTupleType, TupleField

from peek_plugin_branch._private.PluginNames import branchTuplePrefix


@addTupleType
class BranchDetailTuple(Tuple):
    """ Branch Tuple

    This tuple is a create example of defining classes to work with our data.
    """
    __tupleType__ = branchTuplePrefix + 'BranchDetailTuple'

    LOCATION_SERVER_BRANCH = 1
    LOCATION_LOCAL_BRANCH = 2

    #: Model Set Key
    modelSetKey: str = TupleField()

    #: Key
    # 
    # The key of this branch
    key: str = TupleField()

    #: Location
    # 
    # The location of this branch
    location: int = TupleField()

    #: Name
    # 
    # The location of this branch
    name: str = TupleField()

    #: Comment
    # 
    # The location of this branch
    comment: str = TupleField()

    #: User
    # 
    # The location of this branch
    user: str = TupleField()

    #: Updated Date
    # 
    # The location of this branch
    updatedDate: datetime = TupleField()

    #: Created Date
    # 
    # The location of this branch
    createdDate: datetime = TupleField()