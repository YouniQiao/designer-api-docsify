# BackupExtensionAbility

Class to be override for backup extension ability.

**Since:** 10

**System capability:** SystemCapability.FileManagement.StorageService.Backup

## Modules to Import

```TypeScript
import { BackupExtensionAbility, BundleVersion } from 'kits/@kit.CoreFileKit';
import { BackupExtensionAbility } from 'kits/@kit.CoreFileKit';
import { BundleVersion } from 'kits/@kit.CoreFileKit';
```

## onBackup

```TypeScript
onBackup(): void
```

Callback to be called when the backup procedure is started. Developer could override this method to build files to be backup.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

## onBackupEx

```TypeScript
onBackupEx(backupInfo: string): string | Promise<string>
```

Callback to be called when the backup procedure is started. Developer could override this method to restore.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| backupInfo | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string \| Promise & lt;string & gt; |

## onProcess

```TypeScript
onProcess(): string
```

Callback to be called when getting backup/restore process info. Developer could override this method to provide the backup/restore process info.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## onRelease

```TypeScript
onRelease(scenario: number): Promise<void>
```

Callback to be called before extension ability exits. Developer could override this method to clean abnormal data.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scenario | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## onRestore

```TypeScript
onRestore(bundleVersion: BundleVersion): void
```

Callback to be called when the restore procedure is started. Developer could override this method to restore from copies for various bundle versions.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleVersion | [BundleVersion](arkts-corefile-application-backupextensionability-bundleversion-i.md) | Yes |

## onRestoreEx

```TypeScript
onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string | Promise<string>
```

Callback to be called when the restore procedure is started. Developer could override this method to restore.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleVersion | [BundleVersion](arkts-corefile-application-backupextensionability-bundleversion-i.md) | Yes |
| restoreInfo | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string \| Promise & lt;string & gt; |

## context

```TypeScript
context: BackupExtensionContext
```

Indicates backup extension ability context.

**Type:** [BackupExtensionContext](arkts-corefile-file-backupextensioncontext-backupextensioncontext-c.md)

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Backup
