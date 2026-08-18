# OnReceiveDataCallback (System API)

```TypeScript
export type OnReceiveDataCallback = (data: Record<string, RecordData>) => void
```

Sets the callback for the ui extension to receive data from an ui extension component.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnReceiveDataCallback = (data: Record<string, RecordData>) => void--><!--Device-unnamed-export type OnReceiveDataCallback = (data: Record<string, RecordData>) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt; | Yes |
