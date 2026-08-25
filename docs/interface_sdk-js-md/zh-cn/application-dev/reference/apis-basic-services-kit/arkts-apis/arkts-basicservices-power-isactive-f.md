# isActive

## 导入模块

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## isActive

```TypeScript
function isActive(): boolean
```

检测当前设备是否处于活动状态。可用于应用根据设备活动状态调整行为，例如在设备非活动状态下暂停后台任务等。  
- 有屏的设备亮屏时为活动状态，灭屏时为非活动状态。 - 无屏的设备非休眠时为活动状态，休眠时为非活动状态。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
let isActive = power.isActive();
console.info('power is active: ' + isActive);
```
