# BackupExtensionAbility

Class to be override for backup extension ability.

**Since:** 10

**System capability:** SystemCapability.FileManagement.StorageService.Backup

## Modules to Import

```TypeScript
import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';
```

## getBackupCompatibilityInfo

```TypeScript
getBackupCompatibilityInfo(extInfo: string) : Promise<string>
```

Callback to be called when getting application backup compatibilityInfo. Developer could override this method to provide the backup compatibilityInfo.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

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

**Examples**

```TypeScript
class BackupExt extends BackupExtensionAbility {
  async getBackupCompatibilityInfo(extInfo: string): Promise<string> {
    let ret: string = '';
    try {
      // Here JSON is used only as an example. The corresponding judgment logic and relevant fields should be customized by the application.
      if (!extInfo) {
        ret = '{"dbVersion": "1.0", "isThemCardEnable": "true"}';
      } else {
        let extJson: Record<string, string> = JSON.parse(extInfo);
        if (extJson?.requireCompatibility) {
          ret = '{"isSupportBackup": "true"}';
        } else {
          ret = '{"isSupportBackup": "false"}';
        }
      }
    } catch (error) {
      console.error(`getBackupCompatibilityInfo failed with error. Code: ${error.code}, message: ${error.message}`);
    }
    return JSON.stringify(ret);
  }
}
```

## getBackupInfo

```TypeScript
getBackupInfo(): string
```

Callback to be called when getting application backupInfo. Developer could override this method to provide the backupInfo.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| string | Return the backup application's info. |

**Examples**

```TypeScript
class BackupExt extends BackupExtensionAbility {
  getBackupInfo(): string {
    console.info('getBackupInfo ok');
    let info = "app diy info";
    return info;
  }
}
```

## getRestoreCompatibilityInfo

```TypeScript
getRestoreCompatibilityInfo(extInfo: string) : Promise<string>
```

Callback to be called when getting application restore compatibilityInfo. Developer could override this method to provide the restore compatibilityInfo.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

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

**Examples**

```TypeScript
class BackupExt extends BackupExtensionAbility {
  async getRestoreCompatibilityInfo(extInfo: string): Promise<string> {
    let ret: string = '';
    try {
      // Here JSON is used only as an example. The corresponding judgment logic and relevant fields should be customized by the application.
      if (!extInfo) {
        ret = '{"dbVersion": "1.0", "isThemCardEnable": "true"}';
      } else {
        let extJson: Record<string, string> = JSON.parse(extInfo);
        if (extJson?.requireCompatibility) {
          ret = '{"isSupportRestore": "true"}';
        } else {
          ret = '{"isSupportRestore": "false"}';
        }
      }
    } catch (error) {
      console.error(`getRestoreCompatibilityInfo failed with error. Code: ${error.code}, message: ${error.message}`);
    }
    return JSON.stringify(ret);
  }
}
```
