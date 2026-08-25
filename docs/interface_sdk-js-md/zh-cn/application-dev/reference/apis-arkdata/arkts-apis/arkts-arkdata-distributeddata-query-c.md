# Query

使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** Query

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## 导入模块

```TypeScript
```

## and

```TypeScript
and(): Query
```

构造一个带有与条件的查询对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** and

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## beginGroup

```TypeScript
beginGroup(): Query
```

创建一个带有左括号的查询条件组。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** beginGroup

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## constructor

```TypeScript
constructor()
```

用于创建Query实例的构造函数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** constructor

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## deviceId

```TypeScript
deviceId(deviceId: string): Query
```

添加设备ID作为key的前缀。

> **说明：**&gt;
> 其中deviceId通过调用<!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync)
> 方法得到。<!--RP1End-->deviceManager模块的接口均为系统接口，仅系统应用可用。
> 
> deviceId具体获取方式请参考[sync接口示例](arkts-arkdata-distributeddata-singlekvstore-i.md#sync)。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** deviceId

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [deviceId](#deviceid) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## endGroup

```TypeScript
endGroup(): Query
```

创建一个带有右括号的查询条件组。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** endGroup

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## equalTo

```TypeScript
equalTo(field: string, value: number | string | boolean): Query
```

构造一个Query对象来查询具有指定字段的条目，其值等于指定的值。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** equalTo

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| string \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## getSqlLike

```TypeScript
getSqlLike(): string
```

获取Query对象的查询语句。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getSqlLike

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| string |

## greaterThan

```TypeScript
greaterThan(field: string, value: number | string | boolean): Query
```

构造一个Query对象以查询具有大于指定值的指定字段的条目。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** greaterThan

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| string \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: number | string): Query
```

构造一个Query对象以查询具有指定字段且值大于或等于指定值的条目。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** greaterThanOrEqualTo

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## inNumber

```TypeScript
inNumber(field: string, valueList: number[]): Query
```

构造一个Query对象以查询具有指定字段的条目，其值在指定的值列表中。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** inNumber

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| valueList | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## inString

```TypeScript
inString(field: string, valueList: string[]): Query
```

构造一个Query对象以查询具有指定字段的条目，其值在指定的字符串值列表中。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** inString

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| valueList | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## isNotNull

```TypeScript
isNotNull(field: string): Query
```

构造一个Query对象以查询具有值不为null的指定字段的条目。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** isNotNull

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## isNull

```TypeScript
isNull(field: string): Query
```

构造一个Query对象以查询具有值为null的指定字段的条目。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** isNull

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## lessThan

```TypeScript
lessThan(field: string, value: number | string): Query
```

构造一个Query对象以查询具有小于指定值的指定字段的条目。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** lessThan

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: number | string): Query
```

构造一个Query对象以查询具有指定字段且值小于或等于指定值的条目。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** lessThanOrEqualTo

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## like

```TypeScript
like(field: string, value: string): Query
```

构造一个Query对象以查询具有与指定字符串值相似的指定字段的条目。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** like

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## limit

```TypeScript
limit(total: number, offset: number): Query
```

构造一个Query对象来指定结果的数量和开始位置。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** limit

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| total | number | 是 |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## notEqualTo

```TypeScript
notEqualTo(field: string, value: number | string | boolean): Query
```

构造一个Query对象以查询具有指定字段且值不等于指定值的条目。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** notEqualTo

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| string \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## notInNumber

```TypeScript
notInNumber(field: string, valueList: number[]): Query
```

构造一个Query对象以查询具有指定字段的条目，该字段的值不在指定的值列表中。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** notInNumber

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| valueList | number[] | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## notInString

```TypeScript
notInString(field: string, valueList: string[]): Query
```

构造一个Query对象以查询具有指定字段且值不在指定字符串值列表中的条目。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** notInString

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| valueList | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## or

```TypeScript
or(): Query
```

构造一个带有或条件的Query对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** or

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## orderByAsc

```TypeScript
orderByAsc(field: string): Query
```

构造一个Query对象，将查询结果按升序排序。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** orderByAsc

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## orderByDesc

```TypeScript
orderByDesc(field: string): Query
```

构造一个Query对象，将查询结果按降序排序。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** orderByDesc

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## prefixKey

```TypeScript
prefixKey(prefix: string): Query
```

创建具有指定键前缀的查询条件。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** prefixKey

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| prefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## reset

```TypeScript
reset(): Query
```

重置Query对象。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** reset

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## setSuggestIndex

```TypeScript
setSuggestIndex(index: string): Query
```

设置一个指定的索引，将优先用于查询。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** setSuggestIndex

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## unlike

```TypeScript
unlike(field: string, value: string): Query
```

构造一个Query对象以查询具有与指定字符串值不相似的指定字段的条目。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** unlike

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |
