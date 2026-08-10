# unmount (System API)

## Modules to Import

```TypeScript
import { volumeManager } from 'kits/@kit.CoreFileKit';
```

## unmount

```TypeScript
function unmount(volumeId: string, callback: AsyncCallback<void>): void
```

卸载指定卷设备，使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MOUNT_UNMOUNT_MANAGER

<!--Device-volumeManager-function unmount(volumeId: string, callback: AsyncCallback<void>): void--><!--Device-volumeManager-function unmount(volumeId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeId | string | Yes | 卷设备id。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 卸载指定卷设备之后的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13600008 | No such object. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600005 | Incorrect volume state. |
| 13600004 | Failed to unmount. |
| 13600002 | Not supported filesystem. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


## unmount

```TypeScript
function unmount(volumeId: string): Promise<void>
```

卸载指定卷设备，使用Promise异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MOUNT_UNMOUNT_MANAGER

<!--Device-volumeManager-function unmount(volumeId: string): Promise<void>--><!--Device-volumeManager-function unmount(volumeId: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeId | string | Yes | 卷设备id。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13600008 | No such object. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600005 | Incorrect volume state. |
| 13600004 | Failed to unmount. |
| 13600002 | Not supported filesystem. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

