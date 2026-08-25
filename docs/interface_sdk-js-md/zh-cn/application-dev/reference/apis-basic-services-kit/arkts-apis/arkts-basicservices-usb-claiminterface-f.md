# claimInterface

## 导入模块

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## claimInterface

```TypeScript
function claimInterface(pipe: USBDevicePipe, iface: USBInterface, force?: boolean): number
```

注册通信接口。需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md)获取设备信息以及interfaces；调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md)获取设备请求权限；调 用[usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md)接口得到devicepipe作为参数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md)

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | 是 |
| iface | [USBInterface](arkts-basicservices-usb-usbinterface-i.md) | 是 |
| [force](../../apis-arkui/arkts-components/arkts-arkui-historicalpoint-i.md) | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| number |
