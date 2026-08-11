# Config (System API)

Provides APIs for setting device-cloud synergy, including enabling and disabling device-cloud synergy, clearing data, and notifying data changes.

**Since:** 10

<!--Device-cloudData-class Config--><!--Device-cloudData-class Config-End-->

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

<!--Device-Config-static batchQueryLastSyncInfo(        accountId: string,        bundleInfos: Array<BundleInfo>    ): Promise<Record<string, Record<string, SyncInfo>>>--><!--Device-Config-static batchQueryLastSyncInfo(        accountId: string,        bundleInfos: Array<BundleInfo>    ): Promise<Record<string, Record<string, SyncInfo>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleInfos | Array&lt;BundleInfo&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Record&lt;string, Record&lt;string, SyncInfo&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const accountId: string = "accountId";
const bundleInfos: Array<cloudData.BundleInfo> = [
  { bundleName: "bundleName1", storeId: "storeId1" },
  { bundleName: "bundleName2" }
];

try {
  cloudData.Config.batchQueryLastSyncInfo(accountId, bundleInfos).then((result) => {
    console.info(`Succeeded in querying last sync info. Result is ${JSON.stringify(result)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to query last sync info. Error code is ${err.code}, message is ${err.message}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

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

<!--Device-Config-static changeAppCloudSwitch(      accountId: string,      bundleName: string,      status: boolean,      callback: AsyncCallback<void>    ): void--><!--Device-Config-static changeAppCloudSwitch(      accountId: string,      bundleName: string,      status: boolean,      callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleName | string | Yes |
| status | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
let bundleName: string = "test_bundleName";
try {
  cloudData.Config.changeAppCloudSwitch(account, bundleName, true, (err: BusinessError) => {
    if (err === undefined) {
      console.info('Succeeded in changing App cloud switch');
    } else {
      console.error(`Failed to change App cloud switch. Code: ${err.code}, message: ${err.message}`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## changeAppCloudSwitch

```TypeScript
static changeAppCloudSwitch(accountId: string, bundleName: string, status: boolean): Promise<void>
```

Changes the device-cloud synergy setting for an application. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static changeAppCloudSwitch(accountId: string, bundleName: string, status: boolean): Promise<void>--><!--Device-Config-static changeAppCloudSwitch(accountId: string, bundleName: string, status: boolean): Promise<void>-End-->

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
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
let bundleName: string = "test_bundleName";
try {
  cloudData.Config.changeAppCloudSwitch(account, bundleName, true).then(() => {
    console.info('Succeeded in changing App cloud switch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to change App cloud switch. Code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

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

<!--Device-Config-static changeAppCloudSwitch(      accountId: string,      bundleName: string,      status: boolean,      config?: SwitchConfig    ): Promise<void>--><!--Device-Config-static changeAppCloudSwitch(      accountId: string,      bundleName: string,      status: boolean,      config?: SwitchConfig    ): Promise<void>-End-->

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
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
let bundleName: string = "test_bundleName";
let config: cloudData.SwitchConfig = {
  dbInfo: {
    'test_storeName1': {
      enable: true,
      tableInfo: {
        'test_tableName1': true,
        'test_tableName2': false
      }
    }
  }
}
try {
  cloudData.Config.changeAppCloudSwitch(account, bundleName, true, config).then(() => {
    console.info('Succeeded in changing App cloud switch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to change App cloud switch. Code is ${err.code}, message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

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

<!--Device-Config-static clear(      accountId: string,      appActions: Record<string, ClearAction>,      callback: AsyncCallback<void>    ): void--><!--Device-Config-static clear(      accountId: string,      appActions: Record<string, ClearAction>,      callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| appActions | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, ClearAction&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
type dataType = Record<string, cloudData.ClearAction>
let appActions: dataType = {
  'test_bundleName1': cloudData.ClearAction.CLEAR_CLOUD_INFO,
  'test_bundleName2': cloudData.ClearAction.CLEAR_CLOUD_DATA_AND_INFO
};
try {
  cloudData.Config.clear(account, appActions, (err: BusinessError) => {
    if (err === undefined) {
      console.info('Succeeded in clearing cloud data');
    } else {
      console.error(`Failed to clear cloud data. Code: ${err.code}, message: ${err.message}`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## clear

```TypeScript
static clear(accountId: string, appActions: Record<string, ClearAction>): Promise<void>
```

Clears the cloud data locally. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static clear(accountId: string, appActions: Record<string, ClearAction>): Promise<void>--><!--Device-Config-static clear(accountId: string, appActions: Record<string, ClearAction>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| appActions | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, ClearAction&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
type dataType = Record<string, cloudData.ClearAction>;
let appActions: dataType = {
  'test_bundleName1': cloudData.ClearAction.CLEAR_CLOUD_INFO,
  'test_bundleName2': cloudData.ClearAction.CLEAR_CLOUD_DATA_AND_INFO
};
try {
  cloudData.Config.clear(account, appActions).then(() => {
    console.info('Succeeded in clearing cloud data');
  }).catch((err: BusinessError) => {
    console.error(`Failed to clear cloud data. Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

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

<!--Device-Config-static clear(      accountId: string,      appActions: Record<string, ClearAction>,      config?: Record<string, ClearConfig>    ): Promise<void>--><!--Device-Config-static clear(      accountId: string,      appActions: Record<string, ClearAction>,      config?: Record<string, ClearConfig>    ): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| appActions | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, ClearAction&gt; | Yes |
| config | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, ClearConfig&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
let appActions: Record<string, cloudData.ClearAction> = {
  'test_bundleName1': cloudData.ClearAction.CLEAR_CLOUD_INFO,
  'test_bundleName2': cloudData.ClearAction.CLEAR_CLOUD_DATA_AND_INFO,
  'test_bundleName3': cloudData.ClearAction.CLEAR_CLOUD_NONE,
};
let config: Record<string, cloudData.ClearConfig> = {
  'test_bundleName': {
    dbInfo: {
      'test_storeName': {
        action: cloudData.ClearAction.CLEAR_CLOUD_INFO,
        tableInfo: {
          'test_tableName1': cloudData.ClearAction.CLEAR_CLOUD_INFO,
          'test_tableName2': cloudData.ClearAction.CLEAR_CLOUD_DATA_AND_INFO,
        }
      }
    }
  }
}
try {
  cloudData.Config.clear(account, appActions, config).then(() => {
    console.info('Succeeded in clearing cloud data');
  }).catch((err: BusinessError) => {
    console.error(`Failed to clear cloud data. Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

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

<!--Device-Config-static cloudSync(      bundleName: string,      storeId: string,      mode: relationalStore.SyncMode,      progress: Callback<relationalStore.ProgressDetails>    ): Promise<void>--><!--Device-Config-static cloudSync(      bundleName: string,      storeId: string,      mode: relationalStore.SyncMode,      progress: Callback<relationalStore.ProgressDetails>    ): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| storeId | string | Yes |
| mode | relationalStore.SyncMode | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;relationalStore.ProgressDetails&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { relationalStore } from '@kit.ArkData';

try {
  cloudData.Config.cloudSync("bundleName", "storeId", relationalStore.SyncMode.SYNC_MODE_TIME_FIRST, (progress)=>{
    console.info('Succeeded in getting progress details.');
  }).then(() => {
    console.info('Succeeded in syncing cloud data.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to sync cloud data. Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to sync cloud data. Code: ${error.code}, message: ${error.message}`);
}
```

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

<!--Device-Config-static cloudSyncEx(        bundleInfo: BundleInfo,        config: relationalStore.CloudSyncConfig,        progress: Callback<relationalStore.ProgressDetails>    ): Promise<void>--><!--Device-Config-static cloudSyncEx(        bundleInfo: BundleInfo,        config: relationalStore.CloudSyncConfig,        progress: Callback<relationalStore.ProgressDetails>    ): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleInfo | [BundleInfo](../../apis-ability-kit/arkts-apis/arkts-ability-bundleinfo-i-sys.md) | Yes |
| config | relationalStore.CloudSyncConfig | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;relationalStore.ProgressDetails&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleInfo: cloudData.BundleInfo = {
  bundleName: 'com.example.myapplication',
  // Other BundleInfo fields
};

let config: relationalStore.CloudSyncConfig = {
  mode: relationalStore.SyncMode.SYNC_MODE_TIME_FIRST,
  enablePredicate: true
};

try {
  cloudData.Config.cloudSyncEx(bundleInfo, config, (progressDetails: relationalStore.ProgressDetails) => {
    console.info(`Cloud sync progress: ${progressDetails.schedule}, code: ${progressDetails.code}`);
  }).then(() => {
    console.info('Succeeded in cloud sync');
  }).catch((err: BusinessError) => {
    console.error(`Failed to cloud sync. Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## disableCloud

```TypeScript
static disableCloud(accountId: string, callback: AsyncCallback<void>): void
```

Disables device-cloud synergy. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static disableCloud(accountId: string, callback: AsyncCallback<void>): void--><!--Device-Config-static disableCloud(accountId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
try {
  cloudData.Config.disableCloud(account, (err: BusinessError) => {
    if (err === undefined) {
      console.info('Succeeded in disabling cloud');
    } else {
      console.error(`Failed to disableCloud. Code: ${err.code}, message: ${err.message}`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## disableCloud

```TypeScript
static disableCloud(accountId: string): Promise<void>
```

Disables device-cloud synergy. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static disableCloud(accountId: string): Promise<void>--><!--Device-Config-static disableCloud(accountId: string): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
try {
  cloudData.Config.disableCloud(account).then(() => {
    console.info('Succeeded in disabling cloud');
  }).catch((err: BusinessError) => {
    console.error(`Failed to disableCloud. Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

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

<!--Device-Config-static enableCloud(      accountId: string,      switches: Record<string, boolean>,      callback: AsyncCallback<void>    ): void--><!--Device-Config-static enableCloud(      accountId: string,      switches: Record<string, boolean>,      callback: AsyncCallback<void>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| switches | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, boolean&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
let switches: Record<string, boolean> = { 'test_bundleName1': true, 'test_bundleName2': false };
try {
  cloudData.Config.enableCloud(account, switches, (err: BusinessError) => {
    if (err === undefined) {
      console.info('Succeeded in enabling cloud');
    } else {
      console.error(`Failed to enable.Code: ${err.code}, message: ${err.message}`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## enableCloud

```TypeScript
static enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>
```

Enables device-cloud synergy. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>--><!--Device-Config-static enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| switches | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, boolean&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
let switches: Record<string, boolean> = { 'test_bundleName1': true, 'test_bundleName2': false };
try {
  cloudData.Config.enableCloud(account, switches).then(() => {
    console.info('Succeeded in enabling cloud');
  }).catch((err: BusinessError) => {
    console.error(`Failed to enable.Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## notifyDataChange

```TypeScript
static notifyDataChange(extInfo: ExtraData, userId?: number): Promise<void>
```

Notifies the data changes in the cloud. This API uses a promise to return the result. You can specify the database and tables with data changes in the **extraData** field in **extInfo**, and specify the user ID.

**Since:** 11

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static notifyDataChange(extInfo: ExtraData, userId?: int): Promise<void>--><!--Device-Config-static notifyDataChange(extInfo: ExtraData, userId?: int): Promise<void>-End-->

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
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let eventId: string = "cloud_data_change";
let extraData: string = '{"data":"{"accountId":"aaa","bundleName":"com.bbb.xxx","containerName":"alias", "databaseScopes": ["private", "shared"],"recordTypes":"["xxx","yyy","zzz"]"}"}';
let userId: number = 100;
try {
  cloudData.Config.notifyDataChange({
    eventId: eventId, extraData: extraData
  }, userId).then(() => {
    console.info('Succeeded in notifying the change of data');
  }).catch((err: BusinessError) => {
    console.error(`Failed to notify the change of data. Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## notifyDataChange

```TypeScript
static notifyDataChange(extInfo: ExtraData, callback: AsyncCallback<void>): void
```

Notifies the data changes in the cloud with the specified information, such as the database and table names (specified by the **extraData** field in **extInfo**). This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static notifyDataChange(extInfo: ExtraData, callback: AsyncCallback<void>): void--><!--Device-Config-static notifyDataChange(extInfo: ExtraData, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| extInfo | [ExtraData](../../apis-core-file-kit/arkts-apis/arkts-corefile-cloudsyncmanager-extradata-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let eventId: string = "cloud_data_change";
let extraData: string = '{"data":"{"accountId":"aaa","bundleName":"com.bbb.xxx","containerName":"alias", "databaseScopes": ["private", "shared"],"recordTypes":"["xxx","yyy","zzz"]"}"}';
try {
  cloudData.Config.notifyDataChange({
    eventId: eventId, extraData: extraData
  }, (err: BusinessError) => {
    if (err === undefined) {
      console.info('Succeeded in notifying the change of data');
    } else {
      console.error(`Failed to notify the change of data. Code: ${err.code}, message: ${err.message}`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## notifyDataChange

```TypeScript
static notifyDataChange(extInfo: ExtraData, userId: number, callback: AsyncCallback<void>): void
```

Notifies the data changes of a user in the cloud. This API uses an asynchronous callback to return the result. You can also specify the database and tables with data changes in the **extraData** field in **extInfo**, and specify the user ID.

**Since:** 11

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static notifyDataChange(extInfo: ExtraData, userId: int, callback: AsyncCallback<void>): void--><!--Device-Config-static notifyDataChange(extInfo: ExtraData, userId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| extInfo | [ExtraData](../../apis-core-file-kit/arkts-apis/arkts-corefile-cloudsyncmanager-extradata-i-sys.md) | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let eventId: string = "cloud_data_change";
let extraData: string = '{"data":"{"accountId":"aaa","bundleName":"com.bbb.xxx","containerName":"alias", "databaseScopes": ["private", "shared"],"recordTypes":"["xxx","yyy","zzz"]"}"}';
let userId: number = 100;
try {
  cloudData.Config.notifyDataChange({
    eventId: eventId, extraData: extraData
  }, userId, (err: BusinessError) => {
    if (err === undefined) {
      console.info('Succeeded in notifying the change of data');
    } else {
      console.error(`Failed to notify the change of data. Code: ${err.code}, message: ${err.message}`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## notifyDataChange

```TypeScript
static notifyDataChange(accountId: string, bundleName: string): Promise<void>
```

Notifies the data changes in the cloud. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static notifyDataChange(accountId: string, bundleName: string): Promise<void>--><!--Device-Config-static notifyDataChange(accountId: string, bundleName: string): Promise<void>-End-->

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
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
let bundleName: string = "test_bundleName";
try {
  cloudData.Config.notifyDataChange(account, bundleName).then(() => {
    console.info('Succeeded in notifying the change of data');
  }).catch((err: BusinessError) => {
    console.error(`Failed to notify the change of data. Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## notifyDataChange

```TypeScript
static notifyDataChange(accountId: string, bundleName: string, callback: AsyncCallback<void>): void
```

Notifies the data changes in the cloud. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static notifyDataChange(accountId: string, bundleName: string, callback: AsyncCallback<void>): void--><!--Device-Config-static notifyDataChange(accountId: string, bundleName: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
let bundleName: string = "test_bundleName";
try {
  cloudData.Config.notifyDataChange(account, bundleName, (err: BusinessError) => {
    if (err === undefined) {
      console.info('Succeeded in notifying the change of data');
    } else {
      console.error(`Failed to notify the change of data. Code: ${err.code}, message: ${err.message}`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

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

<!--Device-Config-static offSyncInfoChanged(        bundleInfos: Array<BundleInfo>,        progress?: Callback<Record<string, Record<string, SyncInfo>>>    ): void--><!--Device-Config-static offSyncInfoChanged(        bundleInfos: Array<BundleInfo>,        progress?: Callback<Record<string, Record<string, SyncInfo>>>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleInfos | Array&lt;BundleInfo&gt; | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Record&lt;string, SyncInfo&gt;&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const bundleInfos: Array<cloudData.BundleInfo> = [
  { bundleName: "bundleName1", storeId: "storeId1" },
  { bundleName: "bundleName2" }
];

const progressCallback = (result: Record<string, Record<string, cloudData.SyncInfo>>) => {
  console.info(`Sync info changed. Result is ${JSON.stringify(result)}`);
};

// Subscribe to sync information changes.
try {
  cloudData.Config.onSyncInfoChanged(bundleInfos, progressCallback);
} catch(e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}

// Unsubscribe from a specified callback.
try {
  cloudData.Config.offSyncInfoChanged(bundleInfos, progressCallback);
} catch(e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}

// Unsubscribe from all callbacks.
try {
  cloudData.Config.offSyncInfoChanged(bundleInfos);
} catch(e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

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

<!--Device-Config-static onSyncInfoChanged(        bundleInfos: Array<BundleInfo>,        progress: Callback<Record<string, Record<string, SyncInfo>>>    ): void--><!--Device-Config-static onSyncInfoChanged(        bundleInfos: Array<BundleInfo>,        progress: Callback<Record<string, Record<string, SyncInfo>>>    ): void-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleInfos | Array&lt;BundleInfo&gt; | Yes |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Record&lt;string, SyncInfo&gt;&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const bundleInfos: Array<cloudData.BundleInfo> = [
  { bundleName: "bundleName1", storeId: "storeId1" },
  { bundleName: "bundleName2" }
];

try {
  cloudData.Config.onSyncInfoChanged(bundleInfos, (result) => {
    console.info(`Sync info changed. Result is ${JSON.stringify(result)}`);
  });
} catch(e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

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

<!--Device-Config-static queryLastSyncInfo(        accountId: string,        bundleName: string,        storeId?: string    ): Promise<Record<string, SyncInfo>>--><!--Device-Config-static queryLastSyncInfo(        accountId: string,        bundleName: string,        storeId?: string    ): Promise<Record<string, SyncInfo>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleName | string | Yes |
| storeId | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Record&lt;string, SyncInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const accountId: string = "accountId";
const bundleName: string = "bundleName";
const storeId: string = "storeId";
try {
  cloudData.Config.queryLastSyncInfo(accountId, bundleName, storeId).then((result) => {
    console.info(`Succeeded in querying last syncinfo. Info is ${JSON.stringify(result)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to query last syncinfo. Error code is ${err.code}, message is ${err.message}`);
	});
} catch(e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

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

<!--Device-Config-static queryStatistics(        accountId: string,        bundleName: string,        storeId?: string    ): Promise<Record<string, Array<StatisticInfo>>>--><!--Device-Config-static queryStatistics(        accountId: string,        bundleName: string,        storeId?: string    ): Promise<Record<string, Array<StatisticInfo>>>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| accountId | string | Yes |
| bundleName | string | Yes |
| storeId | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Record&lt;string, Array&lt;StatisticInfo&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const accountId: string = "accountId";
const bundleName: string = "bundleName";
const storeId: string = "storeId";

cloudData.Config.queryStatistics(accountId, bundleName, storeId).then((result) => {
  console.info(`Succeeded in querying statistics. Info is ${JSON.stringify(result)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query statistics. Error code is ${err.code}, message is ${err.message}`);
});
```

## setGlobalCloudStrategy

```TypeScript
static setGlobalCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>
```

Sets a global device-cloud sync strategy. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static setGlobalCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>--><!--Device-Config-static setGlobalCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | [StrategyType](arkts-arkdata-clouddata-strategytype-e.md) | Yes |
| param | Array&lt;commonType.ValueType&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

cloudData.Config.setGlobalCloudStrategy(cloudData.StrategyType.NETWORK, [cloudData.NetWorkStrategy.WIFI]).then(() => {
  console.info('Succeeded in setting the global cloud strategy');
}).catch((err: BusinessError) => {
  console.error(`Failed to set global cloud strategy. Code: ${err.code}, message: ${err.message}`);
});
```

## stopCloudSync

```TypeScript
static stopCloudSync(bundleInfos: Array<BundleInfo>): Promise<void>
```

Stops syncing data to the cloud.

**Since:** 26.0.0

**Required permissions:** ohos.permission.CLOUDDATA_CONFIG

**Model restriction:** This API can be used only in the stage model.

<!--Device-Config-static stopCloudSync(bundleInfos: Array<BundleInfo>): Promise<void>--><!--Device-Config-static stopCloudSync(bundleInfos: Array<BundleInfo>): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Config

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleInfos | Array&lt;BundleInfo&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-invalid-arguments) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let bundleInfos: Array<cloudData.BundleInfo> = [
  { bundleName: 'com.example.myapplication1' },
  { bundleName: 'com.example.myapplication2' }
];

try {
  cloudData.Config.stopCloudSync(bundleInfos).then(() => {
    console.info('Succeeded in stopping cloud sync');
  }).catch((err: BusinessError) => {
    console.error(`Failed to stop cloud sync. Code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```
