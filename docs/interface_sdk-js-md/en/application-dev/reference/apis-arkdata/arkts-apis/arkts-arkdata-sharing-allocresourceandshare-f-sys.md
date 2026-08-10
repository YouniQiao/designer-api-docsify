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

根据谓词条件匹配的数据申请共享资源标识并发起共享，返回已共享资源的结果集。如果指定了列字段，则返回的结果集中同时包含对应列的字段值，使用Promise异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns?: Array<string>    ): Promise<relationalStore.ResultSet>--><!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns?: Array<string>    ): Promise<relationalStore.ResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| storeId | string | Yes | 数据库名称。 |
| predicates | relationalStore.RdbPredicates | Yes | 表示查找共享资源标识的数据的谓词条件。 |
| participants | Array&lt;Participant&gt; | Yes | 端云共享的参与者。 |
| columns | Array&lt;string&gt; | No | 表示要查找的列字段名。默认为undefined，不返回列字段。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;relationalStore.ResultSet&gt; | Promise对象，返回查询并共享的共享资源标识结果集。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 202 | Permission verification failed, application which is not a system application uses system API. |

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

根据谓词条件匹配的数据申请共享资源标识并发起共享，返回已共享资源的结果集，使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void--><!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| storeId | string | Yes | 数据库名称。 |
| predicates | relationalStore.RdbPredicates | Yes | 表示查找共享资源标识的数据的谓词条件。 |
| participants | Array&lt;Participant&gt; | Yes | 端云共享的参与者。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;relationalStore.ResultSet&gt; | Yes | 回调函数。返回查询并共享的共享资源标识结果集。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 202 | Permission verification failed, application which is not a system application uses system API. |

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

根据谓词条件匹配的数据申请共享资源标识并发起共享，返回已共享资源的结果集并根据指定的列字段，返回的结果集中同时包含对应列的字段值，使用callback异步回调。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns: Array<string>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void--><!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns: Array<string>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| storeId | string | Yes | 数据库名称。 |
| predicates | relationalStore.RdbPredicates | Yes | 表示查找共享资源标识的数据的谓词条件。 |
| participants | Array&lt;Participant&gt; | Yes | 端云共享的参与者。 |
| columns | Array&lt;string&gt; | Yes | 表示要查找的列字段名。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;relationalStore.ResultSet&gt; | Yes | 回调函数。返回查询并共享的共享资源标识结果集。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 202 | Permission verification failed, application which is not a system application uses system API. |

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

