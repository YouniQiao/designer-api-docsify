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

Allocates a shared resource ID based on the data that matches the specified predicates.This API uses a promise to return the result set of the data to share,which also includes the column names if they are specified.

**Since:** 11

<!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns?: Array<string>    ): Promise<relationalStore.ResultSet>--><!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns?: Array<string>    ): Promise<relationalStore.ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| storeId | string | Yes |
| predicates | relationalStore.RdbPredicates | Yes |
| participants | Array&lt;Participant&gt; | Yes |
| columns | Array&lt;string&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;relationalStore.ResultSet&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { relationalStore } from '@kit.ArkData';

let participants = new Array<cloudData.sharing.Participant>();
participants.push({
  identity: '000000000',
  role: cloudData.sharing.Role.ROLE_INVITER,
  state: cloudData.sharing.State.STATE_UNKNOWN,
  privilege: {
    writable: true,
    readable: true,
    creatable: false,
    deletable: false,
    shareable: false
  },
  attachInfo: ''
})
let sharingResource: string;
let predicates = new relationalStore.RdbPredicates('test_table');
predicates.equalTo('data', 'data_test');
cloudData.sharing.allocResourceAndShare('storeName', predicates, participants, ['uuid', 'data']).then((resultSet) => {
  if (!resultSet.goToFirstRow()) {
    console.error(`row error`);
    return;
  }
  const res = resultSet.getString(resultSet.getColumnIndex(relationalStore.Field.SHARING_RESOURCE_FIELD));
  console.info(`sharing resource: ${res}`);
  sharingResource = res;
}).catch((err: BusinessError) => {
  console.error(`alloc resource and share failed, code is ${err.code},message is ${err.message}`);
})
```


## allocResourceAndShare

```TypeScript
function allocResourceAndShare(
      storeId: string,
      predicates: relationalStore.RdbPredicates,
      participants: Array<Participant>,
      callback: AsyncCallback<relationalStore.ResultSet>
    ): void
```

Allocates a shared resource ID based on the data that matches the specified predicates.This API uses an asynchronous callback to return the result.

**Since:** 11

<!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void--><!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| storeId | string | Yes |
| predicates | relationalStore.RdbPredicates | Yes |
| participants | Array&lt;Participant&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;relationalStore.ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let participants = new Array<cloudData.sharing.Participant>();
participants.push({
  identity: '000000000',
  role: cloudData.sharing.Role.ROLE_INVITER,
  state: cloudData.sharing.State.STATE_UNKNOWN,
  privilege: {
    writable: true,
    readable: true,
    creatable: false,
    deletable: false,
    shareable: false
  },
  attachInfo: ''
})
let sharingResource: string;
let predicates = new relationalStore.RdbPredicates('test_table');
predicates.equalTo('data', 'data_test');
cloudData.sharing.allocResourceAndShare('storeName', predicates, participants, (err: BusinessError, resultSet) => {
  if (err) {
    console.error(`alloc resource and share failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  if (!resultSet.goToFirstRow()) {
    console.error(`row error`);
    return;
  }
  const res = resultSet.getString(resultSet.getColumnIndex(relationalStore.Field.SHARING_RESOURCE_FIELD));
  console.info(`sharing resource: ${res}`);
  sharingResource = res;
})
```


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

Allocates a shared resource ID based on the data that matches the specified predicates.This API uses an asynchronous callback to return the result set of the data to share,which includes the shared resource ID and column names.

**Since:** 11

<!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns: Array<string>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void--><!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns: Array<string>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| storeId | string | Yes |
| predicates | relationalStore.RdbPredicates | Yes |
| participants | Array&lt;Participant&gt; | Yes |
| columns | Array&lt;string&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;relationalStore.ResultSet&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let participants = new Array<cloudData.sharing.Participant>();
participants.push({
  identity: '000000000',
  role: cloudData.sharing.Role.ROLE_INVITER,
  state: cloudData.sharing.State.STATE_UNKNOWN,
  privilege: {
    writable: true,
    readable: true,
    creatable: false,
    deletable: false,
    shareable: false
  },
  attachInfo: ''
})
let sharingResource: string;
let predicates = new relationalStore.RdbPredicates('test_table');
predicates.equalTo('data', 'data_test');
cloudData.sharing.allocResourceAndShare('storeName', predicates, participants, ['uuid', 'data'], (err: BusinessError, resultSet) => {
  if (err) {
    console.error(`alloc resource and share failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  if (!resultSet.goToFirstRow()) {
    console.error(`row error`);
    return;
  }
  const res = resultSet.getString(resultSet.getColumnIndex(relationalStore.Field.SHARING_RESOURCE_FIELD));
  console.info(`sharing resource: ${res}`);
  sharingResource = res;
})
```
