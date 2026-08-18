# getPrinterInformationById

## 导入模块

```TypeScript
```

## getPrinterInformationById

```TypeScript
function getPrinterInformationById(printerId: string): Promise<PrinterInformation>
```

根据打印机id获取打印机信息，使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.PRINT

<!--Device-print-function getPrinterInformationById(printerId: string): Promise<PrinterInformation>--><!--Device-print-function getPrinterInformationById(printerId: string): Promise<PrinterInformation>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PrinterInformation](arkts-basicservices-print-printerinformation-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

// printerId可通过on('printerChange')回调获取
let printerId : string = 'testPrinterId';
print.getPrinterInformationById(printerId).then((printerInformation : print.PrinterInformation) => {
    console.info('getPrinterInformationById data : ' + JSON.stringify(printerInformation));
}).catch((error: BusinessError) => {
    console.error(`Failed to getPrinterInformationById. Code: ${error.code}, message: ${error.message}`);
})
```
