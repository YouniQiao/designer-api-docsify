# @ohos.usbManager(USB管理)

本模块主要提供管理USB设备的相关功能，包括主机端的查询USB设备列表、批量数据传输、控制命令传输、权限控制等；设备端的端口管理、功能切换及查询等。适用于需要与USB设备进行数据交互、管理USB设备权限、动态切换USB设备模式等场景。

## 使用说明

凡是参数类型为[USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md)的接口，都需要执行如下操作：  
**在使用接口前：**
1. 调用[usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md)获取设备列表。
2. 调用[usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md)获取请求权限。
3. 调用[usbManager.connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md)得到USBDevicePipe作为参数。  
**在使用接口后：**调用[usbManager.closePipe](arkts-basicservices-usbmanager-closepipe-f.md)关闭设备连接通道。

**起始版本：** 9

**系统能力：** SystemCapability.USB.USBManager

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [bulkTransfer(USB管理)](arkts-basicservices-usbmanager-bulktransfer-f.md) |
| [cancelAccessoryRight(USB管理)](arkts-basicservices-usbmanager-cancelaccessoryright-f.md) |
| [claimInterface(USB管理)](arkts-basicservices-usbmanager-claiminterface-f.md) |
| [closeAccessory(USB管理)](arkts-basicservices-usbmanager-closeaccessory-f.md) |
| [closePipe(USB管理)](arkts-basicservices-usbmanager-closepipe-f.md) |
| [connectDevice(USB管理)](arkts-basicservices-usbmanager-connectdevice-f.md) |
| [controlTransfer(USB管理)](arkts-basicservices-usbmanager-controltransfer-f.md) |
| [getAccessoryList(USB管理)](arkts-basicservices-usbmanager-getaccessorylist-f.md) |
| [getDevices(USB管理)](arkts-basicservices-usbmanager-getdevices-f.md) |
| [getFileDescriptor(USB管理)](arkts-basicservices-usbmanager-getfiledescriptor-f.md) |
| [getRawDescriptor(USB管理)](arkts-basicservices-usbmanager-getrawdescriptor-f.md) |
| [hasAccessoryRight(USB管理)](arkts-basicservices-usbmanager-hasaccessoryright-f.md) |
| [hasRight(USB管理)](arkts-basicservices-usbmanager-hasright-f.md) |
| [openAccessory(USB管理)](arkts-basicservices-usbmanager-openaccessory-f.md) |
| [releaseInterface(USB管理)](arkts-basicservices-usbmanager-releaseinterface-f.md) |
| [removeRight(USB管理)](arkts-basicservices-usbmanager-removeright-f.md) |
| [requestAccessoryRight(USB管理)](arkts-basicservices-usbmanager-requestaccessoryright-f.md) |
| [requestRight(USB管理)](arkts-basicservices-usbmanager-requestright-f.md) |
| [resetUsbDevice(USB管理)](arkts-basicservices-usbmanager-resetusbdevice-f.md) |
| [setConfiguration(USB管理)](arkts-basicservices-usbmanager-setconfiguration-f.md) |
| [setInterface(USB管理)](arkts-basicservices-usbmanager-setinterface-f.md) |
| [usbCancelTransfer(USB管理)](arkts-basicservices-usbmanager-usbcanceltransfer-f.md) |
| [usbControlTransfer(USB管理)](arkts-basicservices-usbmanager-usbcontroltransfer-f.md) |
| [usbSubmitTransfer(USB管理)](arkts-basicservices-usbmanager-usbsubmittransfer-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [addAccessoryRight(USB管理)](arkts-basicservices-usbmanager-addaccessoryright-f-sys.md) |
| [addDeviceAccessRight(USB管理)](arkts-basicservices-usbmanager-adddeviceaccessright-f-sys.md) |
| [getCurrentFunctions(USB管理)](arkts-basicservices-usbmanager-getcurrentfunctions-f-sys.md) |
| [getDeviceFunctions(USB管理)](arkts-basicservices-usbmanager-getdevicefunctions-f-sys.md) |
| [getFunctionsFromString(USB管理)](arkts-basicservices-usbmanager-getfunctionsfromstring-f-sys.md) |
| [getPortList(USB管理)](arkts-basicservices-usbmanager-getportlist-f-sys.md) |
| [getPorts(USB管理)](arkts-basicservices-usbmanager-getports-f-sys.md) |
| [getPortSupportModes(USB管理)](arkts-basicservices-usbmanager-getportsupportmodes-f-sys.md) |
| [getStringFromFunctions(USB管理)](arkts-basicservices-usbmanager-getstringfromfunctions-f-sys.md) |
| [getSupportedModes(USB管理)](arkts-basicservices-usbmanager-getsupportedmodes-f-sys.md) |
| [setCurrentFunctions(USB管理)](arkts-basicservices-usbmanager-setcurrentfunctions-f-sys.md) |
| [setDeviceFunctions(USB管理)](arkts-basicservices-usbmanager-setdevicefunctions-f-sys.md) |
| [setPortRoles(USB管理)](arkts-basicservices-usbmanager-setportroles-f-sys.md) |
| [setPortRoleTypes(USB管理)](arkts-basicservices-usbmanager-setportroletypes-f-sys.md) |
| [usbFunctionsFromString(USB管理)](arkts-basicservices-usbmanager-usbfunctionsfromstring-f-sys.md) |
| [usbFunctionsToString(USB管理)](arkts-basicservices-usbmanager-usbfunctionstostring-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [SubmitTransferCallback(USB管理)](arkts-basicservices-usbmanager-submittransfercallback-i.md) |
| [USBAccessory(USB管理)](arkts-basicservices-usbmanager-usbaccessory-i.md) |
| [USBAccessoryHandle(USB管理)](arkts-basicservices-usbmanager-usbaccessoryhandle-i.md) |
| [USBConfiguration(USB管理)](arkts-basicservices-usbmanager-usbconfiguration-i.md) |
| [USBControlParams(USB管理)](arkts-basicservices-usbmanager-usbcontrolparams-i.md) |
| [UsbDataTransferParams(USB管理)](arkts-basicservices-usbmanager-usbdatatransferparams-i.md) |
| [USBDevice(USB管理)](arkts-basicservices-usbmanager-usbdevice-i.md) |
| [USBDevicePipe(USB管理)](arkts-basicservices-usbmanager-usbdevicepipe-i.md) |
| [USBDeviceRequestParams(USB管理)](arkts-basicservices-usbmanager-usbdevicerequestparams-i.md) |
| [USBEndpoint(USB管理)](arkts-basicservices-usbmanager-usbendpoint-i.md) |
| [USBInterface(USB管理)](arkts-basicservices-usbmanager-usbinterface-i.md) |
| [UsbIsoPacketDescriptor(USB管理)](arkts-basicservices-usbmanager-usbisopacketdescriptor-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [USBPort(USB管理)](arkts-basicservices-usbmanager-usbport-i-sys.md) |
| [USBPortStatus(USB管理)](arkts-basicservices-usbmanager-usbportstatus-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [USBControlRequestType(USB管理)](arkts-basicservices-usbmanager-usbcontrolrequesttype-e.md) |
| [UsbEndpointTransferType(USB管理)](arkts-basicservices-usbmanager-usbendpointtransfertype-e.md) |
| [USBRequestDirection(USB管理)](arkts-basicservices-usbmanager-usbrequestdirection-e.md) |
| [USBRequestTargetType(USB管理)](arkts-basicservices-usbmanager-usbrequesttargettype-e.md) |
| [UsbTransferFlags(USB管理)](arkts-basicservices-usbmanager-usbtransferflags-e.md) |
| [UsbTransferStatus(USB管理)](arkts-basicservices-usbmanager-usbtransferstatus-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [DataRoleType(USB管理)](arkts-basicservices-usbmanager-dataroletype-e-sys.md) |
| [FunctionType(USB管理)](arkts-basicservices-usbmanager-functiontype-e-sys.md) |
| [PortModeType(USB管理)](arkts-basicservices-usbmanager-portmodetype-e-sys.md) |
| [PowerRoleType(USB管理)](arkts-basicservices-usbmanager-powerroletype-e-sys.md) |
<!--DelEnd-->
