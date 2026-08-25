# startGettingPrintFile (System API)

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## startGettingPrintFile

```TypeScript
function startGettingPrintFile(jobId: string, printAttributes: PrintAttributes, fd: number,
    onFileStateChanged: Callback<PrintFileCreationState>): void
```

Starts to obtain the print file. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| jobId | string | Yes |
| printAttributes | [PrintAttributes](arkts-basicservices-print-printattributes-i.md) | Yes |
| fd | number | Yes |
| onFileStateChanged | [Callback](arkts-basicservices-base-callback-i.md)&lt;[PrintFileCreationState](arkts-basicservices-print-printfilecreationstate-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
