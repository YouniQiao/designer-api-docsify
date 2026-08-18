# MovingPhoto

动态照片对象。 > **说明：** > > - 本Interface首批接口从API version 12开始支持。

**起始版本：** 23

<!--Device-photoAccessHelper-interface MovingPhoto--><!--Device-photoAccessHelper-interface MovingPhoto-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
```

## getUri

```TypeScript
getUri(): string
```

获取动态照片的uri。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MovingPhoto-getUri(): string--><!--Device-MovingPhoto-getUri(): string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## getUri

```TypeScript
getUri(): string | null
```

Obtains the URI of this moving photo.

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MovingPhoto-getUri(): string | null--><!--Device-MovingPhoto-getUri(): string | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## requestContent

```TypeScript
requestContent(imageFileUri: string, videoFileUri: string): Promise<void>
```

同时请求动态照片的图片内容和视频内容，并写入参数指定的对应的uri中。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MovingPhoto-requestContent(imageFileUri: string, videoFileUri: string): Promise<void>--><!--Device-MovingPhoto-requestContent(imageFileUri: string, videoFileUri: string): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| imageFileUri | string | 是 |
| videoFileUri | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## requestContent

```TypeScript
requestContent(resourceType: ResourceType, fileUri: string): Promise<void>
```

请求指定资源类型的动态照片内容，并写入参数指定的uri中。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MovingPhoto-requestContent(resourceType: ResourceType, fileUri: string): Promise<void>--><!--Device-MovingPhoto-requestContent(resourceType: ResourceType, fileUri: string): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [resourceType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-sceneresource-i.md) | [ResourceType](../../apis-ability-kit/arkts-apis/arkts-ability-errormanager-resourcetype-e.md) | 是 |
| [fileUri](../../apis-core-file-kit/arkts-apis/arkts-file-fileuri.md) | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## requestContent

```TypeScript
requestContent(resourceType: ResourceType): Promise<ArrayBuffer>
```

请求指定资源类型的动态照片内容，以ArrayBuffer的形式返回。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-MovingPhoto-requestContent(resourceType: ResourceType): Promise<ArrayBuffer>--><!--Device-MovingPhoto-requestContent(resourceType: ResourceType): Promise<ArrayBuffer>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [resourceType](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-sceneresource-i.md) | [ResourceType](../../apis-ability-kit/arkts-apis/arkts-ability-errormanager-resourcetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ArrayBuffer & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |
