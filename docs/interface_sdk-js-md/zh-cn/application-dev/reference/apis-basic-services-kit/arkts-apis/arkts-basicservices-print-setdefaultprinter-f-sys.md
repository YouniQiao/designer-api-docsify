# setDefaultPrinter（系统接口）

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## setDefaultPrinter

```TypeScript
function setDefaultPrinter(printerId: string, type: DefaultPrinterType): Promise<void>
```

设置默认打印机，使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.MANAGE_PRINT_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | string | 是 |
| type | [DefaultPrinterType](arkts-basicservices-print-defaultprintertype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
