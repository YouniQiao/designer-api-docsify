# MovingPhoto

MovingPhoto provides APIs for managing a moving photo instance.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface MovingPhoto--><!--Device-photoAccessHelper-interface MovingPhoto-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## getUri

```TypeScript
getUri(): string
```

Obtains the URI of this moving photo.

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MovingPhoto-getUri(): string--><!--Device-MovingPhoto-getUri(): string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | URI of the moving photo obtained. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |
| 14000011 | System inner fail |

## getUri

```TypeScript
getUri(): string | null
```

Obtains the URI of this moving photo.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MovingPhoto-getUri(): string | null--><!--Device-MovingPhoto-getUri(): string | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Returns uri of the moving photo, if the operation fails, returns null |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## requestContent

```TypeScript
requestContent(imageFileUri: string, videoFileUri: string): Promise<void>
```

Requests the image data and video data of this moving photo and writes them to the specified URIs, respectively. This API uses a promise to return the result.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MovingPhoto-requestContent(imageFileUri: string, videoFileUri: string): Promise<void>--><!--Device-MovingPhoto-requestContent(imageFileUri: string, videoFileUri: string): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageFileUri | string | 是 | URI to which the image data of the moving photo is to be written. Example: **"file://com.example.temptest/data/storage/el2/base/haps/ImageFile.jpg"**. |
| videoFileUri | string | 是 | URI to which the video data of the moving photo is to be written. Example: **"file://com.example.temptest/data/storage/el2/base/haps/VideoFile.mp4"**. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied |
| 14000011 | System inner fail. Possible causes: &lt;br&gt;1. The database is corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## requestContent

```TypeScript
requestContent(resourceType: ResourceType, fileUri: string): Promise<void>
```

Requests the moving photo content of the specified resource type and writes it to the specified URI. This API uses a promise to return the result.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MovingPhoto-requestContent(resourceType: ResourceType, fileUri: string): Promise<void>--><!--Device-MovingPhoto-requestContent(resourceType: ResourceType, fileUri: string): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceType | [ResourceType](../../apis-ability-kit/arkts-apis/arkts-ability-errormanager-resourcetype-e.md) | 是 | Resource type of the moving photo content to request. |
| fileUri | string | 是 | URI to which the moving photo content is to be written. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied |
| 14000011 | System inner fail. Possible causes: &lt;br&gt;1. The database is corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## requestContent

```TypeScript
requestContent(resourceType: ResourceType): Promise<ArrayBuffer>
```

Requests the moving photo content of the specified resource type and returns it in ArrayBuffer format. This API uses a promise to return the result.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MovingPhoto-requestContent(resourceType: ResourceType): Promise<ArrayBuffer>--><!--Device-MovingPhoto-requestContent(resourceType: ResourceType): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resourceType | [ResourceType](../../apis-ability-kit/arkts-apis/arkts-ability-errormanager-resourcetype-e.md) | 是 | Resource type of the moving photo content to request. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;ArrayBuffer&gt; | Promise used to return the requested content in an ArrayBuffer. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied |
| 14000011 | System inner fail. Possible causes: &lt;br&gt;1. The database is corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

