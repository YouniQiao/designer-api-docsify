# @ohos.usbManager

The **usbManager** module provides USB device management functions, including USB device list query, bulk data transfer, control transfer, and permission control on the host side as well as USB interface management, and function switch and query on the device side. > **NOTE：**> > Perform the following steps when using the APIs with the [usbManager.USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md#USBDevicePipe) parameter: > **Before use**: > 1. Call [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getDevices) to obtain the USB device list. > 2. Call [usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestRight) to request the temporary device access permission. > 3. Call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectDevice) to obtain [usbManager.USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md#USBDevicePipe) as an input parameter. > **After use**: > Call [usbManager.closePipe](arkts-basicservices-usbmanager-closepipe-f.md#closePipe) to close a USB device pipe. >

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace usbManager--><!--Device-unnamed-declare namespace usbManager-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usbManager } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [bulkTransfer](arkts-basicservices-usbmanager-bulktransfer-f.md#bulkTransfer) |
| [cancelAccessoryRight](arkts-basicservices-usbmanager-cancelaccessoryright-f.md#cancelAccessoryRight) |
| [claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md#claimInterface) |
| [closeAccessory](arkts-basicservices-usbmanager-closeaccessory-f.md#closeAccessory) |
| [closePipe](arkts-basicservices-usbmanager-closepipe-f.md#closePipe) |
| [connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectDevice) |
| [controlTransfer](arkts-basicservices-usbmanager-controltransfer-f.md#controlTransfer) |
| [getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md#getAccessoryList) |
| [getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getDevices) |
| [getFileDescriptor](arkts-basicservices-usbmanager-getfiledescriptor-f.md#getFileDescriptor) |
| [getRawDescriptor](arkts-basicservices-usbmanager-getrawdescriptor-f.md#getRawDescriptor) |
| [hasAccessoryRight](arkts-basicservices-usbmanager-hasaccessoryright-f.md#hasAccessoryRight) |
| [hasRight](arkts-basicservices-usbmanager-hasright-f.md#hasRight) |
| [openAccessory](arkts-basicservices-usbmanager-openaccessory-f.md#openAccessory) |
| [releaseInterface](arkts-basicservices-usbmanager-releaseinterface-f.md#releaseInterface) |
| [removeRight](arkts-basicservices-usbmanager-removeright-f.md#removeRight) |
| [requestAccessoryRight](arkts-basicservices-usbmanager-requestaccessoryright-f.md#requestAccessoryRight) |
| [requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestRight) |
| [resetUsbDevice](arkts-basicservices-usbmanager-resetusbdevice-f.md#resetUsbDevice) |
| [setConfiguration](arkts-basicservices-usbmanager-setconfiguration-f.md#setConfiguration) |
| [setInterface](arkts-basicservices-usbmanager-setinterface-f.md#setInterface) |
| [usbCancelTransfer](arkts-basicservices-usbmanager-usbcanceltransfer-f.md#usbCancelTransfer) |
| [usbControlTransfer](arkts-basicservices-usbmanager-usbcontroltransfer-f.md#usbControlTransfer) |
| [usbSubmitTransfer](arkts-basicservices-usbmanager-usbsubmittransfer-f.md#usbSubmitTransfer) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAccessoryRight](arkts-basicservices-usbmanager-addaccessoryright-f-sys.md#addAccessoryRight-(System-API)) |
| [addDeviceAccessRight](arkts-basicservices-usbmanager-adddeviceaccessright-f-sys.md#addDeviceAccessRight-(System-API)) |
| [getCurrentFunctions](arkts-basicservices-usbmanager-getcurrentfunctions-f-sys.md#getCurrentFunctions-(System-API)) |
| [getDeviceFunctions](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md#getDeviceFunctions-(System-API)) |
| [getDeviceFunctions](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md#getDeviceFunctions-(System-API)) |
| [getFunctionsFromString](arkts-basicservices-usbmanager-getfunctionsfromstring-f-sys.md#getFunctionsFromString-(System-API)) |
| [getPortList](arkts-basicservices-usbmanager-getportlist-f-sys.md#getPortList-(System-API)) |
| [getPortSupportModes](arkts-basicservices-usbmanager-getportsupportmodes-f-sys.md#getPortSupportModes-(System-API)) |
| [getPorts](arkts-basicservices-usbmanager-getports-f-sys.md#getPorts-(System-API)) |
| [getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md#getStringFromFunctions-(System-API)) |
| [getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md#getStringFromFunctions-(System-API)) |
| [getSupportedModes](arkts-basicservices-usbmanager-getsupportedmodes-f-sys.md#getSupportedModes-(System-API)) |
| [setCurrentFunctions](arkts-basicservices-usbmanager-setcurrentfunctions-f-sys.md#setCurrentFunctions-(System-API)) |
| [setDeviceFunctions](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md#setDeviceFunctions-(System-API)) |
| [setDeviceFunctions](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md#setDeviceFunctions-(System-API)) |
| [setPortRoleTypes](arkts-basicservices-usbmanager-setportroletypes-f-sys.md#setPortRoleTypes-(System-API)) |
| [setPortRoles](arkts-basicservices-usbmanager-setportroles-f-sys.md#setPortRoles-(System-API)) |
| [usbFunctionsFromString](arkts-basicservices-usbmanager-usbfunctionsfromstring-f-sys.md#usbFunctionsFromString-(System-API)) |
| [usbFunctionsToString](arkts-basicservices-usbmanager-usbfunctionstostring-f-sys.md#usbFunctionsToString-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [SubmitTransferCallback](arkts-basicservices-usbmanager-submittransfercallback-i.md) |
| [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) |
| [USBAccessoryHandle](arkts-basicservices-usbmanager-usbaccessoryhandle-i.md) |
| [USBConfiguration](arkts-basicservices-usbmanager-usbconfiguration-i.md) |
| [USBControlParams](arkts-basicservices-usbmanager-usbcontrolparams-i.md) |
| [USBDevice](arkts-basicservices-usbmanager-usbdevice-i.md) |
| [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) |
| [USBDeviceRequestParams](arkts-basicservices-usbmanager-usbdevicerequestparams-i.md) |
| [USBEndpoint](arkts-basicservices-usbmanager-usbendpoint-i.md) |
| [USBInterface](arkts-basicservices-usbmanager-usbinterface-i.md) |
| [UsbDataTransferParams](arkts-basicservices-usbmanager-usbdatatransferparams-i.md) |
| [UsbIsoPacketDescriptor](arkts-basicservices-usbmanager-usbisopacketdescriptor-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBPort](arkts-basicservices-usbmanager-usbport-i-sys.md) |
| [USBPortStatus](arkts-basicservices-usbmanager-usbportstatus-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBControlRequestType](arkts-basicservices-usbmanager-usbcontrolrequesttype-e.md) |
| [USBRequestDirection](arkts-basicservices-usbmanager-usbrequestdirection-e.md) |
| [USBRequestTargetType](arkts-basicservices-usbmanager-usbrequesttargettype-e.md) |
| [UsbEndpointTransferType](arkts-basicservices-usbmanager-usbendpointtransfertype-e.md) |
| [UsbTransferFlags](arkts-basicservices-usbmanager-usbtransferflags-e.md) |
| [UsbTransferStatus](arkts-basicservices-usbmanager-usbtransferstatus-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataRoleType](arkts-basicservices-usbmanager-dataroletype-e-sys.md) |
| [FunctionType](arkts-basicservices-usbmanager-functiontype-e-sys.md) |
| [PortModeType](arkts-basicservices-usbmanager-portmodetype-e-sys.md) |
| [PowerRoleType](arkts-basicservices-usbmanager-powerroletype-e-sys.md) |
<!--DelEnd-->
