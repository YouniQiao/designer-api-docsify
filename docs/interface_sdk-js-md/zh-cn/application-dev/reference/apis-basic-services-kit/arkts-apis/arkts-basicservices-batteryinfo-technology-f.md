# technology

## 导入模块

```TypeScript
import { batteryInfo } from '@kit.BasicServicesKit';
```

## technology

```TypeScript
function technology(): string
```

表示当前设备电池的技术型号。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
// ArkTS-Sta示例
let result = batteryInfo.technology();
console.info("The result is: " + result);
```
