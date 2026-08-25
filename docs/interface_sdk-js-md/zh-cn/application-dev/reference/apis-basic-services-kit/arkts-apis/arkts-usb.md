# @ohos.usb(USB Manager)

本模块主要提供管理USB设备的相关功能，包括查询USB设备列表、批量数据传输、控制命令传输、权限控制等。

> **说明：**&gt;
> 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> 从API version 9开始，该接口不再维护，推荐使用新接口[@ohos.usbManager](arkts-usbmanager.md)。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [usbManager](arkts-usbmanager.md)

**系统能力：** SystemCapability.USB.USBManager

## 导入模块

```TypeScript
import { usb } from '@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [getCurrentFunctions(USB Manager)](arkts-basicservices-usb-getcurrentfunctions-f-sys.md) |
| [getPorts(USB Manager)](arkts-basicservices-usb-getports-f-sys.md) |
| [getSupportedModes(USB Manager)](arkts-basicservices-usb-getsupportedmodes-f-sys.md) |
| [setCurrentFunctions(USB Manager)](arkts-basicservices-usb-setcurrentfunctions-f-sys.md) |
| [setPortRoles(USB Manager)](arkts-basicservices-usb-setportroles-f-sys.md) |
| [usbFunctionsFromString(USB Manager)](arkts-basicservices-usb-usbfunctionsfromstring-f-sys.md) |
| [usbFunctionsToString(USB Manager)](arkts-basicservices-usb-usbfunctionstostring-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [USBConfig(USB Manager)](arkts-basicservices-usb-usbconfig-i.md) |
| [USBControlParams(USB Manager)](arkts-basicservices-usb-usbcontrolparams-i.md) |
| [USBDevice(USB Manager)](arkts-basicservices-usb-usbdevice-i.md) |
| [USBDevicePipe(USB Manager)](arkts-basicservices-usb-usbdevicepipe-i.md) |
| [USBEndpoint(USB Manager)](arkts-basicservices-usb-usbendpoint-i.md) |
| [USBInterface(USB Manager)](arkts-basicservices-usb-usbinterface-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [USBPort(USB Manager)](arkts-basicservices-usb-usbport-i-sys.md) |
| [USBPortStatus(USB Manager)](arkts-basicservices-usb-usbportstatus-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [USBControlRequestType(USB Manager)](arkts-basicservices-usb-usbcontrolrequesttype-e.md) |
| [USBRequestDirection(USB Manager)](arkts-basicservices-usb-usbrequestdirection-e.md) |
| [USBRequestTargetType(USB Manager)](arkts-basicservices-usb-usbrequesttargettype-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [DataRoleType(USB Manager)](arkts-basicservices-usb-dataroletype-e-sys.md) |
| [FunctionType(USB Manager)](arkts-basicservices-usb-functiontype-e-sys.md) |
| [PortModeType(USB Manager)](arkts-basicservices-usb-portmodetype-e-sys.md) |
| [PowerRoleType(USB Manager)](arkts-basicservices-usb-powerroletype-e-sys.md) |
<!--DelEnd-->
