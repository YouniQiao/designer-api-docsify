# Query

使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。Query对象的谓词方法均返回自身，支持链式调用。一个Query对象中谓词数量上限为256个。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## 导入模块

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## and

```TypeScript
and(): Query
```

构造一个带有与条件的查询对象。需先通过equalTo、notEqualTo等谓词方法添加查询条件后，再调用and()连接多个条件，无前置谓词时调用and()无效。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## beginGroup

```TypeScript
beginGroup(): Query
```

创建一个带有左括号的查询条件组。必须与[endGroup()](#endgroup)成对使用，以形成完整的查询条件分组。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

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

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## deviceId

```TypeScript
deviceId(deviceId: string): Query
```

添加设备ID作为Key的前缀。

> **说明：**&gt;
> 其中deviceId为[DeviceBasicInfo](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicebasicinfo-i.md)中的
> networkId，通过调用
> [deviceManager.getAvailableDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-distributeddevicemanager-devicemanager-i.md#getavailabledevicelistsync)
> 方法得到。&gt;
> deviceId具体获取方式请参考
> [sync接口示例](arkts-arkdata-distributedkvstore-singlekvstore-i.md#sync)。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [deviceId](#deviceid) | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## endGroup

```TypeScript
endGroup(): Query
```

创建一个带有右括号的查询条件组。必须与[beginGroup()](#begingroup)成对使用，以形成完整的查询条件分组。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

## equalTo

```TypeScript
equalTo(field: string, value: number | number | string | boolean): Query
```

构造一个Query对象来查询具有指定字段的条目，其值等于指定的值。

> **说明：**&gt;
> 使用equalTo时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| number \| string \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getSqlLike

```TypeScript
getSqlLike(): string
```

获取Query对象的查询语句。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| string |

## greaterThan

```TypeScript
greaterThan(field: string, value: number | number | string | boolean): Query
```

构造一个Query对象以查询具有大于指定值的指定字段的条目。

> **说明：**&gt;
> 使用greaterThan时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| number \| string \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## greaterThanOrEqualTo

```TypeScript
greaterThanOrEqualTo(field: string, value: number | number | string): Query
```

构造一个Query对象以查询具有指定字段且值大于或等于指定值的条目。

> **说明：**&gt;
> 使用greaterThanOrEqualTo时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## inNumber

```TypeScript
inNumber(field: string, valueList: number[] | number[]): Query
```

构造一个Query对象以查询具有指定字段的条目，其值在指定的值列表中。

> **说明：**&gt;
> 使用inNumber时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| valueList | number[] \| number[] | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## inString

```TypeScript
inString(field: string, valueList: string[]): Query
```

构造一个Query对象以查询具有指定字段的条目，其值在指定的字符串值列表中。

> **说明：**&gt;
> 使用inString时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## isNotNull

```TypeScript
isNotNull(field: string): Query
```

构造一个Query对象以查询具有值不为null的指定字段的条目。

> **说明：**&gt;
> 使用isNotNull时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## isNull

```TypeScript
isNull(field: string): Query
```

构造一个Query对象以查询具有值为null的指定字段的条目。

> **说明：**&gt;
> 使用isNull时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## lessThan

```TypeScript
lessThan(field: string, value: number | number | string): Query
```

构造一个Query对象以查询具有小于指定值的指定字段的条目。

> **说明：**&gt;
> 使用lessThan时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## lessThanOrEqualTo

```TypeScript
lessThanOrEqualTo(field: string, value: number | number | string): Query
```

构造一个Query对象以查询具有指定字段且值小于或等于指定值的条目。

> **说明：**&gt;
> 使用lessThanOrEqualTo时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| number \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## like

```TypeScript
like(field: string, value: string): Query
```

构造一个Query对象以查询具有与指定字符串值相似的指定字段的条目。

> **说明：**&gt;
> 使用like时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## limit

```TypeScript
limit(total: number, offset: number): Query
```

构造一个Query对象来指定结果的数量和开始位置。该接口必须要在Query对象查询和升降序等操作之后调用，调用limit接口后，不可再对Query对象进行查询和升降序等操作。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## notEqualTo

```TypeScript
notEqualTo(field: string, value: number | number | string | boolean): Query
```

构造一个Query对象以查询具有指定字段且值不等于指定值的条目。

> **说明：**&gt;
> 使用notEqualTo时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | number \| number \| string \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## notInNumber

```TypeScript
notInNumber(field: string, valueList: number[] | number[]): Query
```

构造一个Query对象以查询具有指定字段的条目，该字段的值不在指定的值列表中。

> **说明：**&gt;
> 使用notInNumber时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| valueList | number[] \| number[] | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## notInString

```TypeScript
notInString(field: string, valueList: string[]): Query
```

构造一个Query对象以查询具有指定字段且值不在指定字符串值列表中的条目。

> **说明：**&gt;
> 使用notInString时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## or

```TypeScript
or(): Query
```

构造一个带有或条件的Query对象。需先通过equalTo、notEqualTo等谓词方法添加查询条件后，再调用or()连接多个条件，无前置谓词时调用or()无效。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

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

> **说明：**&gt;
> 使用orderByAsc时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## orderByDesc

```TypeScript
orderByDesc(field: string): Query
```

构造一个Query对象，将查询结果按降序排序。

> **说明：**&gt;
> 使用orderByDesc时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## prefixKey

```TypeScript
prefixKey(prefix: string): Query
```

创建具有指定键前缀的查询条件。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| prefix | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## reset

```TypeScript
reset(): Query
```

重置Query对象。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

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

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## unlike

```TypeScript
unlike(field: string, value: string): Query
```

构造一个Query对象以查询具有与指定字符串值不相似的指定字段的条目。

> **说明：**&gt;
> 使用unlike时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

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

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
