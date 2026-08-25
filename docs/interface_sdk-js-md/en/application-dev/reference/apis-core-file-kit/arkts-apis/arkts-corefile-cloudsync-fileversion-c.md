# FileVersion

Represents the device-cloud file version management class. It allows you to manage historical versions of client- cloud files, obtain the list of historical versions, download historical versions to the local device, replace the current local file with a historical version file, and query and remove conflict flags for version conflicts.

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

## Modules to Import

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## clearFileConflict

```TypeScript
clearFileConflict(uri: string): Promise<void>
```

Clears the version conflict flag of the local file. If a conflict occurs, you need to call this API to clear the conflict flag after the conflict is resolved locally and trigger automatic synchronization. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900002 |
| 13900010 |
| 13900012 |
| 13900020 |
| 14000002 |
| 22400005 |

## constructor

```TypeScript
constructor()
```

A constructor used to create a **FileVersion** instance.

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Error codes:**

| Error Code ID |
| --- |
| 22400005 |

## downloadHistoryVersion

```TypeScript
downloadHistoryVersion(uri: string, versionId: string, callback: Callback<VersionDownloadProgress>): Promise<string>
```

Obtains the content of a file of a specified version based on the version number. You can download a file of a specified version from the cloud to a temporary local path. The application determines whether to replace the original file with the temporary file, or retain or delete the temporary file. The callback returns the file download progress, and the promise returns the URI of the temporary file of an earlier version.

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| versionId | string | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[VersionDownloadProgress](arkts-corefile-cloudsync-versiondownloadprogress-i.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900002 |
| 13900010 |
| 13900012 |
| 13900020 |
| 14000002 |
| 22400002 |
| 22400005 |

## getHistoryVersionList

```TypeScript
getHistoryVersionList(uri: string, versionNumLimit: number): Promise<Array<HistoryVersion>>
```

Obtains the list of historical versions. The returned versions are sorted by modification time. The earlier the modification time, the later the version. This API uses a promise to return the result.If the number of cloud versions is less than the length limit, the list will be returned with the actual number of versions.If the number of cloud versions is greater than or equal to the length limit, the number of the latest versions (specified by **versionNumLimit**) will be returned.

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| versionNumLimit | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[HistoryVersion](arkts-corefile-cloudsync-historyversion-i.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900002 |
| 13900010 |
| 13900012 |
| 13900020 |
| 14000002 |
| 22400002 |
| 22400005 |

## isFileConflict

```TypeScript
isFileConflict(uri: string): Promise<boolean>
```

Obtains the version conflict flag of a local file. This API uses a promise to return the result. This API takes effect only when the application is configured for manual conflict resolution. Otherwise, conflicts are automatically resolved during synchronization, and the return value will be **false**.Once the application is configured for manual conflict resolution, calling this API returns whether the current local file conflicts with the cloud file. The application then prompts the user to handle the conflict. After the conflict is resolved, you need to call the [clearFileConflict](#clearfileconflict) method to clear the conflict flag and synchronize the file to the cloud.

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900002 |
| 13900010 |
| 13900012 |
| 13900020 |
| 14000002 |
| 22400005 |

## replaceFileWithHistoryVersion

```TypeScript
replaceFileWithHistoryVersion(originalUri: string, versionUri: string): Promise<void>
```

Replaces the local file with the file of a historical version. Before replacement, call the [downloadHistoryVersion](#downloadhistoryversion) method to download the selected historical version and obtain its version URI. If this API is called directly without prior download or the version URI is invalid, an exception will be thrown. Once replacement is complete, the temporary file will be automatically deleted. This API uses a promise to return the result.

**Since:** 20

**System capability:** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| originalUri | string | Yes |
| versionUri | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13600001 |
| 13900002 |
| 13900005 |
| 13900008 |
| 13900010 |
| 13900012 |
| 13900020 |
| 14000002 |
| 22400005 |
| 22400007 |
