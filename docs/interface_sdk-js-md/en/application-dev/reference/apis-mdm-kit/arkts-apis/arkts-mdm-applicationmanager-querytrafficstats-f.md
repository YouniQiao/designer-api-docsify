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

> **NOTE：**&gt;
> The input network type (**networkInfo.type**) can only be **connection.NetBearType.BEARER_CELLULAR** or
> **connection.NetBearType.BEARER_WIFI**. If any other value is passed, the API returns error code 9200012.&gt;
> The input start time (**networkInfo.startTime**) and end time (**networkInfo.endTime**) are second-level
> timestamps. If the input start time and end time are negative numbers or the start time is later than the end
> time, the API returns error code 9200012.&gt;
> If the input user ID (**accountId**) is not the ID of the current user, the API returns error code 9200012.&gt;
> It is advised that the query interval (end time – start time) be 1 to 30 days. If the interval is too short, the
> query result may be inaccurate. If the interval is too long, the query will take a long time.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

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
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
