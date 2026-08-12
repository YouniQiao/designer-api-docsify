# cancelAccessoryRight

## cancelAccessoryRight

```TypeScript
function cancelAccessoryRight(accessory: USBAccessory): void
```

取消当前应用程序访问USB配件的权限。需要调用[usbManager.getAccessoryList](arkts-basicservices-usbmanager-getaccessorylist-f.md#getAccessoryList)获取配件列表，得到  
[USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md#USBAccessory)作为参数。

**起始版本：** 14

<!--Device-usbManager-function cancelAccessoryRight(accessory: USBAccessory): void--><!--Device-usbManager-function cancelAccessoryRight(accessory: USBAccessory): void-End-->

**系统能力：** SystemCapability.USB.USBManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| accessory | [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [14401001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#14401001-目标usb配件未匹配) |
| [14400005](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#14400005-数据库操作异常) |
| [14400004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-usb.md#14400004-服务异常) |

## 示例

```TypeScript
async function cancelAccessoryRight() {
  try {
    let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList();
    let flag = await usbManager.requestAccessoryRight(accList?.[0]);
    if (!flag) {
      return;
    }
    usbManager.cancelAccessoryRight(accList?.[0]);
    console.info(`cancelAccessoryRight success`);
  } catch (error) {
    console.error(`cancelAccessoryRight error ${error.code}, message is ${error.message}`);
  }
}
```
