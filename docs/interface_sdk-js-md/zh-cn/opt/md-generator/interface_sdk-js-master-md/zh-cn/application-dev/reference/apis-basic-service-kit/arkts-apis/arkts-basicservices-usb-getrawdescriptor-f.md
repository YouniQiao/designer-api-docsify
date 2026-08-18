# getRawDescriptor

## 导入模块

```TypeScript
```

## getRawDescriptor

```TypeScript
function getRawDescriptor(pipe: USBDevicePipe): Uint8Array
```

获取原始的USB描述符。 需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getdevices)获取设备列表；调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestright)获取设备请求权限；调用 [usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectdevice)接口得到devicepipe作为参数。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getRawDescriptor](arkts-basicservices-usbmanager-getrawdescriptor-f.md#getrawdescriptor)

<!--Device-usb-function getRawDescriptor(pipe: USBDevicePipe): Uint8Array--><!--Device-usb-function getRawDescriptor(pipe: USBDevicePipe): Uint8Array-End-->

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**示例**

```TypeScript
let ret = usb.getRawDescriptor(devicepipe);
```
