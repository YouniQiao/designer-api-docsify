# @ohos.power

The **power** module provides APIs for rebooting and shutting down the system, as well as querying the screen status. You can use these APIs to obtain the device activity status, power mode, and screen on/off status.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace power--><!--Device-unnamed-declare namespace power-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

## Modules to Import

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getPowerMode](arkts-basicservices-power-getpowermode-f.md#getPowerMode) |
| [isActive](arkts-basicservices-power-isactive-f.md#isActive) |
| [isScreenOn](arkts-basicservices-power-isscreenon-f.md#isScreenOn) |
| [isScreenOn](arkts-basicservices-power-isscreenon-f.md#isScreenOn) |
| [isStandby](arkts-basicservices-power-isstandby-f.md#isStandby) |
| [rebootDevice](arkts-basicservices-power-rebootdevice-f.md#rebootDevice) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getPowerConfig](arkts-basicservices-power-getpowerconfig-f-sys.md#getPowerConfig-(System-API)) |
| [hibernate](arkts-basicservices-power-hibernate-f-sys.md#hibernate-(System-API)) |
| [reboot](arkts-basicservices-power-reboot-f-sys.md#reboot-(System-API)) |
| [refreshActivity](arkts-basicservices-power-refreshactivity-f-sys.md#refreshActivity-(System-API)) |
| [registerShutdownCallback](arkts-basicservices-power-registershutdowncallback-f-sys.md#registerShutdownCallback-(System-API)) |
| [setPowerConfig](arkts-basicservices-power-setpowerconfig-f-sys.md#setPowerConfig-(System-API)) |
| [setPowerKeyFilteringStrategy](arkts-basicservices-power-setpowerkeyfilteringstrategy-f-sys.md#setPowerKeyFilteringStrategy-(System-API)) |
| [setPowerMode](arkts-basicservices-power-setpowermode-f-sys.md#setPowerMode-(System-API)) |
| [setPowerMode](arkts-basicservices-power-setpowermode-f-sys.md#setPowerMode-(System-API)) |
| [setScreenOffTime](arkts-basicservices-power-setscreenofftime-f-sys.md#setScreenOffTime-(System-API)) |
| [shutdown](arkts-basicservices-power-shutdown-f-sys.md#shutdown-(System-API)) |
| [suspend](arkts-basicservices-power-suspend-f-sys.md#suspend-(System-API)) |
| [unregisterShutdownCallback](arkts-basicservices-power-unregistershutdowncallback-f-sys.md#unregisterShutdownCallback-(System-API)) |
| [wakeup](arkts-basicservices-power-wakeup-f-sys.md#wakeup-(System-API)) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DevicePowerMode](arkts-basicservices-power-devicepowermode-e.md) |
| [PowerKeyFilteringStrategy](arkts-basicservices-power-powerkeyfilteringstrategy-e.md) |
