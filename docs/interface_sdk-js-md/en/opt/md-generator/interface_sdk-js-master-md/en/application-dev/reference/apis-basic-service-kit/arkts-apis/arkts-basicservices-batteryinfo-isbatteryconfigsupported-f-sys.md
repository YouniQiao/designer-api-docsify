# isBatteryConfigSupported (System API)

## Modules to Import

```TypeScript
import { batteryInfo } from 'kits/@kit.BasicServicesKit';
```

## isBatteryConfigSupported

```TypeScript
function isBatteryConfigSupported(sceneName: string): boolean
```

Checks whether the battery configuration is enabled based on the specified scenario.

**Since:** 11

<!--Device-batteryInfo-function isBatteryConfigSupported(sceneName: string): boolean--><!--Device-batteryInfo-function isBatteryConfigSupported(sceneName: string): boolean-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sceneName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [5100101](../../apis-basic-services-kit/errorcode-battery-info.md#5100101-service-connection-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import {batteryInfo} from '@kit.BasicServicesKit';

let sceneName = 'xxx';
let result = batteryInfo.isBatteryConfigSupported(sceneName);

console.info("The result is: " + result);
```
