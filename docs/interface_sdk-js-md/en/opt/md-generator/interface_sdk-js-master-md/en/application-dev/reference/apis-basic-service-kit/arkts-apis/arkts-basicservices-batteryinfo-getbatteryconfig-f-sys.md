# getBatteryConfig (System API)

## Modules to Import

```TypeScript
import { batteryInfo } from '@kit.BasicServicesKit';
```

## getBatteryConfig

```TypeScript
function getBatteryConfig(sceneName: string): string
```

Obtains the battery configuration based on the specified scenario.

**Since:** 11

**Deprecated since:** -1

<!--Device-batteryInfo-function getBatteryConfig(sceneName: string): string--><!--Device-batteryInfo-function getBatteryConfig(sceneName: string): string-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [sceneName](../../apis-notification-kit/arkts-apis/arkts-notification-notificationrequest-unifiedgroupinfo-i-sys.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [5100101](../../apis-basic-services-kit/errorcode-battery-info.md#5100101-service-connection-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import {batteryInfo} from '@kit.BasicServicesKit';

let sceneName = 'xxx';
let result = batteryInfo.getBatteryConfig(sceneName);

console.info("The result is: " + result);
```
