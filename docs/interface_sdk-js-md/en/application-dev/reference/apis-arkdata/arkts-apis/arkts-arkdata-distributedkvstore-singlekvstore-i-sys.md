# SingleKVStore

SingleKVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据端端同步完成的方法。

在调用SingleKVStore的方法前，需要先通过  
[getKVStore](arkts-arkdata-distributedkvstore-kvmanager-i.md#getkvstore)构建一个SingleKVStore实例。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-distributedKVStore-interface SingleKVStore--><!--Device-distributedKVStore-interface SingleKVStore-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

## Modules to Import

```TypeScript
import { distributedKVStore } from 'kits/@kit.ArkData';
```

## delete

```TypeScript
delete(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): void
```

从数据库中删除符合predicates条件的键值对，使用callback异步回调。

**ArkTS mode:** ArkTS-Dyn only

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): void--><!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes | 指示筛选条件，不允许为null。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。成功时err为undefined，失败时err为错误对象。 [ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameters types. [ |
| 15100003 | Database corrupted. [ |
| 14800047 | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |

## delete

```TypeScript
delete(predicates: dataSharePredicates.DataSharePredicates): Promise<void>
```

从数据库中删除符合predicates条件的键值对，使用Promise异步回调。

**ArkTS mode:** ArkTS-Dyn only

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates): Promise<void>--><!--Device-SingleKVStore-delete(predicates: dataSharePredicates.DataSharePredicates): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes | 指示筛选条件，不允许为null。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 [ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameters types. [ |
| 15100003 | Database corrupted. [ |
| 14800047 | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |

## getResultSet

```TypeScript
getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void
```

获取与指定Predicates对象匹配的KVStoreResultSet对象，使用callback异步回调。获取结果集后，需要及时调用closeResultSet方法关闭结果集以释放资源。

**ArkTS mode:** ArkTS-Dyn only

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void--><!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<KVStoreResultSet>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes | 指示筛选条件，不允许为null。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;KVStoreResultSet&gt; | Yes | 回调函数，获取与指定Predicates对象匹配的KVStoreResultSet对象。 [ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameters types. [ |
| 15100003 | Database corrupted. [ |
| 15100001 | Over max limits.<br>**Applicable version:** 10 and later |

## getResultSet

```TypeScript
getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>
```

获取与指定Predicates对象匹配的KVStoreResultSet对象，使用Promise异步回调。获取结果集后，需要及时调用closeResultSet方法关闭结果集以释放资源。

**ArkTS mode:** ArkTS-Dyn only

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>--><!--Device-SingleKVStore-getResultSet(predicates: dataSharePredicates.DataSharePredicates): Promise<KVStoreResultSet>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Provider

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | Yes | 指示筛选条件，不允许为null。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;KVStoreResultSet&gt; | Promise对象。返回KVStoreResultSet对象。 [ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameters types. [ |
| 15100003 | Database corrupted. [ |
| 15100001 | Over max limits.<br>**Applicable version:** 10 and later |

## putBatch

```TypeScript
putBatch(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void
```

批量写入键值对数据，每个ValuesBucket对象包含key和value字段，使用callback异步回调。

**ArkTS mode:** ArkTS-Dyn only

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void--><!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | 表示要插入的数据。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。成功时err为undefined，失败时err为错误对象。 [ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameters types. [ |
| 15100003 | Database corrupted. [ |
| 14800047 | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |

## putBatch

```TypeScript
putBatch(value: Array<ValuesBucket>): Promise<void>
```

批量写入键值对数据，每个ValuesBucket对象包含key和value字段，使用Promise异步回调。

**ArkTS mode:** ArkTS-Dyn only

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>): Promise<void>--><!--Device-SingleKVStore-putBatch(value: Array<ValuesBucket>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | 表示要插入的数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 [ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error.Possible causes:1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameters types. [ |
| 15100003 | Database corrupted. [ |
| 14800047 | The WAL file size exceeds the default limit.<br>**Applicable version:** 10 and later |

## putValuesBuckets

```TypeScript
putValuesBuckets(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void
```

将值写入SingleKVStore数据库，使用callback异步回调。

**ArkTS mode:** ArkTS-Dyn only

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void--><!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | 表示要插入的数据。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 回调函数。 [ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15100005 | Database or result set already closed. [ |
| 202 | Permission verification failed, application which is not a system application uses system API. [ |

## putValuesBuckets

```TypeScript
putValuesBuckets(value: Array<ValuesBucket>): Promise<void>
```

将valuesbucket类型的值写入SingleKVStore数据库，使用Promise异步回调。

**ArkTS mode:** ArkTS-Dyn only

**Model restriction:** This API can be used only in the stage model.

<!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>): Promise<void>--><!--Device-SingleKVStore-putValuesBuckets(value: Array<ValuesBucket>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes | 表示要插入的数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 [ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15100005 | Database or result set already closed. [ |
| 202 | Permission verification failed, application which is not a system application uses system API. [ |

