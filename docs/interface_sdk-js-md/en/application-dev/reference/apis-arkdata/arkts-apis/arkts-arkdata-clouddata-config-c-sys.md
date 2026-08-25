# Config (System API)

Provides APIs for setting device-cloud synergy, including enabling and disabling device-cloud synergy, clearing data, and notifying data changes.

**Since:** 10

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudData } from 'kits/@kit.ArkData';
```

## batchQueryLastSyncInfo

```TypeScript
static batchQueryLastSyncInfo(
        accountId: string,
        bundleInfos: Array<BundleInfo>
    ): Promise<Record<string, Record<string, SyncInfo>>>
```

Queries the last synchronization information in batch

**Since:** 26.0.0

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleInfos | Array & lt;BundleInfo & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Record&lt;string, Record&lt;string, [SyncInfo](arkts-arkdata-clouddata-syncinfo-i-sys.md)&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |

## changeAppCloudSwitch

```TypeScript
static changeAppCloudSwitch(
      accountId: string,
      bundleName: string,
      status: boolean,
      callback: AsyncCallback<void>
    ): void
```

Changes the device-cloud synergy setting for an application. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleName | string | Yes |
| status | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## changeAppCloudSwitch

```TypeScript
static changeAppCloudSwitch(accountId: string, bundleName: string, status: boolean): Promise<void>
```

Changes the device-cloud synergy setting for an application. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleName | string | Yes |
| status | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## changeAppCloudSwitch

```TypeScript
static changeAppCloudSwitch(
      accountId: string,
      bundleName: string,
      status: boolean,
      config?: SwitchConfig
    ): Promise<void>
```

Changes the device-cloud synergy setting for an application. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleName | string | Yes |
| status | boolean | Yes |
| config | [SwitchConfig](arkts-arkdata-clouddata-switchconfig-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## clear

```TypeScript
static clear(
      accountId: string,
      appActions: Record<string, ClearAction>,
      callback: AsyncCallback<void>
    ): void
```

Clears the cloud data locally. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| appActions | Record&lt;string, [ClearAction](arkts-arkdata-clouddata-clearaction-e-sys.md)&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## clear

```TypeScript
static clear(accountId: string, appActions: Record<string, ClearAction>): Promise<void>
```

Clears the cloud data locally. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| appActions | Record&lt;string, [ClearAction](arkts-arkdata-clouddata-clearaction-e-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## clear

```TypeScript
static clear(
      accountId: string,
      appActions: Record<string, ClearAction>,
      config?: Record<string, ClearConfig>
    ): Promise<void>
```

Clears the cloud data locally. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| appActions | Record&lt;string, [ClearAction](arkts-arkdata-clouddata-clearaction-e-sys.md)&gt; | Yes |
| config | Record&lt;string, [ClearConfig](arkts-arkdata-clouddata-clearconfig-i-sys.md)&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## cloudSync

```TypeScript
static cloudSync(
      bundleName: string,
      storeId: string,
      mode: relationalStore.SyncMode,
      progress: Callback<relationalStore.ProgressDetails>
    ): Promise<void>
```

Synchronizes data of a specified application on the device to the cloud. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| [storeId](arkts-arkdata-clouddata-bundleinfo-i-sys.md) | string | Yes |
| mode | relationalStore.SyncMode | Yes |
| progress | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;relationalStore.ProgressDetails&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |

## cloudSyncEx

```TypeScript
static cloudSyncEx(
        bundleInfo: BundleInfo,
        config: relationalStore.CloudSyncConfig,
        progress: Callback<relationalStore.ProgressDetails>
    ): Promise<void>
```

Sync data to cloud. This API uses a promise to return the result.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleInfo | [BundleInfo](../../apis-ability-kit/arkts-apis/arkts-ability-bundleinfo-i.md) | Yes |
| config | relationalStore.CloudSyncConfig | Yes |
| progress | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;relationalStore.ProgressDetails&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |

## disableCloud

```TypeScript
static disableCloud(accountId: string, callback: AsyncCallback<void>): void
```

Disables device-cloud synergy. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## disableCloud

```TypeScript
static disableCloud(accountId: string): Promise<void>
```

Disables device-cloud synergy. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## enableCloud

```TypeScript
static enableCloud(
      accountId: string,
      switches: Record<string, boolean>,
      callback: AsyncCallback<void>
    ): void
```

Enables device-cloud synergy. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| switches | Record & lt;string, boolean & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## enableCloud

```TypeScript
static enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>
```

Enables device-cloud synergy. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| switches | Record & lt;string, boolean & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## notifyDataChange

```TypeScript
static notifyDataChange(extInfo: ExtraData, userId?: number): Promise<void>
```

Notifies the data changes in the cloud. This API uses a promise to return the result. You can specify the database and tables with data changes in the **extraData** field in **extInfo**, and specify the user ID.

**Since:** 11

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| extInfo | [ExtraData](../../apis-core-file-kit/arkts-apis/arkts-corefile-cloudsyncmanager-extradata-i-sys.md) | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## notifyDataChange

```TypeScript
static notifyDataChange(extInfo: ExtraData, callback: AsyncCallback<void>): void
```

Notifies the data changes in the cloud with the specified information, such as the database and table names (specified by the **extraData** field in **extInfo**). This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| extInfo | [ExtraData](../../apis-core-file-kit/arkts-apis/arkts-corefile-cloudsyncmanager-extradata-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## notifyDataChange

```TypeScript
static notifyDataChange(extInfo: ExtraData, userId: number, callback: AsyncCallback<void>): void
```

Notifies the data changes of a user in the cloud. This API uses an asynchronous callback to return the result. You can also specify the database and tables with data changes in the **extraData** field in **extInfo**, and specify the user ID.

**Since:** 11

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| extInfo | [ExtraData](../../apis-core-file-kit/arkts-apis/arkts-corefile-cloudsyncmanager-extradata-i-sys.md) | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## notifyDataChange

```TypeScript
static notifyDataChange(accountId: string, bundleName: string): Promise<void>
```

Notifies the data changes in the cloud. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## notifyDataChange

```TypeScript
static notifyDataChange(accountId: string, bundleName: string, callback: AsyncCallback<void>): void
```

Notifies the data changes in the cloud. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## offSyncInfoChanged

```TypeScript
static offSyncInfoChanged(
        bundleInfos: Array<BundleInfo>,
        progress?: Callback<Record<string, Record<string, SyncInfo>>>
    ): void
```

Remove specified observer of specified type from the database.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleInfos | Array & lt;BundleInfo & gt; | Yes |
| progress | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Record&lt;string, [SyncInfo](arkts-arkdata-clouddata-syncinfo-i-sys.md)&gt;&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |

## onSyncInfoChanged

```TypeScript
static onSyncInfoChanged(
        bundleInfos: Array<BundleInfo>,
        progress: Callback<Record<string, Record<string, SyncInfo>>>
    ): void
```

Subscribes to changes in the sync information of a specified application.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleInfos | Array & lt;BundleInfo & gt; | Yes |
| progress | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Record&lt;string, [SyncInfo](arkts-arkdata-clouddata-syncinfo-i-sys.md)&gt;&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |

## queryLastSyncInfo

```TypeScript
static queryLastSyncInfo(
        accountId: string,
        bundleName: string,
        storeId?: string
    ): Promise<Record<string, SyncInfo>>
```

Queries information about the last device-cloud sync. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleName | string | Yes |
| [storeId](arkts-arkdata-clouddata-bundleinfo-i-sys.md) | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Record&lt;string, [SyncInfo](arkts-arkdata-clouddata-syncinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## queryStatistics

```TypeScript
static queryStatistics(
        accountId: string,
        bundleName: string,
        storeId?: string
    ): Promise<Record<string, Array<StatisticInfo>>>
```

Queries device-cloud data statistics, which include the data not synced, data synced and consistent, and data synced but inconsistent between the device and the cloud. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleName | string | Yes |
| [storeId](arkts-arkdata-clouddata-bundleinfo-i-sys.md) | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Record&lt;string, Array&lt;[StatisticInfo](arkts-arkdata-clouddata-statisticinfo-i-sys.md)&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## setGlobalCloudStrategy

```TypeScript
static setGlobalCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>
```

Sets a global device-cloud sync strategy. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | [StrategyType](arkts-arkdata-clouddata-strategytype-e.md) | Yes |
| param | Array & lt;commonType.ValueType & gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## stopCloudSync

```TypeScript
static stopCloudSync(bundleInfos: Array<BundleInfo>): Promise<void>
```

Stops syncing data to the cloud.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleInfos | Array & lt;BundleInfo & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
