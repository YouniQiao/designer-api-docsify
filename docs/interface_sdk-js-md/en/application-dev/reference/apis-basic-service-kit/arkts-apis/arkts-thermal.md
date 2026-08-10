# @ohos.thermal

该模块提供热管理相关的接口，包括热档位查询及注册回调等功能。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace thermal--><!--Device-unnamed-declare namespace thermal-End-->

**System capability:** SystemCapability.PowerManager.ThermalManager

## Modules to Import

```TypeScript
import { thermal } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getLevel](arkts-basicservices-thermal-getlevel-f.md#getlevel) | 获取当前热档位信息。 |
| [getThermalLevel](arkts-basicservices-thermal-getthermallevel-f.md#getthermallevel) | 获取当前热档位信息。 |
| [registerThermalLevelCallback](arkts-basicservices-thermal-registerthermallevelcallback-f.md#registerthermallevelcallback) | 订阅热档位变化时的回调提醒。使用callback异步回调。 |
| [subscribeThermalLevel](arkts-basicservices-thermal-subscribethermallevel-f.md#subscribethermallevel) | 订阅热档位变化时的回调提醒。使用callback异步回调。 |
| [unregisterThermalLevelCallback](arkts-basicservices-thermal-unregisterthermallevelcallback-f.md#unregisterthermallevelcallback) | 取消订阅热档位变化时的回调提醒。使用callback异步回调。 |
| [unsubscribeThermalLevel](arkts-basicservices-thermal-unsubscribethermallevel-f.md#unsubscribethermallevel) | 取消订阅热档位变化时的回调提醒。使用callback异步回调。 |

### Enums

| Name | Description |
| --- | --- |
| [ThermalLevel](arkts-basicservices-thermal-thermallevel-e.md) | 热档位信息。 |

