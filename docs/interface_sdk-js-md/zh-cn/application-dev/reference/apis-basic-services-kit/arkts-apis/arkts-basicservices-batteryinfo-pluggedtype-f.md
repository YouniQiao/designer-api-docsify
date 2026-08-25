# pluggedType

## 导入模块

```TypeScript
import { batteryInfo } from '@kit.BasicServicesKit';
```

## pluggedType

```TypeScript
function pluggedType(): BatteryPluggedType
```

表示当前设备连接的充电器类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**返回值：**

| 类型 |
| --- |
| [BatteryPluggedType](arkts-basicservices-batteryinfo-batterypluggedtype-e.md) |

**示例**

```TypeScript
// ArkTS-Sta示例
let result = batteryInfo.pluggedType();
console.info("The result is: " + result);
```
