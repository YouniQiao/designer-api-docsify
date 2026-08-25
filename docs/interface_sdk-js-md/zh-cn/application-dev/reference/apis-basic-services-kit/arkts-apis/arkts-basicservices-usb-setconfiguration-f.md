# setConfiguration

## 导入模块

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## setConfiguration

```TypeScript
function setConfiguration(pipe: USBDevicePipe, config: USBConfig): number
```

设置设备配置。需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md)获取设备信息以及config；调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md)获取设备请求权限；调用 [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md)得到devicepipe作为参数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setConfiguration](arkts-basicservices-usbmanager-setconfiguration-f.md)

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | 是 |
| config | [USBConfig](arkts-basicservices-usb-usbconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |
