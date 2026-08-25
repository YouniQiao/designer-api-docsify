# KVStoreResultSet

提供获取数据库结果集的相关方法，包括查询和移动数据读取位置等。同时允许打开的结果集的最大数量为8个。KVStoreResultSet实例不会实时刷新。使用结果集后，如果数据库中的数据发生变化（如增删改操作），需要重新查询才能获取到最新的数据。在调用KVStoreResultSet的方法前，需要先通过 getKVStore 构建一个SingleKVStore或者DeviceKVStore实例。

> **说明：**&gt;
> KVStoreResultSet的游标起始位置为-1。

**起始版本：** 9

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## 导入模块

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## getCount

```TypeScript
getCount(): number
```

获取结果集中的总行数。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| number |

## getEntry

```TypeScript
getEntry(): Entry
```

从当前位置获取对应的键值对。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Entry](arkts-arkdata-distributeddata-entry-i.md) |

## getPosition

```TypeScript
getPosition(): number
```

获取结果集中当前的读取位置。读取位置会因[moveToFirst](#movetofirst)、 [moveToLast](#movetolast)等操作而发生变化。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| number |

## isAfterLast

```TypeScript
isAfterLast(): boolean
```

检查读取位置是否在最后一行之后。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isBeforeFirst

```TypeScript
isBeforeFirst(): boolean
```

检查读取位置是否在第一行之前。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isFirst

```TypeScript
isFirst(): boolean
```

检查读取位置是否为第一行。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isLast

```TypeScript
isLast(): boolean
```

检查读取位置是否为最后一行。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## move

```TypeScript
move(offset: number): boolean
```

将读取位置移动到当前位置的相对偏移量。即当前游标位置向下偏移 offset 行。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## moveToFirst

```TypeScript
moveToFirst(): boolean
```

将读取位置移动到第一行。如果结果集为空，则返回false。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## moveToLast

```TypeScript
moveToLast(): boolean
```

将读取位置移动到最后一行。如果结果集为空，则返回false。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## moveToNext

```TypeScript
moveToNext(): boolean
```

将读取位置移动到下一行。如果结果集为空，则返回false。适用于全量获取数据库结果集的场景。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## moveToPosition

```TypeScript
moveToPosition(position: number): boolean
```

将读取位置从 0 移动到绝对位置。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## moveToPrevious

```TypeScript
moveToPrevious(): boolean
```

将读取位置移动到上一行。如果结果集为空，则返回false。适用于全量获取数据库结果集的场景。

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |
