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

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes | Indicates the receive data callback to set. |

