# getAppPowerValue (System API)

## Modules to Import

```TypeScript
import { batteryStats } from 'batteryStats';
```

## getAppPowerValue

```TypeScript
function getAppPowerValue(uid: int): double
```

Obtains the power consumption of an application, in unit of mAh.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-batteryStats-function getAppPowerValue(uid: int): double--><!--Device-batteryStats-function getAppPowerValue(uid: int): double-End-->

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | int | Yes | Application UID. |

**Return value:**

| Type | Description |
| --- | --- |
| double | Power consumption of the application with this UID, in unit of mAh. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Parameter verification failed. |
| [4600101](../../apis-basic-services-kit/errorcode-batteryStatistics.md#4600101-service-connection-failure) | Failed to connect to the service. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
try {
    let value = batteryStats.getAppPowerValue(10021);
    console.info('battery statistics value of app is: ' + value);
} catch(err) {
    console.error('get battery statistics value of app failed, err: ' + err);
}
```

