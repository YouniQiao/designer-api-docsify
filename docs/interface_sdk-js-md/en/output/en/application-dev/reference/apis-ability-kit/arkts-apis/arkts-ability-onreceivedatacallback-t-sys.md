# OnReceiveDataCallback (System API)

```TypeScript
export type OnReceiveDataCallback = (data: Record<string, RecordData>) => void
```

Sets the callback for the ui extension to receive data from an ui extension component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnReceiveDataCallback = (data: Record<string, RecordData>) => void--><!--Device-unnamed-export type OnReceiveDataCallback = (data: Record<string, RecordData>) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, RecordData&gt; | Yes | Indicates the receive data callback to set.  |

