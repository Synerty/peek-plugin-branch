import {ComponentLifecycleEventEmitter} from "@synerty/vortexjs";
import {branchTuplePrefix} from "./_private/PluginNames";
import {Injectable} from "@angular/core";
import {BranchDetailTuple} from "./BranchDetailTuple";


@Injectable()
export class BranchService extends ComponentLifecycleEventEmitter {
    public static readonly tupleName = branchTuplePrefix + "BranchDetailTable";


    constructor() {
        super()
    }

    createBranch(newBranch: BranchDetailTuple) {

    }

    branches(modelSetKey: string): BranchDetailTuple[] {
        let branchA = new BranchDetailTuple();
        branchA.name = 'Test branch name';
        return [
            branchA
        ];
    }
}