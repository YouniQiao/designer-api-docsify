# push (System API)

## Modules to Import

```TypeScript
```

## push

```TypeScript
export function push(param: PushParameterForStage, callback: AsyncCallback<void>): void
```

Plugin component push method used to send the information of the template it provides.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginComponentManager-export function push(param: PushParameterForStage, callback: AsyncCallback<void>): void--><!--Device-pluginComponentManager-export function push(param: PushParameterForStage, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| param | [PushParameterForStage](arkts-plugincomponentmanager-pushparameterforstage-i-sys.md) | Yes | Plugin component push parameters for stage. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Plugin component push event callback. |

