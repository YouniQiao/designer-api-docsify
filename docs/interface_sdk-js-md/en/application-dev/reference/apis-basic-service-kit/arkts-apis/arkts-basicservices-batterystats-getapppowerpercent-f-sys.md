# getAppPowerPercent (System API)

## Modules to Import

```TypeScript
import { batteryStats } from '@kit.BasicServicesKit';
```

## getAppPowerPercent

```TypeScript
function getAppPowerPercent(uid: int): double
```

Obtains the proportion of the power consumption of an application.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-batteryStats-function getAppPowerPercent(uid: int): double--><!--Device-batteryStats-function getAppPowerPercent(uid: int): double-End-->

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Application UID. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | Proportion of the power consumption of an application with this UID, which ranges from 0.00 to 1.00. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Parameter verification failed. |
| [4600101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-batteryStatistics.md#4600101-service-connection-failure) | Failed to connect to the service. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
try {
    let percent = batteryStats.getAppPowerPercent(10021);
    console.info('battery statistics percent of app is: ' + percent);
} catch(err) {
    console.error('get battery statistics percent of app failed, err: ' + err);
}
```

