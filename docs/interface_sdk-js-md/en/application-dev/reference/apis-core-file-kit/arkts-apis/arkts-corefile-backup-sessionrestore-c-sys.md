# SessionRestore (System API)

Control class for restore procedure.

**Since:** 10

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## appendBundles

```TypeScript
appendBundles(remoteCapabilitiesFd: number, bundlesToBackup: string[], infos?: string[]): Promise<void>
```

Append new bundles and restoreInfos to be restore up during the restore.

**Since:** 12

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| remoteCapabilitiesFd | number | Yes |
| bundlesToBackup | string[] | Yes |
| infos | string[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900001 |
| 13900005 |
| 13900011 |
| 13900020 |
| 13900025 |
| 13900042 |

## appendBundles

```TypeScript
appendBundles(remoteCapabilitiesFd: number, bundlesToBackup: string[], callback: AsyncCallback<void>): void
```

Append new bundles to be restore up during the restore.

**Since:** 10

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| remoteCapabilitiesFd | number | Yes |
| bundlesToBackup | string[] | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900001 |
| 13900005 |
| 13900011 |
| 13900020 |
| 13900025 |
| 13900042 |

## cancel

```TypeScript
cancel(bundleName: string): number
```

cancel the application being restore.

**Since:** 18

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## cleanBundleTempDir

```TypeScript
cleanBundleTempDir(bundleName: string): Promise<boolean>
```

Provides an interface for the tool to clear temporary directories

**Since:** 20

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## constructor

```TypeScript
constructor(callbacks: GeneralCallbacks)
```

Constructor for obtaining the instance of the SessionBackup class.

**Since:** 10

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [callbacks](../../apis-ability-kit/arkts-apis/arkts-ability-appmanager-appstatefilter-i-sys.md) | [GeneralCallbacks](arkts-corefile-backup-generalcallbacks-i-sys.md) | Yes |

## getApkFileHandle

```TypeScript
getApkFileHandle(path: string, fileName: string): Promise<FileData>
```

Get the file handle of an APK file.

**Since:** 26.0.0

**Required permissions:** ohos.permission.BACKUP

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| fileName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[FileData](arkts-corefile-backup-filedata-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900001 |
| 13900020 |

## getCompatibilityInfo

```TypeScript
getCompatibilityInfo(bundleName: string, extInfo: string): Promise<string>
```

Provides an interface for the tool to get compatibility info.

**Since:** 20

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| extInfo | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getFileHandle

```TypeScript
getFileHandle(fileMeta: FileMeta): Promise<void>
```

Request to get a shared file from the service. This interface is part of the zero-copy feature. Developers could get the file through onFileReady callback. When the client accomplished the file, use publishFile to publish.

**Since:** 10

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900001 |
| 13900020 |
| 13900042 |

## getFileHandle

```TypeScript
getFileHandle(fileMeta: FileMeta, callback: AsyncCallback<void>): void
```

Request to get a shared file from the service. This interface is part of the zero-copy feature. Developers could get the file through onFileReady callback. When the client accomplished the file, use publishFile to publish.

**Since:** 10

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900001 |
| 13900020 |
| 13900042 |

## getFileHandles

```TypeScript
getFileHandles(fileMeta: FileMeta): Promise<void>
```

Request to get shared files from the service. This interface is part of the zero-copy feature. Developers could get the file through onFileReadyBatch callback. When the client accomplished the file, use publishFile to publish.

**Since:** 26.0.0

**Required permissions:** ohos.permission.BACKUP

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900001 |
| 13900020 |

## getLocalCapabilities

```TypeScript
getLocalCapabilities(): Promise<FileData>
```

Obtain a Json file that describes local capabilities.

**Since:** 18

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900001 |
| 13900020 |
| 13900042 |

## migrateFile

```TypeScript
migrateFile(pathInfo: PathInfo, fileMeta: FileMeta): Promise<void>
```

Migrate file from source path to destination path.

**Since:** 26.0.0

**Required permissions:** ohos.permission.BACKUP

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [pathInfo](../../apis-arkui/arkts-components/arkts-arkui-navdestinationcontext-i.md) | [PathInfo](arkts-corefile-backup-pathinfo-i-sys.md) | Yes |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600001 |
| 13900001 |
| 13900020 |

## publishFile

```TypeScript
publishFile(fileMeta: FileMeta): Promise<void>
```

Publish the file handle to the backup service to make the service aware that the file's content is ready. This interface is part of the zero-copy feature.

**Since:** 10

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900001 |
| 13900020 |
| 13900042 |

## publishFile

```TypeScript
publishFile(fileMeta: FileMeta, callback: AsyncCallback<void>): void
```

Publish the file handle to the backup service to make the service aware that the file's content is ready. This interface is part of the zero-copy feature.

**Since:** 10

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| fileMeta | [FileMeta](arkts-corefile-backup-filemeta-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900001 |
| 13900020 |
| 13900042 |

## release

```TypeScript
release(): Promise<void>
```

End restore process

**Since:** 12

**Required permissions:** ohos.permission.BACKUP

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600001 |
| 13900001 |
| 13900005 |
| 13900042 |
