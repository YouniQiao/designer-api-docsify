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


**Since:** 8

**Deprecated since:** 9

**Substitutes:** [usbManager](arkts-usbmanager.md#@ohos.usbManager)

<!--Device-unnamed-declare namespace usb--><!--Device-unnamed-declare namespace usb-End-->

**System capability:** SystemCapability.USB.USBManager

## Modules to Import

```TypeScript
import { usb } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [bulkTransfer](arkts-basicservices-usb-bulktransfer-f.md#bulkTransfer) |
| [claimInterface](arkts-basicservices-usb-claiminterface-f.md#claimInterface) |
| [closePipe](arkts-basicservices-usb-closepipe-f.md#closePipe) |
| [connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectDevice) |
| [controlTransfer](arkts-basicservices-usb-controltransfer-f.md#controlTransfer) |
| [getDevices](arkts-basicservices-usb-getdevices-f.md#getDevices) |
| [getFileDescriptor](arkts-basicservices-usb-getfiledescriptor-f.md#getFileDescriptor) |
| [getRawDescriptor](arkts-basicservices-usb-getrawdescriptor-f.md#getRawDescriptor) |
| [hasRight](arkts-basicservices-usb-hasright-f.md#hasRight) |
| [releaseInterface](arkts-basicservices-usb-releaseinterface-f.md#releaseInterface) |
| [requestRight](arkts-basicservices-usb-requestright-f.md#requestRight) |
| [setConfiguration](arkts-basicservices-usb-setconfiguration-f.md#setConfiguration) |
| [setInterface](arkts-basicservices-usb-setinterface-f.md#setInterface) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getCurrentFunctions](arkts-basicservices-usb-getcurrentfunctions-f-sys.md#getCurrentFunctions-(System-API)) |
| [getPorts](arkts-basicservices-usb-getports-f-sys.md#getPorts-(System-API)) |
| [getSupportedModes](arkts-basicservices-usb-getsupportedmodes-f-sys.md#getSupportedModes-(System-API)) |
| [setCurrentFunctions](arkts-basicservices-usb-setcurrentfunctions-f-sys.md#setCurrentFunctions-(System-API)) |
| [setPortRoles](arkts-basicservices-usb-setportroles-f-sys.md#setPortRoles-(System-API)) |
| [usbFunctionsFromString](arkts-basicservices-usb-usbfunctionsfromstring-f-sys.md#usbFunctionsFromString-(System-API)) |
| [usbFunctionsToString](arkts-basicservices-usb-usbfunctionstostring-f-sys.md#usbFunctionsToString-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBConfig](arkts-basicservices-usb-usbconfig-i.md) |
| [USBControlParams](arkts-basicservices-usb-usbcontrolparams-i.md) |
| [USBDevice](arkts-basicservices-usb-usbdevice-i.md) |
| [USBDevicePipe](arkts-basicservices-usb-usbdevicepipe-i.md) |
| [USBEndpoint](arkts-basicservices-usb-usbendpoint-i.md) |
| [USBInterface](arkts-basicservices-usb-usbinterface-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBPort](arkts-basicservices-usb-usbport-i-sys.md) |
| [USBPortStatus](arkts-basicservices-usb-usbportstatus-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [USBControlRequestType](arkts-basicservices-usb-usbcontrolrequesttype-e.md) |
| [USBRequestDirection](arkts-basicservices-usb-usbrequestdirection-e.md) |
| [USBRequestTargetType](arkts-basicservices-usb-usbrequesttargettype-e.md) |

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DataRoleType](arkts-basicservices-usb-dataroletype-e-sys.md) |
| [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) |
| [PortModeType](arkts-basicservices-usb-portmodetype-e-sys.md) |
| [PowerRoleType](arkts-basicservices-usb-powerroletype-e-sys.md) |
<!--DelEnd-->
