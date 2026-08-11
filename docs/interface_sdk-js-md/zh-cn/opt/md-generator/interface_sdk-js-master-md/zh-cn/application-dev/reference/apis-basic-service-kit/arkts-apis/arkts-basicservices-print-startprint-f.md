# startPrint

## startPrint

```TypeScript
function startPrint(job: PrintJobData): Promise<void>
```

打印接口，传入文件或者二进制数据进行打印，使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.PRINT

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-print-function startPrint(job: PrintJobData): Promise<void>--><!--Device-print-function startPrint(job: PrintJobData): Promise<void>-End-->

**系统能力：** SystemCapability.Print.PrintFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| job | [PrintJobData](arkts-basicservices-print-printjobdata-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let tempPath = '/data/storage/el2/base/haps/entry/files/note.jpg';
let file: fileIo.File;
file = fileIo.openSync(tempPath, 4);

let printJobData: print.PrintJobData = {
    printerId: 'printerId', // printerId可通过on('printerChange')回调获取
    jobName: 'jobName',
    documentFormat: print.PrintDocumentFormat.DOCUMENT_FORMAT_AUTO,
    docFlavor: print.DocFlavor.FILE_DESCRIPTOR,
    copyNumber: 1,
    isLandscape: false,
    colorMode: print.PrintColorMode.COLOR_MODE_MONOCHROME,
    duplexMode: print.PrintDuplexMode.DUPLEX_MODE_NONE,
    pageSize: {id: 'ISO_A4', name: 'ISO_A4', width: 8268, height: 11692},
    fdList: [file.fd],
};
print.startPrint(printJobData).then(() => {
    console.info('start print success');
}).catch((error: BusinessError) => {
    console.error(`Failed to startPrint. Code: ${error.code}, message: ${error.message}`);
})
```
