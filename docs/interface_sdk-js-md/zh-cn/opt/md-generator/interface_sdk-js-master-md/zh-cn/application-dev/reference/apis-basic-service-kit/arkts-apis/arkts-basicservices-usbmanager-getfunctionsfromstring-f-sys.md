# getFunctionsFromString（系统接口）

## getFunctionsFromString

```TypeScript
function getFunctionsFromString(funcs: string): number
```

在设备模式下，将字符串形式的USB功能列表转化为数字掩码。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getFunctionsFromString(funcs: string): int--><!--Device-usbManager-function getFunctionsFromString(funcs: string): int-End-->

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| funcs | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
