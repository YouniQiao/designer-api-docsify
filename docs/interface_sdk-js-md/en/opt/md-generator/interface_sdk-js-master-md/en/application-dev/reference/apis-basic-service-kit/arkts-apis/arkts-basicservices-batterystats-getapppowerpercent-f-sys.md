# getAppPowerPercent (System API)

## Modules to Import

```TypeScript
import { batteryStats } from 'kits/@kit.BasicServicesKit';
```

## getAppPowerPercent

```TypeScript
function getAppPowerPercent(uid: number): number
```

Obtains the proportion of the power consumption of an application.

**Since:** 8

<!--Device-batteryStats-function getAppPowerPercent(uid: int): double--><!--Device-batteryStats-function getAppPowerPercent(uid: int): double-End-->

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
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [4600101](../../apis-basic-services-kit/errorcode-batteryStatistics.md#4600101-service-connection-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
try {
    let percent = batteryStats.getAppPowerPercent(10021);
    console.info('battery statistics percent of app is: ' + percent);
} catch(err) {
    console.error('get battery statistics percent of app failed, err: ' + err);
}
```
