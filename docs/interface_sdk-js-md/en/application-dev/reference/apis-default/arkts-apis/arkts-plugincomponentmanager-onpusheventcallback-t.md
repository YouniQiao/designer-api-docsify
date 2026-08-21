# OnPushEventCallback

```TypeScript
export type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,
    extraData: KVObject) => void
```

Plugin component push event callback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginComponentManager-export type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,    extraData: KVObject) => void--><!--Device-pluginComponentManager-export type OnPushEventCallback = (source: Want, template: PluginComponentTemplate, data: KVObject,    extraData: KVObject) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-appabilitywant-want-c.md) | Yes | Push request sender's relevant information. |
| template | [PluginComponentTemplate](arkts-plugincomponent-plugincomponenttemplate-i.md) | Yes | Request component template name. |
| data | [KVObject](arkts-plugincomponentmanager-kvobject-t.md) | Yes | data info. |
| extraData | [KVObject](arkts-plugincomponentmanager-kvobject-t.md) | Yes | extra data info. |

