# isActive

## Modules to Import

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## isActive

```TypeScript
function isActive(): boolean
```

检测当前设备是否处于活动状态。

- 有屏的设备亮屏时为活动状态，熄屏时为非活动状态。  
- 无屏的设备非休眠时为活动状态，休眠时为非活动状态。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-power-function isActive(): boolean--><!--Device-power-function isActive(): boolean-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 活动状态返回true，非活动状态返回false。 |

## Examples

```TypeScript
let isActive = power.isActive();
console.info('power is active: ' + isActive);
```

