# openAccessory

## 导入模块

```TypeScript
import { usbManager } from 'kits/@kit.BasicServicesKit';
```

## openAccessory

```TypeScript
function openAccessory(accessory: USBAccessory): USBAccessoryHandle
```

获取配件句柄并打开配件文件描述符。之后可以通过CoreFileKit提供的read/write接口和配件进行通信。使用完后需要调用[closeAccessory](arkts-basicservices-usbmanager-closeaccessory-f.md)接 口关闭文件描述符。需要调用[usbManager.getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md)获取配件列表，得到 [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md)作为参数。调用前需先调用 [usbManager.requestAccessoryRight](arkts-basicservices-usbmanager-requestaccessoryright-f.md)请求访问配件权限，权限申请成功（返回true）后方可调用本接口打开配件。

**起始版本：** 14

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accessory | [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [USBAccessoryHandle](arkts-basicservices-usbmanager-usbaccessoryhandle-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14400001](../errorcode-usb.md#14400001-usb设备访问权限被拒绝) |
| [14400004](../errorcode-usb.md#14400004-服务异常) |
| [14401001](../errorcode-usb.md#14401001-目标usb配件未匹配) |
| [14401002](../errorcode-usb.md#14401002-打开配件节点失败) |
| [14401003](../errorcode-usb.md#14401003-不能重复打开配件) |
