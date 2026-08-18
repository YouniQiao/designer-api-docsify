# queryTrafficStats

## Modules to Import

```TypeScript
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

Queries the data usage of a specified application within a specified period for the current user. This API uses a promise to return the result. > **NOTE：**> > The input network type (**networkInfo.type**) can only be **connection.NetBearType.BEARER_CELLULAR** or > **connection.NetBearType.BEARER_WIFI**. If any other value is passed, the API returns error code 9200012. > > The input start time (**networkInfo.startTime**) and end time (**networkInfo.endTime**) are second-level > timestamps. If the input start time and end time are negative numbers or the start time is later than the end > time, the API returns error code 9200012. > > If the input user ID (**accountId**) is not the ID of the current user, the API returns error code 9200012. > > It is advised that the query interval (end time – start time) be 1 to 30 days. If the interval is too short, the > query result may be inaccurate. If the interval is too long, the query will take a long time.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function queryTrafficStats(    admin: Want,    bundleName: string,    appIndex: number,    accountId: number,    networkInfo: statistics.NetworkInfo  ): Promise<statistics.NetStatsInfo>--><!--Device-applicationManager-function queryTrafficStats(    admin: Want,    bundleName: string,    appIndex: number,    accountId: number,    networkInfo: statistics.NetworkInfo  ): Promise<statistics.NetStatsInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| bundleName | string | Yes |
| appIndex | number | Yes |
| accountId | number | Yes |
| networkInfo | statistics.NetworkInfo | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;statistics.NetStatsInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

**Examples**

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
