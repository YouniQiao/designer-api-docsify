# @ohos.usbManager

本模块主要提供管理USB设备的相关功能，包括主机端的查询USB设备列表、批量数据传输、控制命令传输、权限控制等；设备端的端口管理、功能切换及查询等。适用于需要与USB设备进行数据交互、管理USB设备权限、动态切换USB设备模式等场景。

## 使用说明 凡是参数类型为[USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md#usbdevicepipe)的接口，都需要执行如下操作： **在使用接口前：** 1. 调用[usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md#getdevices)获取设备列表。 2. 调用[usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md#requestright)获取请求权限。 3. 调用[usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectdevice)得到USBDevicePipe作为参数。 **在使用接口后：** 调用[usbManager.closePipe](arkts-basicservices-usbmanager-closepipe-f.md#closepipe)关闭设备连接通道。 

**起始版本：** 23

<!--Device-unnamed-declare namespace usbManager--><!--Device-unnamed-declare namespace usbManager-End-->

**系统能力：** SystemCapability.USB.USBManager

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [addAccessoryRight](arkts-basicservices-usbmanager-addaccessoryright-f-sys.md#addaccessoryright系统接口) |
| [addDeviceAccessRight](arkts-basicservices-usbmanager-adddeviceaccessright-f-sys.md#adddeviceaccessright系统接口) |
| [getCurrentFunctions](arkts-basicservices-usbmanager-getcurrentfunctions-f-sys.md#getcurrentfunctions系统接口) |
| [getDeviceFunctions](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md#getdevicefunctions系统接口) |
| [getDeviceFunctions](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md#getdevicefunctions系统接口) |
| [getFunctionsFromString](arkts-basicservices-usbmanager-getfunctionsfromstring-f-sys.md#getfunctionsfromstring系统接口) |
| [getPortList](arkts-basicservices-usbmanager-getportlist-f-sys.md#getportlist系统接口) |
| [getPortSupportModes](arkts-basicservices-usbmanager-getportsupportmodes-f-sys.md#getportsupportmodes系统接口) |
| [getPorts](arkts-basicservices-usbmanager-getports-f-sys.md#getports系统接口) |
| [getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md#getstringfromfunctions系统接口) |
| [getStringFromFunctions](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md#getstringfromfunctions系统接口) |
| [getSupportedModes](arkts-basicservices-usbmanager-getsupportedmodes-f-sys.md#getsupportedmodes系统接口) |
| [setCurrentFunctions](arkts-basicservices-usbmanager-setcurrentfunctions-f-sys.md#setcurrentfunctions系统接口) |
| [setDeviceFunctions](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md#setdevicefunctions系统接口) |
| [setDeviceFunctions](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md#setdevicefunctions系统接口) |
| [setPortRoleTypes](arkts-basicservices-usbmanager-setportroletypes-f-sys.md#setportroletypes系统接口) |
| [setPortRoles](arkts-basicservices-usbmanager-setportroles-f-sys.md#setportroles系统接口) |
| [usbFunctionsFromString](arkts-basicservices-usbmanager-usbfunctionsfromstring-f-sys.md#usbfunctionsfromstring系统接口) |
| [usbFunctionsToString](arkts-basicservices-usbmanager-usbfunctionstostring-f-sys.md#usbfunctionstostring系统接口) |
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
