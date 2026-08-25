# Scope

Scope 接口用于描述字段的有效范围。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [ScopeHelper](arkts-arkts-util-scopehelper-c.md)

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [clamp](arkts-arkts-util-scopehelper-c.md#clamp)

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

用于创建具有指定上下限的 **Scope** 对象的构造函数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** constructor

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

判断一个值是否在此 **Scope** 范围内。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [contains](arkts-arkts-util-lrucache-c.md#contains)

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
contains(range: Scope): boolean
```

判断一个范围是否在此 **Scope** 范围内。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [contains](arkts-arkts-util-lrucache-c.md#contains)

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## expand

```TypeScript
expand(lowerObj: ScopeType, upperObj: ScopeType): Scope
```

获取此 **Scope** 与给定上下限的并集。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** expand

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

## expand

```TypeScript
expand(range: Scope): Scope
```

获取此 **Scope** 与给定 **Scope** 的并集。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** expand

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

## expand

```TypeScript
expand(value: ScopeType): Scope
```

获取此 **Scope** 与给定值的并集。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** expand

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

## getLower

```TypeScript
getLower(): ScopeType
```

获取此 **Scope** 的下限。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getLower](arkts-arkts-util-scopehelper-c.md#getlower)

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getUpper](arkts-arkts-util-scopehelper-c.md#getupper)

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| [ScopeType](arkts-arkts-util-scopetype-t.md) |

## intersect

```TypeScript
intersect(range: Scope): Scope
```

获取此 **Scope** 与给定 **Scope** 的交集。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** intersect

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| range | [Scope](arkts-arkts-util-scope-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

## intersect

```TypeScript
intersect(lowerObj: ScopeType, upperObj: ScopeType): Scope
```

获取此 **Scope** 与给定上下限的交集。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** intersect

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lowerObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |
| upperObj | [ScopeType](arkts-arkts-util-scopetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Scope](arkts-arkts-util-scope-c.md) |

## toString

```TypeScript
toString(): string
```

获取包含此 **Scope** 的字符串表示形式。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [toString](arkts-arkts-util-lrucache-c.md#tostring)

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 |
| --- |
| string |
