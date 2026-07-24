# on

## Modules to Import

```TypeScript
import { PluginComponentTemplate } from '@kit.ArkUI';
```

## on

```TypeScript
function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void
```

Listens for events of the request type and returns the requested data, or listens for events of the push type and receives the data pushed by the provider.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-pluginComponentManager-function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void--><!--Device-pluginComponentManager-function on(eventType: string, callback: OnPushEventCallback | OnRequestEventCallback): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventType | string | Yes | Type of the event to listen for. The options are as follows:<br>**"push"**: The component provider pushes data to the component user.<br>**"request"**: The component user proactively requests data from the component provider. |
| callback | [OnPushEventCallback](arkts-arkui-plugincomponentmanager-onpusheventcallback-t.md) \| OnRequestEventCallback | Yes | Callback used to return the result. The type is [OnPushEventCallback](arkts-arkui-plugincomponentmanager-onpusheventcallback-t.md) for the push event and [OnRequestEventCallback](arkts-arkui-plugincomponentmanager-onrequesteventcallback-t.md) for the request event. |

**Example**

```TypeScript
import { pluginComponentManager, PluginComponentTemplate } from '@kit.ArkUI';
import { Want } from '@kit.AbilityKit';

function onPushListener(source:Want, template:PluginComponentTemplate, data:pluginComponentManager.KVObject, extraData:pluginComponentManager.KVObject) {
  console.info("onPushListener template.source=" + template.source);
  console.info("onPushListener source=" + JSON.stringify(source));
  console.info("onPushListener template=" + JSON.stringify(template));
  console.info("onPushListener data=" + JSON.stringify(data));
  console.info("onPushListener extraData=" + JSON.stringify(extraData));
}
function onRequestListener(source:Want, name:string, data:pluginComponentManager.KVObject) {
  console.info("onRequestListener");
  console.info("onRequestListener source=" + JSON.stringify(source));
  console.info("onRequestListener name=" + name);
  console.info("onRequestListener data=" + JSON.stringify(data));
  let RtnData:Record<string,string|pluginComponentManager.KVObject> = { 'template': "ets/pages/plugin.js", 'data': data };
  return RtnData;
}
pluginComponentManager.on("push", onPushListener);
pluginComponentManager.on("request", onRequestListener);

```

