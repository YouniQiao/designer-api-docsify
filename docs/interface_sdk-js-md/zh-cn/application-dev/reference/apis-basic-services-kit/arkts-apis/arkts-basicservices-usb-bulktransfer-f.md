# bulkTransfer

## 导入模块

```TypeScript
import { usb } from 'kits/@kit.BasicServicesKit';
```

## bulkTransfer

```TypeScript
function bulkTransfer(
    pipe: USBDevicePipe,
    endpoint: USBEndpoint,
    buffer: Uint8Array,
    timeout?: number
  ): Promise<number>
```

批量传输。需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md)获取设备信息列表以及endpoint；再调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md)获取设备请求权限； 然后调用[usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md)接口得到返回数据devicepipe之后，再次获取接口 [usb.claimInterface](arkts-basicservices-usb-claiminterface-f.md)；再调用usb.bulkTransfer接口。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [bulkTransfer](arkts-basicservices-usbmanager-bulktransfer-f.md)

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [pipe](../../apis-arkts/arkts-apis/arkts-arkts-stream-readable-c.md) | [USBDevicePipe](arkts-basicservices-usbmanager-usbdevicepipe-i.md) | 是 |
| [endpoint](arkts-basicservices-usbmanager-usbdatatransferparams-i.md) | [USBEndpoint](arkts-basicservices-usbmanager-usbendpoint-i.md) | 是 |
| buffer | Uint8Array | 是 |
| timeout | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
