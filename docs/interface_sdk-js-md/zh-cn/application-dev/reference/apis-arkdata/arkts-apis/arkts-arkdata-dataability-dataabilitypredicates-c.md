# DataAbilityPredicates

提供用于实现不同查询方法的谓词。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

## 导入模块

```TypeScript
import { dataAbility } from 'kits/@kit.ArkData';
```

## and

```TypeScript
and(): DataAbilityPredicates
```

将和条件添加到谓词中。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## beginsWith

```TypeScript
beginsWith(field: string, value: string): DataAbilityPredicates
```

配置谓词以匹配数据类型为string且值以指定字符串开头的字段。此方法类似于SQL语句的“value%”。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## beginWrap

```TypeScript
beginWrap(): DataAbilityPredicates
```

在谓词中添加左括号。此方法类似于SQL语句的“(”，需要与[endWrap](#endwrap)一起使用。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## between

```TypeScript
between(field: string, low: ValueType, high: ValueType): DataAbilityPredicates
```

配置谓词以匹配数据类型为ValueType且value在指定范围内的指定字段。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## contains

```TypeScript
contains(field: string, value: string): DataAbilityPredicates
```

配置谓词以匹配数据类型为string且value包含指定值的字段。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## distinct

```TypeScript
distinct(): DataAbilityPredicates
```

配置谓词以过滤重复记录并仅保留其中一个。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## endsWith

```TypeScript
endsWith(field: string, value: string): DataAbilityPredicates
```

配置谓词以匹配数据类型为string且值以指定字符串结尾的字段。此方法类似于SQL语句的“%value”。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## endWrap

```TypeScript
endWrap(): DataAbilityPredicates
```

在谓词中添加右括号。此方法类似于SQL语句的“)”，需要和[beginWrap](#beginwrap)一起使用。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## equalTo

```TypeScript
equalTo(field: string, value: ValueType): DataAbilityPredicates
```

配置谓词以匹配数据，数据的指定字段数据类型为ValueType且值等于指定值。此方法类似于SQL语句的“=”。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## glob

```TypeScript
glob(field: string, value: string): DataAbilityPredicates
```

配置谓词以匹配数据类型为string的指定字段。与like方法不同，该方法的输入参数区分大小写。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## greaterThan

```TypeScript
greaterThan(field: string, value: ValueType): DataAbilityPredicates
```

配置谓词以匹配数据类型为ValueType且值大于指定值的字段。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: ValueType): DataAbilityPredicates
```

配置谓词以匹配数据类型为ValueType且value大于或等于指定值的字段。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## groupBy

```TypeScript
groupBy(fields: Array<string>): DataAbilityPredicates
```

配置谓词按指定列分组查询结果。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fields](arkts-arkdata-cloudextension-table-i-sys.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## in

```TypeScript
in(field: string, value: Array<ValueType>): DataAbilityPredicates
```

配置谓词以匹配数据类型为ValueType数组且值在给定范围内的指定字段。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | Array & lt;ValueType & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## indexedBy

```TypeScript
indexedBy(field: string): DataAbilityPredicates
```

配置谓词以指定索引列。在使用此方法之前，您需要创建一个索引列。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## isNotNull

```TypeScript
isNotNull(field: string): DataAbilityPredicates
```

配置谓词以匹配值不为null的指定字段。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## isNull

```TypeScript
isNull(field: string): DataAbilityPredicates
```

配置谓词以匹配值为null的字段。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## lessThan

```TypeScript
lessThan(field: string, value: ValueType): DataAbilityPredicates
```

配置谓词以匹配数据类型为ValueType且value小于指定值的字段。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: ValueType): DataAbilityPredicates
```

配置谓词以匹配数据类型为ValueType且value小于或等于指定值的字段。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## like

```TypeScript
like(field: string, value: string): DataAbilityPredicates
```

配置谓词以匹配数据类型为string且值类似于指定字符串的字段。此方法类似于SQL语句“like”。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## limitAs

```TypeScript
limitAs(value: number): DataAbilityPredicates
```

设置谓词的最大数据记录数量。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## notBetween

```TypeScript
notBetween(field: string, low: ValueType, high: ValueType): DataAbilityPredicates
```

配置谓词以匹配数据类型为ValueType且value超出给定范围的指定字段。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## notEqualTo

```TypeScript
notEqualTo(field: string, value: ValueType): DataAbilityPredicates
```

配置谓词以匹配数据，数据的指定字段数据类型为ValueType且不等于指定值。此方法类似于SQL语句的“!=”。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## notIn

```TypeScript
notIn(field: string, value: Array<ValueType>): DataAbilityPredicates
```

配置谓词以匹配数据类型为ValueType数组且值不在给定范围内的指定字段。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | Array & lt;ValueType & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## offsetAs

```TypeScript
offsetAs(rowOffset: number): DataAbilityPredicates
```

设置谓词查询结果的起始位置。需要同步调用[limitAs](#limitas)接口指定查询数量，否则无查询结果。查询指定偏移位置后的所有行时， [limitAs](#limitas)接口需传入参数-1。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rowOffset | number | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## or

```TypeScript
or(): DataAbilityPredicates
```

将或条件添加到谓词中。此方法类似于SQL语句“or”。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## orderByAsc

```TypeScript
orderByAsc(field: string): DataAbilityPredicates
```

配置谓词以匹配其值按升序排序的列。当有多个orderByAsc使用时，最先使用的具有最高优先级。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |

## orderByDesc

```TypeScript
orderByDesc(field: string): DataAbilityPredicates
```

配置谓词以匹配其值按降序排序的列。当有多个orderByDesc使用时，最先使用的具有最高优先级。

**起始版本：** 7

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [DataAbilityPredicates](arkts-arkdata-dataability-dataabilitypredicates-c.md) |
