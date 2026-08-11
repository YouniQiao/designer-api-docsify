# hasAccessoryRight

## hasAccessoryRight

```TypeScript
function hasAccessoryRight(accessory: USBAccessory): boolean
```

检查应用程序是否有权访问USB配件。需要调用[usbManager.getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md#getaccessorylist)获取配件列表，得到  
[USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md)作为参数。

**起始版本：** 14

<!--Device-usbManager-function hasAccessoryRight(accessory: USBAccessory): boolean--><!--Device-usbManager-function hasAccessoryRight(accessory: USBAccessory): boolean-End-->

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accessory | [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14401001](../../apis-basic-services-kit/errorcode-usb.md#14401001-目标usb配件未匹配) |
| [14400005](../../apis-basic-services-kit/errorcode-usb.md#14400005-数据库操作异常) |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-服务异常) |

## 示例

```TypeScript
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList();
  let flag = usbManager.hasAccessoryRight(accList?.[0]);
  console.info(`hasAccessoryRight success, ret:${flag}`);
} catch (error) {
  console.error(`hasAccessoryRight error ${error.code}, message is ${error.message}`);
}
```
