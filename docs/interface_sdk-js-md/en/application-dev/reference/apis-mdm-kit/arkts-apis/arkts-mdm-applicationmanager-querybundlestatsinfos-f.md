# queryBundleStatsInfos

## Modules to Import

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## queryBundleStatsInfos

```TypeScript
function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array<BundleStatsInfo>
```

Queries the accumulated foreground runtime statistics of applications under a specified user account within a given time period. The minimum query granularity is one day. The API requires the start time (**startTime**), end time (**endTime**), and target user account ID (**accountId**) to be passed in. **startTime** and **endTime** are millisecond-level timestamps. The caller can pass custom values. The default value of **startTime** is 00:00:00.000 of the current day, and the default of **endTime** is 24:00:00.000 of the current day (that is, 00:00:00 of the following day). The API returns an array of **BundleStatsInfo**, where each element contains the bundle name of an application, its clone index, and the foreground usage duration (in milliseconds) within the specified time period. If **startTime** is set to **0**, the query starts from the device's first boot time. If **startTime** is later than **endTime**, the API returns error code 9200012.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| startTime | number | Yes |
| endTime | number | Yes |
| accountId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;BundleStatsInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
