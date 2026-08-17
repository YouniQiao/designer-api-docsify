# DeviceKVStore

Provides APIs for querying data in a device KV store and performing cross-device data sync. This class inherits from **SingleKVStore**. The **SingleKVStore** APIs such as **put** and **putBatch** can be used. Data is distinguished by device in a device KV store. Each device can only write and modify its own data. Data of other devices is read-only and cannot be modified. For example, a device KV store can be used to implement image sharing between devices. The images of other devices can be viewed, but not be modified or deleted. Before calling any method in **DeviceKVStore**, you must use getKVStore to obtain a **DeviceKVStore** object.

**Inheritance/Implementation:** DeviceKVStore extends [SingleKVStore](arkts-arkdata-distributedkvstore-singlekvstore-i.md#singlekvstore)

**Since:** 23

<!--Device-distributedKVStore-interface DeviceKVStore--><!--Device-distributedKVStore-interface DeviceKVStore-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## Modules to Import

```TypeScript
import { distributedKVStore } from 'distributedKVStore';
```

## getResultSet

```TypeScript
getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void
```

Obtains the KVStoreResultSet object matching the local device ID and specified predicate object.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void--><!--Device-DeviceKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates the datasharePredicates. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | Yes | {KVStoreResultSet}: the {@code KVStoreResultSet} object matching the local device ID and specified {@code dataSharePredicates.DataSharePredicates} object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameters types. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100001](../errorcode-distributedKVStore.md#15100001-subscription-count-or-result-set-count-reaches-the-limit) | Over max limits.<br>**Applicable version:** 10 and later |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |

## getResultSet

```TypeScript
getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>
```

Obtains the KVStoreResultSet object matching the local device ID and specified predicate object.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>--><!--Device-DeviceKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates the datasharePredicates. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | {KVStoreResultSet}: the { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameters types. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100001](../errorcode-distributedKVStore.md#15100001-subscription-count-or-result-set-count-reaches-the-limit) | Over max limits.<br>**Applicable version:** 10 and later |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |

## getResultSet

```TypeScript
getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void
```

Obtains the KVStoreResultSet object matching a specified Device ID and Predicate object.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceKVStore-getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void--><!--Device-DeviceKVStore-getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates the ID of the device to which the results belong. |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates the dataSharePredicates. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | Yes | {KVStoreResultSet}: the {@code KVStoreResultSet} object matching the specified deviceId and {@code dataSharePredicates.DataSharePredicates} object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameters types. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100001](../errorcode-distributedKVStore.md#15100001-subscription-count-or-result-set-count-reaches-the-limit) | Over max limits.<br>**Applicable version:** 10 and later |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |

## getResultSet

```TypeScript
getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>
```

Obtains the KVStoreResultSet object matching a specified Device ID and Predicate object.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-DeviceKVStore-getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>--><!--Device-DeviceKVStore-getResultSet(deviceId: string, predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates the ID of the device to which the results belong. |
| predicates | dataSharePredicates.DataSharePredicates | Yes | Indicates the dataSharePredicates. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[KVStoreResultSet](arkts-arkdata-distributedkvstore-kvstoreresultset-i.md)&gt; | {KVStoreResultSet}: the { |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; <br>2.Incorrect parameters types. |
| [15100005](../errorcode-distributedKVStore.md#15100005-kv-store-or-result-set-closed) | Database or result set already closed. |
| [15100003](../errorcode-distributedKVStore.md#15100003-kv-store-corrupted) | Database corrupted. |
| [15100001](../errorcode-distributedKVStore.md#15100001-subscription-count-or-result-set-count-reaches-the-limit) | Over max limits.<br>**Applicable version:** 10 and later |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed, application which is not a system application uses system API. |

