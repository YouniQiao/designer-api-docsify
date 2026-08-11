# BackupExtensionAbility

Class to be override for backup extension ability.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class BackupExtensionAbility--><!--Device-unnamed-declare class BackupExtensionAbility-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

## Modules to Import

```TypeScript
import { BundleVersion } from 'kits/@kit.CoreFileKit';
```

## getBackupCompatibilityInfo

```TypeScript
getBackupCompatibilityInfo(extInfo: string) : Promise<string>
```

Callback to be called when getting application backup compatibilityInfo.Developer could override this method to provide the backup compatibilityInfo.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupExtensionAbility-getBackupCompatibilityInfo(extInfo: string) : Promise<string>--><!--Device-BackupExtensionAbility-getBackupCompatibilityInfo(extInfo: string) : Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| extInfo | string | Yes | Information about the capabilities of the peer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Return backup compatibilityInfo, support promise. |

## getBackupInfo

```TypeScript
getBackupInfo(): string
```

Callback to be called when getting application backupInfo.Developer could override this method to provide the backupInfo.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupExtensionAbility-getBackupInfo(): string--><!--Device-BackupExtensionAbility-getBackupInfo(): string-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the backup application's info. |

## getRestoreCompatibilityInfo

```TypeScript
getRestoreCompatibilityInfo(extInfo: string) : Promise<string>
```

Callback to be called when getting application restore compatibilityInfo.Developer could override this method to provide the restore compatibilityInfo.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BackupExtensionAbility-getRestoreCompatibilityInfo(extInfo: string) : Promise<string>--><!--Device-BackupExtensionAbility-getRestoreCompatibilityInfo(extInfo: string) : Promise<string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| extInfo | string | Yes | Information about the capabilities of the peer. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Return restore compatibilityInfo, support promise. |

