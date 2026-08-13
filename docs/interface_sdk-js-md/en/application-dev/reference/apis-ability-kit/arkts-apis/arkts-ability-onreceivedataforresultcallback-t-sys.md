# OnReceiveDataForResultCallback (System API)

```TypeScript
export type OnReceiveDataForResultCallback = (data: Record<string, RecordData>) => Record<string, RecordData>
```

Sets the callback with return value for the ui extension to receive data from an ui extension component.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnReceiveDataForResultCallback = (data: Record<string, RecordData>) => Record<string, RecordData>--><!--Device-unnamed-export type OnReceiveDataForResultCallback = (data: Record<string, RecordData>) => Record<string, RecordData>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Yes | Indicates the receive data callback to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt; | Returns the custom data. |

