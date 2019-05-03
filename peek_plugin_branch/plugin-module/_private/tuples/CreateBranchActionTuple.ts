 import {addTupleType, Tuple, TupleActionABC} from "@synerty/vortexjs";
import {branchTuplePrefix} from "../PluginNames";

@addTupleType
export class CreateBranchActionTuple extends TupleActionABC {
    static readonly tupleName = branchTuplePrefix + "CreateBranchActionTuple";

    branchDetailId: number;
    offset: number;

    constructor() {
        super(CreateBranchActionTuple.tupleName)
    }
}