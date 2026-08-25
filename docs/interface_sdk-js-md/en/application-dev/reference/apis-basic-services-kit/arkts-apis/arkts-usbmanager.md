# @ohos.usbManager

The **usbManager** module provides USB device management functions, including USB device list query, bulk data transfer, control transfer, and permission control on the host side as well as USB interface management, and function switch and query on the device side.

> **NOTE：**&gt;
> Perform the following steps when using the APIs with the [usbManager.USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) parameter:
> **Before use**:
> 1. Call [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md) to obtain the USB device list.
> 2. Call [usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md) to request the temporary device access permission.
> 3. Call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md) to obtain [usbManager.USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) as an input parameter.
> **After use**:
> Call [usbManager.closePipe](arkts-basicservices-usbmanager-closepipe-f.md) to close a USB device pipe.&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [bulkTransfer](arkts-basicservices-usbmanager-bulktransfer-f.md) |
| [cancelAccessoryRight](arkts-basicservices-usbmanager-cancelaccessoryright-f.md) |
| [claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md) |
| [closeAccessory](arkts-basicservices-usbmanager-closeaccessory-f.md) |
| [closePipe](arkts-basicservices-usbmanager-closepipe-f.md) |
| [connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md) |
| [controlTransfer](arkts-basicservices-usbmanager-controltransfer-f.md) |
| [getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md) |
| [getDevices](arkts-basicservices-usbmanager-getdevices-f.md) |
| [getFileDescriptor](arkts-basicservices-usbmanager-getfiledescriptor-f.md) |
| [getRawDescriptor](arkts-basicservices-usbmanager-getrawdescriptor-f.md) |
| [hasAccessoryRight](arkts-basicservices-usbmanager-hasaccessoryright-f.md) |
| [hasRight](arkts-basicservices-usbmanager-hasright-f.md) |
| [openAccessory](arkts-basicservices-usbmanager-openaccessory-f.md) |
| [releaseInterface](arkts-basicservices-usbmanager-releaseinterface-f.md) |
| [removeRight](arkts-basicservices-usbmanager-removeright-f.md) |
| [requestAccessoryRight](arkts-basicservices-usbmanager-requestaccessoryright-f.md) |
| [requestRight](arkts-basicservices-usbmanager-requestright-f.md) |
| [resetUsbDevice](arkts-basicservices-usbmanager-resetusbdevice-f.md) |
| [setConfiguration](arkts-basicservices-usbmanager-setconfiguration-f.md) |
| [setInterface](arkts-basicservices-usbmanager-setinterface-f.md) |
| [usbCancelTransfer](arkts-basicservices-usbmanager-usbcanceltransfer-f.md) |
| [usbControlTransfer](arkts-basicservices-usbmanager-usbcontroltransfer-f.md) |
| [usbSubmitTransfer](arkts-basicservices-usbmanager-usbsubmittransfer-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAccessoryRight](arkts-basicservices-usbmanager-addaccessoryright-f-sys.md) |
| [addDeviceAccessRight](arkts-basicservices-usbmanager-adddeviceaccessright-f-sys.md) |
| [getCurrentFunctions](arkts-basicservices-usbmanager-getcurrentfunctions-f-sys.md) |
| [getDeviceFunctions](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md) |
| [getDeviceFunctions](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md) |
| [getFunctionsFromString](arkts-basicservices-usbmanager-getfunctionsfromstring-f-sys.md) |
| [getPortList](arkts-basicservices-usbmanager-getportlist-f-sys.md) |
| [getPorts](arkts-basicservices-usbmanager-getports-f-sys.md) |
| [getPortSupportModes](arkts-basicservices-usbmanager-getportsupportmodes-f-sys.md) |
| [getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md) |
| [getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md) |
| [getSupportedModes](arkts-basicservices-usbmanager-getsupportedmodes-f-sys.md) |
| [setCurrentFunctions](arkts-basicservices-usbmanager-setcurrentfunctions-f-sys.md) |
| [setDeviceFunctions](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md) |
| [setDeviceFunctions](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md) |
| [setPortRoles](arkts-basicservices-usbmanager-setportroles-f-sys.md) |
| [setPortRoleTypes](arkts-basicservices-usbmanager-setportroletypes-f-sys.md) |
| [usbFunctionsFromString](arkts-basicservices-usbmanager-usbfunctionsfromstring-f-sys.md) |
| [usbFunctionsToString](arkts-basicservices-usbmanager-usbfunctionstostring-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SubmitTransferCallback](arkts-basicservices-usbmanager-submittransfercallback-i.md) |
| [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) |
| [USBAccessoryHandle](arkts-basicservices-usbmanager-usbaccessoryhandle-i.md) |
| [USBConfiguration](arkts-basicservices-usbmanager-usbconfiguration-i.md) |
| [USBControlParams](arkts-basicservices-usbmanager-usbcontrolparams-i.md) |
| [UsbDataTransferParams](arkts-basicservices-usbmanager-usbdatatransferparams-i.md) |
| [USBDevice](arkts-basicservices-usbmanager-usbdevice-i.md) |
| [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) |
| [USBDeviceRequestParams](arkts-basicservices-usbmanager-usbdevicerequestparams-i.md) |
| [USBEndpoint](arkts-basicservices-usbmanager-usbendpoint-i.md) |
| [USBInterface](arkts-basicservices-usbmanager-usbinterface-i.md) |
| [UsbIsoPacketDescriptor](arkts-basicservices-usbmanager-usbisopacketdescriptor-i.md) |

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBPort](arkts-basicservices-usbmanager-usbport-i-sys.md) |
| [USBPortStatus](arkts-basicservices-usbmanager-usbportstatus-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBControlRequestType](arkts-basicservices-usbmanager-usbcontrolrequesttype-e.md) |
| [UsbEndpointTransferType](arkts-basicservices-usbmanager-usbendpointtransfertype-e.md) |
| [USBRequestDirection](arkts-basicservices-usbmanager-usbrequestdirection-e.md) |
| [USBRequestTargetType](arkts-basicservices-usbmanager-usbrequesttargettype-e.md) |
| [UsbTransferFlags](arkts-basicservices-usbmanager-usbtransferflags-e.md) |
| [UsbTransferStatus](arkts-basicservices-usbmanager-usbtransferstatus-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataRoleType](arkts-basicservices-usbmanager-dataroletype-e-sys.md) |
| [FunctionType](arkts-basicservices-usbmanager-functiontype-e-sys.md) |
| [PortModeType](arkts-basicservices-usbmanager-portmodetype-e-sys.md) |
| [PowerRoleType](arkts-basicservices-usbmanager-powerroletype-e-sys.md) |
<!--DelEnd-->
