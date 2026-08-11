# request (System API)

## Modules to Import

```TypeScript
import { PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## request

```TypeScript
function request(param: RequestParameterForStage, callback: AsyncCallback<RequestCallbackParameters>): void
```

Plugin component request method used to send a request for the information of the template it wants.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginComponentManager-function request(param: RequestParameterForStage, callback: AsyncCallback<RequestCallbackParameters>): void--><!--Device-pluginComponentManager-function request(param: RequestParameterForStage, callback: AsyncCallback<RequestCallbackParameters>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [RequestParameterForStage](arkts-arkui-plugincomponentmanager-requestparameterforstage-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;RequestCallbackParameters&gt; | Yes |
