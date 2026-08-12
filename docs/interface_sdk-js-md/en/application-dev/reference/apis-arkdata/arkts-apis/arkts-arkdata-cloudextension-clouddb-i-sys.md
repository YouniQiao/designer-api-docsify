# CloudDB (System API)

Provides APIs for performing cloud database operations.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-export interface CloudDB--><!--Device-cloudExtension-export interface CloudDB-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## Modules to Import

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

Deletes data from a cloud database table. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudDB-delete(      table: string,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>--><!--Device-CloudDB-delete(      table: string,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | Table name. |
| extensions | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | Yes | Extended information about the current data. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt;&gt;&gt; | Promise used to return the deleted data and operation result. |

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

ArkTS-Dyn:
```TypeScript
generateId(count: number): Promise<Result<Array<string>>>
```

ArkTS-Sta:
```TypeScript
generateId(count: int): Promise<Result<Array<string>>>
```

Generates IDs for the data records inserted to the cloud database.The IDs are unique. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudDB-generateId(count: int): Promise<Result<Array<string>>>--><!--Device-CloudDB-generateId(count: int): Promise<Result<Array<string>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of IDs to generate. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&lt;Array&lt;string&gt;&gt;&gt; | Promise used to return the generated IDs in Result. |

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

ArkTS-Dyn:
```TypeScript
heartbeat(lockId: number): Promise<Result<LockInfo>>
```

ArkTS-Sta:
```TypeScript
heartbeat(lockId: int): Promise<Result<LockInfo>>
```

Extends the lock period of the database. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudDB-heartbeat(lockId: int): Promise<Result<LockInfo>>--><!--Device-CloudDB-heartbeat(lockId: int): Promise<Result<LockInfo>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lockId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Lock ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&lt;LockInfo&gt;&gt; | Promise used to return the lock ID and lock period. |

## Examples

```TypeScript
let test_lockId: number = 1;
let test_time: number = 10;
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
        interval: test_time,
        lockId: test_lockId
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

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudDB-insert(      table: string,      values: Array<Record<string, CloudType>>,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>--><!--Device-CloudDB-insert(      table: string,      values: Array<Record<string, CloudType>>,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | Table name. |
| values | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | Yes | Data to insert. |
| extensions | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | Yes | Extended information about the current data. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt;&gt;&gt; | Promise used to return the inserted data and operation result. |

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

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudDB-lock(): Promise<Result<LockInfo>>--><!--Device-CloudDB-lock(): Promise<Result<LockInfo>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&lt;LockInfo&gt;&gt; | Promise used to return the lock ID and lock period. |

## Examples

```TypeScript
let test_time: number = 10;
let test_lockId: number = 1;
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
        interval: test_time,
        lockId: test_lockId
      }
    };
  }
  // ...
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

Queries data in a cloud database table. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudDB-query(table: string, fields: Array<string>, queryCount: int, queryCursor: string): Promise<Result<CloudData>>--><!--Device-CloudDB-query(table: string, fields: Array<string>, queryCount: int, queryCursor: string): Promise<Result<CloudData>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | Table name. |
| fields | Array&lt;string&gt; | Yes | Name of the fields to query. |
| queryCount | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Number of data records to query. |
| queryCursor | string | Yes | Cursor for the query. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&lt;[CloudData](arkts-arkdata-cloudextension-clouddata-i-sys.md)&gt;&gt; | Promise used to return the data and operation result. |

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

ArkTS-Dyn:
```TypeScript
unlock(lockId: number): Promise<Result<boolean>>
```

ArkTS-Sta:
```TypeScript
unlock(lockId: int): Promise<Result<boolean>>
```

Unlocks a cloud database. This API uses a promise to return the result.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudDB-unlock(lockId: int): Promise<Result<boolean>>--><!--Device-CloudDB-unlock(lockId: int): Promise<Result<boolean>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lockId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Lock ID to release. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Result&lt;boolean&gt;&gt; | Promise used to return the result. The value true means the operation is successful; the value false means the opposite. |

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

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-CloudDB-update(      table: string,      values: Array<Record<string, CloudType>>,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>--><!--Device-CloudDB-update(      table: string,      values: Array<Record<string, CloudType>>,      extensions: Array<Record<string, CloudType>>    ): Promise<Array<Result<Record<string, CloudType>>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| table | string | Yes | Table name. |
| values | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | Yes | Data to insert. |
| extensions | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | Yes | Extended information about the current data. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt;&gt;&gt; | Promise used to return the update result and updated data. |

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

