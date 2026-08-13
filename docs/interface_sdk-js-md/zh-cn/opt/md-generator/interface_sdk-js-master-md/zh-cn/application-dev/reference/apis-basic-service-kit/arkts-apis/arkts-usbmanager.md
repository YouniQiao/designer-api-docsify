# @ohos.usbManager

本模块主要提供管理USB设备的相关功能，包括主设备上查询USB设备列表、批量数据传输、控制命令传输、权限控制等；从设备上端口管理、功能切换及查询等。 > **使用说明** > > 凡是参数类型为[usbManager.USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md#USBDevicePipe)的接口,都需要执行如下操作： > **在使用接口前：** > 1. 调用[usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getDevices)获取设备列表。 > 2. 调用[usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestRight)获取请求权限。 > 3. 调用[usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectDevice)得到[usbManager.USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md#USBDevicePipe)作为参数。 > **在使用接口后：** > 调用[usbManager.closePipe](arkts-basicservices-usbmanager-closepipe-f.md#closePipe)关闭设备消息控制通道。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace usbManager--><!--Device-unnamed-declare namespace usbManager-End-->

**系统能力：** SystemCapability.USB.USBManager

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [addAccessoryRight](arkts-basicservices-usbmanager-addaccessoryright-f-sys.md#addAccessoryRight（系统接口）) |
| [addDeviceAccessRight](arkts-basicservices-usbmanager-adddeviceaccessright-f-sys.md#addDeviceAccessRight（系统接口）) |
| [getCurrentFunctions](arkts-basicservices-usbmanager-getcurrentfunctions-f-sys.md#getCurrentFunctions（系统接口）) |
| [getDeviceFunctions](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md#getDeviceFunctions（系统接口）) |
| [getDeviceFunctions](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md#getDeviceFunctions（系统接口）) |
| [getFunctionsFromString](arkts-basicservices-usbmanager-getfunctionsfromstring-f-sys.md#getFunctionsFromString（系统接口）) |
| [getPortList](arkts-basicservices-usbmanager-getportlist-f-sys.md#getPortList（系统接口）) |
| [getPortSupportModes](arkts-basicservices-usbmanager-getportsupportmodes-f-sys.md#getPortSupportModes（系统接口）) |
| [getPorts](arkts-basicservices-usbmanager-getports-f-sys.md#getPorts（系统接口）) |
| [getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md#getStringFromFunctions（系统接口）) |
| [getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md#getStringFromFunctions（系统接口）) |
| [getSupportedModes](arkts-basicservices-usbmanager-getsupportedmodes-f-sys.md#getSupportedModes（系统接口）) |
| [setCurrentFunctions](arkts-basicservices-usbmanager-setcurrentfunctions-f-sys.md#setCurrentFunctions（系统接口）) |
| [setDeviceFunctions](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md#setDeviceFunctions（系统接口）) |
| [setDeviceFunctions](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md#setDeviceFunctions（系统接口）) |
| [setPortRoleTypes](arkts-basicservices-usbmanager-setportroletypes-f-sys.md#setPortRoleTypes（系统接口）) |
| [setPortRoles](arkts-basicservices-usbmanager-setportroles-f-sys.md#setPortRoles（系统接口）) |
| [usbFunctionsFromString](arkts-basicservices-usbmanager-usbfunctionsfromstring-f-sys.md#usbFunctionsFromString（系统接口）) |
| [usbFunctionsToString](arkts-basicservices-usbmanager-usbfunctionstostring-f-sys.md#usbFunctionsToString（系统接口）) |
<!--DelEnd-->

### 接口

| 名称 |
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
### 接口（系统接口）

| 名称 |
| --- |
| [USBPort](arkts-basicservices-usbmanager-usbport-i-sys.md) |
| [USBPortStatus](arkts-basicservices-usbmanager-usbportstatus-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [USBControlRequestType](arkts-basicservices-usbmanager-usbcontrolrequesttype-e.md) |
| [USBRequestDirection](arkts-basicservices-usbmanager-usbrequestdirection-e.md) |
| [USBRequestTargetType](arkts-basicservices-usbmanager-usbrequesttargettype-e.md) |
| [UsbEndpointTransferType](arkts-basicservices-usbmanager-usbendpointtransfertype-e.md) |
| [UsbTransferFlags](arkts-basicservices-usbmanager-usbtransferflags-e.md) |
| [UsbTransferStatus](arkts-basicservices-usbmanager-usbtransferstatus-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [DataRoleType](arkts-basicservices-usbmanager-dataroletype-e-sys.md) |
| [FunctionType](arkts-basicservices-usbmanager-functiontype-e-sys.md) |
| [PortModeType](arkts-basicservices-usbmanager-portmodetype-e-sys.md) |
| [PowerRoleType](arkts-basicservices-usbmanager-powerroletype-e-sys.md) |
<!--DelEnd-->
