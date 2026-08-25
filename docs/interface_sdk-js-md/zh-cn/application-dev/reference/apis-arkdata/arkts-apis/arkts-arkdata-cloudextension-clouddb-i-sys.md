# CloudDB（系统接口）

提供云数据库操作接口的类。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { cloudExtension } from '@kit.ArkData';
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

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

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

**示例**

ArkTS-Dyn示例：

```TypeScript
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async delete(table: string, extensions: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    console.info(`delete, table: ${table}`);
    let deleteRes: Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>> = [];
    // ...
    // 返回删除数据的结果
    return deleteRes;
  }
  // ...
}
```

ArkTS-Sta示例：

```TypeScript
import cloudExtension from '@ohos.data.cloudExtension';
export default class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async delete(table: string, extensions: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    console.info(`delete, table: ${table}`);
    let deleteRes: Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>> = [];
    // ...
    // 返回插入数据的结果
    return deleteRes;
  }
  // ...
  async generateId(count: int): Promise<cloudExtension.Result<string[]>> {
    return { code: 0, value: [] };
  }
  async query(table: string, fields: string[], queryCount: int, queryCursor: string): Promise<cloudExtension.Result<cloudExtension.CloudData>> {
    return { code: 0, value: { values: [], hasMore: false, nextCursor: "" } as cloudExtension.CloudData };
  }
  async insert(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async update(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async lock(): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
  async unlock(sessionId: int): Promise<cloudExtension.Result<boolean>> {
    return { code: 0, value: true };
  }
  async heartbeat(sessionId: int): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
}
```

## generateId

ArkTS-Dyn:
```TypeScript
generateId(count: number): Promise<Result<Array<string>>>
```

ArkTS-Sta:
```TypeScript
generateId(count: int): Promise<Result<Array<string>>>
```

为插入的云数据生成具有唯一性的ID。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;Array & lt;string & gt; & gt; & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
class MyCloudDB implements cloudExtension.CloudDB {
  async generateId(count: number): Promise<cloudExtension.Result<Array<string>>> {
    console.info(`generate id, count: ${count}`);
    let result = new Array<string>();
    // ...
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'generateId succeeded',
      value: result
    };
  }
  // ...
}
```

ArkTS-Sta示例：

```TypeScript
import cloudExtension from '@ohos.data.cloudExtension';
export default class MyCloudDB implements cloudExtension.CloudDB {
  async generateId(count: int): Promise<cloudExtension.Result<Array<string>>> {
    console.info(`generate id, count: ${count}`);
    let result = new Array<string>();
    // ...
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'generateId succeeded',
      value: result
    };
  }
  // ...
  async query(table: string, fields: string[], queryCount: int, queryCursor: string): Promise<cloudExtension.Result<cloudExtension.CloudData>> {
    return {
      code: 0,
      value: {
        values: [],
        hasMore: false,
        nextCursor: ""
      } as cloudExtension.CloudData
    };
  }
  async insert(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async update(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async delete(table: string, values: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async lock(): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
  async unlock(sessionId: int): Promise<cloudExtension.Result<boolean>> {
    return { code: 0, value: true };
  }
  async heartbeat(sessionId: int): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
}
```

## heartbeat

ArkTS-Dyn:
```TypeScript
heartbeat(lockId: number): Promise<Result<LockInfo>>
```

ArkTS-Sta:
```TypeScript
heartbeat(lockId: int): Promise<Result<LockInfo>>
```

延长数据库的加锁时效。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [lockId](arkts-arkdata-cloudextension-lockinfo-i-sys.md) | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;LockInfo & gt; & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
let test_lockId: number = 1;
let test_time: number = 10;
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async heartbeat(lockId: number): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    console.info(`heartbeat lock`);
    // ...
    // 返回心跳检查的结果
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'heartbeat succeeded',
      value: {
        interval: test_time,
        lockId: test_lockId
      }
    };
  }
  // ...
}
```

ArkTS-Sta示例：

```TypeScript
import cloudExtension from '@ohos.data.cloudExtension';
let test_lockId: int = 1;
let test_time: int = 10;
export default class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async heartbeat(lockId: int): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    console.info(`heartbeat lock`);
    // ...
    // 返回插入数据的结果
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'heartbeat succeeded',
      value: {
        interval: test_time,
        lockId: test_lockId
      }
    };
  }
  // ...
  async generateId(count: int): Promise<cloudExtension.Result<string[]>> {
    return { code: 0, value: [] };
  }
  async query(table: string, fields: string[], queryCount: int, queryCursor: string): Promise<cloudExtension.Result<cloudExtension.CloudData>> {
    return { code: 0, value: { values: [], hasMore: false, nextCursor: "" } as cloudExtension.CloudData };
  }
  async insert(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async update(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async delete(table: string, values: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async lock(): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
  async unlock(sessionId: int): Promise<cloudExtension.Result<boolean>> {
    return { code: 0, value: true };
  }
}
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

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

**示例**

ArkTS-Dyn示例：

```TypeScript
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async insert(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extensions: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    console.info(`insert, table: ${table}`);
    let insertRes: Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>> = [];
    // ...
    // 返回插入数据的结果
    return insertRes;
  }
  // ...
}
```

ArkTS-Sta示例：

```TypeScript
import cloudExtension from '@ohos.data.cloudExtension';
export default class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async insert(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extensions: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    console.info(`insert, table: ${table}`);
    let insertRes: Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>> = [];
    // ...
    // 返回插入数据的结果
    return insertRes;
  }
  // ...
  async generateId(count: int): Promise<cloudExtension.Result<string[]>> {
    return { code: 0, value: [] };
  }
  async query(table: string, fields: string[], queryCount: int, queryCursor: string): Promise<cloudExtension.Result<cloudExtension.CloudData>> {
    return {
      code: 0,
      value: {
        values: [],
        hasMore: false,
        nextCursor: ""
      } as cloudExtension.CloudData
    };
  }
  async update(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async delete(table: string, values: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async lock(): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
  async unlock(sessionId: int): Promise<cloudExtension.Result<boolean>> {
    return { code: 0, value: true };
  }
  async heartbeat(sessionId: int): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
}
```

## lock

```TypeScript
lock(): Promise<Result<LockInfo>>
```

为云数据库加锁。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;LockInfo & gt; & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
let test_time: number = 10;
let test_lockId: number = 1;
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async lock(): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    console.info(`DB lock`);
    // ...
    // 返回锁定数据的结果
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'lock succeeded',
      value: {
        interval: test_time,
        lockId: test_lockId
      }
    };
  }
  // ...
}
```

ArkTS-Sta示例：

```TypeScript
import cloudExtension from '@ohos.data.cloudExtension';
let test_time: int = 10;
let test_lockId: int = 1;
export default class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async lock(): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    console.info(`DB lock`);
    // ...
    // 返回插入数据的结果
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'lock succeeded',
      value: {
        interval: test_time,
        lockId: test_lockId
      }
    };
  }
  // ...
  async generateId(count: int): Promise<cloudExtension.Result<string[]>> {
    return { code: 0, value: [] };
  }
  async query(table: string, fields: string[], queryCount: int, queryCursor: string): Promise<cloudExtension.Result<cloudExtension.CloudData>> {
    return { code: 0, value: { values: [], hasMore: false, nextCursor: "" } as cloudExtension.CloudData };
  }
  async insert(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async update(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async delete(table: string, values: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async unlock(sessionId: int): Promise<cloudExtension.Result<boolean>> {
    return { code: 0, value: true };
  }
  async heartbeat(sessionId: int): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
}
```

## query

ArkTS-Dyn:
```TypeScript
query(table: string, fields: Array<string>, queryCount: number, queryCursor: string): Promise<Result<CloudData>>
```

ArkTS-Sta:
```TypeScript
query(table: string, fields: Array<string>, queryCount: int, queryCursor: string): Promise<Result<CloudData>>
```

在云数据库表中查询数据。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| table | string | 是 |
| [fields](arkts-arkdata-cloudextension-table-i-sys.md) | Array & lt;string & gt; | 是 |
| queryCount | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| queryCursor | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Result&lt;[CloudData](arkts-arkdata-cloudextension-clouddata-i-sys.md)&gt;&gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async query(table: string, fields: Array<string>, queryCount: number, queryCursor: string): Promise<cloudExtension.Result<cloudExtension.CloudData>> {
    console.info(`query, table: ${table}`);
    // ...
    // 返回查询数据的结果
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'query succeeded',
      value: {
        nextCursor: "test_nextCursor",
        hasMore: true,
        values: []
      }
    };
  }
  // ...
}
```

ArkTS-Sta示例：

```TypeScript
import cloudExtension from '@ohos.data.cloudExtension';
export default class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async query(table: string, fields: Array<string>, queryCount: int, queryCursor: string): Promise<cloudExtension.Result<cloudExtension.CloudData>> {
    console.info(`query, table: ${table}`);
    // ...
    // 返回插入数据的结果
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'query succeeded',
      value: {
        nextCursor: "test_nextCursor",
        hasMore: true,
        values: []
      }
    };
  }
  // ...
  async generateId(count: int): Promise<cloudExtension.Result<string[]>> {
    return { code: 0, value: [] };
  }
  async insert(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async update(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async delete(table: string, values: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async lock(): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
  async unlock(sessionId: int): Promise<cloudExtension.Result<boolean>> {
    return { code: 0, value: true };
  }
  async heartbeat(sessionId: int): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
}
```

## unlock

ArkTS-Dyn:
```TypeScript
unlock(lockId: number): Promise<Result<boolean>>
```

ArkTS-Sta:
```TypeScript
unlock(lockId: int): Promise<Result<boolean>>
```

为云数据库解锁。使用Promise异步回调。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [lockId](arkts-arkdata-cloudextension-lockinfo-i-sys.md) | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & lt;boolean & gt; & gt; |

**示例**

ArkTS-Dyn示例：

```TypeScript
class MyCloudDB implements cloudExtension.CloudDB {
    // ...
  async unlock(lockId: number): Promise<cloudExtension.Result<boolean>> {
    console.info(`unlock`);
    // ...
    // 返回解锁数据的结果
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'unlock succeeded',
      value: false
    };
  }
  // ...
}
```

ArkTS-Sta示例：

```TypeScript
import cloudExtension from '@ohos.data.cloudExtension';
export default class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async unlock(lockId: int): Promise<cloudExtension.Result<boolean>> {
    console.info(`unlock`);
    // ...
    // 返回插入数据的结果
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'unlock succeeded',
      value: false
    };
  }
  // ...
  async generateId(count: int): Promise<cloudExtension.Result<string[]>> {
    return { code: 0, value: [] };
  }
  async query(table: string, fields: string[], queryCount: int, queryCursor: string): Promise<cloudExtension.Result<cloudExtension.CloudData>> {
    return { code: 0, value: { values: [], hasMore: false, nextCursor: "" } as cloudExtension.CloudData };
  }
  async insert(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async update(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async delete(table: string, values: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async lock(): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
  async heartbeat(sessionId: int): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
}
```

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

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

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

**示例**

ArkTS-Dyn示例：

```TypeScript
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async update(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extensions: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    console.info(`update, table: ${table}`);
    let updateRes: Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>> = [];
    // ...
    // 返回更新数据的结果
    return updateRes;
  }
  // ...
}
```

ArkTS-Sta示例：

```TypeScript
import cloudExtension from '@ohos.data.cloudExtension';
export default class MyCloudDB implements cloudExtension.CloudDB {
  async update(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extensions: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    console.info(`update, table: ${table}`);
    let updateRes: Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>> = [];
    // ...
    // 返回更新数据的结果
    return updateRes;
  }
  async generateId(count: int): Promise<cloudExtension.Result<string[]>> {
    return { code: 0, value: [] };
  }
  async query(table: string, fields: string[], queryCount: int, queryCursor: string): Promise<cloudExtension.Result<cloudExtension.CloudData>> {
    return {
      code: 0,
      value: {
        values: [],
        hasMore: false,
        nextCursor: ""
      } as cloudExtension.CloudData
    };
  }
  async insert(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extValues: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async delete(table: string, values: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    return [{ code: 0, value: {} } as cloudExtension.Result<Record<string, cloudExtension.CloudType>>];
  }
  async lock(): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
  async unlock(sessionId: int): Promise<cloudExtension.Result<boolean>> {
    return { code: 0, value: true };
  }
  async heartbeat(sessionId: int): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    return { code: 0, value: { lockId: 0, interval: 0 } };
  }
  // ...
}
```
