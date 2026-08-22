# OnRequestEventCallback

```TypeScript
type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult
```

Registers the listener for the request event.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-pluginComponentManager-type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult--><!--Device-pluginComponentManager-type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Information about the request sender. |
| name | string | Yes | Template name. |
| data | [KVObject](../../apis-default/arkts-apis/arkts-plugincomponentmanager-kvobject-t.md) | Yes | Data. |

**Return value:**

| Type | Description |
| --- | --- |
| [RequestEventResult](../../apis-default/arkts-apis/arkts-plugincomponentmanager-requesteventresult-i.md) | Provides the result returned after the request listener is registered and the requested event is received. |

**Examples**

```TypeScript
import { pluginComponentManager } from '@kit.ArkUI';
import { Want } from '@kit.AbilityKit';

function onRequestListener(source: Want, name: string, data: pluginComponentManager.KVObject) {
  console.info("onRequestListener");
  console.info("onRequestListener source=" + JSON.stringify(source));
  console.info("onRequestListener name=" + name);
  console.info("onRequestListener data=" + JSON.stringify(data));
  let RtnData: Record<string, string | pluginComponentManager.KVObject> = {
    'template': "ets/pages/plugin.js",
    'data': data,
  }
  return RtnData;
}
```

