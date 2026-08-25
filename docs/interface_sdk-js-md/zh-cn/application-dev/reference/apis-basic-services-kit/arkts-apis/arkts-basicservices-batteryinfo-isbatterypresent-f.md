# isBatteryPresent

## 导入模块

```TypeScript
import { batteryInfo } from '@kit.BasicServicesKit';
```

## isBatteryPresent

```TypeScript
function isBatteryPresent(): boolean
```

表示当前设备是否支持电池以及电池是否在位。true表示设备支持电池且电池在位，false表示设备不支持电池或电池不在位，默认为false。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
// ArkTS-Sta示例
let result = batteryInfo.isBatteryPresent();
console.info("The result is: " + result);
```
