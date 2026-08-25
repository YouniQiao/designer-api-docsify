# Query

使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。Query对象的谓词方法均返回自身，支持链式调用。一个Query对象中谓词数量上限为256个。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## 导入模块

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## and

```TypeScript
and(): Query
```

构造一个带有与条件的查询对象。需先通过equalTo、notEqualTo等谓词方法添加查询条件后，再调用and()连接多个条件，无前置谓词时调用and()无效。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo('field', 'value1');
      query.and();
      query.notEqualTo('field', 'value2');
      console.info(`query is ` + query.getSqlLike());
    }
    query = null;
} catch (err) {
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## beginGroup

```TypeScript
beginGroup(): Query
```

创建一个带有左括号的查询条件组。必须与[endGroup()](#endgroup)成对使用，以形成完整的查询条件分组。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.beginGroup();
      query.isNotNull('field');
      query.endGroup();
      console.info(`query is ` + query.getSqlLike());
    }
    query = null;
} catch (err) {
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## constructor

```TypeScript
constructor()
```

用于创建Query实例的构造函数。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**示例**

ArkTS-Dyn示例：

```TypeScript
let child1 = new distributedKVStore.FieldNode('id');
child1.type = distributedKVStore.ValueType.INTEGER;
child1.nullable = false;
child1.default = '1';
let child2 = new distributedKVStore.FieldNode('name');
child2.type = distributedKVStore.ValueType.STRING;
child2.nullable = false;
child2.default = 'zhangsan';

let schema = new distributedKVStore.Schema();
schema.root.appendChild(child1);
schema.root.appendChild(child2);
schema.indexes = ['$.id', '$.name'];
schema.mode = 1;
schema.skip = 0;
```

ArkTS-Sta示例：

```TypeScript
let child1 = new distributedKVStore.FieldNode('id');
child1.type = distributedKVStore.ValueType.LONG;
child1.nullable = false;
child1.defaultValue = '1';
let child2 = new distributedKVStore.FieldNode('name');
child2.type = distributedKVStore.ValueType.STRING;
child2.nullable = false;
child2.defaultValue = 'zhangsan';

let schema = new distributedKVStore.Schema();
schema.root.appendChild(child1);
schema.root.appendChild(child2);
schema.indexes = ['$.id', '$.name'];
schema.mode = 1;
schema.skip = 0;
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.deviceId('deviceId');
      console.info(`query is ${query.getSqlLike()}`);
    }
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## endGroup

```TypeScript
endGroup(): Query
```

创建一个带有右括号的查询条件组。必须与[beginGroup()](#begingroup)成对使用，以形成完整的查询条件分组。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.beginGroup();
      query.isNotNull('field');
      query.endGroup();
      console.info(`query is ` + query.getSqlLike());
    }
    query = null;
} catch (err) {
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## equalTo

ArkTS-Dyn:
```TypeScript
equalTo(field: string, value: number | number | string | boolean): Query
```

ArkTS-Sta:
```TypeScript
equalTo(field: string, value: long | double | string | boolean): Query
```

构造一个Query对象来查询具有指定字段的条目，其值等于指定的值。

> **说明：**&gt;
> 使用equalTo时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | ArkTS-Dyn: number \| number \| string \| boolean<br>ArkTS-Sta：long \ | double \| string \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.equalTo('field', 'value');
    console.info(`query is ${query.getSqlLike()}`);
  }
  query = null;
} catch (err) {
  let error = err as BusinessError;
  console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## getSqlLike

```TypeScript
getSqlLike(): string
```

获取Query对象的查询语句。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      let sql1 = query.getSqlLike();
      console.info(`GetSqlLike sql= ${sql1}`);
    }
} catch (err) {
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## greaterThan

ArkTS-Dyn:
```TypeScript
greaterThan(field: string, value: number | number | string | boolean): Query
```

ArkTS-Sta:
```TypeScript
greaterThan(field: string, value: long | double | string | boolean): Query
```

构造一个Query对象以查询具有大于指定值的指定字段的条目。

> **说明：**&gt;
> 使用greaterThan时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | ArkTS-Dyn: number \| number \| string \| boolean<br>ArkTS-Sta：long \ | double \| string \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.greaterThan('field', 'value');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## greaterThanOrEqualTo

ArkTS-Dyn:
```TypeScript
greaterThanOrEqualTo(field: string, value: number | number | string): Query
```

ArkTS-Sta:
```TypeScript
greaterThanOrEqualTo(field: string, value: long | double | string): Query
```

构造一个Query对象以查询具有指定字段且值大于或等于指定值的条目。

> **说明：**&gt;
> 使用greaterThanOrEqualTo时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | ArkTS-Dyn: number \| number \| string<br>ArkTS-Sta：long \ | double \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.greaterThanOrEqualTo('field', 'value');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## inNumber

ArkTS-Dyn:
```TypeScript
inNumber(field: string, valueList: number[] | number[]): Query
```

ArkTS-Sta:
```TypeScript
inNumber(field: string, valueList: long[] | double[]): Query
```

构造一个Query对象以查询具有指定字段的条目，其值在指定的值列表中。

> **说明：**&gt;
> 使用inNumber时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| valueList | ArkTS-Dyn: number[] \| number[]<br>ArkTS-Sta：long[] \ | double[] | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.inNumber('field', [0, 1]);
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.inString('field', ['test1', 'test2']);
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.isNotNull('field');
    console.info(`query is ${query.getSqlLike()}`);
  }
  query = null;
} catch (err) {
  let error = err as BusinessError;
  console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.isNull('field');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## lessThan

ArkTS-Dyn:
```TypeScript
lessThan(field: string, value: number | number | string): Query
```

ArkTS-Sta:
```TypeScript
lessThan(field: string, value: long | double | string): Query
```

构造一个Query对象以查询具有小于指定值的指定字段的条目。

> **说明：**&gt;
> 使用lessThan时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | ArkTS-Dyn: number \| number \| string<br>ArkTS-Sta：long \ | double \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.lessThan('field', 'value');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## lessThanOrEqualTo

ArkTS-Dyn:
```TypeScript
lessThanOrEqualTo(field: string, value: number | number | string): Query
```

ArkTS-Sta:
```TypeScript
lessThanOrEqualTo(field: string, value: long | double | string): Query
```

构造一个Query对象以查询具有指定字段且值小于或等于指定值的条目。

> **说明：**&gt;
> 使用lessThanOrEqualTo时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | ArkTS-Dyn: number \| number \| string<br>ArkTS-Sta：long \ | double \| string | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.lessThanOrEqualTo('field', 'value');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.like('field', 'value');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## limit

ArkTS-Dyn:
```TypeScript
limit(total: number, offset: number): Query
```

ArkTS-Sta:
```TypeScript
limit(total: int, offset: int): Query
```

构造一个Query对象来指定结果的数量和开始位置。该接口必须要在Query对象查询和升降序等操作之后调用，调用limit接口后，不可再对Query对象进行查询和升降序等操作。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| total | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| offset | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let total = 10;
let offset = 1;
try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.notEqualTo('field', 'value');
    query.limit(total, offset);
    console.info(`query is ${query.getSqlLike()}`);
  }
  query = null;
} catch (err) {
  let error = err as BusinessError;
  console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## notEqualTo

ArkTS-Dyn:
```TypeScript
notEqualTo(field: string, value: number | number | string | boolean): Query
```

ArkTS-Sta:
```TypeScript
notEqualTo(field: string, value: long | double | string | boolean): Query
```

构造一个Query对象以查询具有指定字段且值不等于指定值的条目。

> **说明：**&gt;
> 使用notEqualTo时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| value | ArkTS-Dyn: number \| number \| string \| boolean<br>ArkTS-Sta：long \ | double \| string \| boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.notEqualTo('field', 'value');
    console.info(`query is ${query.getSqlLike()}`);
  }
  query = null;
} catch (err) {
  let error = err as BusinessError;
  console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## notInNumber

ArkTS-Dyn:
```TypeScript
notInNumber(field: string, valueList: number[] | number[]): Query
```

ArkTS-Sta:
```TypeScript
notInNumber(field: string, valueList: long[] | double[]): Query
```

构造一个Query对象以查询具有指定字段的条目，该字段的值不在指定的值列表中。

> **说明：**&gt;
> 使用notInNumber时需要结合[Schema](arkts-arkdata-distributedkvstore-schema-c.md)使用。&gt;
> 使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../../database/data-persistence-by-kv-store.md#开发步骤)中使用getKVStore()方法创建并获
> 取键值数据库示例。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| field | string | 是 |
| valueList | ArkTS-Dyn: number[] \| number[]<br>ArkTS-Sta：long[] \ | double[] | 是 |

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notInNumber('field', [0, 1]);
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notInString('field', ['test1', 'test2']);
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## or

```TypeScript
or(): Query
```

构造一个带有或条件的Query对象。需先通过equalTo、notEqualTo等谓词方法添加查询条件后，再调用or()连接多个条件，无前置谓词时调用or()无效。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo('field', 'value1');
      query.or();
      query.notEqualTo('field', 'value2');
      console.info(`query is ` + query.getSqlLike());
    }
    query = null;
} catch (err) {
    console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo('field', 'value');
      query.orderByAsc('field');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo('field', 'value');
      query.orderByDesc('field');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## prefixKey

```TypeScript
prefixKey(prefix: string): Query
```

创建具有指定键前缀的查询条件。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.prefixKey('$.name');
      query.prefixKey('0');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

## reset

```TypeScript
reset(): Query
```

重置Query对象。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Query](arkts-arkdata-distributeddata-query-c.md) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.equalTo('key', 'value');
    console.info(`query is ` + query.getSqlLike());
    query.reset();
    console.info(`query is ` + query.getSqlLike());
  }
  query = null;
} catch (err) {
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## setSuggestIndex

```TypeScript
setSuggestIndex(index: string): Query
```

设置一个指定的索引，将优先用于查询。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.setSuggestIndex('$.name');
      query.setSuggestIndex('0');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

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

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.unlike('field', 'value');
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (err) {
    let error = err as BusinessError;
    console.error(`duplicated calls should be ok. Code: ${error.code}, message: ${error.message}`);
}
```
