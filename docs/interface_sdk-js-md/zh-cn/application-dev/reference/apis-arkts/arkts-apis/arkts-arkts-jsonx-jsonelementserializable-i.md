# JsonElementSerializable

可从JSON反序列化的类型所实现的接口。 实现该接口的类可以由JsonElement转换得到。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

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

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) |
