# getPrinterInformationById

## getPrinterInformationById

```TypeScript
function getPrinterInformationById(printerId: string): Promise<PrinterInformation>
```

根据打印机id获取打印机信息，使用Promise异步回调。

**起始版本：** 14

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
| Promise&lt;PrinterInformation&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

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
