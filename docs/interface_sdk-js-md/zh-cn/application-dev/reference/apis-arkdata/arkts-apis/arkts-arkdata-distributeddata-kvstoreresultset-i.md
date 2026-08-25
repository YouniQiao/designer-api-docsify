# KvStoreResultSet

提供获取KVStore数据库结果集的相关方法，包括查询和移动数据读取位置等。 在调用KvStoreResultSet的方法前，需要先通过 getKVStore 构建一个KVStore实例。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

## 导入模块

```TypeScript
```

## getCount

```TypeScript
getCount(): number
```

获取结果集中的总行数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getCount

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getEntry

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| [Entry](arkts-arkdata-distributeddata-entry-i.md) |

## getPosition

```TypeScript
getPosition(): number
```

获取结果集中当前的读取位置。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getPosition

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** isAfterLast

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** isBeforeFirst

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** isFirst

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** isLast

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## move

```TypeScript
move(offset: number): boolean
```

将读取位置移动到当前位置的相对偏移量。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** move

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| offset | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## moveToFirst

```TypeScript
moveToFirst(): boolean
```

将读取位置移动到第一行。如果结果集为空，则返回false。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** moveToFirst

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** moveToLast

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## moveToNext

```TypeScript
moveToNext(): boolean
```

将读取位置移动到下一行。如果结果集为空，则返回false。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** moveToNext

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

**起始版本：** 8

**废弃版本：** 9

**替代接口：** moveToPosition

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| position | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## moveToPrevious

```TypeScript
moveToPrevious(): boolean
```

将读取位置移动到上一行。如果结果集为空，则返回false。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** moveToPrevious

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 |
| --- |
| boolean |
