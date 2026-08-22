# ToJSONType

```TypeScript
export declare type ToJSONType<T> = (value: T) => jsonx.JsonElement
```

Define toJson type function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type ToJSONType<T> = (value: T) => jsonx.JsonElement--><!--Device-unnamed-export declare type ToJSONType<T> = (value: T) => jsonx.JsonElement-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | toJson value |

**Return value:**

| Type | Description |
| --- | --- |
| jsonx.JsonElement | Json stringify element object |

