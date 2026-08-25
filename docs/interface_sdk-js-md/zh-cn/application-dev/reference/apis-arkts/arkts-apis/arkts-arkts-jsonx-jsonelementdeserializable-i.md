# JsonElementDeserializable

可序列化为JSON的类型所实现的接口。 实现该接口的类可以转换为JsonElement。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## fromJSON

```TypeScript
fromJSON(jsonElem: JsonElement): void
```

将JsonElement反序列化到该对象中。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| jsonElem | [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 是 |
