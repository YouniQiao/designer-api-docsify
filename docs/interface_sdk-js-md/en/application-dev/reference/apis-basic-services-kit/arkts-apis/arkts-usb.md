# @ohos.usb(USB Manager)

The **usb** module provides USB device management functions, including USB device list query, bulk data transfer, control transfer, and permission control.

> **NOTE：**
> 
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
import usb from '@kit.BasicServicesKit';
import usbManager from '@kit.BasicServicesKitManager';
import serialManager from '@kit.BasicServicesKitManager.serial';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [bulkTransfer(USB Manager)](arkts-basicservices-usb-bulktransfer-f.md) | Performs bulk transfer.Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md) to obtain the USB device list and endpoints, call [usb.requestRight](arkts-basicservices-usb-requestright-f.md) to request the device access permission, call [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md) to obtain **devicepipe** as an input parameter, and call [usb.claimInterface](arkts-basicservices-usb-claiminterface-f.md) to claim the USB interface. |
| [claimInterface(USB Manager)](arkts-basicservices-usb-claiminterface-f.md) | Claims a USB interface.Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md) to obtain the USB device list and USB interfaces, call [usb.requestRight](arkts-basicservices-usb-requestright-f.md) to request the device access permission, and call [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md) to obtain **devicepipe** as an input parameter. |
| [closePipe(USB Manager)](arkts-basicservices-usb-closepipe-f.md) | Closes a USB device pipe.Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md) to obtain the USB device list, call [usb.requestRight](arkts-basicservices-usb-requestright-f.md) to request the device access permission, and call [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md) to obtain **devicepipe** as an input parameter. |
| [connectDevice(USB Manager)](arkts-basicservices-usb-connectdevice-f.md) | Connects to a USB device.Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md) to obtain the USB device list, and then call [usb.requestRight](arkts-basicservices-usb-requestright-f.md) to request the device access permission. |
| [controlTransfer(USB Manager)](arkts-basicservices-usb-controltransfer-f.md) | Performs control transfer.Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md) to obtain the USB device list, call [usb.requestRight](arkts-basicservices-usb-requestright-f.md) to request the device access permission, and call [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md) to obtain **devicepipe** as an input parameter. |
| [getDevices(USB Manager)](arkts-basicservices-usb-getdevices-f.md) | Obtains the USB device list. |
| [getFileDescriptor(USB Manager)](arkts-basicservices-usb-getfiledescriptor-f.md) | Obtains the file descriptor.Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md) to obtain the USB device list, call [usb.requestRight](arkts-basicservices-usb-requestright-f.md) to request the device access permission, and call [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md) to obtain **devicepipe** as an input parameter. |
| [getRawDescriptor(USB Manager)](arkts-basicservices-usb-getrawdescriptor-f.md) | Obtains the raw USB descriptor.Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md) to obtain the USB device list, call [usb.requestRight](arkts-basicservices-usb-requestright-f.md) to request the device access permission, and call [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md) to obtain **devicepipe** as an input parameter. |
| [hasRight(USB Manager)](arkts-basicservices-usb-hasright-f.md) | Checks whether the application has the permission to access the device. |
| [releaseInterface(USB Manager)](arkts-basicservices-usb-releaseinterface-f.md) | Releases a USB interface.Before you do this, ensure that you have claimed the interface by calling [usb.claimInterface](arkts-basicservices-usb-claiminterface-f.md). |
| [requestRight(USB Manager)](arkts-basicservices-usb-requestright-f.md) | Requests the temporary permission for the application to access a USB device. This API uses a promise to return the result. System applications are granted the device access permission by default, and you do not need to apply for the permission separately. |
| [setConfiguration(USB Manager)](arkts-basicservices-usb-setconfiguration-f.md) | Sets the device configuration.Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md) to obtain the USB device list and device configuration, call [usb.requestRight](arkts-basicservices-usb-requestright-f.md) to request the device access permission, and call [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md) to obtain **devicepipe** as an input parameter. |
| [setInterface(USB Manager)](arkts-basicservices-usb-setinterface-f.md) | Sets a USB interface.Before you do this, call [usb.getDevices](arkts-basicservices-usb-getdevices-f.md) to obtain the USB device list and interfaces, call [usb.requestRight](arkts-basicservices-usb-requestright-f.md) to request the device access permission, call [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md) to obtain **devicepipe** as an input parameter, and call [usb.claimInterface](arkts-basicservices-usb-claiminterface-f.md) to claim the USB interface. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getCurrentFunctions(USB Manager)](arkts-basicservices-usb-getcurrentfunctions-f-sys.md) | Obtains the numeric mask combination for the USB function list in Device mode. |
| [getPorts(USB Manager)](arkts-basicservices-usb-getports-f-sys.md) | Obtains the list of all physical USB ports. |
| [getSupportedModes(USB Manager)](arkts-basicservices-usb-getsupportedmodes-f-sys.md) | Obtains the mask combination for the supported mode list of a given USB port. |
| [setCurrentFunctions(USB Manager)](arkts-basicservices-usb-setcurrentfunctions-f-sys.md) | Sets the current USB function list in Device mode. |
| [setPortRoles(USB Manager)](arkts-basicservices-usb-setportroles-f-sys.md) | Sets the role types supported by a specified port, which can be **powerRole** (for charging) and **dataRole** (for data transfer). |
| [usbFunctionsFromString(USB Manager)](arkts-basicservices-usb-usbfunctionsfromstring-f-sys.md) | Converts the USB function list in the string format to a numeric mask in Device mode. |
| [usbFunctionsToString(USB Manager)](arkts-basicservices-usb-usbfunctionstostring-f-sys.md) | Converts the USB function list in the numeric mask format to a string in Device mode. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [USBConfig(USB Manager)](arkts-basicservices-usb-usbconfig-i.md) | Represents the USB configuration. One [USBDevice](arkts-basicservices-usb-usbdevice-i.md) can contain multiple **USBConfig** instances. |
| [USBControlParams(USB Manager)](arkts-basicservices-usb-usbcontrolparams-i.md) | Represents control transfer parameters. |
| [USBDevice(USB Manager)](arkts-basicservices-usb-usbdevice-i.md) | Represents the USB device information. |
| [USBDevicePipe(USB Manager)](arkts-basicservices-usb-usbdevicepipe-i.md) | Represents a USB device pipe, which is used to determine a USB device. |
| [USBEndpoint(USB Manager)](arkts-basicservices-usb-usbendpoint-i.md) | Represents the USB endpoint from which data is sent or received. You can obtain the USB endpoint through [USBInterface](arkts-basicservices-usb-usbinterface-i.md). |
| [USBInterface(USB Manager)](arkts-basicservices-usb-usbinterface-i.md) | Represents a USB interface. One [USBConfig](arkts-basicservices-usb-usbconfig-i.md) can contain multiple **USBInterface** instances, each providing a specific function. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [USBPort(USB Manager)](arkts-basicservices-usb-usbport-i-sys.md) | Represents a USB port. |
| [USBPortStatus(USB Manager)](arkts-basicservices-usb-usbportstatus-i-sys.md) | Enumerates USB port roles. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [USBControlRequestType(USB Manager)](arkts-basicservices-usb-usbcontrolrequesttype-e.md) | Enumerates control request types. |
| [USBRequestDirection(USB Manager)](arkts-basicservices-usb-usbrequestdirection-e.md) | Enumerates request directions. |
| [USBRequestTargetType(USB Manager)](arkts-basicservices-usb-usbrequesttargettype-e.md) | Enumerates request target types. |

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [DataRoleType(USB Manager)](arkts-basicservices-usb-dataroletype-e-sys.md) | Enumerates data role types. |
| [FunctionType(USB Manager)](arkts-basicservices-usb-functiontype-e-sys.md) | Enumerates USB device function types. |
| [PortModeType(USB Manager)](arkts-basicservices-usb-portmodetype-e-sys.md) | Enumerates USB port mode types. |
| [PowerRoleType(USB Manager)](arkts-basicservices-usb-powerroletype-e-sys.md) | Enumerates power role types. |
<!--DelEnd-->
