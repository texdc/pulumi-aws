// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

/**
 * Provides an IAM group.
 */
export class Group extends pulumi.CustomResource {
    /**
     * Get an existing Group resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState): Group {
        return new Group(name, <any>state, { id });
    }

    /**
     * The ARN assigned by AWS for this group.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * The group's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins".
     */
    public readonly name: pulumi.Output<string>;
    /**
     * Path in which to create the group.
     */
    public readonly path: pulumi.Output<string | undefined>;
    /**
     * The [unique ID][1] assigned by AWS.
     */
    public /*out*/ readonly uniqueId: pulumi.Output<string>;

    /**
     * Create a Group resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: GroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupArgs | GroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: GroupState = argsOrState as GroupState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["path"] = state ? state.path : undefined;
            inputs["uniqueId"] = state ? state.uniqueId : undefined;
        } else {
            const args = argsOrState as GroupArgs | undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["path"] = args ? args.path : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["uniqueId"] = undefined /*out*/;
        }
        super("aws:iam/group:Group", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Group resources.
 */
export interface GroupState {
    /**
     * The ARN assigned by AWS for this group.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The group's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins".
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Path in which to create the group.
     */
    readonly path?: pulumi.Input<string>;
    /**
     * The [unique ID][1] assigned by AWS.
     */
    readonly uniqueId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Group resource.
 */
export interface GroupArgs {
    /**
     * The group's name. The name must consist of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: `=,.@-_.`. Group names are not distinguished by case. For example, you cannot create groups named both "ADMINS" and "admins".
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Path in which to create the group.
     */
    readonly path?: pulumi.Input<string>;
}
