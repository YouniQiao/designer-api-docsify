# SyncFolderAccessor (System API)

A sync root management class that enables the File Manager to access the sync root information registered by third- party cloud disks.

**Since:** 21

**System capability:** SystemCapability.FileManagement.CloudDiskManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { cloudDiskManager } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **SyncFolderAccessor** instance.

**Since:** 21

**Required permissions:** ohos.permission.ACCESS_CLOUD_DISK_INFO

**System capability:** SystemCapability.FileManagement.CloudDiskManager

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## getAllSyncFolders

```TypeScript
getAllSyncFolders(): Promise<Array<SyncFolder>>
```

Obtains information about all registered sync roots. This API uses a promise to return the result.

**Since:** 21

**Required permissions:** ohos.permission.ACCESS_CLOUD_DISK_INFO

**System capability:** SystemCapability.FileManagement.CloudDiskManager

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[SyncFolder](arkts-corefile-clouddiskmanager-syncfolder-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [34400003](../errorcode-clouddiskmanager-sys.md#34400003-ipc-failed) |
| [34400014](../errorcode-clouddiskmanager-sys.md#34400014-system-internal-error) |
| [34400015](../errorcode-clouddiskmanager-sys.md#34400015-cloud-disk-not-allowed) |
