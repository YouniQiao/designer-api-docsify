# MediaAnalysisAlbumChangeRequest（系统接口）

智慧相册变更请求。

**继承/实现关系：** MediaAnalysisAlbumChangeRequest extends [MediaAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c.md)

**起始版本：** 18

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## constructor

```TypeScript
constructor(album: Album)
```

构造函数。

**起始版本：** 18

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

## createAnalysisAlbumRequest

```TypeScript
static createAnalysisAlbumRequest(
      context: Context, 
      name: string, 
      subtype: AlbumSubtype
    ): MediaAnalysisAlbumChangeRequest
```

创建智慧相册的变更请求。

> **说明：**&gt;
> 相册名的参数规格如下：&gt;
> - 相册名字符串长度的取值范围为[1, 255]。&gt;
> - 不允许出现非法英文字符，包括：. .. \ / : * ? " ' ` &lt;
&gt; | { } [ ]

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |
| name | string | 是 |
| subtype | [AlbumSubtype](arkts-medialibrary-sendablephotoaccesshelper-albumsubtype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [MediaAnalysisAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaanalysisalbumchangerequest-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setDefaultCoverUri

```TypeScript
setDefaultCoverUri(coverUri: string): void
```

设置智慧相册的默认封面。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

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
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## setOrderPosition

```TypeScript
setOrderPosition(assets: Array<PhotoAsset>, position: Array<number>): void
```

设置智慧相册中资产的顺序位置。

**起始版本：** 18

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | 是 |
| position | Array & lt;number & gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## setRelationship

```TypeScript
setRelationship(relationship: string): Promise<void>
```

设置人像相册中的人物关系。支持的人物关系名称范围： | 唯一标识 | 含义 | | ---------- | ------- | | me | 我 | | son | 儿子 | | daughter | 女儿 | | wife | 妻子 | | husband | 丈夫 | | father | 爸爸 | | mother | 妈妈 | | colleague | 同事 | | friend | 朋友 | | classmate | 同学 | | best_friend_female | 闺蜜 | | boyfriend | 男朋友 | | girlfriend | 女朋友 | | family | 家人 | | maternal_grandfather | 外公 | | maternal_grandmother | 外婆 | | paternal_grandfather | 爷爷 | | paternal_grandmother | 奶奶 | | older_brother | 哥哥 | | older_sister | 姐姐 | | younger_brother | 弟弟 | | younger_sister | 妹妹 | | relative | 亲戚 | | other | 其他 |

**起始版本：** 21

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| relationship | string | 是 |

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
