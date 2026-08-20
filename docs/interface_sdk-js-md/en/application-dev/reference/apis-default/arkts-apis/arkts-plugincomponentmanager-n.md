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
| [push](arkts-plugincomponentmanager-push-f.md) | Plugin component push method. |
| [request](arkts-plugincomponentmanager-request-f.md) | Plugin component request method. |
| [on_string](arkts-plugincomponentmanager-onstring-f.md#on_string) | Plugin component event listener. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [push](arkts-plugincomponentmanager-push-f-sys.md) | Plugin component push method used to send the information of the template it provides. |
| [request](arkts-plugincomponentmanager-request-f-sys.md) | Plugin component request method used to send a request for the information of the template it wants. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [PushParameters](arkts-plugincomponentmanager-pushparameters-i.md) | Plugin component push parameters. |
| [RequestParameters](arkts-plugincomponentmanager-requestparameters-i.md) | Plugin component request parameters. |
| [RequestCallbackParameters](arkts-plugincomponentmanager-requestcallbackparameters-i.md) | Plugin component request callback parameters. |
| [RequestEventResult](arkts-plugincomponentmanager-requesteventresult-i.md) | Plugin component request event result value. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [PushParameterForStage](arkts-plugincomponentmanager-pushparameterforstage-i-sys.md) | Plugin component push parameters which is used in push function. |
| [RequestParameterForStage](arkts-plugincomponentmanager-requestparameterforstage-i-sys.md) | Plugin component request parameters which is used in request function. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [KVObject](arkts-plugincomponentmanager-kvobject-t.md) | Defines KVObject. |
| [OnPushEventCallback](arkts-plugincomponentmanager-onpusheventcallback-t.md) | Plugin component push event callback. |
| [OnRequestEventCallback](arkts-plugincomponentmanager-onrequesteventcallback-t.md) | Plugin component request event callback. |

