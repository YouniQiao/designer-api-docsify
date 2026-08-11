# @ohos.enterprise.deviceControl(Device Control Management)

This module provides device control capabilities for enterprise device management scenarios. Administrators can remotely control devices through this module, including operations such as device restart, shutdown, screen lock, and factory reset, helping enterprises achieve unified device management and security control.

> **NOTE：**
> 
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare namespace deviceControl--><!--Device-unnamed-declare namespace deviceControl-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { deviceControl } from 'kits/@kit.MDMKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [lockScreen](arkts-mdm-devicecontrol-lockscreen-f.md#lockscreen) | Locks the device screen immediately. |
| [operateDevice](arkts-mdm-devicecontrol-operatedevice-f.md#operatedevice) | Allows administrators to perform operations such as factory reset, restart, shutdown, and screen lock on devices.For example, in enterprise device management scenarios, administrators can remotely control employee devices to perform factory reset, restart, shutdown, or screen lock operations. |
| [operateDevice](arkts-mdm-devicecontrol-operatedevice-f.md#operatedevice-1) | Allows the administrator to operate devices, for example, erasing disks. |
| [reboot](arkts-mdm-devicecontrol-reboot-f.md#reboot) | Reboots the device. |
| [resetFactory](arkts-mdm-devicecontrol-resetfactory-f.md#resetfactory) | Restores factory settings. This API uses an asynchronous callback to return the result. |
| [resetFactory](arkts-mdm-devicecontrol-resetfactory-f.md#resetfactory-1) | Restores factory settings. This API uses a promise to return the result. |
| [shutdown](arkts-mdm-devicecontrol-shutdown-f.md#shutdown) | Shuts down the device. |

### Enums

| Name | Description |
| --- | --- |
| [Operation](arkts-mdm-devicecontrol-operation-e.md) | Defines the device operation. |

