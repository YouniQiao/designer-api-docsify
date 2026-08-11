# addDeviceAccessRight（系统接口）

## addDeviceAccessRight

```TypeScript
function addDeviceAccessRight(tokenId: string, deviceName: string): boolean
```

添加软件包访问设备的权限。系统应用默认拥有访问设备权限，调用此接口不会产生影响。  
[usbManager.requestRight]{(@link usbManager.requestRight)}会触发弹框请求用户授权；addDeviceAccessRight不会触发弹框，而是直接添加软件包访问设备的权限。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function addDeviceAccessRight(tokenId: string, deviceName: string): boolean--><!--Device-usbManager-function addDeviceAccessRight(tokenId: string, deviceName: string): boolean-End-->

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenId | string | 是 |
| deviceName | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
