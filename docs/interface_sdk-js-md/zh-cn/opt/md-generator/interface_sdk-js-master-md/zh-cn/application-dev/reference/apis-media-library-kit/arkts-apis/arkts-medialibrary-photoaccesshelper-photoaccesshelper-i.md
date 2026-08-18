# PhotoAccessHelper

提供访问照片和相册的功能。

**起始版本：** 23

<!--Device-photoAccessHelper-interface PhotoAccessHelper--><!--Device-photoAccessHelper-interface PhotoAccessHelper-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
```

## applyChanges

```TypeScript
applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>
```

提交媒体变更请求，使用Promise方式返回结果。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>--><!--Device-PhotoAccessHelper-applyChanges(mediaChangeRequest: MediaChangeRequest): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mediaChangeRequest | [MediaChangeRequest](arkts-medialibrary-photoaccesshelper-mediachangerequest-i.md) | 是 |

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

## checkPhotoUrisReadPermission

```TypeScript
checkPhotoUrisReadPermission(uris: string[]): Promise<Map<string, MediaAssetPermissionState>>
```

查询URI对应资产的读权限，以及资产是否存在。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoAccessHelper-checkPhotoUrisReadPermission(uris: string[]): Promise<Map<string, MediaAssetPermissionState>>--><!--Device-PhotoAccessHelper-checkPhotoUrisReadPermission(uris: string[]): Promise<Map<string, MediaAssetPermissionState>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uris | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Map&lt;string, [MediaAssetPermissionState](arkts-medialibrary-photoaccesshelper-mediaassetpermissionstate-e.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## createAsset

```TypeScript
createAsset(photoType: PhotoType, extension: string, options: CreateOptions, callback: AsyncCallback<string>): void
```

指定文件类型、后缀和创建选项，创建图片或视频资源。使用callback方式返回结果。 在未申请相册管理模块权限'ohos.permission.WRITE_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考 [保存媒体库资源](../../../media/medialibrary/photoAccessHelper-savebutton.md)。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, options: CreateOptions, callback: AsyncCallback<string>): void--><!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, options: CreateOptions, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoType | [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md) | 是 |
| extension | string | 是 |
| options | [CreateOptions](arkts-medialibrary-photoaccesshelper-createoptions-i.md) | 是 | 创建选项，当前仅支持'title'，例如{title: 'testPhoto'}。 <br>**注意：** <br>传入'subtype'选项，配置不生效，仅支持保存DEFAULT类型图片。 <br>文件名中不允许出现非法英文字符，包括： . .. \ / : ? " ' ` &lt; &gt; \|
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## createAsset

```TypeScript
createAsset(photoType: PhotoType, extension: string, callback: AsyncCallback<string>): void
```

指定文件类型和后缀，创建图片或视频资源，使用callback方式返回结果。 在未申请相册管理模块权限'ohos.permission.WRITE_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考 [保存媒体库资源](../../../media/medialibrary/photoAccessHelper-savebutton.md)。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, callback: AsyncCallback<string>): void--><!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoType | [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md) | 是 |
| extension | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## createAsset

```TypeScript
createAsset(photoType: PhotoType, extension: string, options?: CreateOptions): Promise<string>
```

指定文件类型、后缀和创建选项，创建图片或视频资源，以Promise方式返回结果。 在未申请相册管理模块权限'ohos.permission.WRITE_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考 [保存媒体库资源](../../../media/medialibrary/photoAccessHelper-savebutton.md)。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, options?: CreateOptions): Promise<string>--><!--Device-PhotoAccessHelper-createAsset(photoType: PhotoType, extension: string, options?: CreateOptions): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoType | [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md) | 是 |
| extension | string | 是 |
| options | [CreateOptions](arkts-medialibrary-photoaccesshelper-createoptions-i.md) | 否 | 创建选项，当前仅支持'title'，例如{title: 'testPhoto'}。 <br>**注意：** <br>传入'subtype'选项，配置不生效，仅支持保存DEFAULT类型图片。 <br>文件名中不允许出现非法英文字符，包括： . .. \ / : ? " ' ` &lt; &gt; \|

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## createAssetWithShortTermPermission

```TypeScript
createAssetWithShortTermPermission(photoCreationConfig: PhotoCreationConfig): Promise<string>
```

接口提供给应用调用，支持首次调用后拉起保存确认弹框。在用户同意保存后返回已创建并授予保存权限的uri，支持应用使用uri写入图片/视频。 在用户"同意"后的5分钟之内，同一个应用再次调用接口，支持无需弹框确认自动返回已授权的uri给应用，支持应用保存图片/视频。退出应用会结束授权，再次进入需要重新弹出弹框进行确认授权。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAssetWithShortTermPermission(photoCreationConfig: PhotoCreationConfig): Promise<string>--><!--Device-PhotoAccessHelper-createAssetWithShortTermPermission(photoCreationConfig: PhotoCreationConfig): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoCreationConfig | [PhotoCreationConfig](arkts-medialibrary-photoaccesshelper-photocreationconfig-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## createAssetWithShortTermPermissionEx

```TypeScript
createAssetWithShortTermPermissionEx(creationSetting: CreationSetting): Promise<string>
```

应用调用该接口后，系统会首次拉起保存确认弹框。使用Promise异步回调。 > **说明：** > > - 用户同意保存后，接口将返回已创建并授予保存权限的URI，应用可使用该URI写入图片/视频。 > > - 在用户同意后的5分钟内，若同一应用再次调用此接口，系统将无需弹框确认，直接返回已授权的URI，供应用保存图片/视频。退出应用会结束授权，再次进入需要重新弹出弹框进行确认授权。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoAccessHelper-createAssetWithShortTermPermissionEx(creationSetting: CreationSetting): Promise<string>--><!--Device-PhotoAccessHelper-createAssetWithShortTermPermissionEx(creationSetting: CreationSetting): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| creationSetting | [CreationSetting](arkts-medialibrary-photoaccesshelper-creationsetting-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## createDeleteRequest

```TypeScript
createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void
```

创建一个弹出框来删除照片，删除的文件进入到回收站，使用callback方式返回结果。 > **说明：** > > 从API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [deleteAssets](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteassets)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void--><!--Device-PhotoAccessHelper-createDeleteRequest(uriList: Array<string>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [uriList](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 14000011 |

## createDeleteRequest

```TypeScript
createDeleteRequest(uriList: Array<string>): Promise<void>
```

创建一个弹出框来删除照片，删除的文件进入到回收站，使用Promise方式返回结果。 > **说明：** > > 从API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [deleteAssets](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteassets)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createDeleteRequest(uriList: Array<string>): Promise<void>--><!--Device-PhotoAccessHelper-createDeleteRequest(uriList: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [uriList](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 14000011 |

## createPhotoAsset

```TypeScript
createPhotoAsset(photoType: PhotoType, extension: string, title?: string): Promise<string>
```

指定文件类型、后缀和标题，创建图片或视频资源。使用Promise异步回调。 在未申请相册管理模块权限'ohos.permission.WRITE_IMAGEVIDEO'时，可以使用安全控件或授权弹窗的方式创建媒体资源，详情请参考 [开发指南](../../../media/medialibrary/photoAccessHelper-savebutton.md)。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-createPhotoAsset(photoType: PhotoType, extension: string, title?: string): Promise<string>--><!--Device-PhotoAccessHelper-createPhotoAsset(photoType: PhotoType, extension: string, title?: string): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoType | [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md) | 是 |
| extension | string | 是 |
| title | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) | The scenario parameter verification fails. Possible causes: <br>1. The extension format is unsupported <br>2. Title contains unsupported character, such as . .. \ / : ? " ' ` &lt; &gt; \|

## getAlbumIdByLpath

```TypeScript
getAlbumIdByLpath(lpath: string): Promise<number>
```

根据相册的虚拟路径获取媒体库相册的ID。使用Promise异步回调。 该接口仅支持以下相册：相机相册（'/DCIM/Camera'）、截图相册（'/Pictures/Screenshots'）和屏幕录制相册（'/Pictures/Screenrecords'）。 ​**模型约束**： 此接口仅可在Stage模型下使用。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoAccessHelper-getAlbumIdByLpath(lpath: string): Promise<int>--><!--Device-PhotoAccessHelper-getAlbumIdByLpath(lpath: string): Promise<int>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| lpath | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## getAlbums

```TypeScript
getAlbums(
      type: AlbumType,
      subtype: AlbumSubtype,
      options: FetchOptions,
      callback: AsyncCallback<FetchResult<Album>>
    ): void
```

根据检索选项和相册类型获取相册，使用callback方式返回结果。 获取相册前，确保相册已存在。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getAlbums(      type: AlbumType,      subtype: AlbumSubtype,      options: FetchOptions,      callback: AsyncCallback<FetchResult<Album>>    ): void--><!--Device-PhotoAccessHelper-getAlbums(      type: AlbumType,      subtype: AlbumSubtype,      options: FetchOptions,      callback: AsyncCallback<FetchResult<Album>>    ): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AlbumType](arkts-medialibrary-photoaccesshelper-albumtype-e.md) | 是 |
| subtype | [AlbumSubtype](arkts-medialibrary-sendablephotoaccesshelper-albumsubtype-e.md) | 是 |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## getAlbums

```TypeScript
getAlbums(type: AlbumType, subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void
```

根据相册类型获取相册，使用callback方式返回结果。 获取相册前需先保证相册存在。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getAlbums(type: AlbumType, subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void--><!--Device-PhotoAccessHelper-getAlbums(type: AlbumType, subtype: AlbumSubtype, callback: AsyncCallback<FetchResult<Album>>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AlbumType](arkts-medialibrary-photoaccesshelper-albumtype-e.md) | 是 |
| subtype | [AlbumSubtype](arkts-medialibrary-sendablephotoaccesshelper-albumsubtype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## getAlbums

```TypeScript
getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>
```

根据检索选项和相册类型获取相册，使用Promise方式返回结果。 在获取相册之前，确保相册已存在。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>--><!--Device-PhotoAccessHelper-getAlbums(type: AlbumType, subtype: AlbumSubtype, options?: FetchOptions): Promise<FetchResult<Album>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AlbumType](arkts-medialibrary-photoaccesshelper-albumtype-e.md) | 是 |
| subtype | [AlbumSubtype](arkts-medialibrary-sendablephotoaccesshelper-albumsubtype-e.md) | 是 |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;FetchResult & lt;Album & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## getAssets

```TypeScript
getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void
```

获取相册中的文件。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void--><!--Device-PhotoAccessHelper-getAssets(options: FetchOptions, callback: AsyncCallback<FetchResult<PhotoAsset>>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;PhotoAsset&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## getAssets

```TypeScript
getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>
```

获取图片和视频资源，使用Promise方式返回结果。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>--><!--Device-PhotoAccessHelper-getAssets(options: FetchOptions): Promise<FetchResult<PhotoAsset>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;FetchResult & lt;PhotoAsset & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900012 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## getBurstAssets

```TypeScript
getBurstAssets(burstKey: string, options: FetchOptions): Promise<FetchResult<PhotoAsset>>
```

获取连拍照片资源，使用Promise方式返回结果。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-getBurstAssets(burstKey: string, options: FetchOptions): Promise<FetchResult<PhotoAsset>>--><!--Device-PhotoAccessHelper-getBurstAssets(burstKey: string, options: FetchOptions): Promise<FetchResult<PhotoAsset>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| burstKey | string | 是 |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;FetchResult & lt;PhotoAsset & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## getPhotoPickerComponentDefaultAlbumName

```TypeScript
getPhotoPickerComponentDefaultAlbumName(): Promise<string>
```

应用使用PhotoPickerComponent组件选择照片时，支持调用API获取组件默认显示相册的相册名字符串。跟随当前系统语言，支持返回当前语言的相册名。使用Promise异步回调。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-getPhotoPickerComponentDefaultAlbumName(): Promise<string>--><!--Device-PhotoAccessHelper-getPhotoPickerComponentDefaultAlbumName(): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getRecentPhotoInfo

```TypeScript
getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>
```

应用使用RecentPhotoComponent组件查看最近图片时，支持调用API获取最近图片信息。使用Promise异步回调。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>--><!--Device-PhotoAccessHelper-getRecentPhotoInfo(options?: RecentPhotoOptions): Promise<RecentPhotoInfo>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RecentPhotoOptions](arkts-medialibrary-photoaccesshelper-recentphotooptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RecentPhotoInfo](arkts-medialibrary-photoaccesshelper-recentphotoinfo-c.md)&gt; |

## getSupportedPhotoFormats

```TypeScript
getSupportedPhotoFormats(photoType: PhotoType): Promise<Array<string>>
```

接口提供给应用调用，获取媒体库支持的图片或者视频后缀列表。

**起始版本：** 23

<!--Device-PhotoAccessHelper-getSupportedPhotoFormats(photoType: PhotoType): Promise<Array<string>>--><!--Device-PhotoAccessHelper-getSupportedPhotoFormats(photoType: PhotoType): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoType | [PhotoType](arkts-medialibrary-sendablephotoaccesshelper-phototype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## offMediaLibraryAvailability

```TypeScript
offMediaLibraryAvailability(callback? : Callback<MediaLibraryAvailability>):void
```

取消注册媒体库可用性状态。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoAccessHelper-offMediaLibraryAvailability(callback? : Callback<MediaLibraryAvailability>):void--><!--Device-PhotoAccessHelper-offMediaLibraryAvailability(callback? : Callback<MediaLibraryAvailability>):void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaLibraryAvailability](arkts-medialibrary-photoaccesshelper-medialibraryavailability-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## offPhotoAlbumChange

```TypeScript
offPhotoAlbumChange(callback?: Callback<AlbumChangeInfos>): void
```

注销相册监听。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-offPhotoAlbumChange(callback?: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-offPhotoAlbumChange(callback?: Callback<AlbumChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## offPhotoChange

```TypeScript
offPhotoChange(callback?: Callback<PhotoAssetChangeInfos>): void
```

取消资产的监听。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-offPhotoChange(callback?: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-offPhotoChange(callback?: Callback<PhotoAssetChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## offSinglePhotoAlbumChange

```TypeScript
offSinglePhotoAlbumChange(album?: Album, callback?: Callback<AlbumChangeInfos>): void
```

取消对单个相册的监听。具体规则如下： 1. 不携带任何参数时，取消所有单个相册监听。 2. 携带album，不携带callback时，取消该album下所有callback监听。 3. 携带album和callback时，仅取消指定callback监听。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-offSinglePhotoAlbumChange(album?: Album, callback?: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-offSinglePhotoAlbumChange(album?: Album, callback?: Callback<AlbumChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | 否 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## offSinglePhotoChange

```TypeScript
offSinglePhotoChange(asset?: PhotoAsset, callback?: Callback<PhotoAssetChangeInfos>): void
```

取消单个资产的监听。具体规则如下： 1. 不携带参数时，取消所有单个资产监听。 2. 携带asset，不携带callback时，取消该asset下所有callback监听。 3. 携带asset和callback时，仅取消指定callback监听。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-offSinglePhotoChange(asset?: PhotoAsset, callback?: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-offSinglePhotoChange(asset?: PhotoAsset, callback?: Callback<PhotoAssetChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [asset](../../apis-asset-store-kit/arkts-apis/arkts-security-asset.md) | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 否 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## off_photoAlbumChange

```TypeScript
off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void
```

取消对'photoAlbumChange'相册的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-off(type: 'photoAlbumChange', callback?: Callback<AlbumChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoAlbumChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## off_photoChange

```TypeScript
off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void
```

取消对'photoChange'媒体资产的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-off(type: 'photoChange', callback?: Callback<PhotoAssetChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## onMediaLibraryAvailability

```TypeScript
onMediaLibraryAvailability(callback: Callback<MediaLibraryAvailability>): void
```

注册媒体库可用性状态，返回媒体库当前可用状态和不可用原因。使用callback异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoAccessHelper-onMediaLibraryAvailability(callback: Callback<MediaLibraryAvailability>): void--><!--Device-PhotoAccessHelper-onMediaLibraryAvailability(callback: Callback<MediaLibraryAvailability>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MediaLibraryAvailability](arkts-medialibrary-photoaccesshelper-medialibraryavailability-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## onPhotoAlbumChange

```TypeScript
onPhotoAlbumChange(callback: Callback<AlbumChangeInfos>): void
```

注册相册监听。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-onPhotoAlbumChange(callback: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-onPhotoAlbumChange(callback: Callback<AlbumChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## onPhotoChange

```TypeScript
onPhotoChange(callback: Callback<PhotoAssetChangeInfos>): void
```

注册对普通资产变化的监听。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-onPhotoChange(callback: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-onPhotoChange(callback: Callback<PhotoAssetChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## onSinglePhotoAlbumChange

```TypeScript
onSinglePhotoAlbumChange(album: Album, callback: Callback<AlbumChangeInfos>): void
```

注册对普通单个相册变化的监听。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-onSinglePhotoAlbumChange(album: Album, callback: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-onSinglePhotoAlbumChange(album: Album, callback: Callback<AlbumChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## onSinglePhotoChange

```TypeScript
onSinglePhotoChange(asset: PhotoAsset, callback: Callback<PhotoAssetChangeInfos>): void
```

注册对普通单个资产变化的监听。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-onSinglePhotoChange(asset: PhotoAsset, callback: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-onSinglePhotoChange(asset: PhotoAsset, callback: Callback<PhotoAssetChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [asset](../../apis-asset-store-kit/arkts-apis/arkts-security-asset.md) | [PhotoAsset](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## on_photoAlbumChange

```TypeScript
on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void
```

注册'photoAlbumChange'监听相册，并通过callback方式返回相册变化结果，可以注册多个callback。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void--><!--Device-PhotoAccessHelper-on(type: 'photoAlbumChange', callback: Callback<AlbumChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoAlbumChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## on_photoChange

```TypeScript
on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void
```

注册'photoChange'监听媒体资产，并通过callback方式返回资产变化结果，可以注册多个callback。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAccessHelper-on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void--><!--Device-PhotoAccessHelper-on(type: 'photoChange', callback: Callback<PhotoAssetChangeInfos>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'photoChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## registerChange

```TypeScript
registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>): void
```

注册指定uri的监听，并通过callback方式返回异步结果。

**起始版本：** 23

<!--Device-PhotoAccessHelper-registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>): void--><!--Device-PhotoAccessHelper-registerChange(uri: string, forChildUris: boolean, callback: Callback<ChangeData>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| forChildUris | boolean | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeData&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |

## release

```TypeScript
release(callback: AsyncCallback<void>): void
```

释放PhotoAccessHelper实例。使用callback异步回调。 当后续不需要使用PhotoAccessHelper实例中的方法时调用。

**起始版本：** 23

<!--Device-PhotoAccessHelper-release(callback: AsyncCallback<void>): void--><!--Device-PhotoAccessHelper-release(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## release

```TypeScript
release(): Promise<void>
```

释放PhotoAccessHelper实例。使用Promise异步回调。 当后续不需要使用PhotoAccessHelper实例中的方法时调用。

**起始版本：** 23

<!--Device-PhotoAccessHelper-release(): Promise<void>--><!--Device-PhotoAccessHelper-release(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## requestPhotoUrisReadPermission

```TypeScript
requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>
```

&lt;!--RP1--&gt;&lt;!--RP1End--&gt;调用接口给未授权的URI进行授权，返回已创建并授予保存权限的URI列表。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>--><!--Device-PhotoAccessHelper-requestPhotoUrisReadPermission(srcFileUris: Array<string>): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| srcFileUris | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## requestPhotoUrisReadPermissionEx

```TypeScript
requestPhotoUrisReadPermissionEx(srcFileUris: Array<string>): Promise<RequestReadPermissionResult>
```

应用调用接口为未授权的URI授权。使用promise异步回调。 返回授权结果，其中包含已创建并授予保存权限的URI列表以及无效的URI列表。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-requestPhotoUrisReadPermissionEx(srcFileUris: Array<string>): Promise<RequestReadPermissionResult>--><!--Device-PhotoAccessHelper-requestPhotoUrisReadPermissionEx(srcFileUris: Array<string>): Promise<RequestReadPermissionResult>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| srcFileUris | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RequestReadPermissionResult](arkts-medialibrary-photoaccesshelper-requestreadpermissionresult-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setAssetCompatibleCapability

```TypeScript
setAssetCompatibleCapability(capability: AssetCompatibleCapability): Promise<void>
```

配置资产兼容能力。系统会对特殊的资产（如高分辨率资产）进行兼容性处理，如果开发者希望获得原始资产需要向系统注册兼容能力。 ​

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoAccessHelper-setAssetCompatibleCapability(capability: AssetCompatibleCapability): Promise<void>--><!--Device-PhotoAccessHelper-setAssetCompatibleCapability(capability: AssetCompatibleCapability): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| capability | [AssetCompatibleCapability](arkts-medialibrary-photoaccesshelper-assetcompatiblecapability-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## showAssetsCreationDialog

```TypeScript
showAssetsCreationDialog(srcFileUris: Array<string>, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>
```

调用接口显示保存确认弹窗。如果用户同意保存，将返回一个已创建并授予保存权限的URI列表（此列表永久生效），应用可使用这些URI写入图片或视频。如果用户拒绝保存，将返回一个空列表。 弹框需显示应用名称，但无法直接获取。因此，调用此接口时，请确保[module.json5配置文件](../../../quick-start/module-configuration-file.md)中的 `abilities`标签已配置`label`和`icon`项。需要注意的是，图标不受`abilities`标签中的`icon`项影响，不支持修改。 > **说明：** > > 当传入URI为沙箱路径时，可正常保存图片/视频，但无界面预览。

**起始版本：** 26.0.0

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-showAssetsCreationDialog(srcFileUris: Array<string>, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>--><!--Device-PhotoAccessHelper-showAssetsCreationDialog(srcFileUris: Array<string>, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| srcFileUris | Array & lt;string & gt; | 是 |
| photoCreationConfigs | Array&lt;[PhotoCreationConfig](arkts-medialibrary-photoaccesshelper-photocreationconfig-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## showAssetsCreationDialogEx

```TypeScript
showAssetsCreationDialogEx(srcFileUris: Array<string>, creationSettings: Array<CreationSetting>): Promise<Array<string>>
```

调用接口显示保存确认弹窗。使用Promise异步回调。 > **说明：** > > - 用户同意后，返回已创建并授予保存权限的URI列表，该列表永久有效，支持写入图片/视频。用户拒绝时，返回空列表。 > > - 弹框需显示应用名称，名称和图标需在[module.json5配置文件](../../../quick-start/module-configuration-file.md)的`abilities`标签中配置 > `label`和`icon`项。 > > - 当传入URI为沙箱路径时，可正常保存图片或视频，但不显示界面预览。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-showAssetsCreationDialogEx(srcFileUris: Array<string>, creationSettings: Array<CreationSetting>): Promise<Array<string>>--><!--Device-PhotoAccessHelper-showAssetsCreationDialogEx(srcFileUris: Array<string>, creationSettings: Array<CreationSetting>): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| srcFileUris | Array & lt;string & gt; | 是 |
| creationSettings | Array&lt;[CreationSetting](arkts-medialibrary-photoaccesshelper-creationsetting-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## showSingleAssetCreationDialogEx

```TypeScript
showSingleAssetCreationDialogEx(srcFileUri: string, creationSetting: CreationSetting, isImageFullyDisplayed: boolean): Promise<string>
```

针对单个图片/视频调用接口显示保存确认弹窗。使用Promise异步回调。 > **说明：** > > - 如果用户同意保存，将返回一个已创建并授予保存权限的URI（此URI永久生效），应用可使用这个URI写入图片或视频。如果用户拒绝保存，将返回一个空字符串。 > > - 弹框需显示应用名称，但无法直接获取。因此，调用此接口时，请确保[module.json5配置文件](../../../quick-start/module-configuration-file.md)中的 > `abilities`标签已配置`label`和`icon`项。需要注意的是，图标不受`abilities`标签中的`icon`项影响，不支持修改。 > > - 当传入URI为沙箱路径时，可正常保存图片/视频，但无界面预览。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAccessHelper-showSingleAssetCreationDialogEx(srcFileUri: string, creationSetting: CreationSetting, isImageFullyDisplayed: boolean): Promise<string>--><!--Device-PhotoAccessHelper-showSingleAssetCreationDialogEx(srcFileUri: string, creationSetting: CreationSetting, isImageFullyDisplayed: boolean): Promise<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| srcFileUri | string | 是 |
| creationSetting | [CreationSetting](arkts-medialibrary-photoaccesshelper-creationsetting-i.md) | 是 |
| isImageFullyDisplayed | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## unRegisterChange

```TypeScript
unRegisterChange(uri: string, callback?: Callback<ChangeData>): void
```

取消指定uri的监听，一个uri可以注册多个监听，存在多个callback监听时，可以取消指定注册的callback的监听；不指定callback时取消该uri的所有监听。

**起始版本：** 23

<!--Device-PhotoAccessHelper-unRegisterChange(uri: string, callback?: Callback<ChangeData>): void--><!--Device-PhotoAccessHelper-unRegisterChange(uri: string, callback?: Callback<ChangeData>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeData&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
