# pluginComponentManager

Plugin component manager interface.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace pluginComponentManager--><!--Device-unnamed-declare namespace pluginComponentManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [push](arkts-na-plugincomponentmanager-push-f.md#push) | Plugin component push method. |
| [request](arkts-na-plugincomponentmanager-request-f.md#request) | Plugin component request method. |
| [on_string](arkts-na-plugincomponentmanager-onstring-f.md#onstring) | Plugin component event listener. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [push](arkts-na-plugincomponentmanager-push-f-sys.md#push-system-api) | Plugin component push method used to send the information of the template it provides. |
| [request](arkts-na-plugincomponentmanager-request-f-sys.md#request-system-api) | Plugin component request method used to send a request for the information of the template it wants. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [PushParameters](arkts-na-plugincomponentmanager-pushparameters-i.md) | Plugin component push parameters. |
| [RequestParameters](arkts-na-plugincomponentmanager-requestparameters-i.md) | Plugin component request parameters. |
| [RequestCallbackParameters](arkts-na-plugincomponentmanager-requestcallbackparameters-i.md) | Plugin component request callback parameters. |
| [RequestEventResult](arkts-na-plugincomponentmanager-requesteventresult-i.md) | Plugin component request event result value. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [PushParameterForStage](arkts-na-plugincomponentmanager-pushparameterforstage-i-sys.md) | Plugin component push parameters which is used in push function. |
| [RequestParameterForStage](arkts-na-plugincomponentmanager-requestparameterforstage-i-sys.md) | Plugin component request parameters which is used in request function. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [KVObject](arkts-na-plugincomponentmanager-kvobject-t.md) | Defines KVObject. |
| [OnPushEventCallback](arkts-na-plugincomponentmanager-onpusheventcallback-t.md) | Plugin component push event callback. |
| [OnRequestEventCallback](arkts-na-plugincomponentmanager-onrequesteventcallback-t.md) | Plugin component request event callback. |

