# addPrinterToDiscovery

## addPrinterToDiscovery

```TypeScript
function addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>
```

添加打印机到系统打印机发现列表，使用Promise异步回调。

**起始版本：** 14

**需要权限：** ohos.permission.PRINT

<!--Device-print-function addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>--><!--Device-print-function addPrinterToDiscovery(printerInformation: PrinterInformation): Promise<void>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerInformation : print.PrinterInformation = {
    printerId : 'testPrinterId',
    printerName : 'testPrinterName',
    printerStatus : 0,
    description : 'testDesc',
    uri : 'testUri',
    printerMake : 'testPrinterMake',
    options : 'testOps'
};
print.addPrinterToDiscovery(printerInformation).then(() => {
    console.info('addPrinterToDiscovery success');
}).catch((error: BusinessError) => {
    console.error(`Failed to addPrinterToDiscovery. Code: ${error.code}, message: ${error.message}`);
})
```
