// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

import {ARN} from "../index";

/**
 * Attaches Principal to AWS IoT Thing.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as fs from "fs";
 * 
 * const aws_iot_certificate_cert = new aws.iot.Certificate("cert", {
 *     active: true,
 *     csr: fs.readFileSync("csr.pem", "utf-8"),
 * });
 * const aws_iot_thing_example = new aws.iot.Thing("example", {
 *     name: "example",
 * });
 * const aws_iot_thing_attachment_att = new aws.IotThingAttachment("att", {
 *     principal: aws_iot_certificate_cert.arn,
 *     thing: aws_iot_thing_example.name,
 * });
 * ```
 */
export class ThingPrincipalAttachment extends pulumi.CustomResource {
    /**
     * Get an existing ThingPrincipalAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ThingPrincipalAttachmentState, opts?: pulumi.CustomResourceOptions): ThingPrincipalAttachment {
        return new ThingPrincipalAttachment(name, <any>state, { ...opts, id: id });
    }

    /**
     * The AWS IoT Certificate ARN or Amazon Cognito Identity ID.
     */
    public readonly principal: pulumi.Output<ARN>;
    /**
     * The name of the thing.
     */
    public readonly thing: pulumi.Output<string>;

    /**
     * Create a ThingPrincipalAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ThingPrincipalAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ThingPrincipalAttachmentArgs | ThingPrincipalAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ThingPrincipalAttachmentState = argsOrState as ThingPrincipalAttachmentState | undefined;
            inputs["principal"] = state ? state.principal : undefined;
            inputs["thing"] = state ? state.thing : undefined;
        } else {
            const args = argsOrState as ThingPrincipalAttachmentArgs | undefined;
            if (!args || args.principal === undefined) {
                throw new Error("Missing required property 'principal'");
            }
            if (!args || args.thing === undefined) {
                throw new Error("Missing required property 'thing'");
            }
            inputs["principal"] = args ? args.principal : undefined;
            inputs["thing"] = args ? args.thing : undefined;
        }
        super("aws:iot/thingPrincipalAttachment:ThingPrincipalAttachment", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ThingPrincipalAttachment resources.
 */
export interface ThingPrincipalAttachmentState {
    /**
     * The AWS IoT Certificate ARN or Amazon Cognito Identity ID.
     */
    readonly principal?: pulumi.Input<ARN>;
    /**
     * The name of the thing.
     */
    readonly thing?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ThingPrincipalAttachment resource.
 */
export interface ThingPrincipalAttachmentArgs {
    /**
     * The AWS IoT Certificate ARN or Amazon Cognito Identity ID.
     */
    readonly principal: pulumi.Input<ARN>;
    /**
     * The name of the thing.
     */
    readonly thing: pulumi.Input<string>;
}
