# PrintDocumentAdapter

Provides information about the document to print. This API must be implemented by a third-party application.

**Since:** 11

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## onJobStateChanged

```TypeScript
onJobStateChanged(jobId: string, state: PrintDocumentAdapterState): void
```

Registers a listener for print job state changes.

**Since:** 11

**Required permissions:** ohos.permission.PRINT

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| jobId | string | Yes |
| state | [PrintDocumentAdapterState](arkts-basicservices-print-printdocumentadapterstate-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## onStartLayoutWrite

```TypeScript
onStartLayoutWrite(jobId: string, oldAttrs: PrintAttributes, newAttrs: PrintAttributes, fd: number,
      writeResultCallback: (jobId: string, writeResult: PrintFileCreationState) => void): void
```

Sends an empty PDF file descriptor to a third-party application. The third-party application updates the file with the new print attributes and then calls **writeResultCallback** to print the file.

**Since:** 11

**Required permissions:** ohos.permission.PRINT

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| jobId | string | Yes |
| oldAttrs | [PrintAttributes](arkts-basicservices-print-printattributes-i.md) | Yes |
| newAttrs | [PrintAttributes](arkts-basicservices-print-printattributes-i.md) | Yes |
| fd | number | Yes |
| writeResultCallback | (jobId: string, writeResult: PrintFileCreationState) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
