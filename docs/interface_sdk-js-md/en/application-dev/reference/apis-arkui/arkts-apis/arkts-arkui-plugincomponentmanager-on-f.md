# on

## Modules to Import

```TypeScript
import { pluginComponentManager, PluginComponentTemplate } from 'kits/@kit.ArkUI';
```

## on

```TypeScript
function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void
```

Listens for events of the request type and returns the requested data, or listens for events of the push type and receives the data pushed by the provider.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| eventType | string | Yes |
| callback | [OnPushEventCallback](arkts-arkui-plugincomponentmanager-onpusheventcallback-t.md) \| [OnRequestEventCallback](arkts-arkui-plugincomponentmanager-onrequesteventcallback-t.md) | Yes |
