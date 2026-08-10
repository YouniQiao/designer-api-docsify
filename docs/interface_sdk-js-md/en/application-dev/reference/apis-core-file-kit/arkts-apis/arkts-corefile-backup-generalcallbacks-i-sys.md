# GeneralCallbacks (System API)

备份和恢复过程中的通用回调。备份服务通过这些回调向客户端通知备份或恢复阶段。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-backup-interface GeneralCallbacks--><!--Device-backup-interface GeneralCallbacks-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { backup } from 'kits/@kit.CoreFileKit';
```

## onBackupSizeReport

```TypeScript
onBackupSizeReport?: OnBackupSizeReport
```

备份服务返回结果或进度信息时触发的回调。返回框架扫描到的应用待备份数据量信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-GeneralCallbacks-onBackupSizeReport?: OnBackupSizeReport--><!--Device-GeneralCallbacks-onBackupSizeReport?: OnBackupSizeReport-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onFileReadyBatch

```TypeScript
onFileReadyBatch?: OnFileReadyBatch
```

备份服务向客户端发送文件时触发的回调。File参数表示发送给客户端的文件。返回的文件归备份服务所有，客户端关闭文件句柄后由备份服务清理。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GeneralCallbacks-onFileReadyBatch?: OnFileReadyBatch--><!--Device-GeneralCallbacks-onFileReadyBatch?: OnFileReadyBatch-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 13900005 | I/O error |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 13900025 | No space left on device |
| 13600001 | IPC error |
| 13900011 | Out of memory |

## onProcess

```TypeScript
onProcess(bundleName: string, process: string): void
```

备份服务返回结果或进度信息时触发的回调。返回应用的处理结果或进度信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GeneralCallbacks-onProcess(bundleName: string, process: string): void--><!--Device-GeneralCallbacks-onProcess(bundleName: string, process: string): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 触发回调的应用名称。 |
| process | string | Yes | 应用备份或恢复的进度信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 13900005 | I/O error |
| 13500008 | Untar error |
| 13900001 | Operation not permitted |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 13500006 | Tar error |
| 13900025 | No space left on device |
| 13600001 | IPC error |
| 13900011 | Out of memory |

## onProcess

```TypeScript
onProcess: OnProcess
```

备份服务返回结果或进度信息时触发的回调。返回应用的处理结果或进度信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GeneralCallbacks-onProcess: OnProcess--><!--Device-GeneralCallbacks-onProcess: OnProcess-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 13900020 | Invalid argument |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 13900005 | I/O error |
| 13500008 | Untar error |
| 13900001 | Operation not permitted |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 13500006 | Tar error |
| 13900025 | No space left on device |
| 13600001 | IPC error |
| 13900011 | Out of memory |

## onResultReport

```TypeScript
onResultReport(bundleName: string, result: string): void
```

备份服务返回结果信息时触发的回调。第一个字符串参数表示触发回调的应用名称。第二个字符串参数表示应用的处理结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GeneralCallbacks-onResultReport(bundleName: string, result: string): void--><!--Device-GeneralCallbacks-onResultReport(bundleName: string, result: string): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 触发回调的应用名称。 |
| result | string | Yes | 应用备份或恢复的结果信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 13900005 | I/O error |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 13900025 | No space left on device |
| 13600001 | IPC error |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

## onResultReport

```TypeScript
onResultReport: OnResultReport
```

备份服务返回结果信息时触发的回调。第一个字符串参数表示触发回调的应用名称。第二个字符串参数表示应用的处理结果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GeneralCallbacks-onResultReport: OnResultReport--><!--Device-GeneralCallbacks-onResultReport: OnResultReport-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 13900005 | I/O error |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 13900025 | No space left on device |
| 13600001 | IPC error |
| 13900042 | Unknown error |
| 13900011 | Out of memory |

## onAllBundlesEnd

```TypeScript
onAllBundlesEnd: AsyncCallback<undefined>
```

所有应用的备份或恢复完成或异常中止时触发的回调。

**Type:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;undefined&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-GeneralCallbacks-onAllBundlesEnd: AsyncCallback<undefined>--><!--Device-GeneralCallbacks-onAllBundlesEnd: AsyncCallback<undefined>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onBackupServiceDied

```TypeScript
onBackupServiceDied: Callback<undefined>
```

备份服务异常死亡时触发的回调。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;undefined&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-GeneralCallbacks-onBackupServiceDied: Callback<undefined>--><!--Device-GeneralCallbacks-onBackupServiceDied: Callback<undefined>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onBundleBegin

```TypeScript
onBundleBegin: AsyncCallback<string, void | string>
```

应用备份或恢复开始时触发的回调。第一个字符串参数表示应用名称。发生BusinessError时，第二个字符串参数返回对应的应用名称。

**Type:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string, void \| string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-GeneralCallbacks-onBundleBegin: AsyncCallback<string, void | string>--><!--Device-GeneralCallbacks-onBundleBegin: AsyncCallback<string, void | string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onBundleEnd

```TypeScript
onBundleEnd: AsyncCallback<string, void | string>
```

应用备份或恢复成功结束或异常中止时触发的回调。第一个字符串参数表示应用名称。发生BusinessError时，第二个字符串参数返回对应的应用名称。

**Type:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string, void \| string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-GeneralCallbacks-onBundleEnd: AsyncCallback<string, void | string>--><!--Device-GeneralCallbacks-onBundleEnd: AsyncCallback<string, void | string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onFileReady

```TypeScript
onFileReady: AsyncCallback<File>
```

备份服务向客户端发送文件时触发的回调。File参数表示发送给客户端的文件。 返回的文件归备份服务所有，客户端关闭文件句柄后由备份服务清理。

**Type:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;File&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-GeneralCallbacks-onFileReady: AsyncCallback<File>--><!--Device-GeneralCallbacks-onFileReady: AsyncCallback<File>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

## onMigrateResult

```TypeScript
onMigrateResult?: AsyncCallback<string, void | string>
```

文件迁移流程结束时触发的回调。第一个字符串参数表示应用名称。发生BusinessError时，第二个字符串参数返回对应的应用名称。

**Type:** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string, void \| string&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GeneralCallbacks-onMigrateResult?: AsyncCallback<string, void | string>--><!--Device-GeneralCallbacks-onMigrateResult?: AsyncCallback<string, void | string>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Backup

**System API:** This is a system API.

