# request

## Modules to Import

```TypeScript
import { pluginComponentManager, PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## request

```TypeScript
function request(param: RequestParameters, callback: AsyncCallback<RequestCallbackParameters>): void
```

Requests the component from the component provider.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [RequestParameters](arkts-arkui-plugincomponentmanager-requestparameters-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RequestCallbackParameters](arkts-arkui-plugincomponentmanager-requestcallbackparameters-i.md)&gt; | Yes |
