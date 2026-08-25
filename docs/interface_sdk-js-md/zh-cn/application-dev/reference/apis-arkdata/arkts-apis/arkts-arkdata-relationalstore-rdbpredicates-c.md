# RdbPredicates

表示关系型数据库（RDB）的谓词。该类确定RDB中条件表达式的值是true还是false。谓词间支持多语句拼接，拼接时默认使用and()连接。不支持Sendable跨线程传递。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

## 导入模块

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## and

```TypeScript
and(): RdbPredicates
```

向谓词添加和条件。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## beginsWith

```TypeScript
beginsWith(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据表的field列中以value开头的字段。该方法等同于SQL语句中的"LIKE 'xxx%'"。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## beginWrap

```TypeScript
beginWrap(): RdbPredicates
```

向谓词添加左括号。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## between

```TypeScript
between(field: string, low: ValueType, high: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值在给定范围内的字段（包含范围边界）。该方法等同于SQL语句中的"BETWEEN"。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## constructor

```TypeScript
constructor(name: string)
```

构造函数。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## contains

```TypeScript
contains(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据表的field列中包含value的字段。该方法等同于SQL语句中的"LIKE '%xxx%'"。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## distinct

```TypeScript
distinct(): RdbPredicates
```

配置谓词以过滤重复记录并仅保留其中一个。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## endsWith

```TypeScript
endsWith(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据表的field列中以value结尾的字段。该方法等同于SQL语句中的"LIKE '%xxx'"。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## endWrap

```TypeScript
endWrap(): RdbPredicates
```

向谓词添加右括号。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## equalTo

```TypeScript
equalTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值为value的字段。该方法等同于SQL语句中的"="。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## glob

```TypeScript
glob(field: string, value: string): RdbPredicates
```

配置RdbPredicates匹配数据字段为string且值符合指定通配符模式的字段，其中*匹配任意多个字符，?匹配单个字符。该方法等同于SQL语句中的"GLOB"。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## greaterThan

```TypeScript
greaterThan(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值大于value的字段。该方法等同于SQL语句中的"&gt;"。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值大于或者等于value的字段。该方法等同于SQL语句中的"&gt;="。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## groupBy

```TypeScript
groupBy(fields: Array<string>): RdbPredicates
```

配置谓词按指定列分组查询结果。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fields](arkts-arkdata-cloudextension-table-i-sys.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## having

```TypeScript
having(conditions: string, args?: Array<ValueType>): RdbPredicates
```

筛选符合条件的分组数据。

**起始版本：** 20

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| conditions | string | 是 |
| [args](arkts-arkdata-relationalstore-sqlinfo-i.md) | Array & lt;ValueType & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |

## in

```TypeScript
in(field: string, value: Array<ValueType>): RdbPredicates
```

配置谓词条件，表示字段`field`的值必须在给定的`value`列表内。该方法等同于SQL语句中的"IN"。

> **说明：**&gt;
> `value`集合不能为空。如果传入空集，此条件将失效，导致操作针对所有数据（如全量查询、更新或删除）。请在调用前判断`value`是否为空集，避免误操作。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## inAllDevices

```TypeScript
inAllDevices(): RdbPredicates
```

同步分布式数据库时连接到组网内所有的远程设备。

**起始版本：** 9

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
> 其中devices通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> 调用
> [sync](arkts-arkdata-relationalstore-rdbstore-i.md#sync)
> 接口同步数据库时，在入参谓词中调用inDevices接口以选择设备。如果不调用inDevices接口，则默认连接组网内所有的设备。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| devices | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## indexedBy

```TypeScript
indexedBy(field: string): RdbPredicates
```

配置谓词以指定索引列。

**起始版本：** 9

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

## isNotNull

```TypeScript
isNotNull(field: string): RdbPredicates
```

配置谓词以匹配数据表的field列中值不为null的字段。该方法等同于SQL语句中的"IS NOT NULL"。

**起始版本：** 9

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

配置谓词以匹配数据表的field列中值为null的字段。该方法等同于SQL语句中的"IS NULL"。

**起始版本：** 9

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

## lessThan

```TypeScript
lessThan(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值小于value的字段。该方法等同于SQL语句中的"&lt;"。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值小于或者等于value的字段。该方法等同于SQL语句中的"&lt;="。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## like

```TypeScript
like(field: string, value: string): RdbPredicates
```

配置模糊查询条件，指定`field`列的模糊匹配条件。该方法等同于SQL语句中的"LIKE"。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## limitAs

```TypeScript
limitAs(value: number): RdbPredicates
```

设置谓词的最大数据记录数量。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## notBetween

```TypeScript
notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值超出给定范围的字段（不包含范围边界）。该方法等同于SQL语句中的"NOT BETWEEN"。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## notContains

```TypeScript
notContains(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据表的field列中不包含value的字段。

**起始版本：** 12

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## notEqualTo

```TypeScript
notEqualTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值不为value的字段。该方法等同于SQL语句中的"!="。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## notIn

```TypeScript
notIn(field: string, value: Array<ValueType>): RdbPredicates
```

配置谓词以匹配数据表的field列中值不在给定的value集合内的字段。该方法等同于SQL语句中的"NOT IN"。

**起始版本：** 9

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## notLike

```TypeScript
notLike(field: string, value: string): RdbPredicates
```

配置模糊查询条件，指定`field`列**不包含**的模糊匹配条件。

**起始版本：** 12

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## offsetAs

```TypeScript
offsetAs(rowOffset: number): RdbPredicates
```

设置谓词查询结果返回的起始位置。需要同步调用limitAs接口指定查询数量，否则将无查询结果。如需查询指定偏移位置后的所有行，limitAs接口入参需小于等于0。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rowOffset | number | 是 |

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## or

```TypeScript
or(): RdbPredicates
```

将或条件添加到谓词中。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 |
| --- |
| [RdbPredicates](arkts-arkdata-rdb-rdbpredicates-c.md) |

## orderByAsc

```TypeScript
orderByAsc(field: string): RdbPredicates
```

配置谓词以匹配数据表的field列中值按升序排序的列。该方法等同于SQL语句中的"ORDER BY ASC"。

**起始版本：** 9

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

## orderByDesc

```TypeScript
orderByDesc(field: string): RdbPredicates
```

配置谓词以匹配数据表的field列中值按降序排序的列。该方法等同于SQL语句中的"ORDER BY DESC"。

**起始版本：** 9

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
