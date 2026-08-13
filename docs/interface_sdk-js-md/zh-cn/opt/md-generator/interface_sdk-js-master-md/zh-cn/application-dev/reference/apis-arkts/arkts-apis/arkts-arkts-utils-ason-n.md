# ASON

为支持将JSON字符串解析为共享数据，即Sendable支持的数据类型，ArkTS语言基础库新增了ASON工具。ASON工具支持解析JSON字符串并生成共享数据，用于跨并发实例引用传递，同时也支持将共享数据转换为JSON字符串。

**起始版本：** 12

**废弃版本：** -1

<!--Device-utils-namespace ASON--><!--Device-utils-namespace ASON-End-->

**系统能力：** SystemCapability.Utils.Lang

## 汇总

### 函数

| 名称 |
| --- |
| [parse](arkts-arkts-ason-parse-f.md#parse) |
| [stringify](arkts-arkts-ason-stringify-f.md#stringify) |

### 接口

| 名称 |
| --- |
| [ParseOptions](arkts-arkts-ason-parseoptions-i.md) |

### 枚举

| 名称 |
| --- |
| [BigIntMode](arkts-arkts-ason-bigintmode-e.md) |
| [ParseReturnType](arkts-arkts-ason-parsereturntype-e.md) |

### 类型

| 名称 |
| --- |
| [ISendable](arkts-arkts-ason-isendable-t.md) |
| [Transformer](arkts-arkts-ason-transformer-t.md) |
