# @ohos.thermal

该模块提供热管理相关的接口，包括热档位查询及注册回调等功能。系统根据设备温度阈值将热状态划分为多个档位层级（参见[ThermalLevel](arkts-basicservices-thermal-thermallevel-e.md)）， 当设备温度跨越档位阈值时触发回调通知，开发者可根据档位等级执行相应的业务降级策略。

**起始版本：** 8

**系统能力：** SystemCapability.PowerManager.ThermalManager

## 导入模块

```TypeScript
import { thermal } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getLevel](arkts-basicservices-thermal-getlevel-f.md) |
| [getThermalLevel](arkts-basicservices-thermal-getthermallevel-f.md) |
| [registerThermalLevelCallback](arkts-basicservices-thermal-registerthermallevelcallback-f.md) |
| [subscribeThermalLevel](arkts-basicservices-thermal-subscribethermallevel-f.md) |
| [unregisterThermalLevelCallback](arkts-basicservices-thermal-unregisterthermallevelcallback-f.md) |
| [unsubscribeThermalLevel](arkts-basicservices-thermal-unsubscribethermallevel-f.md) |

### 枚举

| 名称 |
| --- |
| [ThermalLevel](arkts-basicservices-thermal-thermallevel-e.md) |
