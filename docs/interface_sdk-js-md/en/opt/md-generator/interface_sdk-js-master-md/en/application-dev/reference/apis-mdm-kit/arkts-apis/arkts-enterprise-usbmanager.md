# @ohos.enterprise.usbManager

The **usbManager** module provides APIs for USB management. > **NOTE：**> > The APIs of this module can be called only by a device administrator application that is enabled. For details, see > [MDM Kit Development](../../../mdm/mdm-kit-guide.md). > > The global restriction policy is provided by **restrictions**. To disable USB globally, see > [@ohos.enterprise.restrictions (restriction policy)](arkts-enterprise-restrictions.md#@ohos.enterprise.restrictions).

**Since:** 10

**Deprecated since:** -1

<!--Device-unnamed-declare namespace usbManager--><!--Device-unnamed-declare namespace usbManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { usbManager } from '@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedUsbDevices](arkts-mdm-usbmanager-addallowedusbdevices-f.md#addAllowedUsbDevices) |
| [addDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md#addDisallowedPermissiveUsbDevices) |
| [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md#addDisallowedUsbDevices) |
| [getAllowedUsbDevices](arkts-mdm-usbmanager-getallowedusbdevices-f.md#getAllowedUsbDevices) |
| [getAllowedUsbDevices](arkts-mdm-usbmanager-getallowedusbdevices-f.md#getAllowedUsbDevices) |
| [getDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-getdisallowedpermissiveusbdevices-f.md#getDisallowedPermissiveUsbDevices) |
| [getDisallowedUsbDevices](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md#getDisallowedUsbDevices) |
| [getDisallowedUsbDevices](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md#getDisallowedUsbDevices) |
| [getUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md#getUsbStorageDeviceAccessPolicy) |
| [getUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md#getUsbStorageDeviceAccessPolicy) |
| [removeAllowedUsbDevices](arkts-mdm-usbmanager-removeallowedusbdevices-f.md#removeAllowedUsbDevices) |
| [removeDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-removedisallowedpermissiveusbdevices-f.md#removeDisallowedPermissiveUsbDevices) |
| [removeDisallowedUsbDevices](arkts-mdm-usbmanager-removedisallowedusbdevices-f.md#removeDisallowedUsbDevices) |
| [setUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-setusbstoragedeviceaccesspolicy-f.md#setUsbStorageDeviceAccessPolicy) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [disableUsb](arkts-mdm-usbmanager-disableusb-f-sys.md#disableUsb-(System-API)) |
| [isUsbDisabled](arkts-mdm-usbmanager-isusbdisabled-f-sys.md#isUsbDisabled-(System-API)) |
| [setUsbPolicy](arkts-mdm-usbmanager-setusbpolicy-f-sys.md#setUsbPolicy-(System-API)) |
| [setUsbPolicy](arkts-mdm-usbmanager-setusbpolicy-f-sys.md#setUsbPolicy-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PermissiveUsbDeviceType](arkts-mdm-usbmanager-permissiveusbdevicetype-i.md) |
| [UsbDeviceId](arkts-mdm-usbmanager-usbdeviceid-i.md) |
| [UsbDeviceType](arkts-mdm-usbmanager-usbdevicetype-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Descriptor](arkts-mdm-usbmanager-descriptor-e.md) |
| [UsbPolicy](arkts-mdm-usbmanager-usbpolicy-e.md) |
