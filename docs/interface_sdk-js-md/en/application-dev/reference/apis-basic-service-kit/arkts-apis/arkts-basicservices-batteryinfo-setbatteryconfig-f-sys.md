# setBatteryConfig (System API)

## Modules to Import

```TypeScript
import { batteryInfo } from 'kits/@kit.BasicServicesKit';
```

## setBatteryConfig

```TypeScript
function setBatteryConfig(sceneName: string, sceneValue: string): int
```

按场景名称设置电池配置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-batteryInfo-function setBatteryConfig(sceneName: string, sceneValue: string): int--><!--Device-batteryInfo-function setBatteryConfig(sceneName: string, sceneValue: string): int-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sceneName | string | Yes | 设置场景名称；该参数必须为字符串类型。 |
| sceneValue | string | Yes | 设置场景的值；该参数必须为字符串类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| int | 返回设置充电结果。返回0表示设置成功，返回非0表示设置失败。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 5100101 | Failed to connect to the service. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## Examples

```TypeScript
import {batteryInfo} from '@kit.BasicServicesKit';

let sceneName = 'xxx';
let sceneValue = '0';
let result = batteryInfo.setBatteryConfig(sceneName, sceneValue);

console.info("The result is: " + result);
```

