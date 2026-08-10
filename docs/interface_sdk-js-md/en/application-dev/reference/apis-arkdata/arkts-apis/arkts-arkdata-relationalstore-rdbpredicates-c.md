# RdbPredicates

表示关系型数据库（RDB）的谓词。该类确定RDB中条件表达式的值是true还是false。谓词间支持多语句拼接，拼接时默认使用and()连接。不支持Sendable跨线程传递。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-relationalStore-class RdbPredicates--><!--Device-relationalStore-class RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

## Modules to Import

```TypeScript
import { relationalStore } from 'kits/@kit.ArkData';
```

## and

```TypeScript
and(): RdbPredicates
```

向谓词添加和条件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-and(): RdbPredicates--><!--Device-RdbPredicates-and(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回带有和条件的谓词。 |

## beginWrap

```TypeScript
beginWrap(): RdbPredicates
```

向谓词添加左括号。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-beginWrap(): RdbPredicates--><!--Device-RdbPredicates-beginWrap(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回带有左括号的谓词。 |

## beginsWith

```TypeScript
beginsWith(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据表的field列中以value开头的字段。该方法等同于SQL语句中的"LIKE 'xxx%'"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-beginsWith(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-beginsWith(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | string | Yes | 指示要与谓词匹配的值，长度不超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## between

```TypeScript
between(field: string, low: ValueType, high: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值在给定范围内的字段（包含范围边界）。该方法等同于SQL语句中的"BETWEEN"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-between(field: string, low: ValueType, high: ValueType): RdbPredicates--><!--Device-RdbPredicates-between(field: string, low: ValueType, high: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| low | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 指示与谓词匹配的最小值。 |
| high | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 指示与谓词匹配的最大值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## constructor

```TypeScript
constructor(name: string)
```

构造函数。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-constructor(name: string)--><!--Device-RdbPredicates-constructor(name: string)-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | 数据库表名，不能为空字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## contains

```TypeScript
contains(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据表的field列中包含value的字段。该方法等同于SQL语句中的"LIKE '%xxx%'"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-contains(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-contains(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | string | Yes | 指示要与谓词匹配的值，长度不超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## distinct

```TypeScript
distinct(): RdbPredicates
```

配置谓词以过滤重复记录并仅保留其中一个。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-distinct(): RdbPredicates--><!--Device-RdbPredicates-distinct(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回可用于过滤重复记录的谓词。 |

## endWrap

```TypeScript
endWrap(): RdbPredicates
```

向谓词添加右括号。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-endWrap(): RdbPredicates--><!--Device-RdbPredicates-endWrap(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回带有右括号的谓词。 |

## endsWith

```TypeScript
endsWith(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据表的field列中以value结尾的字段。该方法等同于SQL语句中的"LIKE '%xxx'"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-endsWith(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-endsWith(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | string | Yes | 指示要与谓词匹配的值，长度不超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## equalTo

```TypeScript
equalTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值为value的字段。该方法等同于SQL语句中的"="。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-equalTo(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-equalTo(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 指示要与谓词匹配的值，长度不超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## glob

```TypeScript
glob(field: string, value: string): RdbPredicates
```

配置RdbPredicates匹配数据字段为string且值符合指定通配符模式的字段，其中*匹配任意多个字符，?匹配单个字符。该方法等同于SQL语句中的"GLOB"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-glob(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-glob(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | string | Yes | 指示要与谓词匹配的值，长度不超过1024字节。 &lt;br&gt;支持通配符，*表示0个、1个或多个数字或字符，?表示1个数字或字符。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## greaterThan

```TypeScript
greaterThan(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值大于value的字段。该方法等同于SQL语句中的">"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-greaterThan(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-greaterThan(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 指示要与谓词匹配的值，长度不超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值大于或者等于value的字段。该方法等同于SQL语句中的">="。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 指示要与谓词匹配的值，长度不超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## groupBy

```TypeScript
groupBy(fields: Array<string>): RdbPredicates
```

配置谓词按指定列分组查询结果。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-groupBy(fields: Array<string>): RdbPredicates--><!--Device-RdbPredicates-groupBy(fields: Array<string>): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fields | Array&lt;string&gt; | Yes | 指定分组依赖的列名。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回分组查询列的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## having

```TypeScript
having(conditions: string, args?: Array<ValueType>): RdbPredicates
```

筛选符合条件的分组数据。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-having(conditions: string, args?: Array<ValueType>): RdbPredicates--><!--Device-RdbPredicates-having(conditions: string, args?: Array<ValueType>): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| conditions | string | Yes | 用于过滤使用[groupBy](arkts-arkdata-relationalstore-rdbpredicates-c.md#groupby)获得的数据，conditions参数不能为空 字符串且必须与[groupBy](arkts-arkdata-relationalstore-rdbpredicates-c.md#groupby)配合使用。 |
| args | Array&lt;ValueType&gt; | No | 条件中使用的参数，用来替换条件语句中的占位符，不传时默认为空数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range; &lt;br&gt;2. Missing GROUP BY clause. |

## in

```TypeScript
in(field: string, value: Array<ValueType>): RdbPredicates
```

配置谓词条件，表示字段`field`的值必须在给定的`value`列表内。该方法等同于SQL语句中的"IN"。

> **说明：**
> 
> `value`集合不能为空。如果传入空集，此条件将失效，导致操作针对所有数据（如全量查询、更新或删除）。请在调用前判断`value`是否为空集，避免误操作。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-RdbPredicates-in(field: string, value: Array<ValueType>): RdbPredicates--><!--Device-RdbPredicates-in(field: string, value: Array<ValueType>): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | Array&lt;ValueType&gt; | Yes | 以ValueType型数组形式指定的要匹配的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## inAllDevices

```TypeScript
inAllDevices(): RdbPredicates
```

同步分布式数据库时连接到组网内所有的远程设备。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-inAllDevices(): RdbPredicates--><!--Device-RdbPredicates-inAllDevices(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

## inDevices

```TypeScript
inDevices(devices: Array<string>): RdbPredicates
```

同步分布式数据库时连接到组网内指定的远程设备。

> **说明：**
> 
> 其中devices通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。
> 
> 调用
> [sync](arkts-arkdata-relationalstore-rdbstore-i.md#sync)
> 接口同步数据库时，在入参谓词中调用inDevices接口以选择设备。如果不调用inDevices接口，则默认连接组网内所有的设备。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-inDevices(devices: Array<string>): RdbPredicates--><!--Device-RdbPredicates-inDevices(devices: Array<string>): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| devices | Array&lt;string&gt; | Yes | 指定的组网内的远程设备ID。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## inValues

```TypeScript
inValues(field: string, value: Array<ValueType>): RdbPredicates
```

配置谓词条件，表示字段`field`的值必须在给定的`value`列表内。该方法等同于SQL语句中的"IN"。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RdbPredicates-inValues(field: string, value: Array<ValueType>): RdbPredicates--><!--Device-RdbPredicates-inValues(field: string, value: Array<ValueType>): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | Array&lt;ValueType&gt; | Yes | 以ValueType型数组形式指定的要匹配的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回配置了谓词条件的RdbPredicates对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## indexedBy

```TypeScript
indexedBy(field: string): RdbPredicates
```

配置谓词以指定索引列。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-indexedBy(field: string): RdbPredicates--><!--Device-RdbPredicates-indexedBy(field: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 索引列的名称，不能为空字符串。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回具有指定索引列的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## isNotNull

```TypeScript
isNotNull(field: string): RdbPredicates
```

配置谓词以匹配数据表的field列中值不为null的字段。该方法等同于SQL语句中的"IS NOT NULL"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-isNotNull(field: string): RdbPredicates--><!--Device-RdbPredicates-isNotNull(field: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## isNull

```TypeScript
isNull(field: string): RdbPredicates
```

配置谓词以匹配数据表的field列中值为null的字段。该方法等同于SQL语句中的"IS NULL"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-isNull(field: string): RdbPredicates--><!--Device-RdbPredicates-isNull(field: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## lessThan

```TypeScript
lessThan(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值小于value的字段。该方法等同于SQL语句中的"<"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-lessThan(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-lessThan(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 指示要与谓词匹配的值，长度不超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值小于或者等于value的字段。该方法等同于SQL语句中的"<="。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 指示要与谓词匹配的值，长度不超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## like

```TypeScript
like(field: string, value: string): RdbPredicates
```

配置模糊查询条件，指定`field`列的模糊匹配条件。该方法等同于SQL语句中的"LIKE"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-like(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-like(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | string | Yes | 指定模糊匹配条件，通常配合通配符使用，`%`表示任意长度任意字符，`_`表示单个字符。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## limitAs

ArkTS-Dyn:
```TypeScript
limitAs(value: number): RdbPredicates
```

ArkTS-Sta:
```TypeScript
limitAs(value: int): RdbPredicates
```

设置谓词的最大数据记录数量。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-limitAs(value: int): RdbPredicates--><!--Device-RdbPredicates-limitAs(value: int): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 最大数据记录数，取值应为正整数，传入值小于等于0时，不会限制记录数量。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回可用于设置最大数据记录数的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## notBetween

```TypeScript
notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值超出给定范围的字段（不包含范围边界）。该方法等同于SQL语句中的"NOT BETWEEN"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates--><!--Device-RdbPredicates-notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| low | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 指示与谓词匹配的最小值。 |
| high | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 指示与谓词匹配的最大值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## notContains

```TypeScript
notContains(field: string, value: string): RdbPredicates
```

配置谓词以匹配数据表的field列中不包含value的字段。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-notContains(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-notContains(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | string | Yes | 指示要与谓词匹配的值，长度不超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## notEqualTo

```TypeScript
notEqualTo(field: string, value: ValueType): RdbPredicates
```

配置谓词以匹配数据表的field列中值不为value的字段。该方法等同于SQL语句中的"!="。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-notEqualTo(field: string, value: ValueType): RdbPredicates--><!--Device-RdbPredicates-notEqualTo(field: string, value: ValueType): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | [ValueType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-pasteboard-valuetype-t.md) | Yes | 指示要与谓词匹配的值，长度不超过1024字节。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## notIn

```TypeScript
notIn(field: string, value: Array<ValueType>): RdbPredicates
```

配置谓词以匹配数据表的field列中值不在给定的value集合内的字段。该方法等同于SQL语句中的"NOT IN"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-RdbPredicates-notIn(field: string, value: Array<ValueType>): RdbPredicates--><!--Device-RdbPredicates-notIn(field: string, value: Array<ValueType>): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | Array&lt;ValueType&gt; | Yes | 以ValueType数组形式指定的要匹配的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## notInValues

```TypeScript
notInValues(field: string, value: Array<ValueType>): RdbPredicates
```

配置谓词条件，表示字段`field`的值不在给定的`value`列表内。该方法等同于SQL语句中的"NOT IN"。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-RdbPredicates-notInValues(field: string, value: Array<ValueType>): RdbPredicates--><!--Device-RdbPredicates-notInValues(field: string, value: Array<ValueType>): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | Array&lt;ValueType&gt; | Yes | 以ValueType型数组形式指定的要匹配的值。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回配置了谓词条件的RdbPredicates对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |

## notLike

```TypeScript
notLike(field: string, value: string): RdbPredicates
```

配置模糊查询条件，指定`field`列**不包含**的模糊匹配条件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-notLike(field: string, value: string): RdbPredicates--><!--Device-RdbPredicates-notLike(field: string, value: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |
| value | string | Yes | 指定**不包含**的模糊匹配条件，通常配合通配符使用，`%`表示任意长度任意字符，`_`表示单个字符。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## offsetAs

ArkTS-Dyn:
```TypeScript
offsetAs(rowOffset: number): RdbPredicates
```

ArkTS-Sta:
```TypeScript
offsetAs(rowOffset: int): RdbPredicates
```

设置谓词查询结果返回的起始位置。需要同步调用limitAs接口指定查询数量，否则将无查询结果。如需查询指定偏移位置后的所有行，limitAs接口入参需小于等于0。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-offsetAs(rowOffset: int): RdbPredicates--><!--Device-RdbPredicates-offsetAs(rowOffset: int): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| rowOffset | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 指定查询结果的起始位置，默认初始位置为结果集的最前端。当rowOffset为负数时，起始位置为结果集的最前端。当rowOffset超出结果集最后位置时，查询结果为空。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回具有指定返回结果起始位置的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## or

```TypeScript
or(): RdbPredicates
```

将或条件添加到谓词中。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-or(): RdbPredicates--><!--Device-RdbPredicates-or(): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回带有或条件的谓词。 |

## orderByAsc

```TypeScript
orderByAsc(field: string): RdbPredicates
```

配置谓词以匹配数据表的field列中值按升序排序的列。该方法等同于SQL语句中的"ORDER BY ASC"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-orderByAsc(field: string): RdbPredicates--><!--Device-RdbPredicates-orderByAsc(field: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## orderByDesc

```TypeScript
orderByDesc(field: string): RdbPredicates
```

配置谓词以匹配数据表的field列中值按降序排序的列。该方法等同于SQL语句中的"ORDER BY DESC"。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-RdbPredicates-orderByDesc(field: string): RdbPredicates--><!--Device-RdbPredicates-orderByDesc(field: string): RdbPredicates-End-->

**System capability:** SystemCapability.DistributedDataManager.RelationalStore.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| field | string | Yes | 数据库表中的列名，不能为空字符串。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RdbPredicates](arkts-arkdata-relationalstore-rdbpredicates-c.md) | 返回与指定字段匹配的谓词。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

