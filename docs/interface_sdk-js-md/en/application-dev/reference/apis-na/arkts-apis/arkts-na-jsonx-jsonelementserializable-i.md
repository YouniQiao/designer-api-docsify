# JsonElementSerializable

Interface for types that can be deserialized from JSON. Classes implementing this interface can be converted from a JsonElement.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-jsonx-export interface JsonElementSerializable--><!--Device-jsonx-export interface JsonElementSerializable-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## toJSON

```TypeScript
toJSON(): JsonElement
```

Converts the object to a JsonElement.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-JsonElementSerializable-toJSON(): JsonElement--><!--Device-JsonElementSerializable-toJSON(): JsonElement-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| [JsonElement](arkts-na-jsonx-jsonelement-c.md) | The JsonElement representation. |

