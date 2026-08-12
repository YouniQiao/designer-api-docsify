# bulkTransfer

## bulkTransfer

```TypeScript
function bulkTransfer(
    pipe: USBDevicePipe,
    endpoint: USBEndpoint,
    buffer: Uint8Array,
    timeout?: number
  ): Promise<number>
```

批量传输。

需要调用[usb.getDevices](arkts-basicservices-usb-getdevices-f.md#getDevices)获取设备信息列表以及endpoint；再调用[usb.requestRight](arkts-basicservices-usb-requestright-f.md#requestRight)获取设备请求权限；然后调用[usb.connectDevice](arkts-basicservices-usb-connectdevice-f.md#connectDevice)接口得到返回数据devicepipe之后，再次获取接口  
[usb.claimInterface](arkts-basicservices-usb-claiminterface-f.md#claimInterface)；再调用usb.bulkTransfer接口。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [bulkTransfer](arkts-basicservices-usbmanager-bulktransfer-f.md#bulkTransfer)

<!--Device-usb-function bulkTransfer(    pipe: USBDevicePipe,    endpoint: USBEndpoint,    buffer: Uint8Array,    timeout?: number  ): Promise<number>--><!--Device-usb-function bulkTransfer(    pipe: USBDevicePipe,    endpoint: USBEndpoint,    buffer: Uint8Array,    timeout?: number  ): Promise<number>-End-->

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

## 示例

```TypeScript
//usb.getDevices 接口返回数据集合，取其中一个设备对象，并获取权限 。
//把获取到的设备对象作为参数传入usb.connectDevice;当usb.connectDevice接口成功返回之后；
//才可以调用第三个接口usb.claimInterface.当usb.claimInterface 调用成功以后,再调用该接口。
usb.bulkTransfer(devicepipe, endpoint, buffer).then((ret) => {
 console.info(`bulkTransfer = ${ret}`);
});
```
