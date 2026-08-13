# allocResourceAndShare（系统接口）

## allocResourceAndShare

```TypeScript
function allocResourceAndShare(
      storeId: string,
      predicates: relationalStore.RdbPredicates,
      participants: Array<Participant>,
      columns?: Array<string>
    ): Promise<relationalStore.ResultSet>
```

根据谓词条件匹配的数据申请共享资源标识并发起共享，返回已共享资源的结果集。 如果指定了列字段，则返回的结果集中同时包含对应列的字段值，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns?: Array<string>    ): Promise<relationalStore.ResultSet>--><!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns?: Array<string>    ): Promise<relationalStore.ResultSet>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [storeId](arkts-arkdata-clouddata-bundleinfo-i-sys.md) | string | 是 |
| predicates | relationalStore.RdbPredicates | 是 |
| participants | Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt; | 是 |
| columns | Array & lt;string & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;relationalStore.ResultSet & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
});
let sharingResource: string;
let predicates = new relationalStore.RdbPredicates('test_table');
predicates.equalTo('data', 'data_test');
cloudData.sharing.allocResourceAndShare('storeName', predicates, participants, ['uuid', 'data']).then((resultSet) => {
  try {
    if (!resultSet.goToFirstRow()) {
      console.error(`row error`);
      return;
    }
    const res = resultSet.getString(resultSet.getColumnIndex(relationalStore.Field.SHARING_RESOURCE_FIELD));
    console.info(`sharing resource: ${res}`);
    sharingResource = res;
  } catch (err) {
    console.error(`Failed to get sharing resource: ${err}`);
  } finally {
    resultSet.close();
  }
}).catch((err: BusinessError) => {
  console.error(`alloc resource and share failed, code is ${err.code},message is ${err.message}`);
});
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

**起始版本：** 23

**废弃版本：** -1

<!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void--><!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [storeId](arkts-arkdata-clouddata-bundleinfo-i-sys.md) | string | 是 |
| predicates | relationalStore.RdbPredicates | 是 |
| participants | Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;relationalStore.ResultSet&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
});
let sharingResource: string;
let predicates = new relationalStore.RdbPredicates('test_table');
predicates.equalTo('data', 'data_test');
cloudData.sharing.allocResourceAndShare('storeName', predicates, participants, (err: BusinessError, resultSet) => {
  if (err) {
    console.error(`alloc resource and share failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  try {
    if (!resultSet.goToFirstRow()) {
      console.error(`row error`);
      return;
    }
    const res = resultSet.getString(resultSet.getColumnIndex(relationalStore.Field.SHARING_RESOURCE_FIELD));
    console.info(`sharing resource: ${res}`);
    sharingResource = res;
  } catch (err) {
    console.error(`Failed to get sharing resource: ${err}`);
  } finally {
    resultSet.close();
  }
});
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

根据谓词条件匹配的数据申请共享资源标识并发起共享，返回已共享资源的结果集 并根据指定的列字段，返回的结果集中同时包含对应列的字段值，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns: Array<string>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void--><!--Device-sharing-function allocResourceAndShare(      storeId: string,      predicates: relationalStore.RdbPredicates,      participants: Array<Participant>,      columns: Array<string>,      callback: AsyncCallback<relationalStore.ResultSet>    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [storeId](arkts-arkdata-clouddata-bundleinfo-i-sys.md) | string | 是 |
| predicates | relationalStore.RdbPredicates | 是 |
| participants | Array&lt;[Participant](arkts-arkdata-sharing-participant-i-sys.md)&gt; | 是 |
| columns | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;relationalStore.ResultSet&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
});
let sharingResource: string;
let predicates = new relationalStore.RdbPredicates('test_table');
predicates.equalTo('data', 'data_test');
cloudData.sharing.allocResourceAndShare('storeName', predicates, participants, ['uuid', 'data'], (err: BusinessError, resultSet) => {
  if (err) {
    console.error(`alloc resource and share failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  try {
    if (!resultSet.goToFirstRow()) {
      console.error(`row error`);
      return;
    }
    const res = resultSet.getString(resultSet.getColumnIndex(relationalStore.Field.SHARING_RESOURCE_FIELD));
    console.info(`sharing resource: ${res}`);
    sharingResource = res;
  } catch (err) {
    console.error(`Failed to get sharing resource: ${err}`);
  } finally {
    resultSet.close();
  }
});
```
