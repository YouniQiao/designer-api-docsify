# batteryCapacityLevel

## 导入模块

```TypeScript
import { batteryInfo } from '@kit.BasicServicesKit';
```

## batteryCapacityLevel

```TypeScript
function batteryCapacityLevel(): BatteryCapacityLevel
```

表示当前设备电池电量的等级。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**返回值：**

| 类型 |
| --- |
| [BatteryCapacityLevel](arkts-basicservices-batteryinfo-batterycapacitylevel-e.md) |

**示例**

```TypeScript
// ArkTS-Sta示例
let result = batteryInfo.batteryCapacityLevel();
console.info("The result is: " + result);
```
