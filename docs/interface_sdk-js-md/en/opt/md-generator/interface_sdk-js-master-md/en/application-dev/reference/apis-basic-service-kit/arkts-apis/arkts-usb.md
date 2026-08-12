# @ohos.usb(USB Manager)

The **usb** module provides USB device management functions, including USB device list query, bulk data transfer,control transfer, and permission control.

> **NOTE：**
> 
> The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with
> a superscript to indicate their earliest API version.
> The APIs provided by this module are no longer maintained since API version 9. You are advised to use
> [@ohos.usbManager](arkts-usbmanager.md#usbManager).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [usbManager](arkts-usbmanager.md#usbManager)

<!--Device-unnamed-declare namespace usb--><!--Device-unnamed-declare namespace usb-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usb } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [bulkTransfer](arkts-basicservices-usb-bulktransfer-f.md#bulktransfer) |
| [claimInterface](arkts-basicservices-usb-claiminterface-f.md#claiminterface) |
| [closePipe](arkts-basicservices-usb-closepipe-f.md#closepipe) |
| [connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectdevice) |
| [controlTransfer](arkts-basicservices-usb-controltransfer-f.md#controltransfer) |
| [getDevices](arkts-basicservices-usb-getdevices-f.md#getdevices) |
| [getFileDescriptor](arkts-basicservices-usb-getfiledescriptor-f.md#getfiledescriptor) |
| [getRawDescriptor](arkts-basicservices-usb-getrawdescriptor-f.md#getrawdescriptor) |
| [hasRight](arkts-basicservices-usb-hasright-f.md#hasright) |
| [releaseInterface](arkts-basicservices-usb-releaseinterface-f.md#releaseinterface) |
| [requestRight](arkts-basicservices-usb-requestright-f.md#requestright) |
| [setConfiguration](arkts-basicservices-usb-setconfiguration-f.md#setconfiguration) |
| [setInterface](arkts-basicservices-usb-setinterface-f.md#setinterface) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getCurrentFunctions](arkts-basicservices-usb-getcurrentfunctions-f-sys.md#getcurrentfunctions) |
| [getPorts](arkts-basicservices-usb-getports-f-sys.md#getports) |
| [getSupportedModes](arkts-basicservices-usb-getsupportedmodes-f-sys.md#getsupportedmodes) |
| [setCurrentFunctions](arkts-basicservices-usb-setcurrentfunctions-f-sys.md#setcurrentfunctions) |
| [setPortRoles](arkts-basicservices-usb-setportroles-f-sys.md#setportroles) |
| [usbFunctionsFromString](arkts-basicservices-usb-usbfunctionsfromstring-f-sys.md#usbfunctionsfromstring) |
| [usbFunctionsToString](arkts-basicservices-usb-usbfunctionstostring-f-sys.md#usbfunctionstostring) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBConfig](arkts-basicservices-usb-usbconfig-i.md) |
| [USBControlParams](arkts-basicservices-usb-usbcontrolparams-i.md) |
| [USBDevice](arkts-basicservices-usb-usbdevice-i.md) |
| [USBDevicePipe](arkts-basicservices-usb-usbdevicepipe-i.md) |
| [USBEndpoint](arkts-basicservices-usb-usbendpoint-i.md) |
| [USBInterface](arkts-basicservices-usb-usbinterface-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBPort](arkts-basicservices-usb-usbport-i-sys.md) |
| [USBPortStatus](arkts-basicservices-usb-usbportstatus-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBControlRequestType](arkts-basicservices-usb-usbcontrolrequesttype-e.md) |
| [USBRequestDirection](arkts-basicservices-usb-usbrequestdirection-e.md) |
| [USBRequestTargetType](arkts-basicservices-usb-usbrequesttargettype-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataRoleType](arkts-basicservices-usb-dataroletype-e-sys.md) |
| [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) |
| [PortModeType](arkts-basicservices-usb-portmodetype-e-sys.md) |
| [PowerRoleType](arkts-basicservices-usb-powerroletype-e-sys.md) |
<!--DelEnd-->
