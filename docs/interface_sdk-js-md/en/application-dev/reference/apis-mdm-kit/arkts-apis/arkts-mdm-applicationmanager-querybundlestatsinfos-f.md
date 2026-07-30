# queryBundleStatsInfos

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## queryBundleStatsInfos

```TypeScript
function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array<BundleStatsInfo>
```

Queries bundle statistics information of applications.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array<BundleStatsInfo>--><!--Device-applicationManager-function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array<BundleStatsInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-arkui/arkts-apis/arkts-arkui-want-t-sys.md) | Yes | admin indicates the enterprise admin extension ability information. |
| startTime | number | Yes | startTime indicates the start time of the query period.<br>Unit: milliseconds, The value must be an integer greater than or equal to 0. |
| endTime | number | Yes | endTime indicates the end time of the query period.<br>Unit: milliseconds, The value must be an integer greater than or equal to 0. |
| accountId | number | Yes | accountId indicates the local ID of the OS account.<br>The value must be an integer greater than or equal to 0. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;BundleStatsInfo&gt; | returns the bundle statistics information of the applications. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |

**Example**

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Query data from 2026/4/15 00:00:00.000 to 2026/4/16 23:59:59.999. (The month starts from 0.)
  let startTime: number = new Date(2026, 3, 15, 0, 0, 0, 0).getTime();
  let endTime: number = new Date(2026, 3, 16, 23, 59, 59, 999).getTime();
  let accountId: number = 100;
  let result: Array<applicationManager.BundleStatsInfo> = applicationManager.queryBundleStatsInfos(wantTemp, startTime, endTime, accountId);
  console.info(`Succeeded in querying bundle stats infos, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to query bundle stats infos. Code: ${err.code}, message: ${err.message}`);
}

```

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace it as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Query data of the last month.
  // Obtain the current date.
  let currentDate: Date = new Date();
  // Calculate the first day of the last month. (The month starts from 0. Therefore, subtract 1 from the current month.)
  let lastMonthFirstDay: Date = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1, 0, 0, 0, 0);
  // Calculate the last day of the last month. (The 0th day of the next month is the last day of the current month.)
  let lastMonthLastDay: Date = new Date(currentDate.getFullYear(), currentDate.getMonth(), 0, 23, 59, 59, 999);
  
  let startTime: number = lastMonthFirstDay.getTime();
  let endTime: number = lastMonthLastDay.getTime();
  let accountId: number = 100;
  let result: Array<applicationManager.BundleStatsInfo> = applicationManager.queryBundleStatsInfos(wantTemp, startTime, endTime, accountId);
  console.info(`Succeeded in querying bundle stats infos, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to query bundle stats infos. Code: ${err.code}, message: ${err.message}`);
}

```

