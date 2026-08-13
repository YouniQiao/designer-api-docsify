# getAppPowerValue (System API)

## Modules to Import

```TypeScript
import { batteryStats } from '@kit.BasicServicesKit';
```

## getAppPowerValue

```TypeScript
function getAppPowerValue(uid: number): number
```

Obtains the power consumption of an application, in unit of mAh.

**Since:** 23

**Deprecated since:** -1

<!--Device-batteryStats-function getAppPowerValue(uid: int): double--><!--Device-batteryStats-function getAppPowerValue(uid: int): double-End-->

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [4600101](../../apis-basic-services-kit/errorcode-batteryStatistics.md#4600101-service-connection-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
try {
    let value = batteryStats.getAppPowerValue(10021);
    console.info('battery statistics value of app is: ' + value);
} catch(err) {
    console.error('get battery statistics value of app failed, err: ' + err);
}
```
