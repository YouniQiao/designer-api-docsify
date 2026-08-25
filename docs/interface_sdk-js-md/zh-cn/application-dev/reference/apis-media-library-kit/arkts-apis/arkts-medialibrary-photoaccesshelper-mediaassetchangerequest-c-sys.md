# MediaAssetChangeRequest

MediaAssetChangeRequest implements [MediaChangeRequest](arkts-medialibrary-photoaccesshelper-mediachangerequest-i.md).资产变更请求。

> **说明：**&gt;
> - 本Class首批接口从API version 11开始支持。

**继承/实现关系：** MediaAssetChangeRequest implements [MediaChangeRequest](arkts-medialibrary-photoaccesshelper-mediachangerequest-i.md)

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## addResource

```TypeScript
addResource(type: ResourceType, proxy: PhotoProxy): void
```

通过PhotoProxy数据添加资源。

> **注意：**&gt;
> 对于同一个资产变更请求，不支持在成功添加资源后，重复调用该接口。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [ResourceType](../../apis-ability-kit/arkts-apis/arkts-ability-errormanager-resourcetype-e.md) | 是 |
| proxy | [PhotoProxy](arkts-medialibrary-photoaccesshelper-photoproxy-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |
| 14000016 |

## addResourceForPicker

```TypeScript
addResourceForPicker(type: ResourceType, fileUri: string): void
```

通过[fileUri](../../apis-core-file-kit/arkts-apis/arkts-file-fileuri.md)从应用沙箱添加资源。

**起始版本：** 22

**需要权限：** ohos.permission.ACCESS_MEDIALIB_THUMB_DB

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [ResourceType](../../apis-ability-kit/arkts-apis/arkts-ability-errormanager-resourcetype-e.md) | 是 |
| [fileUri](../../apis-core-file-kit/arkts-apis/arkts-file-fileuri.md) | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## createAssetRequest

```TypeScript
static createAssetRequest(context: Context, displayName: string, options?: PhotoCreateOptions): MediaAssetChangeRequest
```

指定待创建的图片或者视频的文件名，创建资产变更请求。待创建的文件名参数规格为：  
- 应包含有效文件主名和图片或视频扩展名。  
- 文件名字符串长度为1~255。  
- 文件主名中不允许出现的非法英文字符。  
API18开始，非法字符包括： \ / : * ? " &lt; &gt; |API10-17，非法字符包括：. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| displayName | string | 是 |
| options | [PhotoCreateOptions](arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [MediaAssetChangeRequest](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000001 |
| 14000011 |

## deleteAssetsPermanentlyWithUri

```TypeScript
static deleteAssetsPermanentlyWithUri(context: Context, assetUris: string[]): Promise<void>
```

通过资产URI批量彻底删除照片或视频，不经过回收站。使用promise异步回调。

> **说明：**&gt;
> - 对仅存在于本端设备的资产、仅存在于云端的资产、存在于本端设备和云端的资产，均可以彻底删除，不经过回收站。&gt;
> - 此操作不可逆。执行此操作后文件资源将被彻底删除，请谨慎操作。

**起始版本：** 24

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## deleteCloudAssetsWithUri

```TypeScript
static deleteCloudAssetsWithUri(context: Context, assetUris: string[]): Promise<void>
```

批量删除云端状态的媒体资产（照片或视频）到回收站。使用promise异步回调。

> **说明：**&gt;
> - 对仅存在于本端设备的资产，不做任何处理。&gt;
> - 对仅存在于云端的资产，直接删除到回收站。&gt;
> - 对存在于本端设备和云端的资产，删除后变化为本地资产，云端资产进入回收站。

**起始版本：** 22

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## deleteLocalAssetsPermanently

```TypeScript
static deleteLocalAssetsPermanently(context: Context, assets: Array<PhotoAsset>): Promise<void>
```

批量彻底删除照片或者视频。使用Promise异步回调。

> **注意：**&gt;
> 此操作不可逆，执行此操作后文件资源将彻底删除，请谨慎操作。

**起始版本：** 18

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| assets | Array & lt;PhotoAsset & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## deleteLocalAssetsPermanentlyWithUri

```TypeScript
static deleteLocalAssetsPermanentlyWithUri(context: Context, assetUris: Array<string>): Promise<void>
```

通过资产Uri批量彻底删除照片或者视频。使用promise异步回调。

> **注意：**&gt;
> 此操作不可逆，执行此操作后文件资源将被彻底删除，请谨慎操作。

**起始版本：** 19

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900020 |
| 14000011 |

## deleteLocalAssetsWithUri

```TypeScript
static deleteLocalAssetsWithUri(context: Context, assetUris: string[]): Promise<void>
```

批量删除本地状态的媒体资产（照片或视频）到回收站。使用promise异步回调。

> **说明：**&gt;
> - 对仅存在于本端设备的资产，直接删除到回收站。&gt;
> - 对仅存在于云端的资产，不做任何处理。&gt;
> - 对存在于本端设备和云端的资产，删除后变化为云端资产，本地资产进入回收站。

**起始版本：** 22

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setAppLinkInfo

```TypeScript
setAppLinkInfo(appLink: string): void
```

设置文件记忆链接的信息。

**起始版本：** 21

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appLink | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## setAppLinkState

```TypeScript
setAppLinkState(appLinkState: AppLinkState): void
```

设置文件记忆链接的状态信息。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appLinkState | [AppLinkState](arkts-medialibrary-photoaccesshelper-applinkstate-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## setCameraEditData

```TypeScript
setCameraEditData(editData: MediaAssetEditData): void
```

保存资产的摄像机编辑数据。

**起始版本：** 26.1.0

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| editData | [MediaAssetEditData](arkts-medialibrary-photoaccesshelper-mediaasseteditdata-c-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setCameraShotKey

```TypeScript
setCameraShotKey(cameraShotKey: string): void
```

设置锁屏相机拍照或录像的标记字段。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cameraShotKey | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setCompositeDisplayMode

```TypeScript
setCompositeDisplayMode(compositeDisplayMode: CompositeDisplayMode): Promise<void>
```

设置复合图的展示模式。使用Promise异步回调。

**起始版本：** 23

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| compositeDisplayMode | [CompositeDisplayMode](arkts-medialibrary-photoaccesshelper-compositedisplaymode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setEditData

```TypeScript
setEditData(editData: MediaAssetEditData): void
```

保存资产的编辑数据。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| editData | [MediaAssetEditData](arkts-medialibrary-photoaccesshelper-mediaasseteditdata-c-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setEffectMode

```TypeScript
setEffectMode(mode: MovingPhotoEffectMode): void
```

设置动态照片的效果模式。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [MovingPhotoEffectMode](arkts-medialibrary-sendablephotoaccesshelper-movingphotoeffectmode-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |
| 14000016 |

## setHasAppLink

```TypeScript
setHasAppLink(hasAppLink: number): void
```

设置文件记忆链接的状态信息。

**起始版本：** 21

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hasAppLink | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## setHidden

```TypeScript
setHidden(hiddenState: boolean): void
```

将文件设置为隐藏文件。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hiddenState | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setHiddenAttribute

```TypeScript
setHiddenAttribute(hiddenState: boolean): void
```

设置资产的UI隐藏属性

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hiddenState | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setIsRecentShow

```TypeScript
setIsRecentShow(isRencentShow: boolean): void
```

Set recentShow state of the asset.

**起始版本：** 18

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isRencentShow | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setLivePhoto4dStatus

```TypeScript
setLivePhoto4dStatus(status: LivePhoto4dStatus, livephoto_4d_latest_pair?: string): void
```

子弹时间状态

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| status | [LivePhoto4dStatus](arkts-medialibrary-photoaccesshelper-livephoto4dstatus-e-sys.md) | 是 |
| livephoto_4d_latest_pair | string | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setLocation

```TypeScript
setLocation(longitude: number, latitude: number): void
```

设置文件的经纬度信息。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| longitude | number | 是 |
| latitude | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setMovingPhotoVersion

```TypeScript
setMovingPhotoVersion(version: number): void
```

保存动态照片的版本号。

**起始版本：** 26.0.0

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| version | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setSupportedWatermarkType

```TypeScript
setSupportedWatermarkType(watermarkType: WatermarkType): void
```

设置拍照照片支持的水印类型。

**起始版本：** 14

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| watermarkType | [WatermarkType](arkts-medialibrary-photoaccesshelper-watermarktype-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setTitleByFile

```TypeScript
setTitleByFile(name: string): void
```

设置文件名，支持文管规则.命名

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 | 资产修改名称。 取值范围:1-255 不应包含扩展名。 文件名字符串长度为1~255。 不允许出现的非法英文字符，包括：. \ / : * ? " ' ` &lt; &gt; \|

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setUserComment

```TypeScript
setUserComment(userComment: string): void
```

修改媒体资产的备注信息。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| userComment | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setVideoEnhancementAttr

```TypeScript
setVideoEnhancementAttr(videoEnhancementType: VideoEnhancementType, photoId: string): void
```

设置视频的二阶段增强处理类型。

**起始版本：** 13

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| videoEnhancementType | [VideoEnhancementType](arkts-medialibrary-photoaccesshelper-videoenhancementtype-e-sys.md) | 是 |
| photoId | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |
| 14000016 |
