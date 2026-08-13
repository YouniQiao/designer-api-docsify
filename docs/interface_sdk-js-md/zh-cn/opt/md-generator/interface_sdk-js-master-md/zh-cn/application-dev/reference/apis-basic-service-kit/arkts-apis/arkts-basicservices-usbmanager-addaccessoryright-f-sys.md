# addAccessoryRight（系统接口）

## addAccessoryRight

```TypeScript
function addAccessoryRight(tokenId: number, accessory: USBAccessory): void
```

为应用程序添加访问USB配requestAccessoryRight件权限。 [usbManager.]{(@link usbManager.requestAccessoryRight)}会触发弹窗请求用户授权；addAccessoryRight不会触发弹窗，而是直接添加应用程序访问设备的权限。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function addAccessoryRight(tokenId: int, accessory: USBAccessory): void--><!--Device-usbManager-function addAccessoryRight(tokenId: int, accessory: USBAccessory): void-End-->

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenId | number | 是 |
| accessory | [USBAccessory](arkts-basicservices-usbmanager-usbaccessory-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14400005](../../apis-basic-services-kit/errorcode-usb.md#14400005-数据库操作异常) |
| [14400004](../../apis-basic-services-kit/errorcode-usb.md#14400004-服务异常) |
