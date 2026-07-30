# getInstalledBundleStorageStats

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.MDMKit';
```

## getInstalledBundleStorageStats

```TypeScript
function getInstalledBundleStorageStats(admin: Want, bundleNames: Array<string>, accountId: number): Promise<Array<BundleStorageStats>>
```

Get the storage statistics of installed bundles on the device.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_GET_ALL_BUNDLE_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getInstalledBundleStorageStats(admin: Want, bundleNames: Array<string>, accountId: number): Promise<Array<BundleStorageStats>>--><!--Device-bundleManager-function getInstalledBundleStorageStats(admin: Want, bundleNames: Array<string>, accountId: number): Promise<Array<BundleStorageStats>>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-arkui/arkts-apis/arkts-arkui-want-t-sys.md) | Yes | admin indicates the enterprise admin extension ability information. |
| bundleNames | Array&lt;string&gt; | Yes | bundleNames indicates the list of application bundle names. |
| accountId | number | Yes | Account ID.<br>The value must be an integer greater than or equal to 0.<br> You can call [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)of @ ohos.account.osAccount to obtain the account ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;BundleStorageStats&gt;&gt; | Returns the bundle statistics of the installed applications. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |

**Example**

```TypeScript
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { bundleManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Replace with actual values.
let bundleNames: Array<string> = ['com.example.app1', 'com.example.app2'];
let accountId: number = 100;
bundleManager.getInstalledBundleStorageStats(wantTemp, bundleNames, accountId).then((result) => {
  console.info('Succeeded in getting installed bundle storage stats.');
}).catch((err: BusinessError) => {
  console.error(`Failed to get installed bundle storage stats. Code is ${err.code}, message is ${err.message}`);
});

```

```TypeScript
// Return value example.
[
  {
    "bundleName": "com.example.edmtest",
    "appSize": 38185408,
    "dataSize": 1216566
  },
  // ...
]

```

