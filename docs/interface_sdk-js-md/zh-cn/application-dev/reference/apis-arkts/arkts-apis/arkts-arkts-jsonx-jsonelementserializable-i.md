# JsonElementSerializable

Interface for types that can be deserialized from JSON.Classes implementing this interface can be converted from a JsonElement.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-jsonx-export interface JsonElementSerializable--><!--Device-jsonx-export interface JsonElementSerializable-End-->

**系统能力：** SystemCapability.Utils.Lang

## toJSON

```TypeScript
toJSON(): JsonElement
```

Converts the object to a JsonElement.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElementSerializable-toJSON(): JsonElement--><!--Device-JsonElementSerializable-toJSON(): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | The JsonElement representation. |

