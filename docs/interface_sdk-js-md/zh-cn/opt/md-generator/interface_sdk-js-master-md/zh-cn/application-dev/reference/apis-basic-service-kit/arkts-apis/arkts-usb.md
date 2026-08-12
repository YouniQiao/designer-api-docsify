# @ohos.usb(USB Manager)

本模块主要提供管理USB设备的相关功能，包括查询USB设备列表、批量数据传输、控制命令传输、权限控制等。

> **说明：**
> 
> 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> 从API version 9开始，该接口不再维护，推荐使用新接口[@ohos.usbManager](arkts-usbmanager.md#usbManager)。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [usbManager](arkts-usbmanager.md#usbManager)

<!--Device-unnamed-declare namespace usb--><!--Device-unnamed-declare namespace usb-End-->

**系统能力：** SystemCapability.USB.USBManager

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [getCurrentFunctions](arkts-basicservices-usb-getcurrentfunctions-f-sys.md#getcurrentfunctions) |
| [getPorts](arkts-basicservices-usb-getports-f-sys.md#getports) |
| [getSupportedModes](arkts-basicservices-usb-getsupportedmodes-f-sys.md#getsupportedmodes) |
| [setCurrentFunctions](arkts-basicservices-usb-setcurrentfunctions-f-sys.md#setcurrentfunctions) |
| [setPortRoles](arkts-basicservices-usb-setportroles-f-sys.md#setportroles) |
| [usbFunctionsFromString](arkts-basicservices-usb-usbfunctionsfromstring-f-sys.md#usbfunctionsfromstring) |
| [usbFunctionsToString](arkts-basicservices-usb-usbfunctionstostring-f-sys.md#usbfunctionstostring) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [USBConfig](arkts-basicservices-usb-usbconfig-i.md) |
| [USBControlParams](arkts-basicservices-usb-usbcontrolparams-i.md) |
| [USBDevice](arkts-basicservices-usb-usbdevice-i.md) |
| [USBDevicePipe](arkts-basicservices-usb-usbdevicepipe-i.md) |
| [USBEndpoint](arkts-basicservices-usb-usbendpoint-i.md) |
| [USBInterface](arkts-basicservices-usb-usbinterface-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [USBPort](arkts-basicservices-usb-usbport-i-sys.md) |
| [USBPortStatus](arkts-basicservices-usb-usbportstatus-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [USBControlRequestType](arkts-basicservices-usb-usbcontrolrequesttype-e.md) |
| [USBRequestDirection](arkts-basicservices-usb-usbrequestdirection-e.md) |
| [USBRequestTargetType](arkts-basicservices-usb-usbrequesttargettype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [DataRoleType](arkts-basicservices-usb-dataroletype-e-sys.md) |
| [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) |
| [PortModeType](arkts-basicservices-usb-portmodetype-e-sys.md) |
| [PowerRoleType](arkts-basicservices-usb-powerroletype-e-sys.md) |
<!--DelEnd-->
