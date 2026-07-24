# OnPushEventCallback

```TypeScript
type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,
    extraData: KVObject) => void
```

Registers the listener for the push event.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-pluginComponentManager-type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,    extraData: KVObject) => void--><!--Device-pluginComponentManager-type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,    extraData: KVObject) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [Want](arkts-arkui-want-t-sys.md) | Yes | Information about the push request sender.  |
| template | [PluginComponentTemplate](arkts-arkui-plugincomponent-plugincomponenttemplate-i.md) | Yes | Name of the requested component template.  |
| data | [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md) | Yes | Data.  |
| extraData | [KVObject](arkts-arkui-plugincomponentmanager-kvobject-t.md) | Yes | Extra data.  |

