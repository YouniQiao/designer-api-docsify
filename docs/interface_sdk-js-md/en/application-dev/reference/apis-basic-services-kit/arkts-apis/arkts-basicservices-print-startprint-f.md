# startPrint

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## startPrint

```TypeScript
function startPrint(job: PrintJobData): Promise<void>
```

Prints a file or binary data. This API uses a promise to return the result.

**Since:** 23

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
