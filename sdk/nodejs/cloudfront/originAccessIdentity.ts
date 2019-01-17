// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Creates an Amazon CloudFront origin access identity.
 * 
 * For information about CloudFront distributions, see the
 * [Amazon CloudFront Developer Guide][1]. For more information on generating
 * origin access identities, see
 * [Using an Origin Access Identity to Restrict Access to Your Amazon S3 Content][2].
 * 
 * ## Example Usage
 * 
 * The following example below creates a CloudFront origin access identity.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const aws_cloudfront_origin_access_identity_origin_access_identity = new aws.cloudfront.OriginAccessIdentity("origin_access_identity", {
 *     comment: "Some comment",
 * });
 * ```
 */
export class OriginAccessIdentity extends pulumi.CustomResource {
    /**
     * Get an existing OriginAccessIdentity resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OriginAccessIdentityState, opts?: pulumi.CustomResourceOptions): OriginAccessIdentity {
        return new OriginAccessIdentity(name, <any>state, { ...opts, id: id });
    }

    /**
     * Internal value used by CloudFront to allow future
     * updates to the origin access identity.
     */
    public /*out*/ readonly callerReference: pulumi.Output<string>;
    /**
     * A shortcut to the full path for the
     * origin access identity to use in CloudFront, see below.
     */
    public /*out*/ readonly cloudfrontAccessIdentityPath: pulumi.Output<string>;
    /**
     * An optional comment for the origin access identity.
     */
    public readonly comment: pulumi.Output<string | undefined>;
    /**
     * The current version of the origin access identity's information.
     * For example: `E2QWRUHAPOMQZL`.
     */
    public /*out*/ readonly etag: pulumi.Output<string>;
    /**
     * A pre-generated ARN for use in S3 bucket policies (see below).
     * Example: `arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity
     * E2QWRUHAPOMQZL`.
     */
    public /*out*/ readonly iamArn: pulumi.Output<string>;
    /**
     * The Amazon S3 canonical user ID for the origin
     * access identity, which you use when giving the origin access identity read
     * permission to an object in Amazon S3.
     */
    public /*out*/ readonly s3CanonicalUserId: pulumi.Output<string>;

    /**
     * Create a OriginAccessIdentity resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: OriginAccessIdentityArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OriginAccessIdentityArgs | OriginAccessIdentityState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: OriginAccessIdentityState = argsOrState as OriginAccessIdentityState | undefined;
            inputs["callerReference"] = state ? state.callerReference : undefined;
            inputs["cloudfrontAccessIdentityPath"] = state ? state.cloudfrontAccessIdentityPath : undefined;
            inputs["comment"] = state ? state.comment : undefined;
            inputs["etag"] = state ? state.etag : undefined;
            inputs["iamArn"] = state ? state.iamArn : undefined;
            inputs["s3CanonicalUserId"] = state ? state.s3CanonicalUserId : undefined;
        } else {
            const args = argsOrState as OriginAccessIdentityArgs | undefined;
            inputs["comment"] = args ? args.comment : undefined;
            inputs["callerReference"] = undefined /*out*/;
            inputs["cloudfrontAccessIdentityPath"] = undefined /*out*/;
            inputs["etag"] = undefined /*out*/;
            inputs["iamArn"] = undefined /*out*/;
            inputs["s3CanonicalUserId"] = undefined /*out*/;
        }
        super("aws:cloudfront/originAccessIdentity:OriginAccessIdentity", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering OriginAccessIdentity resources.
 */
export interface OriginAccessIdentityState {
    /**
     * Internal value used by CloudFront to allow future
     * updates to the origin access identity.
     */
    readonly callerReference?: pulumi.Input<string>;
    /**
     * A shortcut to the full path for the
     * origin access identity to use in CloudFront, see below.
     */
    readonly cloudfrontAccessIdentityPath?: pulumi.Input<string>;
    /**
     * An optional comment for the origin access identity.
     */
    readonly comment?: pulumi.Input<string>;
    /**
     * The current version of the origin access identity's information.
     * For example: `E2QWRUHAPOMQZL`.
     */
    readonly etag?: pulumi.Input<string>;
    /**
     * A pre-generated ARN for use in S3 bucket policies (see below).
     * Example: `arn:aws:iam::cloudfront:user/CloudFront Origin Access Identity
     * E2QWRUHAPOMQZL`.
     */
    readonly iamArn?: pulumi.Input<string>;
    /**
     * The Amazon S3 canonical user ID for the origin
     * access identity, which you use when giving the origin access identity read
     * permission to an object in Amazon S3.
     */
    readonly s3CanonicalUserId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a OriginAccessIdentity resource.
 */
export interface OriginAccessIdentityArgs {
    /**
     * An optional comment for the origin access identity.
     */
    readonly comment?: pulumi.Input<string>;
}
