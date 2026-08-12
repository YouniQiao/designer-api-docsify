# closePipe

## closePipe

```TypeScript
function closePipe(pipe: USBDevicePipe): number
```

关闭设备消息控制通道。

需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getDevices)获取设备列表；调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestRight)获取设备请求权限；调用  
[usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectDevice)得到devicepipe作为参数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [closePipe](arkts-basicservices-usbmanager-closepipe-f.md#closePipe)

<!--Device-usb-function closePipe(pipe: USBDevicePipe): number--><!--Device-usb-function closePipe(pipe: USBDevicePipe): number-End-->

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let ret = usb.closePipe(devicepipe);
console.info(`closePipe = ${ret}`);
```
