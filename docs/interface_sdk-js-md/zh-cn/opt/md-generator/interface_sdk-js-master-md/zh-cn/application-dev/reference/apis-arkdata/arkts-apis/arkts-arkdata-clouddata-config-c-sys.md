# Config（系统接口）

提供配置端云协同的方法，包括云同步打开、关闭、清除数据、数据变化通知。

**起始版本：** 10

<!--Device-cloudData-class Config--><!--Device-cloudData-class Config-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

## batchQueryLastSyncInfo

```TypeScript
static batchQueryLastSyncInfo(
        accountId: string,
        bundleInfos: Array<BundleInfo>
    ): Promise<Record<string, Record<string, SyncInfo>>>
```

批量查询上一次端云同步的信息，使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Config-static batchQueryLastSyncInfo(        accountId: string,        bundleInfos: Array<BundleInfo>    ): Promise<Record<string, Record<string, SyncInfo>>>--><!--Device-Config-static batchQueryLastSyncInfo(        accountId: string,        bundleInfos: Array<BundleInfo>    ): Promise<Record<string, Record<string, SyncInfo>>>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| bundleInfos | Array&lt;BundleInfo&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Record&lt;string, Record&lt;string, SyncInfo&gt;&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch(err) {
  let error = err as BusinessError;
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

修改单个应用端云协同开关，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static changeAppCloudSwitch(      accountId: string,      bundleName: string,      status: boolean,      callback: AsyncCallback<void>    ): void--><!--Device-Config-static changeAppCloudSwitch(      accountId: string,      bundleName: string,      status: boolean,      callback: AsyncCallback<void>    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| bundleName | string | 是 |
| status | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## changeAppCloudSwitch

```TypeScript
static changeAppCloudSwitch(accountId: string, bundleName: string, status: boolean): Promise<void>
```

修改单个应用端云协同开关，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static changeAppCloudSwitch(accountId: string, bundleName: string, status: boolean): Promise<void>--><!--Device-Config-static changeAppCloudSwitch(accountId: string, bundleName: string, status: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| bundleName | string | 是 |
| status | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
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

修改单个应用端云协同开关，使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Config-static changeAppCloudSwitch(      accountId: string,      bundleName: string,      status: boolean,      config?: SwitchConfig    ): Promise<void>--><!--Device-Config-static changeAppCloudSwitch(      accountId: string,      bundleName: string,      status: boolean,      config?: SwitchConfig    ): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| bundleName | string | 是 |
| status | boolean | 是 |
| config | [SwitchConfig](arkts-arkdata-clouddata-switchconfig-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
};
try {
  cloudData.Config.changeAppCloudSwitch(account, bundleName, true, config).then(() => {
    console.info('Succeeded in changing App cloud switch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to change App cloud switch. Code is ${err.code}, message is ${err.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
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

清除本地下载的云端数据，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static clear(      accountId: string,      appActions: Record<string, ClearAction>,      callback: AsyncCallback<void>    ): void--><!--Device-Config-static clear(      accountId: string,      appActions: Record<string, ClearAction>,      callback: AsyncCallback<void>    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| appActions | Record&lt;string, ClearAction&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
type dataType = Record<string, cloudData.ClearAction>;
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
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## clear

```TypeScript
static clear(accountId: string, appActions: Record<string, ClearAction>): Promise<void>
```

清除本地下载的云端数据，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static clear(accountId: string, appActions: Record<string, ClearAction>): Promise<void>--><!--Device-Config-static clear(accountId: string, appActions: Record<string, ClearAction>): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| appActions | Record&lt;string, ClearAction&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
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

清除本地下载的云端数据，使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Config-static clear(      accountId: string,      appActions: Record<string, ClearAction>,      config?: Record<string, ClearConfig>    ): Promise<void>--><!--Device-Config-static clear(      accountId: string,      appActions: Record<string, ClearAction>,      config?: Record<string, ClearConfig>    ): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| appActions | Record&lt;string, ClearAction&gt; | 是 |
| config | Record&lt;string, ClearConfig&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
};
try {
  cloudData.Config.clear(account, appActions, config).then(() => {
    console.info('Succeeded in clearing cloud data');
  }).catch((err: BusinessError) => {
    console.error(`Failed to clear cloud data. Code: ${err.code}, message: ${err.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
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

对指定应用的数据进行端云同步，使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static cloudSync(      bundleName: string,      storeId: string,      mode: relationalStore.SyncMode,      progress: Callback<relationalStore.ProgressDetails>    ): Promise<void>--><!--Device-Config-static cloudSync(      bundleName: string,      storeId: string,      mode: relationalStore.SyncMode,      progress: Callback<relationalStore.ProgressDetails>    ): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| storeId | string | 是 |
| mode | relationalStore.SyncMode | 是 |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;relationalStore.ProgressDetails&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
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

对指定应用的数据按照云同步配置信息进行端云同步，当  
[CloudSyncConfig](../../../reference/apis-arkdata/js-apis-data-relationalStore-sys.md#cloudsyncconfig)中的downloadOnly为true时，端云同步仅把云侧数据同步到本地，使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Config-static cloudSyncEx(        bundleInfo: BundleInfo,        config: relationalStore.CloudSyncConfig,        progress: Callback<relationalStore.ProgressDetails>    ): Promise<void>--><!--Device-Config-static cloudSyncEx(        bundleInfo: BundleInfo,        config: relationalStore.CloudSyncConfig,        progress: Callback<relationalStore.ProgressDetails>    ): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleInfo | [BundleInfo](../../apis-ability-kit/arkts-apis/arkts-ability-bundleinfo-i.md) | 是 |
| config | relationalStore.CloudSyncConfig | 是 |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;relationalStore.ProgressDetails&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

let bundleInfo: cloudData.BundleInfo = {
  bundleName: 'com.example.myapplication',
  // 其他BundleInfo字段...
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
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## disableCloud

```TypeScript
static disableCloud(accountId: string, callback: AsyncCallback<void>): void
```

关闭端云协同，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static disableCloud(accountId: string, callback: AsyncCallback<void>): void--><!--Device-Config-static disableCloud(accountId: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## disableCloud

```TypeScript
static disableCloud(accountId: string): Promise<void>
```

关闭端云协同，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static disableCloud(accountId: string): Promise<void>--><!--Device-Config-static disableCloud(accountId: string): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let account: string = "test_id";
try {
  cloudData.Config.disableCloud(account).then(() => {
    console.info('Succeeded in disabling cloud');
  }).catch((err: BusinessError) => {
    console.error(`Failed to disableCloud. Code: ${err.code}, message: ${err.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
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

打开端云协同开关，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static enableCloud(      accountId: string,      switches: Record<string, boolean>,      callback: AsyncCallback<void>    ): void--><!--Device-Config-static enableCloud(      accountId: string,      switches: Record<string, boolean>,      callback: AsyncCallback<void>    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| switches | Record&lt;string, boolean&gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## enableCloud

```TypeScript
static enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>
```

打开端云协同开关，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>--><!--Device-Config-static enableCloud(accountId: string, switches: Record<string, boolean>): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| switches | Record&lt;string, boolean&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## notifyDataChange

```TypeScript
static notifyDataChange(extInfo: ExtraData, userId?: number): Promise<void>
```

通知云端的数据变更，可以通过extInfo中的extraData字段指定变更的数据库名和表名，可通过userId指定用户ID，使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static notifyDataChange(extInfo: ExtraData, userId?: int): Promise<void>--><!--Device-Config-static notifyDataChange(extInfo: ExtraData, userId?: int): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| extInfo | [ExtraData](../../apis-core-file-kit/arkts-apis/arkts-corefile-cloudsyncmanager-extradata-i-sys.md) | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## notifyDataChange

```TypeScript
static notifyDataChange(extInfo: ExtraData, callback: AsyncCallback<void>): void
```

通知云端的数据变更，可以通过extInfo中的extraData字段指定变更的数据库名和表名，使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static notifyDataChange(extInfo: ExtraData, callback: AsyncCallback<void>): void--><!--Device-Config-static notifyDataChange(extInfo: ExtraData, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| extInfo | [ExtraData](../../apis-core-file-kit/arkts-apis/arkts-corefile-cloudsyncmanager-extradata-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## notifyDataChange

```TypeScript
static notifyDataChange(extInfo: ExtraData, userId: number, callback: AsyncCallback<void>): void
```

通知云端的数据变更，可以通过extInfo中的extraData字段指定变更的数据库名和表名，可通过userId指定用户ID，使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static notifyDataChange(extInfo: ExtraData, userId: int, callback: AsyncCallback<void>): void--><!--Device-Config-static notifyDataChange(extInfo: ExtraData, userId: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| extInfo | [ExtraData](../../apis-core-file-kit/arkts-apis/arkts-corefile-cloudsyncmanager-extradata-i-sys.md) | 是 |
| userId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## notifyDataChange

```TypeScript
static notifyDataChange(accountId: string, bundleName: string): Promise<void>
```

通知云端的数据变更，使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static notifyDataChange(accountId: string, bundleName: string): Promise<void>--><!--Device-Config-static notifyDataChange(accountId: string, bundleName: string): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```

## notifyDataChange

```TypeScript
static notifyDataChange(accountId: string, bundleName: string, callback: AsyncCallback<void>): void
```

通知云端的数据变更，使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static notifyDataChange(accountId: string, bundleName: string, callback: AsyncCallback<void>): void--><!--Device-Config-static notifyDataChange(accountId: string, bundleName: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Server

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
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

取消订阅应用同步信息变化，使用callback异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Config-static offSyncInfoChanged(        bundleInfos: Array<BundleInfo>,        progress?: Callback<Record<string, Record<string, SyncInfo>>>    ): void--><!--Device-Config-static offSyncInfoChanged(        bundleInfos: Array<BundleInfo>,        progress?: Callback<Record<string, Record<string, SyncInfo>>>    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleInfos | Array&lt;BundleInfo&gt; | 是 |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Record&lt;string, SyncInfo&gt;&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

const bundleInfos: Array<cloudData.BundleInfo> = [
  { bundleName: "bundleName1", storeId: "storeId1" },
  { bundleName: "bundleName2" }
];

const progressCallback = (result: Record<string, Record<string, cloudData.SyncInfo>>) => {
  console.info(`Sync info changed. Result is ${JSON.stringify(result)}`);
};

// 订阅同步信息变化
try {
  cloudData.Config.onSyncInfoChanged(bundleInfos, progressCallback);
} catch(err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}

// 取消订阅指定的回调
try {
  cloudData.Config.offSyncInfoChanged(bundleInfos, progressCallback);
} catch(err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}

// 取消所有订阅
try {
  cloudData.Config.offSyncInfoChanged(bundleInfos);
} catch(err) {
  let error = err as BusinessError;
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

订阅应用同步信息变化，使用callback异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Config-static onSyncInfoChanged(        bundleInfos: Array<BundleInfo>,        progress: Callback<Record<string, Record<string, SyncInfo>>>    ): void--><!--Device-Config-static onSyncInfoChanged(        bundleInfos: Array<BundleInfo>,        progress: Callback<Record<string, Record<string, SyncInfo>>>    ): void-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleInfos | Array&lt;BundleInfo&gt; | 是 |
| progress | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Record&lt;string, Record&lt;string, SyncInfo&gt;&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch(err) {
  let error = err as BusinessError;
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

查询上一次端云同步信息，使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static queryLastSyncInfo(        accountId: string,        bundleName: string,        storeId?: string    ): Promise<Record<string, SyncInfo>>--><!--Device-Config-static queryLastSyncInfo(        accountId: string,        bundleName: string,        storeId?: string    ): Promise<Record<string, SyncInfo>>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| bundleName | string | 是 |
| storeId | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Record&lt;string, SyncInfo&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch(err) {
  let error = err as BusinessError;
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

查询端云统计信息，返回未同步、已同步且端云信息一致和已同步且端云信息不一致的统计信息，使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static queryStatistics(        accountId: string,        bundleName: string,        storeId?: string    ): Promise<Record<string, Array<StatisticInfo>>>--><!--Device-Config-static queryStatistics(        accountId: string,        bundleName: string,        storeId?: string    ): Promise<Record<string, Array<StatisticInfo>>>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accountId | string | 是 |
| bundleName | string | 是 |
| storeId | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Record&lt;string, Array&lt;StatisticInfo&gt;&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

设置全局云同步策略，使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

<!--Device-Config-static setGlobalCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>--><!--Device-Config-static setGlobalCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strategy | [StrategyType](arkts-arkdata-clouddata-strategytype-e.md) | 是 |
| param | Array&lt;commonType.ValueType&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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

停止与云端的数据同步，使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.CLOUDDATA_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Config-static stopCloudSync(bundleInfos: Array<BundleInfo>): Promise<void>--><!--Device-Config-static stopCloudSync(bundleInfos: Array<BundleInfo>): Promise<void>-End-->

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Config

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleInfos | Array&lt;BundleInfo&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [14800001](../errorcode-data-rdb.md#14800001-无效的参数) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

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
} catch (err) {
  let error = err as BusinessError;
  console.error(`An unexpected error occurred. Code: ${error.code}, message: ${error.message}`);
}
```
