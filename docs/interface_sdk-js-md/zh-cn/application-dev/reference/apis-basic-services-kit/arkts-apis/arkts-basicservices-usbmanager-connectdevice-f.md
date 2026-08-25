# connectDevice

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## connectDevice

```TypeScript
function connectDevice(device: USBDevice): Readonly<USBDevicePipe>
```

根据getDevices()返回的设备信息打开USB设备，调用成功后建立设备连接通道，可以进行后续的数据传输和设备控制操作。使用完后需要调用 [usbManager.closePipe](arkts-basicservices-usbmanager-closepipe-f.md)关闭设备连接通道。如果USB服务异常，会返回`undefined`，注意需要对接口返回值做判空处理。
1. 调用[usbManager.getDevices](arkts-basicservices-usbmanager-getdevices-f.md)获取设备信息以及USBDevice;
2. 调用[usbManager.requestRight](arkts-basicservices-usbmanager-requestright-f.md)请求使用该设备的权限。

**起始版本：** 9

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| device | [USBDevice](arkts-basicservices-usbmanager-usbdevice-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Readonly & lt;USBDevicePipe & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14400001](../errorcode-usb.md#14400001-usb设备访问权限被拒绝) |
| [14400004](../errorcode-usb.md#14400004-服务异常) |
| [14400012](../errorcode-usb.md#14400012-io错误) |
