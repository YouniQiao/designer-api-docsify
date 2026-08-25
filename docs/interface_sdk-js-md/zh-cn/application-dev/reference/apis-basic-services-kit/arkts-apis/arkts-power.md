# @ohos.power

该模块主要提供查询屏幕状态、查询电源模式、检测待机模式等接口，还提供电源键过滤策略的配置能力。 开发者可以使用该模块的接口获取设备的活动状态、电源模式、亮灭屏状态、待机低功耗状态等，适用于需要根据设备电源状态进行业务逻辑调整的场景， 例如在低功耗模式下限制后台活动、在待机模式下优化续航策略等。

**起始版本：** 7

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

## 导入模块

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [getPowerMode](arkts-basicservices-power-getpowermode-f.md) |
| [isActive](arkts-basicservices-power-isactive-f.md) |
| [isScreenOn](arkts-basicservices-power-isscreenon-f.md) |
| [isScreenOn](arkts-basicservices-power-isscreenon-f.md) |
| [isStandby](arkts-basicservices-power-isstandby-f.md) |
| [rebootDevice](arkts-basicservices-power-rebootdevice-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getPowerConfig](arkts-basicservices-power-getpowerconfig-f-sys.md) |
| [hibernate](arkts-basicservices-power-hibernate-f-sys.md) |
| [reboot](arkts-basicservices-power-reboot-f-sys.md) |
| [refreshActivity](arkts-basicservices-power-refreshactivity-f-sys.md) |
| [registerShutdownCallback](arkts-basicservices-power-registershutdowncallback-f-sys.md) |
| [setPowerConfig](arkts-basicservices-power-setpowerconfig-f-sys.md) |
| [setPowerKeyFilteringStrategy](arkts-basicservices-power-setpowerkeyfilteringstrategy-f-sys.md) |
| [setPowerMode](arkts-basicservices-power-setpowermode-f-sys.md) |
| [setPowerMode](arkts-basicservices-power-setpowermode-f-sys.md) |
| [setScreenOffTime](arkts-basicservices-power-setscreenofftime-f-sys.md) |
| [shutdown](arkts-basicservices-power-shutdown-f-sys.md) |
| [suspend](arkts-basicservices-power-suspend-f-sys.md) |
| [unregisterShutdownCallback](arkts-basicservices-power-unregistershutdowncallback-f-sys.md) |
| [wakeup](arkts-basicservices-power-wakeup-f-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [DevicePowerMode](arkts-basicservices-power-devicepowermode-e.md) |
| [PowerKeyFilteringStrategy](arkts-basicservices-power-powerkeyfilteringstrategy-e.md) |
