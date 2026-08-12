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

Queries the data usage of a specified application within a specified period for the current user. This API uses a promise to return the result.

> **NOTE：**
> 
> The input network type (**networkInfo.type**) can only be **connection.NetBearType.BEARER_CELLULAR** or
> **connection.NetBearType.BEARER_WIFI**. If any other value is passed, the API returns error code 9200012.
> 
> The input start time (**networkInfo.startTime**) and end time (**networkInfo.endTime**) are second-level
> timestamps. If the input start time and end time are negative numbers or the start time is later than the end
> time, the API returns error code 9200012.
> 
> If the input user ID (**accountId**) is not the ID of the current user, the API returns error code 9200012.
> 
> It is advised that the query interval (end time – start time) be 1 to 30 days. If the interval is too short, the
> query result may be inaccurate. If the interval is too long, the query will take a long time.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

<!--Device-applicationManager-function queryTrafficStats(    admin: Want,    bundleName: string,    appIndex: number,    accountId: number,    networkInfo: statistics.NetworkInfo  ): Promise<statistics.NetStatsInfo>--><!--Device-applicationManager-function queryTrafficStats(    admin: Want,    bundleName: string,    appIndex: number,    accountId: number,    networkInfo: statistics.NetworkInfo  ): Promise<statistics.NetStatsInfo>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| bundleName | string | Yes | Bundle name of the application. |
| appIndex | number | Yes | Index of the application clone. The value is an integer greater than or equal to 0. &lt;br&gt; You can call [getAppCloneIdentity](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getappcloneidentity-f.md#getAppCloneIdentity) of @ohos.bundle.bundleManager to obtain the index. |
| accountId | number | Yes | Account ID. The value is an integer greater than or equal to 0. &lt;br&gt; You can call [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getOsAccountLocalId) of @ohos.account.osAccount to obtain the ID. |
| networkInfo | statistics.NetworkInfo | Yes | Network information. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;statistics.NetStatsInfo&gt; | Promise used to return the historical traffic information object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

