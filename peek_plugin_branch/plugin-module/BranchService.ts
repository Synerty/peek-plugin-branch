import {ComponentLifecycleEventEmitter, TupleSelector} from "@synerty/vortexjs";
import {branchTuplePrefix} from "./_private/PluginNames";
import {Injectable} from "@angular/core";
import {BranchDetailTuple} from "./BranchDetailTuple";
import {PrivateBranchTupleService} from "./_private/PrivateBranchTupleService";
import {CreateBranchActionTuple} from "./_private";


@Injectable()
export class BranchService extends ComponentLifecycleEventEmitter {
    public static readonly tupleName = branchTuplePrefix + "BranchDetailTable";


    constructor(private tupleService: PrivateBranchTupleService) {
        super()
    }

    createBranch(newBranch: BranchDetailTuple) {
        let action = new CreateBranchActionTuple();
        action.branchDetail = newBranch;
        this.tupleService.offlineAction.push(action);
    }

    branches(modelSetKey: string): Promise<BranchDetailTuple[]> {
        let ts = new TupleSelector(BranchDetailTuple.tupleName, {
            modelSetKey:modelSetKey
        });
        return this.tupleService.offlineObserver.promiseFromTupleSelector(ts);

    }
}