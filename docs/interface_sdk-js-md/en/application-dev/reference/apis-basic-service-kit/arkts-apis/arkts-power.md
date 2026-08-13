# @ohos.power

The **power** module provides APIs for rebooting and shutting down the system, as well as querying the screen status. You can use these APIs to obtain the device activity status, power mode, and screen on/off status.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace power--><!--Device-unnamed-declare namespace power-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

## Modules to Import

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getPowerMode](arkts-basicservices-power-getpowermode-f.md#getPowerMode) | Obtains the power mode of this device. |
| [isActive](arkts-basicservices-power-isactive-f.md#isActive) | Checks whether the current device is active. - A device with a screen is active when the screen is on and inactive when the screen is off. - A device without a screen is active when it exits the sleep mode and inactive when it enters the sleep mode. |
| [isScreenOn](arkts-basicservices-power-isscreenon-f.md#isScreenOn) | Checks the screen status of the current device. This API uses an asynchronous callback to return the result. |
| [isScreenOn](arkts-basicservices-power-isscreenon-f.md#isScreenOn) | Checks the screen status of the current device. This API uses a promise to return the result. |
| [isStandby](arkts-basicservices-power-isstandby-f.md#isStandby) | Checks whether the device is in standby mode. |
| [rebootDevice](arkts-basicservices-power-rebootdevice-f.md#rebootDevice) | Restarts the system. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getPowerConfig](arkts-basicservices-power-getpowerconfig-f-sys.md#getPowerConfig) | Query the power configuration value for a given scene name. |
| [hibernate](arkts-basicservices-power-hibernate-f-sys.md#hibernate) | Hibernates a device. |
| [reboot](arkts-basicservices-power-reboot-f-sys.md#reboot) | Reboots a device. |
| [refreshActivity](arkts-basicservices-power-refreshactivity-f-sys.md#refreshActivity) | Refreshes the device activity status (for example, resetting the screen-off time). This API takes effect only when the device is active. For details about the device activity status, see [power.isActive](arkts-basicservices-power-isactive-f.md#isActive). |
| [registerShutdownCallback](arkts-basicservices-power-registershutdowncallback-f-sys.md#registerShutdownCallback) | Registers a callback to be invoked when the device is shut down or rebooted. This API uses an asynchronous callback to return the result. |
| [setPowerConfig](arkts-basicservices-power-setpowerconfig-f-sys.md#setPowerConfig) | Update the power configuration value for a given scene name. |
| [setPowerKeyFilteringStrategy](arkts-basicservices-power-setpowerkeyfilteringstrategy-f-sys.md#setPowerKeyFilteringStrategy) | Sets the power key filtering strategy. After the power service subscribes to the power key event, this API is used to configure the processing mode of this event. For details about the power key filtering strategy, see [power.PowerKeyFilteringStrategy](arkts-basicservices-power-powerkeyfilteringstrategy-e.md#PowerKeyFilteringStrategy). |
| [setPowerMode](arkts-basicservices-power-setpowermode-f-sys.md#setPowerMode) | Sets the power mode of a device. This API uses an asynchronous callback to return the result. |
| [setPowerMode](arkts-basicservices-power-setpowermode-f-sys.md#setPowerMode-(System-API)) | Sets the power mode of a device. This API uses a promise to return the result. |
| [setScreenOffTime](arkts-basicservices-power-setscreenofftime-f-sys.md#setScreenOffTime) | Sets the screen-off timeout duration, in unit of ms. |
| [shutdown](arkts-basicservices-power-shutdown-f-sys.md#shutdown) | Shuts down the system. |
| [suspend](arkts-basicservices-power-suspend-f-sys.md#suspend) | Enables a device to enter the sleep state. |
| [unregisterShutdownCallback](arkts-basicservices-power-unregistershutdowncallback-f-sys.md#unregisterShutdownCallback) | Unregisters the callback to be invoked when the device is shut down or rebooted. This API uses a callback to return the result. |
| [wakeup](arkts-basicservices-power-wakeup-f-sys.md#wakeup) | Wakes up a device. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [DevicePowerMode](arkts-basicservices-power-devicepowermode-e.md) | Enumerates power modes. |
| [PowerKeyFilteringStrategy](arkts-basicservices-power-powerkeyfilteringstrategy-e.md) | Enumerates the power key filtering strategies. |

