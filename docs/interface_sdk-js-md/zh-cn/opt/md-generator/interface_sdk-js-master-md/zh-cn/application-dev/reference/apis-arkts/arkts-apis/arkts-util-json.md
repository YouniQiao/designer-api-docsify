# @ohos.util.json

本模块提供了将JSON文本转换为JSON对象或值，以及将对象转换为JSON文本等功能。模块基于标准JSON规范实现解析与序列化，通过Transformer机制支持自定义转换，通过BigIntMode策略解决BigInt兼容问题，并提供has/remove操作便于对解析结果进行属性查询与删除。

**起始版本：** 12

<!--Device-unnamed-declare namespace json--><!--Device-unnamed-declare namespace json-End-->

**系统能力：** SystemCapability.Utils.Lang

## 汇总

### 函数

| 名称 |
| --- |
| [has](arkts-arkts-json-has-f.md#has) |
| [parse](arkts-arkts-json-parse-f.md#parse) |
| [remove](arkts-arkts-json-remove-f.md#remove) |
| [stringify](arkts-arkts-json-stringify-f.md#stringify) |
| [stringify](arkts-arkts-json-stringify-f.md#stringify-1) |

### 接口

| 名称 |
| --- |
| [ParseOptions](arkts-arkts-json-parseoptions-i.md) |

### 枚举

| 名称 |
| --- |
| [BigIntMode](arkts-arkts-json-bigintmode-e.md) |

### 类型

| 名称 |
| --- |
| [Transformer](arkts-arkts-json-transformer-t.md) |
