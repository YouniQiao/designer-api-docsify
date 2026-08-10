# format (System API)

## Modules to Import

```TypeScript
import { volumeManager } from 'kits/@kit.CoreFileKit';
```

## format

```TypeScript
function format(volumeId: string, fsType: string, callback: AsyncCallback<void>): void
```

对指定卷设备进行格式化，使用callback异步回调。当前仅支持vfat和exfat两种文件系统类型的格式化，只有处于卸载状态的卷设备可以进行格式化，格式化后卷设备的uuid、挂载路径和卷设备描述均会发生变化。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

<!--Device-volumeManager-function format(volumeId: string, fsType: string, callback: AsyncCallback<void>): void--><!--Device-volumeManager-function format(volumeId: string, fsType: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeId | string | Yes | 卷设备id。 |
| fsType | string | Yes | 文件系统类型(vfat或者exfat)。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 对指定卷设备格式化后的回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The input parameter is invalid.Possible causes: 1.Mandatory parameters are left unspecified; &lt;br&gt;2.Incorrect parameter types. |
| 13600008 | No such object. |
| 201 | Permission verification failed. |
| 202 | The caller is not a system application. |
| 13600005 | Incorrect volume state. |
| 13600002 | Not supported filesystem. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |


## format

```TypeScript
function format(volumeId: string, fsType: string): Promise<void>
```

对指定卷设备进行格式化，使用Promise异步回调。当前仅支持vfat和exfat两种文件系统类型的格式化，只有处于卸载状态的卷设备可以进行格式化，格式化后卷设备的uuid、挂载路径和卷设备描述均会发生变化。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MOUNT_FORMAT_MANAGER

<!--Device-volumeManager-function format(volumeId: string, fsType: string): Promise<void>--><!--Device-volumeManager-function format(volumeId: string, fsType: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.StorageService.Volume

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| volumeId | string | Yes | 卷设备id。 |
| fsType | string | Yes | 文件系统类型（vfat或者exfat）。 |

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
| 13600002 | Not supported filesystem. |
| 13600001 | IPC error. |
| 13900042 | Unknown error. |

