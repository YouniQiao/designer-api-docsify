# queryTrafficStats

## Modules to Import

```TypeScript
import { applicationManager } from '@kit.MDMKit';
```

## queryTrafficStats

```TypeScript
function queryTrafficStats(
    admin: Want,
    bundleName: string,
    appIndex: number,
    accountId: number,
    networkInfo: statistics.NetworkInfo
  ): Promise<statistics.NetStatsInfo>
```

Queries usage statistics of application traffic.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function queryTrafficStats(    admin: Want,    bundleName: string,    appIndex: number,    accountId: number,    networkInfo: statistics.NetworkInfo  ): Promise<statistics.NetStatsInfo>--><!--Device-applicationManager-function queryTrafficStats(    admin: Want,    bundleName: string,    appIndex: number,    accountId: number,    networkInfo: statistics.NetworkInfo  ): Promise<statistics.NetStatsInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-arkui/arkts-apis/arkts-arkui-want-t-sys.md) | Yes | admin indicates the enterprise admin extension ability information. |
| bundleName | string | Yes | bundleName indicates the bundle name of application to be queried. |
| appIndex | number | Yes | appIndex indicates the index of the bundle.<br>The value must be an integer greater than or equal to 0. |
| accountId | number | Yes | accountId indicates the local ID of the OS account.<br>The value must be an integer greater than or equal to 0.<br>You can call [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)of @ohos.account.osAccount to obtain the ID. |
| networkInfo | statistics.NetworkInfo | Yes | networkInfo indicates the network information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;statistics.NetStatsInfo&gt; | returns the detailed network statistics information. |

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
import { connection, statistics } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

async function queryTrafficStats() {
  let wantTemp: Want = {
    // Replace it as required.
    bundleName: 'com.example.myapplication',
    abilityName: 'EnterpriseAdminAbility'
  };
  // Replace it as required.
  let bundleName: string = 'com.example.test';
  let appIndex: number = 0;
  let accountId: number = 100;
  // In the sample code, sim.getSimAccountInfo is used to obtain the SIM ID.
  let slotId: number = 0;
  let simId: number = 0;
  await sim.getSimAccountInfo(slotId).then((data: sim.IccAccountInfo) => {
    simId = data.simId;
  }).catch((err: BusinessError) => {
    console.error(`getSimAccountInfo failed, promise: err->${JSON.stringify(err)}`);
  });
  let networkInfo: statistics.NetworkInfo = {
    // Replace it as required.
    type: connection.NetBearType.BEARER_CELLULAR,
    // Query data from 2026/4/15 00:00:00.000 to 2026/4/16 00:00:00.000. (The month starts from 0.)
    startTime: Math.floor(new Date(2026, 3, 15, 0, 0, 0, 0).getTime() / 1000),
    endTime: Math.floor(new Date(2026, 3, 16, 0, 0, 0, 0).getTime() / 1000),
    // If the network type is BEARER_CELLULAR, simId needs to be passed. If the network type is BEARER_WIFI, simId does not need to be passed.
    simId: simId
  }
  await applicationManager.queryTrafficStats(wantTemp, bundleName, appIndex, accountId, networkInfo)
    .then(result => {
      console.info('Succeeded in querying traffic stats.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to query traffic stats. Code is ${error.code}, message is ${error.message}`);
    })
}

```

