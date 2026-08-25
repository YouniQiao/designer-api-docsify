# getAppPowerValue (System API)

## Modules to Import

```TypeScript
import { batteryStats } from 'kits/@kit.BasicServicesKit';
```

## getAppPowerValue

```TypeScript
function getAppPowerValue(uid: number): number
```

Obtains the power consumption of an application, in unit of mAh.

**Since:** 8

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [4600101](../errorcode-batteryStatistics.md#4600101-service-connection-failure) |
