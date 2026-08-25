# DataShareHelper (System API)

Provides a **DataShareHelper** instance to access or manage data on the server. Before calling an API provided by **DataShareHelper**, you must create a **DataShareHelper** instance using [createDataShareHelper](arkts-arkdata-datashare-createdatasharehelper-f-sys.md).

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## addTemplate

```TypeScript
addTemplate(uri: string, subscriberId: string, template: Template): void
```

Adds a data template with the specified subscriber. Only silent access is supported.In silent scenarios, the total size of the **uri**, **subscriberId**, and **template** parameters passed in this API cannot exceed 200 KB. If the size exceeds the limit, the operation fails or an exception is thrown.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| subscriberId | string | Yes |
| template | [Template](arkts-arkdata-datashare-template-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700011](../errorcode-datashare.md#15700011-uri-not-exist) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## batchInsert

```TypeScript
batchInsert(uri: string, values: Array<ValuesBucket>, callback: AsyncCallback<number>): void
```

Batch inserts data into the database. This API uses an asynchronous callback to return the result. Silent access is not supported currently.In non-silent scenarios, the size of the **values** parameter and the **uri** parameter passed in this API cannot exceed 128 MB and 900 KB, respectively. Otherwise, the operation fails or an exception is thrown.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| values | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## batchInsert

```TypeScript
batchInsert(uri: string, values: Array<ValuesBucket>): Promise<number>
```

Batch inserts data into the database. This API uses a promise to return the result. Silent access is not supported currently.In non-silent scenarios, the size of the **values** parameter and the **uri** parameter passed in this API cannot exceed 128 MB and 900 KB, respectively. Otherwise, the operation fails or an exception is thrown.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| values | Array&lt;[ValuesBucket](arkts-arkdata-valuesbucket-t.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## batchUpdate

```TypeScript
batchUpdate(operations: Record<string, Array<UpdateOperation>>): Promise<Record<string, Array<number>>>
```

Batch updates data in the database. The total number of objects for operations (that is, KV pairs of the objects) cannot exceed 4000. If the number exceeds 4000, the update will fail. The transaction of this API depends on the data provider. This API uses a promise to return the result. Silent access is not supported currently.In non-silent scenarios, the size of the **operations** parameter passed in this API called cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| operations | Record & lt;string, Array & lt;UpdateOperation & gt; & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Record & lt;string, Array & lt;number & gt; & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## close

```TypeScript
close(): Promise<void>
```

Closes the **DataShareHelper** instance. After this API is called, the instance becomes invalid. This API uses a promise to return the result.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |

## delete

```TypeScript
delete(uri: string, predicates: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<number>): void
```

Deletes one or more data records from the database. This API uses an asynchronous callback to return the result.In non-silent scenarios, the total size of the **uri** and **predicates** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown.In silent scenarios, the total size of the **uri** and **predicates** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## delete

```TypeScript
delete(uri: string, predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

Deletes one or more data records from the database. This API uses a promise to return the result.In non-silent scenarios, the total size of the **uri** and **predicates** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown.In silent scenarios, the total size of the **uri** and **predicates** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## delTemplate

```TypeScript
delTemplate(uri: string, subscriberId: string): void
```

Deletes a data template based on the specified subscriber. Only silent access is supported.In silent scenarios, the total size of the **uri** and **subscriberId** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| subscriberId | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700011](../errorcode-datashare.md#15700011-uri-not-exist) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## denormalizeUri

```TypeScript
denormalizeUri(uri: string, callback: AsyncCallback<string>): void
```

Denormalizes a URI. This API uses an asynchronous callback to return the result. Silent access is not supported currently.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## denormalizeUri

```TypeScript
denormalizeUri(uri: string): Promise<string>
```

Denormalizes a URI. This API uses a promise to return the result. Silent access is not supported currently.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## getPublishedData

```TypeScript
getPublishedData(bundleName: string, callback: AsyncCallback<Array<PublishedItem>>): void
```

Obtains the published data of an application. Only silent access is supported. This API uses an asynchronous callback to return the result.In silent scenarios, the size of the **bundleName** parameter passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700012](../errorcode-datashare.md#15700012-data-area-not-exist) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## getPublishedData

```TypeScript
getPublishedData(bundleName: string): Promise<Array<PublishedItem>>
```

Obtains the published data of an application. Only silent access is supported. This API uses a promise to return the result.In silent scenarios, the size of the **bundleName** parameter passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700012](../errorcode-datashare.md#15700012-data-area-not-exist) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## insert

```TypeScript
insert(uri: string, value: ValuesBucket, callback: AsyncCallback<number>): void
```

Inserts a single data record into the database. This API uses an asynchronous callback to return the result.In non-silent scenarios, the total size of the **uri** and **value** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown.In silent scenarios, the total size of the **uri** and **value** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## insert

```TypeScript
insert(uri: string, value: ValuesBucket): Promise<number>
```

Inserts a single data record into the database. This API uses a promise to return the result.In non-silent scenarios, the total size of the **uri** and **value** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown.In silent scenarios, the total size of the **uri** and **value** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## normalizeUri

```TypeScript
normalizeUri(uri: string, callback: AsyncCallback<string>): void
```

Normalizes a **DataShare** URI. The **DataShare** URI can be used only by the local device, but the normalized URI can be used across devices. This API uses an asynchronous callback to return the result. Silent access is not supported currently.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## normalizeUri

```TypeScript
normalizeUri(uri: string): Promise<string>
```

Normalizes a **DataShare** URI. The **DataShare** URI can be used only by the local device, but the normalized URI can be used across devices. This API uses a promise to return the result. Silent access is not supported currently.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## notifyChange

```TypeScript
notifyChange(uri: string, callback: AsyncCallback<void>): void
```

Notifies the registered observer of data changes. This API uses an asynchronous callback to return the result. Silent access is not supported currently.In non-silent scenarios, the size of the **uri** parameter passed in this API called cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## notifyChange

```TypeScript
notifyChange(uri: string): Promise<void>
```

Notifies the registered observer of data changes. This API uses a promise to return the result. Silent access is not supported currently.In non-silent scenarios, the size of the **uri** parameter passed in this API called cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## notifyChange

```TypeScript
notifyChange(data: ChangeInfo): Promise<void>
```

Notifies the observer of the data change of the specified URI. This API uses a promise to return the result. Silent access is not supported currently.In non-silent scenarios, the size of the **data** parameter passed in this API called cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [ChangeInfo](arkts-arkdata-relationalstore-changeinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## off('dataChange')

```TypeScript
off(type: 'dataChange', uri: string, callback?: AsyncCallback<void>): void
```

Unsubscribes from the data change of the specified URI. This API corresponds to the on API.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataChange' | Yes |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## off

```TypeScript
off(event: 'dataChange', type:SubscriptionType, uri: string, callback?: AsyncCallback<ChangeInfo>): void
```

Unsubscribes from the data change of the specified URI. This API corresponds to the on API.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | Yes |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ChangeInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## off('rdbDataChange')

```TypeScript
off(
       type: 'rdbDataChange',
       uris: Array<string>,
       templateId: TemplateId,
       callback?: AsyncCallback<RdbDataChangeNode>
     ): Array<OperationResult>
```

Unsubscribes from the changes of the data corresponding to the specified URI and template. Only silent access is supported.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'rdbDataChange' | Yes |
| uris | Array & lt;string & gt; | Yes |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## off('publishedDataChange')

```TypeScript
off(
       type: 'publishedDataChange',
       uris: Array<string>,
       subscriberId: string,
       callback?: AsyncCallback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

Unsubscribes from the change of the published data. Only silent access is supported.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'publishedDataChange' | Yes |
| uris | Array & lt;string & gt; | Yes |
| subscriberId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## on('dataChange')

```TypeScript
on(type: 'dataChange', uri: string, callback: AsyncCallback<void>): void
```

Subscribes to the data change of the specified URI. After an observer is registered, the subscriber will receive a notification when the **notifyChange** API is called. This API uses an asynchronous callback to return the result. This function does not support cross-user notification subscription. An application can subscribe to a single URI for a maximum of 51 times.Notification triggering: In non-silent scenarios, a notification is published if the [notifyChange](#notifychange) method is called. In silent scenarios, a notification is automatically published if data is modified via silent access.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'dataChange' | Yes |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## on

```TypeScript
on(event: 'dataChange', type:SubscriptionType, uri: string, callback: AsyncCallback<ChangeInfo>): void
```

Subscribes to the data change of the specified URI. After a change notification is registered, the subscriber will receive a notification when the **notifyChange** API is called. The change notification contains the data change type, URI of the data changed, and the changed data. This API uses an asynchronous callback to return the result. This function does not support cross-user notification subscription. An application can subscribe to a single URI for a maximum of 51 times.Notification triggering: In non-silent scenarios, a notification is published if the [notifyChange](#notifychange) method is called. In silent scenarios, a notification is automatically published if data is modified via silent access, but **changeInfo** in the callback is invalid.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| type | [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e-sys.md) | Yes |
| uri | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;ChangeInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## on('rdbDataChange')

```TypeScript
on(
       type: 'rdbDataChange',
       uris: Array<string>,
       templateId: TemplateId,
       callback: AsyncCallback<RdbDataChangeNode>
     ): Array<OperationResult>
```

Subscribes to the changes of the data corresponding to the specified URI and template. Only silent access is supported. This function does not support cross-user notification subscription.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'rdbDataChange' | Yes |
| uris | Array & lt;string & gt; | Yes |
| templateId | [TemplateId](arkts-arkdata-datashare-templateid-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## on('publishedDataChange')

```TypeScript
on(
       type: 'publishedDataChange',
       uris: Array<string>,
       subscriberId: string,
       callback: AsyncCallback<PublishedDataChangeNode>
     ): Array<OperationResult>
```

Subscribes to the change of the published data. Only silent access is supported. This function does not support cross-user notification subscription.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'publishedDataChange' | Yes |
| uris | Array & lt;string & gt; | Yes |
| subscriberId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## publish

```TypeScript
publish(
       data: Array<PublishedItem>,
       bundleName: string,
       version: number,
       callback: AsyncCallback<Array<OperationResult>>
     ): void
```

Publishes data to the database. You should pass in the version of the data to be published. If the passed version is later than the version recorded in the current database, the operation is successful. Only silent access is supported. This API uses an asynchronous callback to return the result.In silent scenarios, the total size of the **data** and **bundleName** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | Yes |
| bundleName | string | Yes |
| version | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700012](../errorcode-datashare.md#15700012-data-area-not-exist) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## publish

```TypeScript
publish(
       data: Array<PublishedItem>,
       bundleName: string,
       callback: AsyncCallback<Array<OperationResult>>
     ): void
```

Publishes data to the database. Only silent access is supported. This API uses an asynchronous callback to return the result.In silent scenarios, the total size of the **data** and **bundleName** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | Yes |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700012](../errorcode-datashare.md#15700012-data-area-not-exist) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## publish

```TypeScript
publish(data: Array<PublishedItem>, bundleName: string, version?: number): Promise<Array<OperationResult>>
```

Publishes data to the database. You should pass in the version of the data to be published. If the passed version is later than the version recorded in the current database, the operation is successful. Only silent access is supported. This API uses a promise to return the result.In silent scenarios, the total size of the **data** and **bundleName** parameters passed in this API cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | Array&lt;[PublishedItem](arkts-arkdata-datashare-publisheditem-i-sys.md)&gt; | Yes |
| bundleName | string | Yes |
| version | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[OperationResult](arkts-arkdata-datashare-operationresult-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700012](../errorcode-datashare.md#15700012-data-area-not-exist) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## query

```TypeScript
query(
       uri: string,
       predicates: dataSharePredicates.DataSharePredicates,
       columns: Array<string>,
       callback: AsyncCallback<DataShareResultSet>
     ): void
```

Queries data in the database. This API uses an asynchronous callback to return the result.In non-silent scenarios, the size of the **predicates** parameter and the total size of the **uri** and **columns** parameters passed in this API cannot exceed 128 MB and 200 KB, respectively. Otherwise, the operation fails or an exception is thrown.In silent scenarios, the total size of the **uri**, **predicates**, and **columns** parameters passed in this API cannot exceed 200 KB. If the size exceeds the limit, the operation fails or an exception is thrown.When this API is used to query database data, if the query content exceeds the resource limit, the operation fails and an error is returned. You can retry the operation based on the scenario. For details about the resource limit, see [Silent Access via DatamgrService](../../../database/share-data-by-silent-access-sys.md#constraints) and [Sharing Data Using DataShareExtensionAbility](../../../database/share-data-by-datashareextensionability-sys.md#constraints).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| columns | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataShareResultSet](arkts-arkdata-data-datashareresultset-datashareresultset-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## query

```TypeScript
query(
       uri: string,
       predicates: dataSharePredicates.DataSharePredicates,
       columns: Array<string>
     ): Promise<DataShareResultSet>
```

Queries data in the database. This API uses a promise to return the result.In non-silent scenarios, the size of the **predicates** parameter and the total size of the **uri** and **columns** parameters passed in this API cannot exceed 128 MB and 200 KB, respectively. Otherwise, the operation fails or an exception is thrown.In silent scenarios, the total size of the **uri**, **predicates**, and **columns** parameters passed in this API cannot exceed 200 KB. If the size exceeds the limit, the operation fails or an exception is thrown.When this API is used to query database data, if the query content exceeds the resource limit, the operation fails and an error is returned. You can retry the operation based on the scenario. For details about the resource limit, see [Silent Access via DatamgrService (ArkTS) (for System Applications Only)](../../../database/share-data-by-silent-access-sys.md#constraints) and [Sharing Data Using DataShareExtensionAbility (ArkTS) (for System Applications Only)](../../../database/share-data-by-datashareextensionability-sys.md#constraints).

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| columns | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DataShareResultSet](arkts-arkdata-data-datashareresultset-datashareresultset-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## update

```TypeScript
update(
       uri: string,
       predicates: dataSharePredicates.DataSharePredicates,
       value: ValuesBucket,
       callback: AsyncCallback<number>
     ): void
```

Updates data in the database. This API uses an asynchronous callback to return the result.In non-silent scenarios, the total size of the **uri**, **predicates**, and **value** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown.In silent scenarios, the total size of the **uri**, **predicates**, and **value** parameters passed when this API is called cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |

## update

```TypeScript
update(uri: string, predicates: dataSharePredicates.DataSharePredicates, value: ValuesBucket): Promise<number>
```

Updates data in the database. This API uses a promise to return the result.In non-silent scenarios, the total size of the **uri**, **predicates**, and **value** parameters passed in this API cannot exceed 900 KB. Otherwise, the operation fails or an exception is thrown.In silent scenarios, the total size of the **uri**, **predicates**, and **value** parameters passed when this API is called cannot exceed 200 KB. Otherwise, the operation fails or an exception is thrown.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| predicates | dataSharePredicates.DataSharePredicates | Yes |
| value | [ValuesBucket](arkts-arkdata-valuesbucket-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15700013](../errorcode-datashare.md#15700013-datasharehelper-instance-closed) |
