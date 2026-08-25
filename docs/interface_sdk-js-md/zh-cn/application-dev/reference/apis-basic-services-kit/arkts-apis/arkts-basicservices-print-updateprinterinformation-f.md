# updatePrinterInformation

## 导入模块

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## updatePrinterInformation

```TypeScript
function updatePrinterInformation(printerInformation: PrinterInformation): Promise<void>
```

更新系统中打印机的部分信息，使用Promise异步回调。当前仅允许更新[PrinterInformation](arkts-basicservices-print-printerinformation-i.md)的alias和options字段。

**起始版本：** 24

**需要权限：** 
- API版本24+：ohos.permission.MANAGE_PRINT_JOB or ohos.permission.ENTERPRISE_MANAGE_PRINT
- API版本18 - 23：ohos.permission.MANAGE_PRINT_JOB

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerInformation | [PrinterInformation](arkts-basicservices-print-printerinformation-i.md) | 是 |

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
