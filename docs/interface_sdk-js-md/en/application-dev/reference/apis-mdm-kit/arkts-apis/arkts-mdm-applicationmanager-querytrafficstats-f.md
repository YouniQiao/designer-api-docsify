# queryTrafficStats

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
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

查询当前用户下指定应用在特定时间段内使用流量情况。使用Promise异步回调。

> **说明：**
> 
> 传入的网络类型（networkInfo.type）仅支持蜂窝网络（connection.NetBearType.BEARER_CELLULAR）和Wi-Fi网络（
> connection.NetBearType.BEARER_WIFI）。若传入其他值，接口会返回错误码9200012。
> 
> 传入的起始时间（networkInfo.startTime）、结束时间（networkInfo.endTime）为秒级时间戳。若传入的起始时间、结束时间为负数，或起始时间大于结束时间，接口会返回错误码9200012。
> 
> 传入的用户ID（accountId）非当前用户时，接口会返回错误码9200012。
> 
> 建议查询的时间间隔（结束时间-起始时间）最小为1天，最大为30天。时间间隔太小，查询结果可能不准确。时间间隔太大，查询耗时会很长。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function queryTrafficStats(    admin: Want,    bundleName: string,    appIndex: number,    accountId: number,    networkInfo: statistics.NetworkInfo  ): Promise<statistics.NetStatsInfo>--><!--Device-applicationManager-function queryTrafficStats(    admin: Want,    bundleName: string,    appIndex: number,    accountId: number,    networkInfo: statistics.NetworkInfo  ): Promise<statistics.NetStatsInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| bundleName | string | Yes | 应用的包名。 |
| appIndex | number | Yes | 应用分身索引，取值范围：大于等于0的整数。 &lt;br&gt; appIndex可以通过@ohos.bundle.bundleManager中的 [getAppCloneIdentity](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getappcloneidentity-f.md/arkts-ability-bundlemanager-getappcloneidentity-f.md#getappcloneidentity)等接口来获取。 |
| accountId | number | Yes | 用户ID，取值范围：大于等于0的整数。 &lt;br&gt; accountId可以通过@ohos.account.osAccount中的 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)等接口来获取。 |
| networkInfo | statistics.NetworkInfo | Yes | 网络信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;statistics.NetStatsInfo&gt; | Promise对象，返回获取的历史流量信息对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9200012 | Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

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

