# Jsonx

jsonx命名空间。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export namespace jsonx--><!--Device-unnamed-export namespace jsonx-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | 表示JSON元素的核心类，可保存任意合法的JSON值。 同时提供严格与宽松两套API，以类型安全的方式访问JSON值。 该类保持一个不变式：同一时刻只能设置一种类型的值。 尝试设置多个值将导致JsonTypeError。 |
| [JsonError](arkts-arkts-jsonx-jsonerror-c.md) | JSON相关错误的基础错误类。 在发生一般性JSON解析或操作错误时抛出。 |
| [JsonTypeError](arkts-arkts-jsonx-jsontypeerror-c.md) | 以不兼容的类型访问JSON元素时抛出的错误。 例如，尝试从number类型的元素中获取字符串值。 |

### 接口

| 名称 | 说明 |
| --- | --- |
| [JsonElementDeserializable](arkts-arkts-jsonx-jsonelementdeserializable-i.md) | 可序列化为JSON的类型所实现的接口。 实现该接口的类可以转换为JsonElement。 |
| [JsonElementSerializable](arkts-arkts-jsonx-jsonelementserializable-i.md) | 可从JSON反序列化的类型所实现的接口。 实现该接口的类可以由JsonElement转换得到。 |
| [ParseOptions](arkts-arkts-jsonx-parseoptions-i.md) | JSON.parse的ParseOptions，用于传入BigIntMode。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [BigIntMode](arkts-arkts-jsonx-bigintmode-e.md) | BigIntMode枚举。 |
| [JsonType](arkts-arkts-jsonx-jsontype-e.md) | JSON值可能类型的枚举。 用于在运行时识别JsonElement的类型。 |

