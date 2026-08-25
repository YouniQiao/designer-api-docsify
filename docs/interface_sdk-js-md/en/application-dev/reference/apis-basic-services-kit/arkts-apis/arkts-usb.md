# @ohos.usb(USB Manager)

The **usb** module provides USB device management functions, including USB device list query, bulk data transfer, control transfer, and permission control.

> **NOTE：**&gt;
> The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with
> a superscript to indicate their earliest API version.
> The APIs provided by this module are no longer maintained since API version 9. You are advised to use
> [@ohos.usbManager](arkts-usbmanager.md).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [usbManager](arkts-usbmanager.md)

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [bulkTransfer(USB Manager)](arkts-basicservices-usb-bulktransfer-f.md) |
| [claimInterface(USB Manager)](arkts-basicservices-usb-claiminterface-f.md) |
| [closePipe(USB Manager)](arkts-basicservices-usb-closepipe-f.md) |
| [connectDevice(USB Manager)](arkts-basicservices-usb-connectdevice-f.md) |
| [controlTransfer(USB Manager)](arkts-basicservices-usb-controltransfer-f.md) |
| [getDevices(USB Manager)](arkts-basicservices-usb-getdevices-f.md) |
| [getFileDescriptor(USB Manager)](arkts-basicservices-usb-getfiledescriptor-f.md) |
| [getRawDescriptor(USB Manager)](arkts-basicservices-usb-getrawdescriptor-f.md) |
| [hasRight(USB Manager)](arkts-basicservices-usb-hasright-f.md) |
| [releaseInterface(USB Manager)](arkts-basicservices-usb-releaseinterface-f.md) |
| [requestRight(USB Manager)](arkts-basicservices-usb-requestright-f.md) |
| [setConfiguration(USB Manager)](arkts-basicservices-usb-setconfiguration-f.md) |
| [setInterface(USB Manager)](arkts-basicservices-usb-setinterface-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getCurrentFunctions(USB Manager)](arkts-basicservices-usb-getcurrentfunctions-f-sys.md) |
| [getPorts(USB Manager)](arkts-basicservices-usb-getports-f-sys.md) |
| [getSupportedModes(USB Manager)](arkts-basicservices-usb-getsupportedmodes-f-sys.md) |
| [setCurrentFunctions(USB Manager)](arkts-basicservices-usb-setcurrentfunctions-f-sys.md) |
| [setPortRoles(USB Manager)](arkts-basicservices-usb-setportroles-f-sys.md) |
| [usbFunctionsFromString(USB Manager)](arkts-basicservices-usb-usbfunctionsfromstring-f-sys.md) |
| [usbFunctionsToString(USB Manager)](arkts-basicservices-usb-usbfunctionstostring-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBConfig(USB Manager)](arkts-basicservices-usb-usbconfig-i.md) |
| [USBControlParams(USB Manager)](arkts-basicservices-usb-usbcontrolparams-i.md) |
| [USBDevice(USB Manager)](arkts-basicservices-usb-usbdevice-i.md) |
| [USBDevicePipe(USB Manager)](arkts-basicservices-usb-usbdevicepipe-i.md) |
| [USBEndpoint(USB Manager)](arkts-basicservices-usb-usbendpoint-i.md) |
| [USBInterface(USB Manager)](arkts-basicservices-usb-usbinterface-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBPort(USB Manager)](arkts-basicservices-usb-usbport-i-sys.md) |
| [USBPortStatus(USB Manager)](arkts-basicservices-usb-usbportstatus-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBControlRequestType(USB Manager)](arkts-basicservices-usb-usbcontrolrequesttype-e.md) |
| [USBRequestDirection(USB Manager)](arkts-basicservices-usb-usbrequestdirection-e.md) |
| [USBRequestTargetType(USB Manager)](arkts-basicservices-usb-usbrequesttargettype-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataRoleType(USB Manager)](arkts-basicservices-usb-dataroletype-e-sys.md) |
| [FunctionType(USB Manager)](arkts-basicservices-usb-functiontype-e-sys.md) |
| [PortModeType(USB Manager)](arkts-basicservices-usb-portmodetype-e-sys.md) |
| [PowerRoleType(USB Manager)](arkts-basicservices-usb-powerroletype-e-sys.md) |
<!--DelEnd-->
