# OnBackupSizeReport (System API)

```TypeScript
type OnBackupSizeReport = (reportInfo: string) => void
```

function that returns backup datasize by bundleName.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reportInfo | string | Yes |

**Examples**

```TypeScript
import { backup } from '@kit.CoreFileKit';

onBackupSizeReport: (OnBackupSizeReport: backup.OnBackupSizeReport) => {
  console.info('dataSizeCallback success');
  console.info('dataSizeCallback report : ' + OnBackupSizeReport);
}
```
