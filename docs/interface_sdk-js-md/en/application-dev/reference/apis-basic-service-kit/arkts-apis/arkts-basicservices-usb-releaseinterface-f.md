# releaseInterface

## Modules to Import

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## releaseInterface

```TypeScript
function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number
```

释放注册过的通信接口。

需要调用[usb.claimInterface](arkts-basicservices-usb-claiminterface-f.md#claiminterface)先获取接口，才能使用此方法释放接口。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.usbManager:usbManager.releaseInterface](arkts-basicservices-usbmanager-releaseinterface-f.md#releaseinterface)

<!--Device-usb-function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number--><!--Device-usb-function releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number-End-->

**System capability:** SystemCapability.USB.USBManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pipe | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | Yes | 用于确定总线号和设备地址。 |
| iface | [USBInterface](arkts-basicservices-usb-usbinterface-i.md) | Yes | 用于确定需要释放接口的索引。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 释放接口成功返回0；释放接口失败返回其他错误码。 |

## Examples

```TypeScript
let ret = usb.releaseInterface(devicepipe, interfaces);
console.info(`releaseInterface = ${ret}`);
```

