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

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900005 |
| 13900011 |
| 13900025 |
| 13900042 |


## getLocalCapabilities

```TypeScript
function getLocalCapabilities(callback: AsyncCallback<FileData>): void
```

Obtain a Json file that describes local capabilities.

**Since:** 10

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900005 |
| 13900011 |
| 13900025 |
| 13900042 |


## getLocalCapabilities

```TypeScript
function getLocalCapabilities(dataList: Array<IncrementalBackupTime>): Promise<FileData>
```

Obtain a json file that describes local capabilities.

**Since:** 12

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [dataList](../../apis-arkui/arkts-apis/arkts-arkui-arkui-advanced-gridobjectsortcomponent-gridobjectsortcomponent-s.md) | Array&lt;[IncrementalBackupTime](arkts-corefile-backup-incrementalbackuptime-i-sys.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600001 |
| 13900005 |
| 13900011 |
| 13900025 |
| 13900042 |
