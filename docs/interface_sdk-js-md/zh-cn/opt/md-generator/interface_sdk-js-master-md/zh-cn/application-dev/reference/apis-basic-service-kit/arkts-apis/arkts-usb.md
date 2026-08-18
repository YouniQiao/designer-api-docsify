# @ohos.usb(USB Manager)

/*
 Copyright (c) 2021-2023 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**起始版本：** 8

**废弃版本：** 9

**替代接口：** [usbManager](arkts-usbmanager.md#ohosusbmanager)

<!--Device-unnamed-declare namespace usb--><!--Device-unnamed-declare namespace usb-End-->

**系统能力：** SystemCapability.USB.USBManager

## 导入模块

```TypeScript
```

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
| [getCurrentFunctions](arkts-basicservices-usb-getcurrentfunctions-f-sys.md#getcurrentfunctions系统接口) |
| [getPorts](arkts-basicservices-usb-getports-f-sys.md#getports系统接口) |
| [getSupportedModes](arkts-basicservices-usb-getsupportedmodes-f-sys.md#getsupportedmodes系统接口) |
| [setCurrentFunctions](arkts-basicservices-usb-setcurrentfunctions-f-sys.md#setcurrentfunctions系统接口) |
| [setPortRoles](arkts-basicservices-usb-setportroles-f-sys.md#setportroles系统接口) |
| [usbFunctionsFromString](arkts-basicservices-usb-usbfunctionsfromstring-f-sys.md#usbfunctionsfromstring系统接口) |
| [usbFunctionsToString](arkts-basicservices-usb-usbfunctionstostring-f-sys.md#usbfunctionstostring系统接口) |
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
