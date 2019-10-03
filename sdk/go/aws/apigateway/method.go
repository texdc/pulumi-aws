// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a HTTP Method for an API Gateway Resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method.html.markdown.
type Method struct {
	s *pulumi.ResourceState
}

// NewMethod registers a new resource with the given unique name, arguments, and options.
func NewMethod(ctx *pulumi.Context,
	name string, args *MethodArgs, opts ...pulumi.ResourceOpt) (*Method, error) {
	if args == nil || args.Authorization == nil {
		return nil, errors.New("missing required argument 'Authorization'")
	}
	if args == nil || args.HttpMethod == nil {
		return nil, errors.New("missing required argument 'HttpMethod'")
	}
	if args == nil || args.ResourceId == nil {
		return nil, errors.New("missing required argument 'ResourceId'")
	}
	if args == nil || args.RestApi == nil {
		return nil, errors.New("missing required argument 'RestApi'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["apiKeyRequired"] = nil
		inputs["authorization"] = nil
		inputs["authorizationScopes"] = nil
		inputs["authorizerId"] = nil
		inputs["httpMethod"] = nil
		inputs["requestModels"] = nil
		inputs["requestParameters"] = nil
		inputs["requestValidatorId"] = nil
		inputs["resourceId"] = nil
		inputs["restApi"] = nil
	} else {
		inputs["apiKeyRequired"] = args.ApiKeyRequired
		inputs["authorization"] = args.Authorization
		inputs["authorizationScopes"] = args.AuthorizationScopes
		inputs["authorizerId"] = args.AuthorizerId
		inputs["httpMethod"] = args.HttpMethod
		inputs["requestModels"] = args.RequestModels
		inputs["requestParameters"] = args.RequestParameters
		inputs["requestValidatorId"] = args.RequestValidatorId
		inputs["resourceId"] = args.ResourceId
		inputs["restApi"] = args.RestApi
	}
	s, err := ctx.RegisterResource("aws:apigateway/method:Method", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Method{s: s}, nil
}

// GetMethod gets an existing Method resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMethod(ctx *pulumi.Context,
	name string, id pulumi.ID, state *MethodState, opts ...pulumi.ResourceOpt) (*Method, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["apiKeyRequired"] = state.ApiKeyRequired
		inputs["authorization"] = state.Authorization
		inputs["authorizationScopes"] = state.AuthorizationScopes
		inputs["authorizerId"] = state.AuthorizerId
		inputs["httpMethod"] = state.HttpMethod
		inputs["requestModels"] = state.RequestModels
		inputs["requestParameters"] = state.RequestParameters
		inputs["requestValidatorId"] = state.RequestValidatorId
		inputs["resourceId"] = state.ResourceId
		inputs["restApi"] = state.RestApi
	}
	s, err := ctx.ReadResource("aws:apigateway/method:Method", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Method{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Method) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Method) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Specify if the method requires an API key
func (r *Method) ApiKeyRequired() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["apiKeyRequired"])
}

// The type of authorization used for the method (`NONE`, `CUSTOM`, `AWS_IAM`, `COGNITO_USER_POOLS`)
func (r *Method) Authorization() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["authorization"])
}

// The authorization scopes used when the authorization is `COGNITO_USER_POOLS`
func (r *Method) AuthorizationScopes() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["authorizationScopes"])
}

// The authorizer id to be used when the authorization is `CUSTOM` or `COGNITO_USER_POOLS`
func (r *Method) AuthorizerId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["authorizerId"])
}

// The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
func (r *Method) HttpMethod() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["httpMethod"])
}

// A map of the API models used for the request's content type
// where key is the content type (e.g. `application/json`)
// and value is either `Error`, `Empty` (built-in models) or `apigateway.Model`'s `name`.
func (r *Method) RequestModels() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["requestModels"])
}

// A map of request parameters (from the path, query string and headers) that should be passed to the integration. The boolean value indicates whether the parameter is required (`true`) or optional (`false`).
// For example: `requestParameters = {"method.request.header.X-Some-Header" = true "method.request.querystring.some-query-param" = true}` would define that the header `X-Some-Header` and the query string `some-query-param` must be provided in the request.
func (r *Method) RequestParameters() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["requestParameters"])
}

// The ID of a `apigateway.RequestValidator`
func (r *Method) RequestValidatorId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["requestValidatorId"])
}

// The API resource ID
func (r *Method) ResourceId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["resourceId"])
}

// The ID of the associated REST API
func (r *Method) RestApi() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["restApi"])
}

// Input properties used for looking up and filtering Method resources.
type MethodState struct {
	// Specify if the method requires an API key
	ApiKeyRequired interface{}
	// The type of authorization used for the method (`NONE`, `CUSTOM`, `AWS_IAM`, `COGNITO_USER_POOLS`)
	Authorization interface{}
	// The authorization scopes used when the authorization is `COGNITO_USER_POOLS`
	AuthorizationScopes interface{}
	// The authorizer id to be used when the authorization is `CUSTOM` or `COGNITO_USER_POOLS`
	AuthorizerId interface{}
	// The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
	HttpMethod interface{}
	// A map of the API models used for the request's content type
	// where key is the content type (e.g. `application/json`)
	// and value is either `Error`, `Empty` (built-in models) or `apigateway.Model`'s `name`.
	RequestModels interface{}
	// A map of request parameters (from the path, query string and headers) that should be passed to the integration. The boolean value indicates whether the parameter is required (`true`) or optional (`false`).
	// For example: `requestParameters = {"method.request.header.X-Some-Header" = true "method.request.querystring.some-query-param" = true}` would define that the header `X-Some-Header` and the query string `some-query-param` must be provided in the request.
	RequestParameters interface{}
	// The ID of a `apigateway.RequestValidator`
	RequestValidatorId interface{}
	// The API resource ID
	ResourceId interface{}
	// The ID of the associated REST API
	RestApi interface{}
}

// The set of arguments for constructing a Method resource.
type MethodArgs struct {
	// Specify if the method requires an API key
	ApiKeyRequired interface{}
	// The type of authorization used for the method (`NONE`, `CUSTOM`, `AWS_IAM`, `COGNITO_USER_POOLS`)
	Authorization interface{}
	// The authorization scopes used when the authorization is `COGNITO_USER_POOLS`
	AuthorizationScopes interface{}
	// The authorizer id to be used when the authorization is `CUSTOM` or `COGNITO_USER_POOLS`
	AuthorizerId interface{}
	// The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
	HttpMethod interface{}
	// A map of the API models used for the request's content type
	// where key is the content type (e.g. `application/json`)
	// and value is either `Error`, `Empty` (built-in models) or `apigateway.Model`'s `name`.
	RequestModels interface{}
	// A map of request parameters (from the path, query string and headers) that should be passed to the integration. The boolean value indicates whether the parameter is required (`true`) or optional (`false`).
	// For example: `requestParameters = {"method.request.header.X-Some-Header" = true "method.request.querystring.some-query-param" = true}` would define that the header `X-Some-Header` and the query string `some-query-param` must be provided in the request.
	RequestParameters interface{}
	// The ID of a `apigateway.RequestValidator`
	RequestValidatorId interface{}
	// The API resource ID
	ResourceId interface{}
	// The ID of the associated REST API
	RestApi interface{}
}
