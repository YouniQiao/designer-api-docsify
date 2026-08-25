# getLevel

## 导入模块

```TypeScript
import { thermal } from '@kit.BasicServicesKit';
```

## getLevel

```TypeScript
function getLevel(): ThermalLevel
```

获取当前热档位信息。系统根据设备温度实时判定当前所处的热档位层级并返回对应等级，开发者可据此执行相应的业务降级策略。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**返回值：**

| 类型 |
| --- |
| [ThermalLevel](arkts-basicservices-thermal-thermallevel-e.md) |

**示例**

```TypeScript
let level = thermal.getLevel();
console.info('thermal level is: ' + level);
```
