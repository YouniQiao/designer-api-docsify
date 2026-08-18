# format (System API)

## Modules to Import

```TypeScript
```

## format

```TypeScript
function format(volumeId: string, fsType: string, callback: AsyncCallback<void>): void
```

Formats a volume. This API uses an asynchronous callback to return the result. Currently, only the virtual file allocation table (VFAT), ext4 and exFAT file systems are supported. Only unmounted volumes can be formatted. After a volume is formatted, the UUID, mounting path, and description of the volume will change.

**Since:** 23

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

<!--Device-volumeManager-function format(volumeId: string, fsType: string, callback: AsyncCallback<void>): void--><!--Device-volumeManager-function format(volumeId: string, fsType: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeId | string | Yes |
| fsType | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600008 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600005 |
| 13600002 |
| 13600001 |
| 13900042 |


## format

```TypeScript
function format(volumeId: string, fsType: string): Promise<void>
```

Formats a volume. This API uses a promise to return the result. Currently, only the virtual file allocation table ( VFAT), ext4 and exFAT file systems are supported. Only unmounted volumes can be formatted. After a volume is formatted, the UUID, mounting path, and description of the volume will change.

**Since:** 23

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

<!--Device-volumeManager-function format(volumeId: string, fsType: string): Promise<void>--><!--Device-volumeManager-function format(volumeId: string, fsType: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| volumeId | string | Yes |
| fsType | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13600008 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13600005 |
| 13600002 |
| 13600001 |
| 13900042 |
