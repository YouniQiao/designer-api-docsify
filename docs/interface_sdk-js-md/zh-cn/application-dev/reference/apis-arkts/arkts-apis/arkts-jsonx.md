# Jsonx

namespace of jsonx.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-export namespace jsonx--><!--Device-unnamed-export namespace jsonx-End-->

**系统能力：** SystemCapability.Utils.Lang

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [JsonElement](arkts-arkts-jsonx-jsonelement-c.md) | Core class representing a JSON element that can hold any valid JSON value.Provides type-safe access to JSON values with both strict and lenient APIs.The class maintains an invariant that only one type of value can be set at a time.Attempting to set multiple values will result in a JsonTypeError. |
| [JsonError](arkts-arkts-jsonx-jsonerror-c.md) | Base error class for JSON-related errors.Thrown when general JSON parsing or manipulation errors occur. |
| [JsonTypeError](arkts-arkts-jsonx-jsontypeerror-c.md) | Error thrown when attempting to access a JSON element with an incompatible type.For example, trying to get a string value from a number element. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [JsonElementDeserializable](arkts-arkts-jsonx-jsonelementdeserializable-i.md) | Interface for types that can be serialized to JSON.Classes implementing this interface can be converted to a JsonElement. |
| [JsonElementSerializable](arkts-arkts-jsonx-jsonelementserializable-i.md) | Interface for types that can be deserialized from JSON.Classes implementing this interface can be converted from a JsonElement. |
| [ParseOptions](arkts-arkts-jsonx-parseoptions-i.md) | ParseOptions for JSON.parse to pass BigIntMode. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [BigIntMode](arkts-arkts-jsonx-bigintmode-e.md) | Enumeration of BigIntMode. |
| [JsonType](arkts-arkts-jsonx-jsontype-e.md) | Enumeration of possible JSON value types.Used to identify the type of a JsonElement at runtime. |

