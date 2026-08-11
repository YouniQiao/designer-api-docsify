# OnReceiveDataForResultCallback (System API)

```TypeScript
export type OnReceiveDataForResultCallback = (data: Record<string, RecordData>) => Record<string, RecordData>
```

Sets the callback with return value for the ui extension to receive data from an ui extension component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnReceiveDataForResultCallback = (data: Record<string, RecordData>) => Record<string, RecordData>--><!--Device-unnamed-export type OnReceiveDataForResultCallback = (data: Record<string, RecordData>) => Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | Yes | Indicates the receive data callback to set. |

**Return value:**

| Type | Description |
| --- | --- |
| [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, RecordData&gt; | Returns the custom data. |

