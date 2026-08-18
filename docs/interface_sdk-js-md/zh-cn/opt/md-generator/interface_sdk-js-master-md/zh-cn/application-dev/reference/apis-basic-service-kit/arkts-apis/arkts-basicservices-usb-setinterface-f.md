# setInterface

## 导入模块

```TypeScript
```

## setInterface

```TypeScript
function setInterface(pipe: USBDevicePipe, iface: USBInterface): number
```

设置设备接口。 需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getdevices)获取设备列表以及interfaces；调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestright)获取设备请求权限；调 用[usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectdevice)得到devicepipe作为参数；调用[usb.claimInterface](arkts-basicservices-usb-claiminterface-f.md#claiminterface)注册通信接 口。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [setInterface](arkts-basicservices-usbmanager-setinterface-f.md#setinterface)

<!--Device-usb-function setInterface(pipe: USBDevicePipe, iface: USBInterface): number--><!--Device-usb-function setInterface(pipe: USBDevicePipe, iface: USBInterface): number-End-->

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | 是 |
| iface | [USBInterface](arkts-basicservices-usb-usbinterface-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
let ret = usb.setInterface(devicepipe, interfaces);
console.info(`setInterface = ${ret}`);
```
