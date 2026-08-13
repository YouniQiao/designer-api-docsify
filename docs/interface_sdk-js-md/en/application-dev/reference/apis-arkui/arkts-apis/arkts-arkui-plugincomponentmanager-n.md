# pluginComponentManager

Implements a plugin component manager.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace pluginComponentManager--><!--Device-unnamed-declare namespace pluginComponentManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { PluginComponentTemplate } from '@kit.ArkUI';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [push](arkts-arkui-plugincomponentmanager-push-f.md#push) | Pushes the component and data to the component user. |
| [request](arkts-arkui-plugincomponentmanager-request-f.md#request) | Requests the component from the component provider. |
| [on_string](arkts-arkui-plugincomponentmanager-onstring-f.md#on_string) | Listens for events of the request type and returns the requested data, or listens for events of the push type and receives the data pushed by the provider. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [push](arkts-arkui-plugincomponentmanager-push-f-sys.md#push-(System-API)) | Plugin component push method used to send the information of the template it provides. |
| [request](arkts-arkui-plugincomponentmanager-request-f-sys.md#request-(System-API)) | Plugin component request method used to send a request for the information of the template it wants. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [PushParameters](arkts-arkui-plugincomponentmanager-pushparameters-i.md) | Defines the parameters required when using the **PluginManager.Push** API. |
| [RequestParameters](arkts-arkui-plugincomponentmanager-requestparameters-i.md) | Defines the parameters required when using the **PluginManager.Request** API. |
| [RequestCallbackParameters](arkts-arkui-plugincomponentmanager-requestcallbackparameters-i.md) | Provides the result returned after the **PluginManager.Request** API is called. |
| [RequestEventResult](arkts-arkui-plugincomponentmanager-requesteventresult-i.md) | Provides the result returned after the request listener is registered and the requested event is received. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [PushParameterForStage](arkts-arkui-plugincomponentmanager-pushparameterforstage-i-sys.md) | Plugin component push parameters which is used in push function. |
| [RequestParameterForStage](arkts-arkui-plugincomponentmanager-requestparameterforstage-i-sys.md) | Plugin component request parameters which is used in request function. |
<!--DelEnd-->

### Types

| Name | Description |
| --- | --- |
| [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md) | Defines a key-value pair data structure that conforms to JSON format. |
| [OnPushEventCallback](arkts-arkui-plugincomponentmanager-onpusheventcallback-t.md) | Registers the listener for the push event. |
| [OnRequestEventCallback](arkts-arkui-plugincomponentmanager-onrequesteventcallback-t.md) | Registers the listener for the request event. |

