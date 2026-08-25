# MediaAlbumChangeRequest

MediaAlbumChangeRequest implements [MediaChangeRequest](arkts-medialibrary-photoaccesshelper-mediachangerequest-i.md).相册变更请求。

> **说明：**&gt;
> - 本Class首批接口从API version 11开始支持。

**继承/实现关系：** MediaAlbumChangeRequest implements [MediaChangeRequest](arkts-medialibrary-photoaccesshelper-mediachangerequest-i.md)

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## createAlbumRequest

```TypeScript
static createAlbumRequest(context: Context, name: string): MediaAlbumChangeRequest
```

创建相册变更请求。相册名的参数规格为：  
- 相册名字符串长度为1~255。  
- 不允许出现的非法英文字符，包括：  
. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]  
- 英文字符大小写不敏感。  
- 相册名不允许重名。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| [MediaAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## deleteAlbums

```TypeScript
static deleteAlbums(context: Context, albums: Array<Album>): Promise<void>
```

删除存在的用户相册。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| albums | Array & lt;Album & gt; | 是 |

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

## deleteAlbumsWithUri

```TypeScript
static deleteAlbumsWithUri(context: Context, albumUris: Array<string>): Promise<void>
```

删除已存在的用户相册。使用promise异步回调。

**起始版本：** 19

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| albumUris | Array & lt;string & gt; | 是 |

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

## deleteAssets

```TypeScript
deleteAssets(assets: Array<PhotoAsset>): void
```

从回收站中彻底删除资产。

> **注意：**&gt;
> 此操作不可逆，执行此操作后文件资源将彻底删除，请谨慎操作。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |
| 14000016 |

## deleteAssetsWithUri

```TypeScript
deleteAssetsWithUri(assetUris: Array<string>): void
```

从回收站中彻底删除资产。

> **注意：**&gt;
> 此操作不可逆，执行此操作后文件资源将被彻底删除，请谨慎操作。

**起始版本：** 19

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900020 |
| 14000011 |
| 14000016 |

## dismiss

```TypeScript
dismiss(): void
```

删除合影相册。

**起始版本：** 13

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## dismissAssets

```TypeScript
dismissAssets(assets: Array<PhotoAsset>): void
```

从该人像相册或合影相册中移除指定图片。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |
| 14000016 |

## mergeAlbum

```TypeScript
mergeAlbum(target: Album): void
```

将两个人像相册合并。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| target | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |
| 14000016 |

## moveAssets

```TypeScript
moveAssets(assets: Array<PhotoAsset>, targetAlbum: Album): void
```

从相册中移动资产到另一个目标相册。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | 是 |
| targetAlbum | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |
| 14000016 |

## moveAssetsWithUri

```TypeScript
moveAssetsWithUri(assetUris: Array<string>, targetAlbum: Album): void
```

把相册中的资产移动到另一个目标相册。

**起始版本：** 19

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Array & lt;string & gt; | 是 |
| targetAlbum | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900020 |
| 14000011 |
| 14000016 |

## operateAttribute

```TypeScript
operateAttribute(operation: AlbumOperation): void
```

操作相册属性。

**起始版本：** 26.0.0

**需要权限：** 
- API版本26.0.0：ohos.permission.ACCESS_MEDIALIB_THUMB_DB
- API版本26.1.0+：ohos.permission.ACCESS_MEDIALIB_THUMB_DB or ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| operation | [AlbumOperation](arkts-medialibrary-photoaccesshelper-albumoperation-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800201](../errorcode-medialibrary.md#23800201-不支持的操作类型) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## placeBefore

```TypeScript
placeBefore(album: Album): void
```

将当前相册排序到目标相册之前。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## recoverAssets

```TypeScript
recoverAssets(assets: Array<PhotoAsset>): void
```

从回收站中恢复指定的PhotoAsset对象数组所对应的资产。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |
| 14000016 |

## recoverAssetsWithUri

```TypeScript
recoverAssetsWithUri(assetUris: Array<string>): void
```

从回收站中恢复指定的URI字符串数组所对应的资产。

**起始版本：** 19

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Array & lt;string & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900020 |
| 14000011 |
| 14000016 |

## resetCoverUri

```TypeScript
resetCoverUri(): void
```

恢复默认封面。

**起始版本：** 20

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setAlbumNameByFile

```TypeScript
setAlbumNameByFile(name: string): void
```

设置相册名称，支持文管规则的.命名

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 | 相册名。 取值范围:1-255 相册名参数规格： 相册名字符串长度为1~255。 不允许出现的非法英文字符，包括： \ / : * ? " ' ` &lt; &gt; \|

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setCoverUri

```TypeScript
setCoverUri(coverUri: string): void
```

设置相册封面。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| coverUri | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setDisplayLevel

```TypeScript
setDisplayLevel(displayLevel: number): void
```

设置人像相册的显示级别。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayLevel | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setHiddenAttribute

```TypeScript
setHiddenAttribute(hiddenState: boolean, isInherited: boolean): void
```

设置相册的UI隐藏属性

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hiddenState | boolean | 是 |
| isInherited | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setIsMe

```TypeScript
setIsMe(): void
```

将人像相册的人物关系设置为“我”。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setUploadStatus

```TypeScript
static setUploadStatus(context: Context, albums: Album[], allowUpload: boolean): Promise<void>
```

设置相册是否可以同步到云空间或家庭存储。使用promise异步回调。

**起始版本：** 22

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| albums | [Album[]](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | 是 |
| allowUpload | boolean | 是 |

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
