# ScopeComparable

**ScopeComparable** 类型的值用于实现 **compareTo** 方法。因此，请确保输入参数是可比较的。

**起始版本：** 7

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## compareTo

```TypeScript
compareTo(other: ScopeComparable): boolean
```

比较两个值并返回布尔值。

**起始版本：** 8

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| other | [ScopeComparable](arkts-arkts-util-scopecomparable-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
