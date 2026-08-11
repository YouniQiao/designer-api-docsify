# CloudDB (System API)

Provides APIs for performing cloud database operations.

**Since:** 11

<!--Device-cloudExtension-export interface CloudDB--><!--Device-cloudExtension-export interface CloudDB-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

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

Deletes data from a cloud database table. This API uses a promise to return the result.

**Since:** 11

<!--Device-CloudDB-delete(      table: string,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>--><!--Device-CloudDB-delete(      table: string,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| extensions | Array&lt;Record&lt;string, CloudType&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, CloudType&gt;&gt;&gt;&gt; |

## Examples

```TypeScript
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async delete(table: string, extensions: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    console.info(`delete, table: ${table}`);
    let deleteRes: Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>> = [];
    // ...
    // Returns the result of deleting data.
    return deleteRes;
  }
  // ...
}
```

## generateId

```TypeScript
generateId(count: number): Promise<Result<Array<string>>>
```

Generates IDs for the data records inserted to the cloud database.The IDs are unique. This API uses a promise to return the result.

**Since:** 11

<!--Device-CloudDB-generateId(count: int): Promise<Result<Array<string>>>--><!--Device-CloudDB-generateId(count: int): Promise<Result<Array<string>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| count | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Result&lt;Array&lt;string&gt;&gt;&gt; |

## Examples

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

## heartbeat

```TypeScript
heartbeat(lockId: number): Promise<Result<LockInfo>>
```

Extends the lock period of the database. This API uses a promise to return the result.

**Since:** 11

<!--Device-CloudDB-heartbeat(lockId: int): Promise<Result<LockInfo>>--><!--Device-CloudDB-heartbeat(lockId: int): Promise<Result<LockInfo>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lockId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Result&lt;LockInfo&gt;&gt; |

## Examples

```TypeScript
let testLockId: number = 1;
let testTime: number = 10;
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async heartbeat(lockId: number): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    console.info(`heartbeat lock`);
    // ...
    // Return the heartbeat check result.
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'heartbeat succeeded',
      value: {
        interval: testTime,
        lockId: testLockId
      }
    };
  }
  // ...
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

Inserts data to a cloud database table. This API uses a promise to return the result.

**Since:** 11

<!--Device-CloudDB-insert(      table: string,      values: Array<Record<string, CloudType>>,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>--><!--Device-CloudDB-insert(      table: string,      values: Array<Record<string, CloudType>>,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array&lt;Record&lt;string, CloudType&gt;&gt; | Yes |
| extensions | Array&lt;Record&lt;string, CloudType&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, CloudType&gt;&gt;&gt;&gt; |

## Examples

```TypeScript
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async insert(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extensions: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    console.info(`insert, table: ${table}`);
    let insertRes: Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>> = [];
    // ...
    // Return the operation result.
    return insertRes;
  }
  // ...
}
```

## lock

```TypeScript
lock(): Promise<Result<LockInfo>>
```

Locks this cloud database. This API uses a promise to return the result.

**Since:** 11

<!--Device-CloudDB-lock(): Promise<Result<LockInfo>>--><!--Device-CloudDB-lock(): Promise<Result<LockInfo>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Result&lt;LockInfo&gt;&gt; |

## Examples

```TypeScript
let testTime: number = 10;
let testLockId: number = 1;
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async lock(): Promise<cloudExtension.Result<cloudExtension.LockInfo>> {
    console.info(`DB lock`);
    // ...
    // Returns the result of locking data.
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'lock succeeded',
      value: {
        interval: testTime,
        lockId: testLockId
      }
    };
  }
  // ...
}
```

## query

```TypeScript
query(table: string, fields: Array<string>, queryCount: number, queryCursor: string): Promise<Result<CloudData>>
```

Queries data in a cloud database table. This API uses a promise to return the result.

**Since:** 11

<!--Device-CloudDB-query(table: string, fields: Array<string>, queryCount: int, queryCursor: string): Promise<Result<CloudData>>--><!--Device-CloudDB-query(table: string, fields: Array<string>, queryCount: int, queryCursor: string): Promise<Result<CloudData>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| fields | Array&lt;string&gt; | Yes |
| queryCount | number | Yes |
| queryCursor | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Result&lt;CloudData&gt;&gt; |

## Examples

```TypeScript
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async query(table: string, fields: Array<string>, queryCount: number, queryCursor: string): Promise<cloudExtension.Result<cloudExtension.CloudData>> {
    console.info(`query, table: ${table}`);
    // ...
    // Return the result of querying data.
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

## unlock

```TypeScript
unlock(lockId: number): Promise<Result<boolean>>
```

Unlocks a cloud database. This API uses a promise to return the result.

**Since:** 11

<!--Device-CloudDB-unlock(lockId: int): Promise<Result<boolean>>--><!--Device-CloudDB-unlock(lockId: int): Promise<Result<boolean>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| lockId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Result&lt;boolean&gt;&gt; |

## Examples

```TypeScript
class MyCloudDB implements cloudExtension.CloudDB {
    // ...
  async unlock(lockId: number): Promise<cloudExtension.Result<boolean>> {
    console.info(`unlock`);
    // ...
    // Returns the result of unlocking data.
    return {
      code: cloudExtension.ErrorCode.SUCCESS,
      description: 'unlock succeeded',
      value: false
    };
  }
  // ...
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

Updates data in the cloud. This API uses a promise to return the result.

**Since:** 11

<!--Device-CloudDB-update(      table: string,      values: Array<Record<string, CloudType>>,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>--><!--Device-CloudDB-update(      table: string,      values: Array<Record<string, CloudType>>,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array&lt;Record&lt;string, CloudType&gt;&gt; | Yes |
| extensions | Array&lt;Record&lt;string, CloudType&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, CloudType&gt;&gt;&gt;&gt; |

## Examples

```TypeScript
class MyCloudDB implements cloudExtension.CloudDB {
  // ...
  async update(table: string, values: Array<Record<string, cloudExtension.CloudType>>, extensions: Array<Record<string, cloudExtension.CloudType>>): Promise<Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>>> {
    console.info(`update, table: ${table}`);
    let updateRes: Array<cloudExtension.Result<Record<string, cloudExtension.CloudType>>> = [];
    // ...
    // Return the data update result.
    return updateRes;
  }
  // ...
}
```
