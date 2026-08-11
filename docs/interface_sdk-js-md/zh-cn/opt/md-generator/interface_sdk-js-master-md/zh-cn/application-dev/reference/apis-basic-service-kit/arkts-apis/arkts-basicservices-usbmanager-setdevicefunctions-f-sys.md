# setDeviceFunctions（系统接口）

## setDeviceFunctions

```TypeScript
function setDeviceFunctions(funcs: FunctionType): Promise<void>
```

在设备模式下，设置当前的USB功能列表。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function setDeviceFunctions(funcs: FunctionType): Promise<void>--><!--Device-usbManager-function setDeviceFunctions(funcs: FunctionType): Promise<void>-End-->

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| funcs | [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [14400002](../../apis-basic-services-kit/errorcode-usb.md#14400002-hdc功能被禁用) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [14400006](../../apis-basic-services-kit/errorcode-usb.md#14400006-不支持的usb设备侧功能) |
