# getFileDescriptor

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## getFileDescriptor

```TypeScript
function getFileDescriptor(pipe: USBDevicePipe): number
```

获取文件描述符。

需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getdevices)获取设备列表；调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestright)获取设备请求权限；调用  
[usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectdevice)接口得到devicepipe作为参数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.getFileDescriptor](arkts-basicservices-usbmanager-getfiledescriptor-f.md#getfiledescriptor)

<!--Device-usb-function getFileDescriptor(pipe: USBDevicePipe): number--><!--Device-usb-function getFileDescriptor(pipe: USBDevicePipe): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes | 用于确定总线号和设备地址。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 返回设备对应的文件描述符；失败返回-1。 |

## Examples

```TypeScript
let ret = usb.getFileDescriptor(devicepipe);
```

