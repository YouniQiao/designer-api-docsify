# usbSubmitTransfer

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## usbSubmitTransfer

```TypeScript
function usbSubmitTransfer(transfer: UsbDataTransferParams): void
```

提交异步传输请求，调用后立即返回，实际读写操作的结果以回调的方式返回。可通过调用[usbCancelTransfer](arkts-basicservices-usbmanager-usbcanceltransfer-f.md)接口取消异步传输请求。

> **说明：**&gt;
> 本接口为异步接口，调用后立刻返回，实际读写操作的结果以回调的方式返回。&gt;
> 在调用该接口前需要通过[usbManager.claimInterface](arkts-basicservices-usbmanager-claiminterface-f.md) claim通信接口。

**起始版本：** 18

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [transfer](../../apis-arkts/arkts-apis/arkts-arkts-worker-postmessageoptions-i.md) | [UsbDataTransferParams](arkts-basicservices-usbmanager-usbdatatransferparams-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14400001](../errorcode-usb.md#14400001-usb设备访问权限被拒绝) |
| [14400007](../errorcode-usb.md#14400007-资源繁忙) |
| [14400008](../errorcode-usb.md#14400008-没有设备连接已断开) |
| [14400009](../errorcode-usb.md#14400009-内存不足) |
| [14400012](../errorcode-usb.md#14400012-io错误) |
