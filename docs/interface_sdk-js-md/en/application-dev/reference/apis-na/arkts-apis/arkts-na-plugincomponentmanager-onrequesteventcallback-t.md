# OnRequestEventCallback

```TypeScript
export type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult
```

Plugin component request event callback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-pluginComponentManager-export type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult--><!--Device-pluginComponentManager-export type OnRequestEventCallback = (source: Want, name: string, data: KVObject) => RequestEventResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| source | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Request the sender to provide relevant information. |
| name | string | Yes | Template name. |
| data | [KVObject](arkts-na-plugincomponentmanager-kvobject-t.md) | Yes | data info. |

**Return value:**

| Type | Description |
| --- | --- |
| [RequestEventResult](arkts-na-plugincomponentmanager-requesteventresult-i.md) | - |

