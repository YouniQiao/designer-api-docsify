# JsonElementDeserializable

Interface for types that can be serialized to JSON. Classes implementing this interface can be converted to a JsonElement.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-jsonx-export interface JsonElementDeserializable--><!--Device-jsonx-export interface JsonElementDeserializable-End-->

**System capability:** SystemCapability.Utils.Lang

## fromJSON

```TypeScript
fromJSON(jsonElem: JsonElement): void
```

Deserializes a JsonElement into the object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElementDeserializable-fromJSON(jsonElem: JsonElement): void--><!--Device-JsonElementDeserializable-fromJSON(jsonElem: JsonElement): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jsonElem | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The JsonElement to deserialize. |

