# getLocalCapabilities (System API)

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## getLocalCapabilities

```TypeScript
function getLocalCapabilities(): Promise<FileData>
```

Obtain a Json file that describes local capabilities.

**Since:** 10

**Required permissions:** ohos.permission.BACKUP

<!--Device-backup-function getLocalCapabilities(): Promise<FileData>--><!--Device-backup-function getLocalCapabilities(): Promise<FileData>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FileData&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900025 |
| 13600001 |
| 13900042 |
| 13900011 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, backup } from '@kit.CoreFileKit';

async function getLocalCapabilities() {
  try {
    let fileData = await backup.getLocalCapabilities();
    console.info('getLocalCapabilities success');
    console.info('fileData info:' + fileData.fd);
    fileIo.closeSync(fileData.fd);
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`getLocalCapabilities failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

The capability file can be obtained by using [fileIo.stat](js-apis-file-fs.md#fileiostat) of the [@ohos.file.fs](js-apis-file-fs.md) module. The following is an example of the capability file.

```TypeScript
{
 "backupVersion" : "16.0",
 "bundleInfos" :[{
   "allToBackup" : true,
   "extensionName" : "BackupExtensionAbility",
   "name" : "com.example.hiworld",
   "needToInstall" : false,
   "spaceOccupied" : 0,
   "versionCode" : 1000000,
   "versionName" : "1.0.0"
   }],
 "deviceType" : "default",
 "systemFullName" : "OpenHarmony-4.0.0.0"
}
```


## getLocalCapabilities

```TypeScript
function getLocalCapabilities(callback: AsyncCallback<FileData>): void
```

Obtain a Json file that describes local capabilities.

**Since:** 10

**Required permissions:** ohos.permission.BACKUP

<!--Device-backup-function getLocalCapabilities(callback: AsyncCallback<FileData>): void--><!--Device-backup-function getLocalCapabilities(callback: AsyncCallback<FileData>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FileData&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900005 |
| 13900025 |
| 13600001 |
| 13900042 |
| 13900011 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, backup } from '@kit.CoreFileKit';

try {
  backup.getLocalCapabilities((err: BusinessError, fileData: backup.FileData) => {
    if (err) {
      console.error(`getLocalCapabilities failed. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('getLocalCapabilities success');
    console.info('fileData info:' + fileData.fd);
    fileIo.closeSync(fileData.fd);
  });
} catch (error) {
  let err: BusinessError = error as BusinessError;
  console.error(`getLocalCapabilities failed. Code: ${err.code}, message: ${err.message}`);
}
```

The capability file can be obtained by using [fileIo.stat](js-apis-file-fs.md#fileiostat-1) of the [@ohos.file.fs](js-apis-file-fs.md) module. The following is an example of the capability file.

```TypeScript
{
 "backupVersion" : "16.0",
 "bundleInfos" :[{
   "allToBackup" : true,
   "extensionName" : "BackupExtensionAbility",
   "name" : "com.example.hiworld",
   "needToInstall" : false,
   "spaceOccupied" : 0,
   "versionCode" : 1000000,
   "versionName" : "1.0.0"
   }],
 "deviceType" : "default",
 "systemFullName" : "OpenHarmony-4.0.0.0"
}
```


## getLocalCapabilities

```TypeScript
function getLocalCapabilities(dataList: Array<IncrementalBackupTime>): Promise<FileData>
```

Obtain a json file that describes local capabilities.

**Since:** 12

**Required permissions:** ohos.permission.BACKUP

<!--Device-backup-function getLocalCapabilities(dataList: Array<IncrementalBackupTime>): Promise<FileData>--><!--Device-backup-function getLocalCapabilities(dataList: Array<IncrementalBackupTime>): Promise<FileData>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataList | Array&lt;IncrementalBackupTime&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;FileData&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900005 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900025 |
| 13600001 |
| 13900042 |
| 13900011 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo, backup } from '@kit.CoreFileKit';

async function getLocalCapabilities() {
  try {
    let backupApps: backup.IncrementalBackupTime[] = [{
      bundleName: "com.example.hiworld",
      lastIncrementalTime: 1700107870 // Time of the last incremental backup.
    }];
    let fileData = await backup.getLocalCapabilities(backupApps);
    console.info('getLocalCapabilities success');
    console.info('fileData info:' + fileData.fd);
    fileIo.closeSync(fileData.fd);
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(`getLocalCapabilities failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```
