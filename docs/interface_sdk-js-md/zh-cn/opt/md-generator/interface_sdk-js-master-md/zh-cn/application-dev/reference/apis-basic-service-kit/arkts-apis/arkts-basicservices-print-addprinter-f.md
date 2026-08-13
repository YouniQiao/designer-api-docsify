# addPrinter

## addPrinter

```TypeScript
function addPrinter(printerName: string, uri: string, ppdName?: string, options?: string): Promise<boolean>
```

添加打印机到系统中，使用Promise异步回调。

**起始版本：** 24

**废弃版本：** -1

**需要权限：** ohos.permission.MANAGE_PRINT_JOB or ohos.permission.PRINTER_DRIVER

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-print-function addPrinter(printerName: string, uri: string, ppdName?: string, options?: string): Promise<boolean>--><!--Device-print-function addPrinter(printerName: string, uri: string, ppdName?: string, options?: string): Promise<boolean>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| printerName | string | 是 |
| uri | string | 是 |
| [ppdName](arkts-basicservices-print-ppdinfo-i.md) | string | 否 |
| options | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [13100003](../../apis-basic-services-kit/errorcode-print.md#13100003-打印服务异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

let printerName : string = 'printerName';
let uri : string = 'uri';
let ppdName : string = 'ppdName';
print.addPrinter(printerName, uri, ppdName).then(() => {
    console.info('add printer success');
}).catch((error: BusinessError) => {
    console.error(`Failed to addPrinter. Code: ${error.code}, message: ${error.message}`);
})
```
