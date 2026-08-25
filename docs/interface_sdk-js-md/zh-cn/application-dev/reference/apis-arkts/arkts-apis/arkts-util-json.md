# @ohos.util.json

本模块提供了将JSON文本转换为JSON对象或值，以及将对象转换为JSON文本等功能。模块基于标准JSON规范实现解析与序列化， 通过Transformer机制支持自定义转换，通过BigIntMode策略解决BigInt兼容问题，并提供has/remove操作便于对解析结果进行属性查询与删除。

**起始版本：** 12

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { JSON } from 'kits/@kit.ArkTS';
```

## 汇总

### 函数

| 名称 |
| --- |
| [has](arkts-arkts-json-has-f.md) |
| [parse](arkts-arkts-json-parse-f.md) |
| [remove](arkts-arkts-json-remove-f.md) |
| [stringify](arkts-arkts-json-stringify-f.md) |
| [stringify](arkts-arkts-json-stringify-f.md) |

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
