# ScopeHelper

提供定义字段有效范围的 API。此类的构造函数创建具有上下限的可比较对象。

**起始版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## clamp

```TypeScript
clamp(value: ScopeType): ScopeType
```

将一个值限制在此 **Scope** 范围内。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) |

## constructor

```TypeScript
constructor(lowerObj: ScopeType, upperObj: ScopeType)
```

用于创建具有指定上下限的 **ScopeHelper** 对象的构造函数。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |

## contains

```TypeScript
contains(value: ScopeType): boolean
```

判断一个范围是否在此 **Scope** 范围内。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## contains

```TypeScript
contains(range: ScopeHelper): boolean
```

判断一个范围是否在此 **Scope** 范围内。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## expand

```TypeScript
expand(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper
```

获取此 **Scope** 与给定上下限的并集。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) |

## expand

```TypeScript
expand(range: ScopeHelper): ScopeHelper
```

获取此 **Scope** 与给定 **Scope** 的并集。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) |

## expand

```TypeScript
expand(value: ScopeType): ScopeHelper
```

获取此 **Scope** 与给定值的并集。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) |

## getLower

```TypeScript
getLower(): ScopeType
```

获取此 **Scope** 的下限。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) |

## getUpper

```TypeScript
getUpper(): ScopeType
```

获取此 **Scope** 的上限。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) |

## intersect

```TypeScript
intersect(range: ScopeHelper): ScopeHelper
```

获取此 **Scope** 与给定 **Scope** 的交集。如果交集为空，则抛出异常。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [ScopeHelper](arkts-arkts-util-scopehelper-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) |

## intersect

```TypeScript
intersect(lowerObj: ScopeType, upperObj: ScopeType): ScopeHelper
```

获取此 **Scope** 与给定上下限的交集。如果交集为空，则抛出异常。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ScopeHelper](arkts-arkts-util-scopehelper-c.md) |

## toString

```TypeScript
toString(): string
```

获取包含此 **Scope** 的字符串表示形式。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |
