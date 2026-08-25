# usbCancelTransfer

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## usbCancelTransfer

```TypeScript
function usbCancelTransfer(transfer: UsbDataTransferParams): void
```

取消异步传输请求。适用于需要主动终止未完成USB数据传输的场景，如用户手动取消长时间数据传输、传输超时后的错误恢复、应用切换时中止当前传输等。

> **说明：**&gt;
> 主动取消尚未完成的USB数据传输请求（如usbSubmitTransfer提交的传输）。

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
| [14400008](../errorcode-usb.md#14400008-没有设备连接已断开) |
| [14400010](../errorcode-usb.md#14400010-无法识别的错误) |
| [14400011](../errorcode-usb.md#14400011-未找到正在进行的传输) |
