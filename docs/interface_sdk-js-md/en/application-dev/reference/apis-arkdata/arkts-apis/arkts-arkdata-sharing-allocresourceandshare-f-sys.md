# allocResourceAndShare (System API)

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## allocResourceAndShare

```TypeScript
function allocResourceAndShare(
      storeId: string,
      predicates: relationalStore.RdbPredicates,
      participants: Array<Participant>,
      columns?: Array<string>
    ): Promise<relationalStore.ResultSet>
```

Allocates a shared resource ID based on the data that matches the specified predicates. This API uses a promise to return the result set of the data to share, which also includes the column names if they are specified.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [storeId](arkts-arkdata-clouddata-bundleinfo-i-sys.md) | string | Yes |
| predicates | relationalStore.RdbPredicates | Yes |
| participants | Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt; | Yes |
| columns | Array & lt;string & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;relationalStore.ResultSet & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |


## allocResourceAndShare

```TypeScript
function allocResourceAndShare(
      storeId: string,
      predicates: relationalStore.RdbPredicates,
      participants: Array<Participant>,
      callback: AsyncCallback<relationalStore.ResultSet>
    ): void
```

Allocates a shared resource ID based on the data that matches the specified predicates. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [storeId](arkts-arkdata-clouddata-bundleinfo-i-sys.md) | string | Yes |
| predicates | relationalStore.RdbPredicates | Yes |
| participants | Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;relationalStore.ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |


## allocResourceAndShare

```TypeScript
function allocResourceAndShare(
      storeId: string,
      predicates: relationalStore.RdbPredicates,
      participants: Array<Participant>,
      columns: Array<string>,
      callback: AsyncCallback<relationalStore.ResultSet>
    ): void
```

Allocates a shared resource ID based on the data that matches the specified predicates. This API uses an asynchronous callback to return the result set of the data to share, which includes the shared resource ID and column names.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [storeId](arkts-arkdata-clouddata-bundleinfo-i-sys.md) | string | Yes |
| predicates | relationalStore.RdbPredicates | Yes |
| participants | Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt; | Yes |
| columns | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;relationalStore.ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
