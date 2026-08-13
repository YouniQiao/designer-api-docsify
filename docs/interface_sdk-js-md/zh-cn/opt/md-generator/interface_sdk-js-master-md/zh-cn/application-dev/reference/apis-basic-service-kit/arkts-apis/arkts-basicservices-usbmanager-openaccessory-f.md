# openAccessory

## openAccessory

```TypeScript
function openAccessory(accessory: USBAccessory): USBAccessoryHandle
```

获取配件句柄并打开配件文件描述符。之后可以通过CoreFileKit提供的read/write接口和配件进行通信。 需要调用[usbManager.getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md#getAccessoryList)获取配件列表，得到 [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md#USBAccessory)作为参数。

**起始版本：** 23

**废弃版本：** -1

<!--Device-usbManager-function openAccessory(accessory: USBAccessory): USBAccessoryHandle--><!--Device-usbManager-function openAccessory(accessory: USBAccessory): USBAccessoryHandle-End-->

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
| [14401003](../../apis-basic-services-kit/errorcode-usb.md#14401003-不能重复打开配件) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14401002](../../apis-basic-services-kit/errorcode-usb.md#14401002-打开配件节点失败) |
| [14401001](../../apis-basic-services-kit/errorcode-usb.md#14401001-目标usb配件未匹配) |
| [14400001](../../apis-basic-services-kit/errorcode-usb.md#14400001-usb设备访问权限被拒绝) |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-服务异常) |

## 示例

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
async function openAccessory() {
  try {
    let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList();
    let flag = await usbManager.requestAccessoryRight(accList?.[0]);
    if (!flag) {
      return;
    }
    let handle = usbManager.openAccessory(accList?.[0]);
    console.info(`openAccessory success`);
    let arrayBuffer = new ArrayBuffer(4096);
    let readLength = fileIo.readSync(handle.accessoryFd, arrayBuffer, {offset: 0, length: 4096});
    console.info('readSync ret: ' + readLength.toString(10));
    usbManager.closeAccessory(handle);
  } catch (error) {
    console.error(`openAccessory error ${error.code}, message is ${error.message}`);
  }
}
```
