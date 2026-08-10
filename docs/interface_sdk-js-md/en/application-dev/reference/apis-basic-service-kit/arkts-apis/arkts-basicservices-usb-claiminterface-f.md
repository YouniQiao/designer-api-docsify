# claimInterface

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## claimInterface

```TypeScript
function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number
```

注册通信接口。

需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getdevices)获取设备信息以及interfaces；调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestright)获取设备请求权限；调用[usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectdevice)接口得到devicepipe作为参数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md#claiminterface)

<!--Device-usb-function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number--><!--Device-usb-function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes | 用于确定总线号和设备地址。 |
| iface | [USBInterface](arkts-basicservices-usb-usbinterface-i.md) | Yes | 用于确定需要获取接口的索引。 |
| force | boolean | No | 可选参数，是否强制获取。默认值为false?，表示不强制获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 注册通信接口成功返回0；注册通信接口失败返回其他错误码。 |

## Examples

```TypeScript
let ret = usb.claimInterface(devicepipe, interfaces);
console.info(`claimInterface = ${ret}`);
```

