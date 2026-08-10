# JsonElementDeserializable

Interface for types that can be serialized to JSON.Classes implementing this interface can be converted to a JsonElement.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-jsonx-export interface JsonElementDeserializable--><!--Device-jsonx-export interface JsonElementDeserializable-End-->

**系统能力：** SystemCapability.Utils.Lang

## fromJSON

```TypeScript
fromJSON(jsonElem: JsonElement): void
```

Deserializes a JsonElement into the object.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElementDeserializable-fromJSON(jsonElem: JsonElement): void--><!--Device-JsonElementDeserializable-fromJSON(jsonElem: JsonElement): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| jsonElem | [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 是 | The JsonElement to deserialize. |

