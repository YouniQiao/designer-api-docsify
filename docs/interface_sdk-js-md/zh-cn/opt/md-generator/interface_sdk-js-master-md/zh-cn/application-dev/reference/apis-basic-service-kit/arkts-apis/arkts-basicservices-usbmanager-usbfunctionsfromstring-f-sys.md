# usbFunctionsFromString（系统接口）

## usbFunctionsFromString

```TypeScript
function usbFunctionsFromString(funcs: string): number
```

在设备模式下，将字符串形式的USB功能列表转化为数字掩码。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [getFunctionsFromString](arkts-basicservices-usbmanager-getfunctionsfromstring-f-sys.md#getFunctionsFromString（系统接口）)(funcs: string)

<!--Device-usbManager-function usbFunctionsFromString(funcs: string): number--><!--Device-usbManager-function usbFunctionsFromString(funcs: string): number-End-->

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
