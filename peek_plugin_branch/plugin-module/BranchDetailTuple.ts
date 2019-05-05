import {addTupleType, Tuple} from "@synerty/vortexjs";
import {branchTuplePrefix} from "./_private/PluginNames";


/** Diagram Branch Service Enum
 *
 * This enum describes the location of the branch,
 * is the branch local to the UI, or is it persisted on the server.
 *
 */
export enum BranchLocation {
    ServerBranch = 1,
    LocalBranch = 2
}

@addTupleType
export class BranchDetailTuple extends Tuple {
    public static readonly tupleName = branchTuplePrefix + "BranchDetailTuple";


    /** The database ID
     *
     * Consider this field private
     */
    id: number;


    /** Model Set Key */
    modelSetKey: string;

    /** Key
     *
     * The key of this branch
     */
    key: string;

    /** Location
     *
     * The location of this branch
     */
    location: BranchLocation;

    /** Name
     *
     * The location of this branch
     */
    name: string;

    /** Comment
     *
     * The location of this branch
     */
    comment: string;

    /** userName
     *
     * The location of this branch
     */
    userName: string;

    /** Updated Date
     *
     * The location of this branch
     */
    updatedDate: Date;

    /** Created Date
     *
     * The location of this branch
     */
    createdDate: Date;

    constructor() {
        super(BranchDetailTuple.tupleName)
    }
}