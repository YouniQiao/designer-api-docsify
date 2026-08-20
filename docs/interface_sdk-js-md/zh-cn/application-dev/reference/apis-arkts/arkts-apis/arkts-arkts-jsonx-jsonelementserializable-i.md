# JsonElementSerializable

可从JSON反序列化的类型所实现的接口。 实现该接口的类可以由JsonElement转换得到。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-jsonx-export interface JsonElementSerializable--><!--Device-jsonx-export interface JsonElementSerializable-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## toJSON

```TypeScript
toJSON(): JsonElement
```

将该对象转换为JsonElement。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-JsonElementSerializable-toJSON(): JsonElement--><!--Device-JsonElementSerializable-toJSON(): JsonElement-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 对应的JsonElement表示。 |

