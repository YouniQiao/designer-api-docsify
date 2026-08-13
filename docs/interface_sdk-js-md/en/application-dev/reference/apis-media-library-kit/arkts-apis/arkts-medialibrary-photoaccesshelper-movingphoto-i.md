# MovingPhoto

MovingPhoto provides APIs for managing a moving photo instance.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-photoAccessHelper-interface MovingPhoto--><!--Device-photoAccessHelper-interface MovingPhoto-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## getUri

```TypeScript
getUri(): string
```

Obtains the URI of this moving photo.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-MovingPhoto-getUri(): string--><!--Device-MovingPhoto-getUri(): string-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | URI of the moving photo obtained. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |
| 14000011 | System inner fail |

## getUri

```TypeScript
getUri(): string | null
```

Obtains the URI of this moving photo.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MovingPhoto-getUri(): string | null--><!--Device-MovingPhoto-getUri(): string | null-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Returns uri of the moving photo, if the operation fails, returns null |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [23800301](../errorcode-medialibrary.md#23800301-system-internal-error) | Internal system error. It is recommended to retry and check the logs. Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## requestContent

```TypeScript
requestContent(imageFileUri: string, videoFileUri: string): Promise<void>
```

Requests the image data and video data of this moving photo and writes them to the specified URIs, respectively. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MovingPhoto-requestContent(imageFileUri: string, videoFileUri: string): Promise<void>--><!--Device-MovingPhoto-requestContent(imageFileUri: string, videoFileUri: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageFileUri | string | Yes | URI to which the image data of the moving photo is to be written. Example: **"file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg"**. |
| videoFileUri | string | Yes | URI to which the video data of the moving photo is to be written. Example: **"file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4"**. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied |
| 14000011 | System inner fail. Possible causes: &lt;br&gt;1. The database is corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## requestContent

```TypeScript
requestContent(resourceType: ResourceType, fileUri: string): Promise<void>
```

Requests the moving photo content of the specified resource type and writes it to the specified URI. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MovingPhoto-requestContent(resourceType: ResourceType, fileUri: string): Promise<void>--><!--Device-MovingPhoto-requestContent(resourceType: ResourceType, fileUri: string): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceType | ResourceType | Yes | Resource type of the moving photo content to request. |
| fileUri | string | Yes | URI to which the moving photo content is to be written. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied |
| 14000011 | System inner fail. Possible causes: &lt;br&gt;1. The database is corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## requestContent

```TypeScript
requestContent(resourceType: ResourceType): Promise<ArrayBuffer>
```

Requests the moving photo content of the specified resource type and returns it in ArrayBuffer format. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_IMAGEVIDEO

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-MovingPhoto-requestContent(resourceType: ResourceType): Promise<ArrayBuffer>--><!--Device-MovingPhoto-requestContent(resourceType: ResourceType): Promise<ArrayBuffer>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceType | ResourceType | Yes | Resource type of the moving photo content to request. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise used to return the requested content in an ArrayBuffer. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied |
| 14000011 | System inner fail. Possible causes: &lt;br&gt;1. The database is corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

