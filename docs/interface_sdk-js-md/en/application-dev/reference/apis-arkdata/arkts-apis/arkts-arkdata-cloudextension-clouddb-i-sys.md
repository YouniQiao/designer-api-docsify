# CloudDB (System API)

Provides APIs for performing cloud database operations.

**Since:** 11

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

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| [extensions](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-nnrtdevice-i.md) | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt;&gt;&gt; |

## generateId

```TypeScript
generateId(count: number): Promise<Result<Array<string>>>
```

Generates IDs for the data records inserted to the cloud database. The IDs are unique. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| count | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;Array & lt;string & gt; & gt; & gt; |

## heartbeat

```TypeScript
heartbeat(lockId: number): Promise<Result<LockInfo>>
```

Extends the lock period of the database. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [lockId](arkts-arkdata-cloudextension-lockinfo-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
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

Inserts data to a cloud database table. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | Yes |
| [extensions](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-nnrtdevice-i.md) | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt;&gt;&gt; |

## lock

```TypeScript
lock(): Promise<Result<LockInfo>>
```

Locks this cloud database. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Result & lt;LockInfo & gt; & gt; |

## query

```TypeScript
query(table: string, fields: Array<string>, queryCount: number, queryCursor: string): Promise<Result<CloudData>>
```

Queries data in a cloud database table. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| [fields](arkts-arkdata-cloudextension-table-i-sys.md) | Array & lt;string & gt; | Yes |
| queryCount | number | Yes |
| queryCursor | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Result&lt;[CloudData](arkts-arkdata-cloudextension-clouddata-i-sys.md)&gt;&gt; |

## unlock

```TypeScript
unlock(lockId: number): Promise<Result<boolean>>
```

Unlocks a cloud database. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [lockId](arkts-arkdata-cloudextension-lockinfo-i-sys.md) | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
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

Updates data in the cloud. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| table | string | Yes |
| values | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | Yes |
| [extensions](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-nnrtdevice-i.md) | Array&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;Result&lt;Record&lt;string, [CloudType](arkts-arkdata-cloudextension-cloudtype-t-sys.md)&gt;&gt;&gt;&gt; |
