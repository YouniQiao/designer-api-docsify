# getAccessoryList

## getAccessoryList

```TypeScript
function getAccessoryList(): Array<Readonly<USBAccessory>>
```

获取当前已接入主机的USB配件列表。

**起始版本：** 23

**废弃版本：** -1

<!--Device-usbManager-function getAccessoryList(): Array<Readonly<USBAccessory>>--><!--Device-usbManager-function getAccessoryList(): Array<Readonly<USBAccessory>>-End-->

**系统能力：** SystemCapability.USB.USBManager

**返回值：**

| 类型 |
| --- |
| Array&lt;Readonly&lt;[USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-服务异常) |

## 示例

```TypeScript
try {
  let accList: usbManager.USBAccessory[] = usbManager.getAccessoryList();
  console.info(`getAccessoryList success, accList: ${JSON.stringify(accList)}`);
} catch (error) {
  console.error(`getAccessoryList error ${error.code}, message is ${error.message}`);
}
```
