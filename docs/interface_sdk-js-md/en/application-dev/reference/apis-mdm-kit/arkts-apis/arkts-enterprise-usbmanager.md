# @ohos.enterprise.usbManager

The **usbManager** module provides APIs for USB management.

> **NOTE：**&gt;
> The APIs of this module can be called only by a device administrator application that is enabled. For details, see
> [MDM Kit Development](../../../mdm/mdm-kit-guide.md).&gt;
> The global restriction policy is provided by **restrictions**. To disable USB globally, see
> [@ohos.enterprise.restrictions (restriction policy)](arkts-enterprise-restrictions.md).

**Since:** 10

<!--Device-unnamed-declare namespace usbManager--><!--Device-unnamed-declare namespace usbManager-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { usbManager } from '@kit.MDMKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addAllowedUsbDevices](arkts-mdm-usbmanager-addallowedusbdevices-f.md) | Adds allowed USB devices.Use cases:  - Restrict access to only specific USB devices in enterprise security management scenarios. - Enable device administrators to precisely control which USB devices can be recognized and used. - Work with the [removeAllowedUsbDevices](arkts-mdm-usbmanager-removeallowedusbdevices-f.md) API to implement dynamic management of USB devices.  A policy conflict is reported when this API is called in the following scenarios: 1. The USB capability or the USB-to-serial capability of the device has been disabled via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md). 2. The USB storage device access policy has been disabled using the [setUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-setusbstoragedeviceaccesspolicy-f.md) API. 3. Disallowed USB device types have been added using the [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md) API. 4. Disallowed USB device types have been added via [addDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md). |
| [addDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md) | Adds disallowed USB device types. Unlike the [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md) API, this API does not require matching based on the [defined-class-codes](https://www.usb.org/defined-class-codes) standard. This API takes effect immediately on connected USB devices without requiring re-plugging. For example, if a USB wired headset is in normal use and this API is called to disable it, the headset will become unavailable immediately.A policy conflict is reported when this API is called in the following scenarios: 1. Disallowed USB device types have been added using the [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md) API. 2. The USB capability of the device has been disabled via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md). 3. The available USB devices have been added through [addAllowedUsbDevices](arkts-mdm-usbmanager-addallowedusbdevices-f.md). 4. The USB storage write capability has been disabled for specific users via [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md). |
| [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md) | Adds disallowed USB device types.Use cases:  - Disable specific types of USB devices in enterprise security management scenarios. - Prevent data leaks by disabling USB storage device types. - Enable device administrators to prohibit the use of certain USB device types based on security policies. - Work with the [removeDisallowedUsbDevices](arkts-mdm-usbmanager-removedisallowedusbdevices-f.md) API to implement dynamic management of USB device types. |
| [getAllowedUsbDevices](arkts-mdm-usbmanager-getallowedusbdevices-f.md) | Obtains allowed USB devices. |
| [getAllowedUsbDevices](arkts-mdm-usbmanager-getallowedusbdevices-f.md) | Obtains allowed USB devices.Use cases:  - Retrieve the existing policy for evaluation before making any modifications. - Display the current USB storage device access control status on the management page. |
| [getDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-getdisallowedpermissiveusbdevices-f.md) | Obtains the USB device types that have been disallowed via [addDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md). |
| [getDisallowedUsbDevices](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md) | Obtains the disallowed USB device types. |
| [getDisallowedUsbDevices](arkts-mdm-usbmanager-getdisallowedusbdevices-f.md) | Obtains the disallowed USB device types.Use cases:  - Retrieve the current list of disallowed USB device types for review by the device administrator. - Obtain the existing blocklist for comparison before making any modifications. - Display the current USB device type restriction policy configuration on the management page. |
| [getUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md) | Obtains the access policy of the USB storage device. |
| [getUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-getusbstoragedeviceaccesspolicy-f.md) | Obtains the USB storage device (baseClass = 0x08) access policy. |
| [removeAllowedUsbDevices](arkts-mdm-usbmanager-removeallowedusbdevices-f.md) | Removes allowed USB devices.Use cases:  - Revoke access permissions for certain USB devices in enterprise security management scenarios. - Enable device administrators to dynamically adjust the list of allowed USB devices. - Remove USB devices from the trustlist when they are no longer needed or pose a security risk. |
| [removeDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-removedisallowedpermissiveusbdevices-f.md) | Removes the USB device types that have been disallowed via [addDisallowedPermissiveUsbDevices](arkts-mdm-usbmanager-adddisallowedpermissiveusbdevices-f.md). The removed USB device types can be used normally. |
| [removeDisallowedUsbDevices](arkts-mdm-usbmanager-removedisallowedusbdevices-f.md) | Removes the disallowed USB device types.Use cases:  - Lifts the restriction on certain USB device types in enterprise security management scenarios. - Enable device administrators to dynamically adjust the list of disallowed USB device types. - Remove USB device types from the blocklist when they no longer pose a security risk. |
| [setUsbStorageDeviceAccessPolicy](arkts-mdm-usbmanager-setusbstoragedeviceaccesspolicy-f.md) | Sets the USB storage device (baseClass = 0x08) access policy. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [disableUsb](arkts-mdm-usbmanager-disableusb-f-sys.md) | Enables or disables USB. |
| [isUsbDisabled](arkts-mdm-usbmanager-isusbdisabled-f-sys.md) | Queries whether the USB is disabled. |
| [setUsbPolicy](arkts-mdm-usbmanager-setusbpolicy-f-sys.md) | Sets the USB read/write policy. This API uses an asynchronous callback to return the result. |
| [setUsbPolicy](arkts-mdm-usbmanager-setusbpolicy-f-sys.md) | Sets the USB read/write policy. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [PermissiveUsbDeviceType](arkts-mdm-usbmanager-permissiveusbdevicetype-i.md) | USB device type information. Partial field matching is supported.  - Compared with [UsbDeviceType](arkts-mdm-usbmanager-usbdevicetype-i.md), the **subClass**, **protocol**, and **descriptor** parameters in this API are optional, allowing for more flexible USB device disabling policies. - Only the matching based on the **baseClass** parameter is supported. - Multiple parameters can be configured. All parameters must be satisfied simultaneously for a match. - You can obtain the list of USB devices connected to the host device through the [getDevices](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-usbmanager-getdevices-f.md) API, and then find the type of the current device in the returned list. |
| [UsbDeviceId](arkts-mdm-usbmanager-usbdeviceid-i.md) | Represents the USB device identity information. |
| [UsbDeviceType](arkts-mdm-usbmanager-usbdevicetype-i.md) | Represents the USB device type information.You can obtain the list of USB devices connected to the host device through the [getDevices](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-usbmanager-getdevices-f.md) API, and then find the type of the current device in the returned list. |

### Enums

| Name | Description |
| --- | --- |
| [Descriptor](arkts-mdm-usbmanager-descriptor-e.md) | Enumerates USB descriptors. |
| [UsbPolicy](arkts-mdm-usbmanager-usbpolicy-e.md) | Enumerates the USB storage device access policies. |

