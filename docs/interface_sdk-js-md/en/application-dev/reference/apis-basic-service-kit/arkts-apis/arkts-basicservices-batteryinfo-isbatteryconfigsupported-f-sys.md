# isBatteryConfigSupported (System API)

## Modules to Import

```TypeScript
import { batteryInfo } from '@kit.BasicServicesKit';
```

## isBatteryConfigSupported

```TypeScript
function isBatteryConfigSupported(sceneName: string): boolean
```

Checks whether the battery configuration is enabled based on the specified scenario.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-batteryInfo-function isBatteryConfigSupported(sceneName: string): boolean--><!--Device-batteryInfo-function isBatteryConfigSupported(sceneName: string): boolean-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sceneName | string | Yes | Scenario name. The value must be a string. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Operation result. The value **true** indicates that the charging scenario is supported, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [5100101](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-basic-services-kit/errorcode-battery-info.md#5100101-service-connection-failure) | Failed to connect to the service. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import {batteryInfo} from '@kit.BasicServicesKit';

let sceneName = 'xxx';
let result = batteryInfo.isBatteryConfigSupported(sceneName);

console.info("The result is: " + result);
```

