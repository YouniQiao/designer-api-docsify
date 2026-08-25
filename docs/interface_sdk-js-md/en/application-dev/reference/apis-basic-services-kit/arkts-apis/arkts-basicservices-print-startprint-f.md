# startPrint

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## startPrint

```TypeScript
function startPrint(job: PrintJobData): Promise<void>
```

Prints a file or binary data. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.PRINT

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| job | [PrintJobData](arkts-basicservices-print-printjobdata-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

**Examples**

```TypeScript
import { print } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';
import fs from "@ohos.file.fs";

let tempPath = '/data/stroage/el2/base/haps/entry/files/note.jpg';
let file: fs.File;
file = fs.openSync(tempPath, 4);

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
