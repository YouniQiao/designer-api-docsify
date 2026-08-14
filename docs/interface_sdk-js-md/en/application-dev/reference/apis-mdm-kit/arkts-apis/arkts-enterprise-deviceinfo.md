# @ohos.enterprise.deviceInfo

This module provides APIs for enterprise device information management, including obtaining device serial numbers, device names, and SIM card information. Enterprise administrators can use this module to query device details, enabling unified management and tracking of device assets. **Use cases:** - Device asset management and tracking - Enterprise device compliance check - Device information collection and statistics - Fault diagnosis and device identification > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace deviceInfo--><!--Device-unnamed-declare namespace deviceInfo-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { deviceInfo } from 'deviceInfo';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getDeviceInfo](arkts-mdm-deviceinfo-getdeviceinfo-f.md#getDeviceInfo) | Obtains device information. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getDeviceName](arkts-mdm-deviceinfo-getdevicename-f-sys.md#getDeviceName) | Obtains the device name. This API uses an asynchronous callback to return the result. |
| [getDeviceName](arkts-mdm-deviceinfo-getdevicename-f-sys.md#getDeviceName-(System-API)) | Obtains the device name. This API uses a promise to return the result. |
| [getDeviceSerial](arkts-mdm-deviceinfo-getdeviceserial-f-sys.md#getDeviceSerial) | Obtains the device serial number. This API uses an asynchronous callback to return the result. |
| [getDeviceSerial](arkts-mdm-deviceinfo-getdeviceserial-f-sys.md#getDeviceSerial-(System-API)) | Obtains the device serial number. This API uses a promise to return the result. |
| [getDisplayVersion](arkts-mdm-deviceinfo-getdisplayversion-f-sys.md#getDisplayVersion) | Obtains the device version number. This API uses an asynchronous callback to return the result. |
| [getDisplayVersion](arkts-mdm-deviceinfo-getdisplayversion-f-sys.md#getDisplayVersion-(System-API)) | Obtains the device version number. This API uses a promise to return the result. |
<!--DelEnd-->

