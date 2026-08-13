# getStringFromFunctions（系统接口）

## getStringFromFunctions

```TypeScript
function getStringFromFunctions(funcs: FunctionType): string
```

在设备模式下，将数字掩码形式的USB功能列表转化为字符串。

**起始版本：** 12

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getStringFromFunctions(funcs: FunctionType): string--><!--Device-usbManager-function getStringFromFunctions(funcs: FunctionType): string-End-->

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| funcs | [FunctionType](arkts-basicservices-usb-functiontype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## getStringFromFunctions

```TypeScript
function getStringFromFunctions(funcs: number): string
```

Converts the numeric mask combination of a given USB function list to a string descriptor.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_USB_CONFIG

<!--Device-usbManager-function getStringFromFunctions(funcs: int): string--><!--Device-usbManager-function getStringFromFunctions(funcs: int): string-End-->

**系统能力：** SystemCapability.USB.USBManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| funcs | number | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
