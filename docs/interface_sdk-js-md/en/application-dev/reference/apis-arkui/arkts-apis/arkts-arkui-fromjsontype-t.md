# FromJSONType

```TypeScript
export declare type FromJSONType<T> = (element: jsonx.JsonElement) => T
```

Define fromJson type function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type FromJSONType<T> = (element: jsonx.JsonElement) => T--><!--Device-unnamed-export declare type FromJSONType<T> = (element: jsonx.JsonElement) => T-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| element | jsonx.JsonElement | Yes | json element  |

**Return value:**

| Type | Description |
| --- | --- |
| T | deserialization result  |

