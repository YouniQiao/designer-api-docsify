# ASON(Defines the utils for ArkTS)

为支持将JSON字符串解析为共享数据，即Sendable支持的数据类型，ArkTS语言基础库新增了ASON工具。ASON工具支持解析JSON字符串并生成共享数据，用于跨并发实例引用传递，同时也支持将共享数据转换为JSON字符串。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { ArkTSUtils } from '@kit.ArkTS';
```

## 汇总

### 函数

| 名称 |
| --- |
| [parse(Defines the utils for ArkTS)](arkts-arkts-ason-parse-f.md) |
| [stringify(Defines the utils for ArkTS)](arkts-arkts-ason-stringify-f.md) |

### 接口

| 名称 |
| --- |
| [ParseOptions(Defines the utils for ArkTS)](arkts-arkts-ason-parseoptions-i.md) |

### 枚举

| 名称 |
| --- |
| [BigIntMode(Defines the utils for ArkTS)](arkts-arkts-ason-bigintmode-e.md) |
| [ParseReturnType(Defines the utils for ArkTS)](arkts-arkts-ason-parsereturntype-e.md) |

### 类型

| 名称 |
| --- |
| [ISendable(Defines the utils for ArkTS)](arkts-arkts-ason-isendable-t.md) |
| [Transformer(Defines the utils for ArkTS)](arkts-arkts-ason-transformer-t.md) |
