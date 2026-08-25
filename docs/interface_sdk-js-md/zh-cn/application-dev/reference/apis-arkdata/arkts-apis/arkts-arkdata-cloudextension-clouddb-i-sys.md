# CloudDB（系统接口）

提供云数据库操作接口的类。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cloudExtension } from 'kits/@kit.ArkData';
```

## delete

```TypeScript
delete(
      table: string,
      extensions: Array<Record<string, CloudType>>
    ): Promise<Array<Result<Record<string, CloudType>>>>
```

删除云数据库表中的指定数据。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| extensions | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt;&gt;&gt; |

## generateId

```TypeScript
generateId(count: number): Promise<Result<Array<string>>>
```

为插入的云数据生成具有唯一性的ID。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;Array & lt;string & gt; & gt; & gt; |

## heartbeat

```TypeScript
heartbeat(lockId: number): Promise<Result<LockInfo>>
```

延长数据库的加锁时效。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [lockId](arkts-arkdata-cloudextension-lockinfo-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;LockInfo & gt; & gt; |

## insert

```TypeScript
insert(
      table: string,
      values: Array<Record<string, CloudType>>,
      extensions: Array<Record<string, CloudType>>
    ): Promise<Array<Result<Record<string, CloudType>>>>
```

将数据插入云数据库表中。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | 是 |
| extensions | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt;&gt;&gt; |

## lock

```TypeScript
lock(): Promise<Result<LockInfo>>
```

为云数据库加锁。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;LockInfo & gt; & gt; |

## query

```TypeScript
query(table: string, fields: Array<string>, queryCount: number, queryCursor: string): Promise<Result<CloudData>>
```

在云数据库表中查询数据。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| [fields](arkts-arkdata-cloudextension-table-i-sys.md) | Array & lt;string & gt; | 是 |
| queryCount | number | 是 |
| queryCursor | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Result&lt;[CloudData](arkts-arkdata-cloudextension-clouddata-i-sys.md)&gt;&gt; |

## unlock

```TypeScript
unlock(lockId: number): Promise<Result<boolean>>
```

为云数据库解锁。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [lockId](arkts-arkdata-cloudextension-lockinfo-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;boolean & gt; & gt; |

## update

```TypeScript
update(
      table: string,
      values: Array<Record<string, CloudType>>,
      extensions: Array<Record<string, CloudType>>
    ): Promise<Array<Result<Record<string, CloudType>>>>
```

通过该接口更新云上的数据。使用Promise异步回调。

**起始版本：** 11

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| values | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | 是 |
| extensions | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt;&gt;&gt; |
