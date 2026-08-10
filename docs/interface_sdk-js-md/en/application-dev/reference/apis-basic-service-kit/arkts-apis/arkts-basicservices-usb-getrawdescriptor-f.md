# getRawDescriptor

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## getRawDescriptor

```TypeScript
function getRawDescriptor(pipe: USBDevicePipe): Uint8Array
```

获取原始的USB描述符。

需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getdevices)获取设备列表；调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestright)获取设备请求权限；调用  
[usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectdevice)接口得到devicepipe作为参数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.getRawDescriptor](arkts-basicservices-usbmanager-getrawdescriptor-f.md#getrawdescriptor)

<!--Device-usb-function getRawDescriptor(pipe: USBDevicePipe): Uint8Array--><!--Device-usb-function getRawDescriptor(pipe: USBDevicePipe): Uint8Array-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes | 用于确定总线号和设备地址。 |

**Return value:**

| Type | Description |
| --- | --- |
| Uint8Array | 返回获取的原始数据；失败返回undefined。 |

## Examples

```TypeScript
let ret = usb.getRawDescriptor(devicepipe);
```

