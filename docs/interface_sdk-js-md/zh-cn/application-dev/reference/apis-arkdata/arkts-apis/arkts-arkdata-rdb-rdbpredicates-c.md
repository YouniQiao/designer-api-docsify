# RdbPredicates

表示关系型数据库（RDB）的谓词。该类确定RDB中条件表达式的值是true还是false。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## 导入模块

```TypeScript
```

## and

```TypeScript
and(): RdbPredicates
```

向谓词添加和条件。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [and](arkts-arkdata-relationalstore-rdbpredicates-c.md#and)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## beginsWith

```TypeScript
beginsWith(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据字段为string且值以指定字符串开头的字段。该方法等同于SQL语句中的"LIKE 'xxx%'"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [beginsWith](arkts-arkdata-relationalstore-rdbpredicates-c.md#beginswith)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## beginWrap

```TypeScript
beginWrap(): RdbPredicates
```

向谓词添加左括号。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [beginWrap](arkts-arkdata-relationalstore-rdbpredicates-c.md#beginwrap)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## between

```TypeScript
between(field: string, low: ValueType, high: ValueType): RdbPredicates
```

将谓词配置为匹配数据字段为ValueType且value在给定范围内的指定字段。该方法等同于SQL语句中的"BETWEEN"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [between](arkts-arkdata-relationalstore-rdbpredicates-c.md#between)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## constructor

```TypeScript
constructor(name: string)
```

构造函数。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

## contains

```TypeScript
contains(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据字段为string且value包含指定值的字段。该方法等同于SQL语句中的"LIKE '%xxx%'"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [contains](arkts-arkdata-relationalstore-rdbpredicates-c.md#contains)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## distinct

```TypeScript
distinct(): RdbPredicates
```

配置谓词以过滤重复记录并仅保留其中一个。该方法等同于SQL语句中的"DISTINCT"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [distinct](arkts-arkdata-relationalstore-rdbpredicates-c.md#distinct)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## endsWith

```TypeScript
endsWith(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据字段为string且值以指定字符串结尾的字段。该方法等同于SQL语句中的"LIKE '%xxx'"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [endsWith](arkts-arkdata-relationalstore-rdbpredicates-c.md#endswith)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## endWrap

```TypeScript
endWrap(): RdbPredicates
```

向谓词添加右括号。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [endWrap](arkts-arkdata-relationalstore-rdbpredicates-c.md#endwrap)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## equalTo

```TypeScript
equalTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据字段为ValueType且值等于指定值的字段。该方法等同于SQL语句中的"="。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [equalTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#equalto)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## glob

```TypeScript
glob(field: string, value: string): RdbPredicates
```

配置RdbPredicates匹配数据字段为string且值符合指定通配符模式的字段，其中*匹配任意多个字符，?匹配单个字符。该方法等同于SQL语句中的"GLOB"

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [glob](arkts-arkdata-relationalstore-rdbpredicates-c.md#glob)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## greaterThan

```TypeScript
greaterThan(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据字段为ValueType且值大于指定值的字段。该方法等同于SQL语句中的"&gt;"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [greaterThan](arkts-arkdata-relationalstore-rdbpredicates-c.md#greaterthan)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据字段为ValueType且value大于或等于指定值的字段。该方法等同于SQL语句中的"&gt;="。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [greaterThanOrEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#greaterthanorequalto)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## groupBy

```TypeScript
groupBy(fields: Array<string>): RdbPredicates
```

配置RdbPredicates按指定列分组查询结果。该方法等同于SQL语句中的"GROUP BY"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [groupBy](arkts-arkdata-relationalstore-rdbpredicates-c.md#groupby)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fields](arkts-arkdata-cloudextension-table-i-sys.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## in

```TypeScript
in(field: string, value: Array<ValueType>): RdbPredicates
```

配置RdbPredicates以匹配数据字段为ValueType数组且值在给定范围内的指定字段。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [in](arkts-arkdata-relationalstore-rdbpredicates-c.md#in)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | Array & lt;ValueType & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## inAllDevices

```TypeScript
inAllDevices(): RdbPredicates
```

同步分布式数据库时连接到组网内所有的远程设备。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [inAllDevices](arkts-arkdata-relationalstore-rdbpredicates-c.md#inalldevices)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## inDevices

```TypeScript
inDevices(devices: Array<string>): RdbPredicates
```

同步分布式数据库时连接到组网内指定的远程设备。

> **说明：**&gt;
> 其中devices通过调用<!--RP2-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync)
> 方法得到。<!--RP2End-->deviceManager模块的接口均为系统接口，仅系统应用可用。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [inDevices](arkts-arkdata-relationalstore-rdbpredicates-c.md#indevices)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| devices | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## indexedBy

```TypeScript
indexedBy(field: string): RdbPredicates
```

配置RdbPredicates以指定索引列。该方法等同于SQL语句中的"INDEXED BY"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [indexedBy](arkts-arkdata-relationalstore-rdbpredicates-c.md#indexedby)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## isNotNull

```TypeScript
isNotNull(field: string): RdbPredicates
```

配置谓词以匹配值不为null的指定字段。该方法等同于SQL语句中的"IS NOT NULL"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isNotNull](arkts-arkdata-relationalstore-rdbpredicates-c.md#isnotnull)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## isNull

```TypeScript
isNull(field: string): RdbPredicates
```

配置谓词以匹配值为null的字段。该方法等同于SQL语句中的"IS NULL"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isNull](arkts-arkdata-relationalstore-rdbpredicates-c.md#isnull)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## lessThan

```TypeScript
lessThan(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据字段为valueType且value小于指定值的字段。该方法等同于SQL语句中的"&lt;"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [lessThan](arkts-arkdata-relationalstore-rdbpredicates-c.md#lessthan)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据字段为ValueType且value小于或等于指定值的字段。该方法等同于SQL语句中的"&lt;="。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [lessThanOrEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#lessthanorequalto)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## like

```TypeScript
like(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据字段为string且值类似于指定字符串的字段。该方法等同于SQL语句中的"LIKE"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [like](arkts-arkdata-relationalstore-rdbpredicates-c.md#like)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## limitAs

```TypeScript
limitAs(value: number): RdbPredicates
```

设置最大数据记录数的谓词。该方法等同于SQL语句中的"LIMIT"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [limitAs](arkts-arkdata-relationalstore-rdbpredicates-c.md#limitas)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## notBetween

```TypeScript
notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates
```

配置RdbPredicates以匹配数据字段为ValueType且value超出给定范围的指定字段。该方法等同于SQL语句中的"NOT BETWEEN"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [notBetween](arkts-arkdata-relationalstore-rdbpredicates-c.md#notbetween)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| [low](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |
| [high](../../apis-arkui/arkts-components/arkts-arkui-invertoptions-i.md) | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## notEqualTo

```TypeScript
notEqualTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据字段为ValueType且值不等于指定值的字段。该方法等同于SQL语句中的"!="。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [notEqualTo](arkts-arkdata-relationalstore-rdbpredicates-c.md#notequalto)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | [ValueType](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## notIn

```TypeScript
notIn(field: string, value: Array<ValueType>): RdbPredicates
```

将RdbPredicates配置为匹配数据字段为ValueType且值超出给定范围的指定字段。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [notIn](arkts-arkdata-relationalstore-rdbpredicates-c.md#notin)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | Array & lt;ValueType & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## offsetAs

```TypeScript
offsetAs(rowOffset: number): RdbPredicates
```

配置RdbPredicates以指定返回结果的起始位置。需要同步调用limitAs接口指定查询数量，否则将无查询结果。如需查询指定偏移位置后的所有行，limitAs接口调用需传参数-1。该方法等同于SQL语句中的"OFFSET"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [offsetAs](arkts-arkdata-relationalstore-rdbpredicates-c.md#offsetas)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rowOffset | number | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## or

```TypeScript
or(): RdbPredicates
```

将或条件添加到谓词中。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [or](arkts-arkdata-relationalstore-rdbpredicates-c.md#or)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## orderByAsc

```TypeScript
orderByAsc(field: string): RdbPredicates
```

配置谓词以匹配其值按升序排序的列。该方法等同于SQL语句中的"ORDER BY"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [orderByAsc](arkts-arkdata-relationalstore-rdbpredicates-c.md#orderbyasc)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## orderByDesc

```TypeScript
orderByDesc(field: string): RdbPredicates
```

配置谓词以匹配其值按降序排序的列。该方法等同于SQL语句中的"ORDER BY"。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [orderByDesc](arkts-arkdata-relationalstore-rdbpredicates-c.md#orderbydesc)

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |
