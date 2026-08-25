# DeviceKVStore

Provides APIs to query and synchronize data in a device KV store. This class inherits from [KVStore](arkts-arkdata-distributeddata-kvstoretype-e.md). Data is distinguished by device in a device KV store. Each device can only write and modify its own data. Data of other devices is read-only and cannot be modified. For example, a device KV store can be used to implement image sharing between devices. The images of other devices can be viewed, but not be modified or deleted. Before calling any method in **DeviceKVStore**, you must use getKVStore to obtain a **DeviceKVStore** object.

**Inheritance/Implementation:** DeviceKVStore extends [KVStore](arkts-arkdata-distributeddata-kvstore-i.md)

**Since:** 8

**Deprecated since:** 9

**Substitutes:** DeviceKVStore

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

## Modules to Import

```TypeScript
```

## closeResultSet

```TypeScript
closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void
```

Closes the **KvStoreResultSet** object obtained by DeviceKVStore.getResultSet. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** closeResultSet

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [resultSet](arkts-arkdata-relationalstore-result-i.md) | [KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## closeResultSet

```TypeScript
closeResultSet(resultSet: KvStoreResultSet): Promise<void>
```

Closes the **KvStoreResultSet** object obtained by DeviceKVStore.getResultSet. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** closeResultSet

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [resultSet](arkts-arkdata-relationalstore-result-i.md) | [KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## get

```TypeScript
get(deviceId: string, key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void
```

Obtains a string value that matches the specified device ID and key. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** get

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| key | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean \| string \| number \| Uint8Array & gt; | Yes |

## get

```TypeScript
get(deviceId: string, key: string): Promise<boolean | string | number | Uint8Array>
```

Obtains a string value that matches the specified device ID and key. This API uses a promise to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** get

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| key | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean \ | string \| number \| Uint8Array & gt; |

## getEntries

```TypeScript
getEntries(deviceId: string, keyPrefix: string, callback: AsyncCallback<Entry[]>): void
```

Obtains all KV pairs that match the specified device ID and key prefix. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getEntries

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| keyPrefix | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Entry[]&gt; | Yes |

## getEntries

```TypeScript
getEntries(deviceId: string, keyPrefix: string): Promise<Entry[]>
```

Obtains all KV pairs that match the specified device ID and key prefix. This API uses a promise to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getEntries

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| keyPrefix | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Entry[] & gt; |

## getEntries

```TypeScript
getEntries(query: Query, callback: AsyncCallback<Entry[]>): void
```

Obtains the KV pairs that match the specified **Query** object. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getEntries

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Entry[]&gt; | Yes |

## getEntries

```TypeScript
getEntries(query: Query): Promise<Entry[]>
```

Obtains the KV pairs that match the specified **Query** object. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getEntries

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Entry[] & gt; |

## getEntries

```TypeScript
getEntries(deviceId: string, query: Query, callback: AsyncCallback<Entry[]>): void
```

Obtains the KV pairs that match the specified device ID and **Query** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getEntries

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Entry[]&gt; | Yes |

## getEntries

```TypeScript
getEntries(deviceId: string, query: Query): Promise<Entry[]>
```

Obtains the KV pairs that match the specified device ID and **Query** object. This API uses a promise to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getEntries

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Entry[] & gt; |

## getResultSet

```TypeScript
getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void
```

Obtains a **KvStoreResultSet** object that matches the specified device ID and key prefix. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getResultSet

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| keyPrefix | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md)&gt; | Yes |

## getResultSet

```TypeScript
getResultSet(deviceId: string, keyPrefix: string): Promise<KvStoreResultSet>
```

Obtains a **KvStoreResultSet** object that matches the specified device ID and key prefix. This API uses a promise to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getResultSet

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| keyPrefix | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md)&gt; |

## getResultSet

```TypeScript
getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void
```

Obtains a **KvStoreResultSet** object that matches the specified **Query** object. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getResultSet

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md)&gt; | Yes |

## getResultSet

```TypeScript
getResultSet(query: Query): Promise<KvStoreResultSet>
```

Obtains a **KvStoreResultSet** object that matches the specified **Query** object. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getResultSet

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md)&gt; |

## getResultSet

```TypeScript
getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KvStoreResultSet>): void
```

Obtains a **KvStoreResultSet** object that matches the specified device ID and **Query** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getResultSet

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md)&gt; | Yes |

## getResultSet

```TypeScript
getResultSet(deviceId: string, query: Query): Promise<KvStoreResultSet>
```

Obtains a **KvStoreResultSet** object that matches the specified device ID and **Query** object. This API uses a promise to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getResultSet

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[KvStoreResultSet](arkts-arkdata-distributeddata-kvstoreresultset-i.md)&gt; |

## getResultSize

```TypeScript
getResultSize(query: Query, callback: AsyncCallback<number>): void
```

Obtains the number of results that match the specified **Query** object. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getResultSize

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getResultSize

```TypeScript
getResultSize(query: Query): Promise<number>
```

Obtains the number of results that match the specified **Query** object. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getResultSize

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## getResultSize

```TypeScript
getResultSize(deviceId: string, query: Query, callback: AsyncCallback<number>): void
```

Obtains the number of results that match the specified device ID and **Query** object. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getResultSize

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## getResultSize

```TypeScript
getResultSize(deviceId: string, query: Query): Promise<number>
```

Obtains the number of results that match the specified device ID and **Query** object. This API uses a promise to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** getResultSize

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| query | [Query](arkts-arkdata-distributeddata-query-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## off

```TypeScript
off(event: 'dataChange', listener?: Callback<ChangeNotification>): void
```

Unsubscribes from data changes.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** off

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| listener | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeNotification&gt; | No |

## off

```TypeScript
off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void
```

Unsubscribes from sync completion events.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** off

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'syncComplete' | Yes |
| syncCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | No |

## on

```TypeScript
on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void
```

Subscribes to data changes of the specified type.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** on

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| type | [SubscribeType](../../apis-notification-kit/arkts-apis/arkts-notification-notificationextensionsubscription-subscribetype-e.md) | Yes |
| listener | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeNotification&gt; | Yes |

## on

```TypeScript
on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void
```

Subscribes to sync completion events.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** on

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'syncComplete' | Yes |
| syncCallback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[string, number]&gt;&gt; | Yes |

## removeDeviceData

```TypeScript
removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void
```

Deletes data of the specified device from this KV store. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** removeDeviceData

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## removeDeviceData

```TypeScript
removeDeviceData(deviceId: string): Promise<void>
```

Deletes data of the specified device from this KV store. This API uses a promise to return the result.

> **NOTE：**&gt;
> The value of **deviceId** can be obtained by <!--RP1-->
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP1End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.
> For details about how to obtain **deviceId**, see [sync()](arkts-arkdata-distributeddata-singlekvstore-i.md#sync).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** removeDeviceData

**System capability:** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## sync

```TypeScript
sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void
```

Synchronizes the KV store manually.

> **NOTE：**&gt;
> **deviceIds** is **networkId** in <!--RP2-->
> [DeviceInfo](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-deviceinfo-i-sys.md), which can be obtained by
> [deviceManager.getTrustedDeviceListSync](../../apis-distributed-service-kit/arkts-apis/arkts-distributedservice-devicemanager-devicemanager-i-sys.md#gettrusteddevicelistsync).
> <!--RP2End-->The APIs of the **deviceManager** module are system interfaces and available only to system
> applications.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** sync

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.DistributedDataManager.KVStore.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceIds | string[] | Yes |
| mode | [SyncMode](arkts-arkdata-relationalstore-syncmode-e.md) | Yes |
| delayMs | number | No |
