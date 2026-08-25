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

## addAssets

```TypeScript
addAssets(assets: Array<PhotoAsset>): void
```

向相册中添加资产。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |
| 14000016 |

## constructor

```TypeScript
constructor(album: Album)
```

构造函数用于初始化新创建的对象。用于对相册进行操作。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## getAlbum

```TypeScript
getAlbum(): Album
```

获取当前相册变更请求中的相册。

> **注意：**&gt;
> 对于创建相册的变更请求，在调用接口
> 
> [applyChanges](arkts-medialibrary-photoaccesshelper-photoaccesshelper-i.md#applychanges)
> 
> 的提交生效之前，该接口会返回null。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## removeAssets

```TypeScript
removeAssets(assets: Array<PhotoAsset>): void
```

从相册中移除资产。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |
| 14000016 |

## setAlbumName

```TypeScript
setAlbumName(name: string): void
```

设置相册名称。相册名参数规格：  
- 相册名字符串长度为1~255。  
- 不允许出现的非法英文字符，包括：  
. \ / : * ? " ' ` &lt; &gt; | { } [ ]  
- 英文字符大小写不敏感。  
- 相册名不允许重名。

**起始版本：** 11

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## comment

```TypeScript
readonly comment: string
```

用于[MediaChangeRequest](arkts-apis-photoAccessHelper-i.md#mediachangerequest)类型校验。 如果类（如MediaAlbumChangeRequest）对象可以访问，就说明该类是MediaChangeRequest的实现类

**类型：** string

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core
