# OnPushEventCallback

```TypeScript
type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,
    extraData: KVObject) => void
```

Registers the listener for the push event.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-pluginComponentManager-type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,    extraData: KVObject) => void--><!--Device-pluginComponentManager-type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,    extraData: KVObject) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Information about the push request sender. |
| template | [PluginComponentTemplate](../../apis-na/arkts-apis/arkts-na-plugincomponent-plugincomponenttemplate-i.md) | Yes | Name of the requested component template. |
| data | [KVObject](../../apis-na/arkts-apis/arkts-na-plugincomponentmanager-kvobject-t.md) | Yes | Data. |
| extraData | [KVObject](../../apis-na/arkts-apis/arkts-na-plugincomponentmanager-kvobject-t.md) | Yes | Extra data. |

