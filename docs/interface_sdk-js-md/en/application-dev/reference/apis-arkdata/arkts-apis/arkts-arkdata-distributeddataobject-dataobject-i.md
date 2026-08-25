# DataObject

Provides APIs for managing a distributed data object. Before using any API of this class, use create() to create a DataObject object.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

## Modules to Import

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## bindAssetStore

```TypeScript
bindAssetStore(assetKey: string, bindInfo: BindInfo, callback: AsyncCallback<void>): void
```

Binds joint assets. Currently, only the binding between an asset in a distributed data object and an asset in an RDB store is supported. This API uses an asynchronous callback to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assetKey | string | Yes |
| bindInfo | [BindInfo](arkts-arkdata-distributeddataobject-bindinfo-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## bindAssetStore

```TypeScript
bindAssetStore(assetKey: string, bindInfo: BindInfo): Promise<void>
```

Binds joint assets. Currently, only the binding between an asset in a distributed data object and an asset in an RDB store is supported. This API uses a promise to return the result.

**Since:** 11

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assetKey | string | Yes |
| bindInfo | [BindInfo](arkts-arkdata-distributeddataobject-bindinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## off('change')

```TypeScript
off(type: 'change', callback?: (sessionId: string, fields: Array<string>) => void ): void
```

Unsubscribes from data changes of this distributed data object.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | (sessionId: string, fields: Array & lt;string & gt;) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off('status')

```TypeScript
off(
      type: 'status',
      callback?: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void
    ): void
```

Unsubscribes from the status change of this distributed data object.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'status' | Yes |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) = & gt; void | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## off('change')

```TypeScript
off(type: 'change', callback?: DataObserver): void
```

Unsubscribes from data changes of this distributed object.

**Since:** 20

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) | No |

## off('status')

```TypeScript
off(type: 'status', callback?: StatusObserver): void
```

Unsubscribes from status changes of this distributed object.

**Since:** 20

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'status' | Yes |
| callback | [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) | No |

## off('progressChanged')

```TypeScript
off(type: 'progressChanged', callback?: ProgressObserver): void
```

Unsubscribes from asset transfer progress changes.

**Since:** 20

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'progressChanged' | Yes |
| callback | [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) | No |

## on('change')

```TypeScript
on(type: 'change', callback: (sessionId: string, fields: Array<string>) => void ): void
```

Subscribes to data changes of this distributed data object.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | (sessionId: string, fields: Array & lt;string & gt;) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('status')

```TypeScript
on(
      type: 'status',
      callback: (sessionId: string, networkId: string, status: 'online' | 'offline' ) => void
    ): void
```

Subscribes to status changes of this distributed data object.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'status' | Yes |
| callback | (sessionId: string, networkId: string, status: 'online' \| 'offline' ) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('change')

```TypeScript
on(type: 'change', callback: DataObserver): void
```

Subscribes to data changes of this distributed data object.

**Since:** 20

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'change' | Yes |
| callback | [DataObserver](arkts-arkdata-distributeddataobject-dataobserver-t.md) | Yes |

## on('status')

```TypeScript
on(type: 'status', callback: StatusObserver): void
```

Subscribes to the status changes of this distributed object.

**Since:** 20

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'status' | Yes |
| callback | [StatusObserver](arkts-arkdata-distributeddataobject-statusobserver-t.md) | Yes |

## on('progressChanged')

```TypeScript
on(type: 'progressChanged', callback: ProgressObserver): void
```

Subscribes to the asset transfer progress changes.

**Since:** 20

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'progressChanged' | Yes |
| callback | [ProgressObserver](arkts-arkdata-distributeddataobject-progressobserver-t.md) | Yes |

## revokeSave

```TypeScript
revokeSave(callback: AsyncCallback<RevokeSaveSuccessResponse>): void
```

Revokes the data of this distributed data object saved. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RevokeSaveSuccessResponse](arkts-arkdata-distributeddataobject-revokesavesuccessresponse-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## revokeSave

```TypeScript
revokeSave(): Promise<RevokeSaveSuccessResponse>
```

Revokes the data of this distributed data object saved. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[RevokeSaveSuccessResponse](arkts-arkdata-distributeddataobject-revokesavesuccessresponse-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## save

```TypeScript
save(deviceId: string, callback: AsyncCallback<SaveSuccessResponse>): void
```

Saves a distributed data object. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[SaveSuccessResponse](arkts-arkdata-distributeddataobject-savesuccessresponse-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## save

```TypeScript
save(deviceId: string): Promise<SaveSuccessResponse>
```

Saves a distributed data object. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[SaveSuccessResponse](arkts-arkdata-distributeddataobject-savesuccessresponse-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## setAsset

```TypeScript
setAsset(assetKey: string, uri: string): Promise<void>
```

Sets the property information about a single asset in a distributed object. This API must be called before the setSessionId API is called. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assetKey | string | Yes |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15400002](../errorcode-distributed-dataObject.md#15400002-incorrect-parameter) |
| [15400003](../errorcode-distributed-dataObject.md#15400003-sessionid-already-set) |

## setAssets

```TypeScript
setAssets(assetsKey: string, uris: Array<string>): Promise<void>
```

Sets the property information about multiple assets in a distributed object. This API must be called before the setSessionId API is called. The number of values contained in the uris array ranges from 1 to 50. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assetsKey | string | Yes |
| uris | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15400002](../errorcode-distributed-dataObject.md#15400002-incorrect-parameter) |
| [15400003](../errorcode-distributed-dataObject.md#15400003-sessionid-already-set) |

## setSessionId

```TypeScript
setSessionId(sessionId: string, callback: AsyncCallback<void>): void
```

Sets a session ID. This API uses an asynchronous callback to return the result. For the devices in the collaboration state in a trusted network, data of the distributed objects with the same session ID can be automatically synced across devices.

**Since:** 9

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15400001](../errorcode-distributed-dataObject.md#15400001-failed-to-create-the-in-memory-database) |

## setSessionId

```TypeScript
setSessionId(callback: AsyncCallback<void>): void
```

Exits all sessions. This API uses an asynchronous callback to return the result.

**Since:** 9

**Required permissions:** 
- API version 9 - 19: ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15400001](../errorcode-distributed-dataObject.md#15400001-failed-to-create-the-in-memory-database) |

## setSessionId

```TypeScript
setSessionId(sessionId?: string): Promise<void>
```

Sets a session ID or exits the distributed network. This API uses a promise to return the result. If this parameter is set to "" or null, or left empty, the distributed data object exits the network. For the devices in the collaboration state in a trusted network, data of the distributed objects with the same session ID can be automatically synced across devices.

**Since:** 9

**Required permissions:** ohos.permission.DISTRIBUTED_DATASYNC

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [15400001](../errorcode-distributed-dataObject.md#15400001-failed-to-create-the-in-memory-database) |
