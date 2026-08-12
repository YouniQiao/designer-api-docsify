# DeviceKVStore

Provides APIs for querying data in a device KV store and performing cross-device data sync. This class inherits from **SingleKVStore**. The **SingleKVStore** APIs such as **put** and **putBatch** can be used.Data is distinguished by device in a device KV store. Each device can only write and modify its own data. Data of other devices is read-only and cannot be modified.For example, a device KV store can be used to implement image sharing between devices. The images of other devices can be viewed, but not be modified or deleted.Before calling any method in **DeviceKVStore**, you must use  
[getKVStore](distributedKVStore.KVManager.getKVStore&lt;T&gt;(storeId: string, options: Options, callback: AsyncCallback&lt;T&gt;)) to obtain a **DeviceKVStore** object.

**Inheritance/Implementation:** DeviceKVStore extends [SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i.md#SingleKVStore)

**Since:** 9

<!--Device-distributedKVStore-interface DeviceKVStore extends SingleKVStore--><!--Device-distributedKVStore-interface DeviceKVStore extends SingleKVStore-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## Modules to Import

```TypeScript
import { distributedKVStore } from '@kit.ArkData';
```

## getResultSet

```TypeScript
getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void
```

Obtains the KVStoreResultSet object matching the local device ID and specified predicate object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void--><!--Device-DeviceKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15100005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) |
| [15100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100003-kv-store-corrupted) |
| [15100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100001-subscription-count-or-result-set-count-reaches-the-limit) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getResultSet

```TypeScript
getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>
```

Obtains the KVStoreResultSet object matching the local device ID and specified predicate object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>--><!--Device-DeviceKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15100005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) |
| [15100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100003-kv-store-corrupted) |
| [15100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100001-subscription-count-or-result-set-count-reaches-the-limit) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getResultSet

```TypeScript
getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void
```

Obtains the KVStoreResultSet object matching a specified Device ID and Predicate object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceKVStore-getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void--><!--Device-DeviceKVStore-getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15100005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) |
| [15100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100003-kv-store-corrupted) |
| [15100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100001-subscription-count-or-result-set-count-reaches-the-limit) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getResultSet

```TypeScript
getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>
```

Obtains the KVStoreResultSet object matching a specified Device ID and Predicate object.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceKVStore-getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>--><!--Device-DeviceKVStore-getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [15100005](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) |
| [15100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100003-kv-store-corrupted) |
| [15100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkdata/errorcode-distributedKVStore.md#15100001-subscription-count-or-result-set-count-reaches-the-limit) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
