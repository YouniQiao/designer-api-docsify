# @ohos.enterprise.usbManager(USB Management)

The **usbManager** module provides APIs for USB management.

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).&gt;
> The global restriction policy is provided by **restrictions**. To disable USB globally, see
> [@ohos.enterprise.restrictions (restriction policy)](arkts-enterprise-restrictions.md).

**Since:** 12

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAllowedUsbDevices(USB Management)](arkts-mdm-usbmanager-addallowedusbdevices-f.md) |
| [addDisallowedPermissiveUsbDevices(USB Management)](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md) |
| [addDisallowedUsbDevices(USB Management)](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md) |
| [getAllowedUsbDevices(USB Management)](arkts-mdm-usbmanager-getallowedusbdevices-f.md) |
| [getAllowedUsbDevices(USB Management)](arkts-mdm-usbmanager-getallowedusbdevices-f.md) |
| [getDisallowedPermissiveUsbDevices(USB Management)](arkts-mdm-usbmanager-getdisallowedpermissiveusbdevices-f.md) |
| [getDisallowedUsbDevices(USB Management)](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md) |
| [getDisallowedUsbDevices(USB Management)](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md) |
| [getUsbStorageDeviceAccessPolicy(USB Management)](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md) |
| [getUsbStorageDeviceAccessPolicy(USB Management)](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md) |
| [removeAllowedUsbDevices(USB Management)](arkts-mdm-usbmanager-removeallowedusbdevices-f.md) |
| [removeDisallowedPermissiveUsbDevices(USB Management)](arkts-mdm-usbmanager-removedisallowedpermissiveusbdevices-f.md) |
| [removeDisallowedUsbDevices(USB Management)](arkts-mdm-usbmanager-removedisallowedusbdevices-f.md) |
| [setUsbStorageDeviceAccessPolicy(USB Management)](arkts-mdm-usbmanager-setusbstoragedeviceaccesspolicy-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [disableUsb(USB Management)](arkts-mdm-usbmanager-disableusb-f-sys.md) |
| [isUsbDisabled(USB Management)](arkts-mdm-usbmanager-isusbdisabled-f-sys.md) |
| [setUsbPolicy(USB Management)](arkts-mdm-usbmanager-setusbpolicy-f-sys.md) |
| [setUsbPolicy(USB Management)](arkts-mdm-usbmanager-setusbpolicy-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [PermissiveUsbDeviceType(USB Management)](arkts-mdm-usbmanager-permissiveusbdevicetype-i.md) |
| [UsbDeviceId(USB Management)](arkts-mdm-usbmanager-usbdeviceid-i.md) |
| [UsbDeviceType(USB Management)](arkts-mdm-usbmanager-usbdevicetype-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Descriptor(USB Management)](arkts-mdm-usbmanager-descriptor-e.md) |
| [UsbPolicy(USB Management)](arkts-mdm-usbmanager-usbpolicy-e.md) |
