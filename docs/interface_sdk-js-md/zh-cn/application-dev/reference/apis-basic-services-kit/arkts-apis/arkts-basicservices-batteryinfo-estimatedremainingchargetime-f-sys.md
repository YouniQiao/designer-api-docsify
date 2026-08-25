# estimatedRemainingChargeTime（系统接口）

## 导入模块

```TypeScript
import { batteryInfo } from '@kit.BasicServicesKit';
```

## estimatedRemainingChargeTime

```TypeScript
function estimatedRemainingChargeTime(): long
```

获取当前设备充满电的预估时间，单位毫秒。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| long |

**示例**

```TypeScript
// ArkTS-Sta示例
let result = batteryInfo.estimatedRemainingChargeTime();
console.info("The result is: " + result);
```
