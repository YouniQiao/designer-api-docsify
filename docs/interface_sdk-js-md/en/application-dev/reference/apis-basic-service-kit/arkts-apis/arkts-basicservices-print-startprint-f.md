# startPrint

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## startPrint

```TypeScript
function startPrint(job: PrintJobData): Promise<void>
```

打印接口，传入文件或者二进制数据进行打印，使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.PRINT

**Model restriction:** This API can be used only in the stage model.

<!--Device-print-function startPrint(job: PrintJobData): Promise<void>--><!--Device-print-function startPrint(job: PrintJobData): Promise<void>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| job | [PrintJobData](arkts-basicservices-print-printjobdata-i.md) | Yes | 打印任务数据。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | the application does not have permission to call this function. |

## Examples

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';

let tempPath = '/data/storage/el2/base/haps/entry/files/note.jpg';
let file: fileIo.File;
file = fileIo.openSync(tempPath, 4);

let printJobData: print.PrintJobData = {
    printerId: "printerId",
    jobName: "jobName",
    documentFormat: print.PrintDocumentFormat.DOCUMENT_FORMAT_AUTO,
    docFlavor: print.DocFlavor.FILE_DESCRIPTOR,
    copyNumber: 1,
    isLandscape: false,
    colorMode: print.PrintColorMode.COLOR_MODE_MONOCHROME,
    duplexMode: print.PrintDuplexMode.DUPLEX_MODE_NONE,
    pageSize: {id: "ISO_A4", name: "ISO_A4", width:8268, height: 11692},
    fdList: [file.fd],
}
print.startPrint(printJobData).then(() => {
    console.info('start print success');
}).catch((error: BusinessError) => {
    console.error('failed to print because : ' + JSON.stringify(error));
})
```

