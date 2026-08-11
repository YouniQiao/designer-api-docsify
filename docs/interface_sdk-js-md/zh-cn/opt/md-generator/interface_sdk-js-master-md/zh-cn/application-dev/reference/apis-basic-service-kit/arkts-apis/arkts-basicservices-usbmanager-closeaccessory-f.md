# closeAccessory

## closeAccessory

```TypeScript
function closeAccessory(accessoryHandle: USBAccessoryHandle): void
```

关闭配件文件描述符。需要调用[usbManager.openAccessory](arkts-basicservices-usbmanager-openaccessory-f.md#openaccessory)获取配件列表，得到  
[USBAccessoryHandle](arkts-basicservices-usbmanager-usbaccessoryhandle-i.md)作为参数。

**起始版本：** 14

<!--Device-usbManager-function closeAccessory(accessoryHandle: USBAccessoryHandle): void--><!--Device-usbManager-function closeAccessory(accessoryHandle: USBAccessoryHandle): void-End-->

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accessoryHandle | [USBAccessoryHandle](arkts-basicservices-usbmanager-usbaccessoryhandle-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-服务异常) |

## 示例

```TypeScript
async function closeAccessory() {
  try {
    let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList();
    let flag = await usbManager.requestAccessoryRight(accList?.[0]);
    if (!flag) {
      return;
    }
    let handle = usbManager.openAccessory(accList?.[0]);
    usbManager.closeAccessory(handle);
    console.info(`closeAccessory success`);
  } catch (error) {
    console.error(`closeAccessory error ${error.code}, message is ${error.message}`);
  }
}
```
