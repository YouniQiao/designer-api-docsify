# controlTransfer

## 导入模块

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## controlTransfer

```TypeScript
function controlTransfer(pipe: USBDevicePipe, controlparam: USBControlParams, timeout?: number): Promise<number>
```

控制传输。需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md)获取设备列表；调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md)获取设备请求权限；调用 [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md)接口得到devicepipe作为参数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [controlTransfer](arkts-basicservices-usbmanager-controltransfer-f.md)

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | 是 |
| controlparam | [USBControlParams](arkts-basicservices-usbmanager-usbcontrolparams-i.md) | 是 |
| timeout | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
