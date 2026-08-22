# request (System API)

## Modules to Import

```TypeScript
```

## request

```TypeScript
export function request(param: RequestParameterForStage, callback: AsyncCallback<RequestCallbackParameters>): void
```

Plugin component request method used to send a request for the information of the template it wants.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginComponentManager-export function request(param: RequestParameterForStage, callback: AsyncCallback<RequestCallbackParameters>): void--><!--Device-pluginComponentManager-export function request(param: RequestParameterForStage, callback: AsyncCallback<RequestCallbackParameters>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [RequestParameterForStage](arkts-plugincomponentmanager-requestparameterforstage-i-sys.md) | Yes | Plugin component request parameters for stage. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[RequestCallbackParameters](arkts-plugincomponentmanager-requestcallbackparameters-i.md)&gt; | Yes | Plugin component request event callback. |

