# connectDevice

## 导入模块

```TypeScript
import { usb } from '@kit.BasicServicesKit';
```

## connectDevice

```TypeScript
function connectDevice(device: USBDevice): Readonly<USBDevicePipe>
```

打开USB设备。需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md)获取设备信息以及device，再调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md)获取设备请求权限。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md)

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| device | [USBDevice](arkts-basicservices-usb-usbdevice-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Readonly & lt;USBDevicePipe & gt; |

**示例**

```TypeScript
let devicepipe= usb.connectDevice(device);
console.info(`devicepipe = ${devicepipe}`);
```
