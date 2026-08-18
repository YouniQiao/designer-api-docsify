# @ohos.usbManager

The **usbManager** module provides USB device management functions, including USB device list query, bulk data transfer, control transfer, and permission control on the host side as well as USB interface management, and function switch and query on the device side. > **NOTE：**> > Perform the following steps when using the APIs with the [usbManager.USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md#usbdevicepipe) parameter: > **Before use**: > 1. Call [usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getdevices) to obtain the USB device list. > 2. Call [usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestright) to request the temporary device access permission. > 3. Call [usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectdevice) to obtain [usbManager.USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md#usbdevicepipe) as an input parameter. > **After use**: > Call [usbManager.closePipe](arkts-basicservices-usbmanager-closepipe-f.md#closepipe) to close a USB device pipe. >

**Since:** 23

<!--Device-unnamed-declare namespace usbManager--><!--Device-unnamed-declare namespace usbManager-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [bulkTransfer](arkts-basicservices-usbmanager-bulktransfer-f.md#bulktransfer) |
| [cancelAccessoryRight](arkts-basicservices-usbmanager-cancelaccessoryright-f.md#cancelaccessoryright) |
| [claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md#claiminterface) |
| [closeAccessory](arkts-basicservices-usbmanager-closeaccessory-f.md#closeaccessory) |
| [closePipe](arkts-basicservices-usbmanager-closepipe-f.md#closepipe) |
| [connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectdevice) |
| [controlTransfer](arkts-basicservices-usbmanager-controltransfer-f.md#controltransfer) |
| [getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md#getaccessorylist) |
| [getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getdevices) |
| [getFileDescriptor](arkts-basicservices-usbmanager-getfiledescriptor-f.md#getfiledescriptor) |
| [getRawDescriptor](arkts-basicservices-usbmanager-getrawdescriptor-f.md#getrawdescriptor) |
| [hasAccessoryRight](arkts-basicservices-usbmanager-hasaccessoryright-f.md#hasaccessoryright) |
| [hasRight](arkts-basicservices-usbmanager-hasright-f.md#hasright) |
| [openAccessory](arkts-basicservices-usbmanager-openaccessory-f.md#openaccessory) |
| [releaseInterface](arkts-basicservices-usbmanager-releaseinterface-f.md#releaseinterface) |
| [removeRight](arkts-basicservices-usbmanager-removeright-f.md#removeright) |
| [requestAccessoryRight](arkts-basicservices-usbmanager-requestaccessoryright-f.md#requestaccessoryright) |
| [requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestright) |
| [resetUsbDevice](arkts-basicservices-usbmanager-resetusbdevice-f.md#resetusbdevice) |
| [setConfiguration](arkts-basicservices-usbmanager-setconfiguration-f.md#setconfiguration) |
| [setInterface](arkts-basicservices-usbmanager-setinterface-f.md#setinterface) |
| [usbCancelTransfer](arkts-basicservices-usbmanager-usbcanceltransfer-f.md#usbcanceltransfer) |
| [usbControlTransfer](arkts-basicservices-usbmanager-usbcontroltransfer-f.md#usbcontroltransfer) |
| [usbSubmitTransfer](arkts-basicservices-usbmanager-usbsubmittransfer-f.md#usbsubmittransfer) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addAccessoryRight](arkts-basicservices-usbmanager-addaccessoryright-f-sys.md#addaccessoryright-system-api) |
| [addDeviceAccessRight](arkts-basicservices-usbmanager-adddeviceaccessright-f-sys.md#adddeviceaccessright-system-api) |
| [getCurrentFunctions](arkts-basicservices-usbmanager-getcurrentfunctions-f-sys.md#getcurrentfunctions-system-api) |
| [getDeviceFunctions](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md#getdevicefunctions-system-api) |
| [getDeviceFunctions](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md#getdevicefunctions-system-api) |
| [getFunctionsFromString](arkts-basicservices-usbmanager-getfunctionsfromstring-f-sys.md#getfunctionsfromstring-system-api) |
| [getPortList](arkts-basicservices-usbmanager-getportlist-f-sys.md#getportlist-system-api) |
| [getPortSupportModes](arkts-basicservices-usbmanager-getportsupportmodes-f-sys.md#getportsupportmodes-system-api) |
| [getPorts](arkts-basicservices-usbmanager-getports-f-sys.md#getports-system-api) |
| [getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md#getstringfromfunctions-system-api) |
| [getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md#getstringfromfunctions-system-api) |
| [getSupportedModes](arkts-basicservices-usbmanager-getsupportedmodes-f-sys.md#getsupportedmodes-system-api) |
| [setCurrentFunctions](arkts-basicservices-usbmanager-setcurrentfunctions-f-sys.md#setcurrentfunctions-system-api) |
| [setDeviceFunctions](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md#setdevicefunctions-system-api) |
| [setDeviceFunctions](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md#setdevicefunctions-system-api) |
| [setPortRoleTypes](arkts-basicservices-usbmanager-setportroletypes-f-sys.md#setportroletypes-system-api) |
| [setPortRoles](arkts-basicservices-usbmanager-setportroles-f-sys.md#setportroles-system-api) |
| [usbFunctionsFromString](arkts-basicservices-usbmanager-usbfunctionsfromstring-f-sys.md#usbfunctionsfromstring-system-api) |
| [usbFunctionsToString](arkts-basicservices-usbmanager-usbfunctionstostring-f-sys.md#usbfunctionstostring-system-api) |
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
