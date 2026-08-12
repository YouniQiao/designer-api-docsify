# GeneralCallbacks (System API)

General callbacks for both backup and restore procedure.The backup service will notify the client by these callbacks.

**Since:** 10

<!--Device-backup-interface GeneralCallbacks--><!--Device-backup-interface GeneralCallbacks-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from '@kit.CoreFileKit';
```

## onBackupSizeReport

```TypeScript
onBackupSizeReport?: OnBackupSizeReport
```

Callback called when the backup_sa service return result information.The first return string parameter indicates the result of the scanned bundle datasize.

**Since:** 18

<!--Device-GeneralCallbacks-onBackupSizeReport?: OnBackupSizeReport--><!--Device-GeneralCallbacks-onBackupSizeReport?: OnBackupSizeReport-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onFileReadyBatch

```TypeScript
onFileReadyBatch?: OnFileReadyBatch
```

Callback called when the backup service tries to send files to the client.The File argument indicates a file to send to the client.The returned file is owned by the backup service and will be cleaned by the service once the file is closed.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-GeneralCallbacks-onFileReadyBatch?: OnFileReadyBatch--><!--Device-GeneralCallbacks-onFileReadyBatch?: OnFileReadyBatch-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| 13900005 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900025 |
| 13600001 |
| 13900011 |

## onProcess

```TypeScript
onProcess(bundleName: string, process: string): void
```

Callback called when the backup_sa service return result information.The first return string parameter indicates the result of the bundle.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-GeneralCallbacks-onProcess(bundleName: string, process: string): void--><!--Device-GeneralCallbacks-onProcess(bundleName: string, process: string): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| process | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900005 |
| 13500008 |
| 13900001 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13500006 |
| 13900025 |
| 13600001 |
| 13900011 |

## onResultReport

```TypeScript
onResultReport(bundleName: string, result: string): void
```

Callback called when the backup service return result information.The first return string parameter indicates the bundleName that triggers the callback.The second return string parameter indicates the result of the bundle.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

<!--Device-GeneralCallbacks-onResultReport(bundleName: string, result: string): void--><!--Device-GeneralCallbacks-onResultReport(bundleName: string, result: string): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| result | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900005 |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 13900025 |
| 13600001 |
| 13900042 |
| 13900011 |

## onAllBundlesEnd

```TypeScript
onAllBundlesEnd: AsyncCallback<undefined>
```

Callback called when the all the bundles to backup/restore are done or aborted unexpectedly.

**Type:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;undefined&gt;

**Since:** 10

<!--Device-GeneralCallbacks-onAllBundlesEnd: AsyncCallback<undefined>--><!--Device-GeneralCallbacks-onAllBundlesEnd: AsyncCallback<undefined>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onBackupServiceDied

```TypeScript
onBackupServiceDied: Callback<undefined>
```

Callback called when the backup service dies unexpectedly.

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;undefined&gt;

**Since:** 10

<!--Device-GeneralCallbacks-onBackupServiceDied: Callback<undefined>--><!--Device-GeneralCallbacks-onBackupServiceDied: Callback<undefined>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onBundleBegin

```TypeScript
onBundleBegin: AsyncCallback<string, void | string>
```

Callback called when a backup/restore procedure for an bundle is started.The first return string parameter indicates the name of the bundle.The second return string parameter indicates that when BusinessError errors occur,the callback data is the name of the bundle.

**Type:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string, void \| string&gt;

**Since:** 12

<!--Device-GeneralCallbacks-onBundleBegin: AsyncCallback<string, void | string>--><!--Device-GeneralCallbacks-onBundleBegin: AsyncCallback<string, void | string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onBundleEnd

```TypeScript
onBundleEnd: AsyncCallback<string, void | string>
```

Callback called when a backup/restore procedure for an bundle ends successfully or gets aborted unexpectedly.The first return string parameter indicates the name of the bundle.The second return string parameter indicates that when BusinessError errors occur,the callback data is the name of the bundle.

**Type:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string, void \| string&gt;

**Since:** 12

<!--Device-GeneralCallbacks-onBundleEnd: AsyncCallback<string, void | string>--><!--Device-GeneralCallbacks-onBundleEnd: AsyncCallback<string, void | string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onFileReady

```TypeScript
onFileReady: AsyncCallback<File>
```

Callback called when the backup service tries to send files to the client.The File argument indicates a file to send to the client. The returned file is owned by the backup service and will be cleaned by the service once the file is closed.

**Type:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;File&gt;

**Since:** 10

<!--Device-GeneralCallbacks-onFileReady: AsyncCallback<File>--><!--Device-GeneralCallbacks-onFileReady: AsyncCallback<File>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onMigrateResult

```TypeScript
onMigrateResult?: AsyncCallback<string, void | string>
```

Callback called when the migrate result is reported.The first return string parameter indicates the name of the bundle.The second return string parameter indicates that when BusinessError errors occur,the callback data is the name of the bundle.

**Type:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string, void \| string&gt;

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-GeneralCallbacks-onMigrateResult?: AsyncCallback<string, void | string>--><!--Device-GeneralCallbacks-onMigrateResult?: AsyncCallback<string, void | string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.
