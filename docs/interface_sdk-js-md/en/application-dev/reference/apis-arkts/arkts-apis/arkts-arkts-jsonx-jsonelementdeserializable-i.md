# JsonElementDeserializable

Interface for types that can be serialized to JSON. Classes implementing this interface can be converted to a JsonElement.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-jsonx-export interface JsonElementDeserializable--><!--Device-jsonx-export interface JsonElementDeserializable-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## fromJSON

```TypeScript
fromJSON(jsonElem: JsonElement): void
```

Deserializes a JsonElement into the object.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElementDeserializable-fromJSON(jsonElem: JsonElement): void--><!--Device-JsonElementDeserializable-fromJSON(jsonElem: JsonElement): void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| jsonElem | [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | Yes | The JsonElement to deserialize. |

