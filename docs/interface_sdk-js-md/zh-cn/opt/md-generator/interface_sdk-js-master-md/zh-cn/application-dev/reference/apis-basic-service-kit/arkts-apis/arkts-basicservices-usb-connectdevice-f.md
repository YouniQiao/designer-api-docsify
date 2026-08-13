# connectDevice

## connectDevice

```TypeScript
function connectDevice(device: USBDevice): Readonly<USBDevicePipe>
```

打开USB设备。 需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getDevices)获取设备信息以及device，再调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestRight)获取设备请求权限。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [connectDevice](arkts-basicservices-usbmanager-connectdevice-f.md#connectDevice)

<!--Device-usb-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>--><!--Device-usb-function connectDevice(device: USBDevice): Readonly<USBDevicePipe>-End-->

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| device | [USBDevice](arkts-basicservices-usbmanager-usbdevice-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Readonly & lt;USBDevicePipe & gt; |

## 示例

```TypeScript
let devicepipe= usb.connectDevice(device);
console.info(`devicepipe = ${devicepipe}`);
```
