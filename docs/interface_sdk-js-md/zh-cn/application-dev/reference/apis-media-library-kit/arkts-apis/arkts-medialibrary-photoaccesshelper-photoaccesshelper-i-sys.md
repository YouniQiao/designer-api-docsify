# PhotoAccessHelper

提供访问照片和相册的功能。

**起始版本：** 10

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## acquireDebugDatabase

```TypeScript
acquireDebugDatabase(betaIssueId: string, betaScenario: string): Promise<Map<string, string>>
```

Start medialibrary database backup and wait for returning with backup infomation which only works on beta device.

**起始版本：** 23

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| betaIssueId | string | 是 |
| betaScenario | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Map & lt;string, string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800201](../errorcode-medialibrary.md#23800201-不支持的操作类型) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## batchGetPhotoAssetParams

```TypeScript
batchGetPhotoAssetParams(assets: PhotoAsset[], members: string[]): PhotoAssetParams
```

批量获取传入的PhotoAsset对象数组中指定属性的值。

**起始版本：** 21

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | [PhotoAsset[]](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 是 |
| [members](../../apis-connectivity-kit/arkts-apis/arkts-connectivity-cdsm-cdsminfo-i.md) | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| [PhotoAssetParams](arkts-medialibrary-photoaccesshelper-photoassetparams-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800104](../errorcode-medialibrary.md#23800104-传入参数校验不通过) |

## cancelAnalysisTool

```TypeScript
cancelAnalysisTool(config: ToolCancelConfig): Promise<void>
```

取消执行智能分析工具。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.CONTROL_IMAGEVIDEO_ANALYSIS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [ToolCancelConfig](arkts-medialibrary-photoaccesshelper-toolcancelconfig-i-sys.md) | 是 |

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

## cancelPhotoUriPermission

```TypeScript
cancelPhotoUriPermission(tokenId: number, uri: string, photoPermissionType: PhotoPermissionType): Promise<number>
```

取消应用对uri的访问权限。使用Promise异步回调。

**起始版本：** 19

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenId | number | 是 |
| uri | string | 是 |
| photoPermissionType | [PhotoPermissionType](arkts-medialibrary-photoaccesshelper-photopermissiontype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900020 |
| 14000011 |

## canPerformDeepOptimizeSpace

```TypeScript
canPerformDeepOptimizeSpace(): Promise<boolean>
```

查询当前系统是否可以执行深度优化存储空间功能。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## cloneAssetsByPath

```TypeScript
cloneAssetsByPath(assets: string[], target: Album, option?: BatchOperationOptions): Promise<string[]>
```

将文件管理中的资产复制到目标相册中。使用Promise异步回调。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | string[] | 是 |
| target | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | 是 |
| option | [BatchOperationOptions](arkts-medialibrary-photoaccesshelper-batchoperationoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## cloneToAlbum

```TypeScript
cloneToAlbum(assets: PhotoAsset[], target: Album, option?: BatchOperationOptions): Promise<PhotoAsset[]>
```

复制资产到目标相册。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | [PhotoAsset[]](arkts-medialibrary-sendablephotoaccesshelper-photoasset-i.md) | 是 |
| target | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | 是 |
| option | [BatchOperationOptions](arkts-medialibrary-photoaccesshelper-batchoperationoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PhotoAsset[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## cloneToDir

```TypeScript
cloneToDir(assets: string[], target: string, option?: BatchOperationOptions): Promise<string[]>
```

复制资产到文件管理目录中。使用Promise异步回调。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | string[] | 是 |
| target | string | 是 |
| option | [BatchOperationOptions](arkts-medialibrary-photoaccesshelper-batchoperationoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## convertAssetToCompatibleAsset

```TypeScript
convertAssetToCompatibleAsset(assets: Array<PhotoAsset>): Promise<Array<PhotoAsset>>
```

转换传入的PhotoAsset属性到媒体库兼容文件格式属性。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;PhotoAsset & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## convertToAsset

```TypeScript
convertToAsset(path: string): Promise<PhotoAsset>
```

将文件管理公共目录中的资产转换为资产对象。使用Promise异步回调。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PhotoAsset & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## createAlbum

```TypeScript
createAlbum(name: string, callback: AsyncCallback<Album>): void
```

创建相册。使用callback异步回调。待创建的相册名参数规格为：  
- 相册名字符串长度为1~255。  
- 不允许出现的非法英文字符，包括：  
. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]  
- 相册名不允许重名。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [createAlbumRequest](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#createalbumrequest)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Album&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900015 |
| 13900020 |
| 14000011 |

## createAlbum

```TypeScript
createAlbum(name: string): Promise<Album>
```

创建相册。使用Promise异步回调。待创建的相册名参数规格为：  
- 相册名字符串长度为1~255。  
- 不允许出现的非法英文字符，包括：  
. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]  
- 相册名不允许重名。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [createAlbumRequest](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#createalbumrequest)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Album & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900015 |
| 13900020 |
| 14000011 |

## createAsset

```TypeScript
createAsset(displayName: string, callback: AsyncCallback<PhotoAsset>): void
```

指定待创建的图片或者视频的文件名，创建图片或视频资源。使用callback异步回调。待创建的文件名参数规格为：  
- 应包含有效文件主名和图片或视频扩展名。  
- 文件名字符串长度为1~255。  
- 文件主名中不允许出现的非法英文字符。  
API18开始，非法字符包括： \ / : * ? " &lt; &gt; |API10-17，非法字符包括：. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoAsset&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000001 |
| 14000011 |

## createAsset

```TypeScript
createAsset(displayName: string): Promise<PhotoAsset>
```

指定待创建的图片或者视频的文件名，创建图片或视频资源。使用Promise异步回调。待创建的文件名参数规格为：  
- 应包含有效文件主名和图片或视频扩展名。  
- 文件名字符串长度为1~255。  
- 文件主名中不允许出现的非法英文字符。  
API18开始，非法字符包括： \ / : * ? " &lt; &gt; |API10-17，非法字符包括：. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PhotoAsset & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000001 |
| 14000011 |

## createAsset

```TypeScript
createAsset(displayName: string, options: PhotoCreateOptions): Promise<PhotoAsset>
```

指定待创建的图片或者视频的文件名和创建选项，创建图片或视频资源。使用Promise异步回调。待创建的文件名参数规格为：  
- 应包含有效文件主名和图片或视频扩展名。  
- 文件名字符串长度为1~255。  
- 文件主名中不允许出现的非法英文字符。  
API18开始，非法字符包括： \ / : * ? " &lt; &gt; |API10-17，非法字符包括：. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayName | string | 是 |
| options | [PhotoCreateOptions](arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PhotoAsset & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000001 |
| 14000011 |

## createAsset

```TypeScript
createAsset(displayName: string, options: PhotoCreateOptions, callback: AsyncCallback<PhotoAsset>): void
```

指定待创建的图片或者视频的文件名和创建选项，创建图片或视频资源。使用callback异步回调。待创建的文件名参数规格为：  
- 应包含有效文件主名和图片或视频扩展名。  
- 文件名字符串长度为1~255。  
- 文件主名中不允许出现的非法英文字符。  
API18开始，非法字符包括： \ / : * ? " &lt; &gt; |API10-17，非法字符包括：. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayName | string | 是 |
| options | [PhotoCreateOptions](arkts-medialibrary-photoaccesshelper-photocreateoptions-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoAsset&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000001 |
| 14000011 |

## createAssetsForApp

```TypeScript
createAssetsForApp(bundleName: string, appName: string, tokenId: number, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>
```

调用接口代替应用创建媒体库uri列表。Uri已对tokenId对应的应用授权，支持应用使用uri写入图片/视频。

**起始版本：** 19

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| appName | string | 是 |
| tokenId | number | 是 |
| photoCreationConfigs | Array&lt;[PhotoCreationConfig](arkts-medialibrary-photoaccesshelper-photocreationconfig-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900020 |
| 14000011 |

## createAssetsForAppWithAlbum

```TypeScript
createAssetsForAppWithAlbum(source: PhotoCreationSource, albumUri: string, isAuthorized: boolean, photoCreationConfigs: Array<PhotoCreationConfig>): Promise<Array<string>>
```

为应用自己或者其他应用创建资产到指定来源或者用户相册。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | [PhotoCreationSource](arkts-medialibrary-photoaccesshelper-photocreationsource-i-sys.md) | 是 |
| albumUri | string | 是 |
| isAuthorized | boolean | 是 |
| photoCreationConfigs | Array&lt;[PhotoCreationConfig](arkts-medialibrary-photoaccesshelper-photocreationconfig-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## createAssetsForAppWithMode

```TypeScript
createAssetsForAppWithMode(
      bundleName: string,
      appName: string,
      appId: string,
      tokenId: number,
      authorizationMode: AuthorizationMode,
      photoCreationConfigs: Array<PhotoCreationConfig>
    ): Promise<Array<string>>
```

提供给应用保存短时授权。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| appName | string | 是 |
| appId | string | 是 |
| tokenId | number | 是 |
| authorizationMode | [AuthorizationMode](arkts-medialibrary-photoaccesshelper-authorizationmode-e-sys.md) | 是 |
| photoCreationConfigs | Array&lt;[PhotoCreationConfig](arkts-medialibrary-photoaccesshelper-photocreationconfig-i.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## createAssetsWithAlbum

```TypeScript
createAssetsWithAlbum(
      creationSettings: CreationSetting[], 
      isRealTimeThumb: boolean, 
      albumUri?: string): Promise<string[]>
```

批量创建资产 同时支持选择是否指定相册和是否立即生成缩略图

**起始版本：** 26.0.0

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| creationSettings | [CreationSetting](arkts-medialibrary-photoaccesshelper-creationsetting-i.md)[] | 是 |
| isRealTimeThumb | boolean | 是 |
| albumUri | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## deleteAlbums

```TypeScript
deleteAlbums(albums: Array<Album>, callback: AsyncCallback<void>): void
```

删除存在的用户相册。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [deleteAlbums](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#deletealbums)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| albums | Array & lt;Album & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000011 |

## deleteAlbums

```TypeScript
deleteAlbums(albums: Array<Album>): Promise<void>
```

删除存在的用户相册。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [deleteAlbums](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c-sys.md#deletealbums)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| albums | Array & lt;Album & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000011 |

## deleteAssets

```TypeScript
deleteAssets(uriList: Array<string>, callback: AsyncCallback<void>): void
```

删除媒体文件，删除的文件进入到回收站。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [deleteAssets](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteassets)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [uriList](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | Array & lt;string & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000002 |
| 14000011 |

## deleteAssets

```TypeScript
deleteAssets(uriList: Array<string>): Promise<void>
```

删除媒体文件，删除的文件进入到回收站。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [deleteAssets](arkts-medialibrary-photoaccesshelper-mediaassetchangerequest-c.md#deleteassets)

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000002 |
| 14000011 |

## getAlbumIdByBundleName

```TypeScript
getAlbumIdByBundleName(bundleName: string): Promise<number>
```

根据bundleName获取媒体库相册的ID。使用Promise异步回调。

**起始版本：** 22

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getAlbumsByIds

```TypeScript
getAlbumsByIds(albumIds: Array<number>): Promise<Map<number, Album>>
```

通过相册id查询相册信息。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| albumIds | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Map & lt;number, Album & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## getAssetCompatibleCapability

```TypeScript
getAssetCompatibleCapability(bundleName: string): Promise<AssetCompatibleCapability>
```

根据bundleName获取资产兼容能力。当应用程序获取文件时，可判断该应用程序是否需要进行兼容性转换。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[AssetCompatibleCapability](arkts-medialibrary-photoaccesshelper-assetcompatiblecapability-i.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getAssetCompatibleUris

```TypeScript
getAssetCompatibleUris(bundleName: string, assets: Array<PhotoAsset>, compatibleFlag?: number): Promise<Array<string>>
```

根据bundleName、photoAsset列表和compatibleFlag获取需要转码的URI列表。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| assets | Array & lt;PhotoAsset & gt; | 是 |
| compatibleFlag | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getClonedAlbumUris

```TypeScript
getClonedAlbumUris(oldUris: Array<string>): Promise<Map<string, string>>
```

通过克隆后的相册URI列表获取当前uri。使用Promise异步回调。为控制数据库表空间占用规模，当前每次克隆时都会自动将上次存储的克隆数据进行清除，所以该接口只保存最近一次克隆时用户新/旧设备uri的对应关系。

**起始版本：** 22

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| oldUris | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Map & lt;string, string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getClonedAssetUris

```TypeScript
getClonedAssetUris(oldUris: Array<string>): Promise<Map<string, string>>
```

通过克隆后的资产URI列表获取当前uri。使用Promise异步回调。为控制数据库表空间占用规模，当前每次克隆时都会自动将上次存储的克隆数据进行清除，所以该接口只保存最近一次克隆时用户新/旧设备uri的对应关系。

**起始版本：** 22

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| oldUris | Array & lt;string & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Map & lt;string, string & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getDataAnalysisProgress

```TypeScript
getDataAnalysisProgress(analysisType?: AnalysisType): Promise<string>
```

获取资产的分析进度。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| analysisType | [AnalysisType](arkts-medialibrary-photoaccesshelper-analysistype-e-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## getDeepOptimizeSpace

```TypeScript
getDeepOptimizeSpace(): Promise<number>
```

获取可以深度优化存储空间的大小，单位为字节（byte）。使用Promise异步回调。

 Unit:Byte{s}.  
- 此接口耗时较长，建议先调用[canPerformDeepOptimizeSpace](#canperformdeepoptimizespace)确认当前系统状态是否允许执行。  
- 仅在返回true时调用此接口。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getHiddenAlbums

```TypeScript
getHiddenAlbums(mode: HiddenPhotosDisplayMode, options: FetchOptions, callback: AsyncCallback<FetchResult<Album>>): void
```

根据隐藏文件显示模式和检索选项获取系统中的隐藏相册。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [HiddenPhotosDisplayMode](arkts-medialibrary-photoaccesshelper-hiddenphotosdisplaymode-e-sys.md) | 是 |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## getHiddenAlbums

```TypeScript
getHiddenAlbums(mode: HiddenPhotosDisplayMode, callback: AsyncCallback<FetchResult<Album>>): void
```

根据隐藏文件显示模式获取系统中的隐藏相册。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [HiddenPhotosDisplayMode](arkts-medialibrary-photoaccesshelper-hiddenphotosdisplaymode-e-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;FetchResult&lt;Album&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## getHiddenAlbums

```TypeScript
getHiddenAlbums(mode: HiddenPhotosDisplayMode, options?: FetchOptions): Promise<FetchResult<Album>>
```

根据隐藏文件显示模式和检索选项获取系统中的隐藏相册。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [HiddenPhotosDisplayMode](arkts-medialibrary-photoaccesshelper-hiddenphotosdisplaymode-e-sys.md) | 是 |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;FetchResult & lt;Album & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## getIndexConstructProgress

```TypeScript
getIndexConstructProgress(): Promise<string>
```

获取索引构建进度。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

## getPhotoAlbumOrder

```TypeScript
getPhotoAlbumOrder(orderStyle: number, options?: FetchOptions): Promise<FetchResult<AlbumOrder>>
```

获取系统、用户和来源相册的排序信息。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| orderStyle | number | 是 |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;FetchResult&lt;[AlbumOrder](arkts-medialibrary-photoaccesshelper-albumorder-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getPhotoAlbums

```TypeScript
getPhotoAlbums(options?: FetchOptions):Promise<FetchResult<Album>>
```

根据指定的选项获取系统、用户和来源相册。使用Promise异步回调。在获取相册之前，确保相册已存在。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;FetchResult & lt;Album & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getPhotoAssets

```TypeScript
getPhotoAssets(assetsData: ValuesBucket[]): Promise<PhotoAsset[]>
```

将ValuesBucket记录转换为PhotoAsset对象。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetsData | [ValuesBucket[]](../../apis-arkdata/arkts-apis/arkts-arkdata-rdb-valuesbucket-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PhotoAsset[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getPhotoIndex

```TypeScript
getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions, callback: AsyncCallback<number>): void
```

获取相册中图片或视频的位置。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoUri | string | 是 |
| albumUri | string | 是 |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000011 |

## getPhotoIndex

```TypeScript
getPhotoIndex(photoUri: string, albumUri: string, options: FetchOptions): Promise<number>
```

获取相册中图片或视频的位置。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| photoUri | string | 是 |
| albumUri | string | 是 |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 13900020 |
| 14000011 |

## getPreferredCompatibleMode

```TypeScript
getPreferredCompatibleMode(bundleName: string): Promise<PreferredCompatibleMode>
```

根据bundleName获取应用配置的首选兼容模式。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[PreferredCompatibleMode](arkts-medialibrary-photoaccesshelper-preferredcompatiblemode-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## getSharedPhotoAssets

```TypeScript
getSharedPhotoAssets(options: FetchOptions): Array<SharedPhotoAsset>
```

获取共享的照片资产。

**起始版本：** 13

**需要权限：** ohos.permission.ACCESS_MEDIALIB_THUMB_DB

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [FetchOptions](arkts-medialibrary-photoaccesshelper-fetchoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;SharedPhotoAsset & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## grantPhotoUriPermission

```TypeScript
grantPhotoUriPermission(
      tokenId: number, 
      uri: string, 
      photoPermissionType: PhotoPermissionType, 
      hideSensitiveType: HideSensitiveType
    ): Promise<number>
```

给应用授予uri的访问权限。使用Promise异步回调。

**起始版本：** 19

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenId | number | 是 |
| uri | string | 是 |
| photoPermissionType | [PhotoPermissionType](arkts-medialibrary-photoaccesshelper-photopermissiontype-e-sys.md) | 是 |
| hideSensitiveType | [HideSensitiveType](arkts-medialibrary-photoaccesshelper-hidesensitivetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900020 |
| 14000011 |

## grantPhotoUrisPermission

```TypeScript
grantPhotoUrisPermission(
      tokenId: number, 
      uriList: Array<string>, 
      photoPermissionType: PhotoPermissionType, 
      hideSensitiveType: HideSensitiveType
    ): Promise<number>
```

给应用授予uri列表的访问权限。使用Promise异步回调。

**起始版本：** 19

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tokenId | number | 是 |
| [uriList](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-certificatemanager-cmresult-i.md) | Array & lt;string & gt; | 是 |
| photoPermissionType | [PhotoPermissionType](arkts-medialibrary-photoaccesshelper-photopermissiontype-e-sys.md) | 是 |
| hideSensitiveType | [HideSensitiveType](arkts-medialibrary-photoaccesshelper-hidesensitivetype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13900020 |
| 14000011 |

## invokeAnalysisTool

```TypeScript
invokeAnalysisTool(config: ToolInvokeConfig, callback: Callback<AnalysisToolResult>): Promise<string>
```

触发分析工具的执行。该接口使用promise返回结果。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.CONTROL_IMAGEVIDEO_ANALYSIS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [ToolInvokeConfig](arkts-medialibrary-photoaccesshelper-toolinvokeconfig-i-sys.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AnalysisToolResult](arkts-medialibrary-photoaccesshelper-analysistoolresult-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## isCompatibleDuplicateSupported

```TypeScript
isCompatibleDuplicateSupported(bundleName: string): Promise<boolean>
```

检查是否要为指定应用创建JPEG格式的临时副本。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## isMediaDataReady

```TypeScript
isMediaDataReady(mediaDataKey: string): Promise<boolean>
```

判断指定的媒体数据是否已经准备完成。

**起始版本：** 24

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mediaDataKey | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## modifyAlbumDefaultCoverOrder

```TypeScript
modifyAlbumDefaultCoverOrder(coverOrderInfos: DefaultCoverOrderInfo[], 
    disableModification: boolean, 
    isAsyncRefreshAlbum: boolean): Promise<void>
```

修改相册的默认封面选择顺序

**起始版本：** 26.0.0

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| coverOrderInfos | [DefaultCoverOrderInfo](arkts-medialibrary-photoaccesshelper-defaultcoverorderinfo-c-sys.md)[] | 是 |
| disableModification | boolean | 是 |
| isAsyncRefreshAlbum | boolean | 是 |

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

## modifyHiddenAlbumDefaultCoverOrder

```TypeScript
modifyHiddenAlbumDefaultCoverOrder(coverOrderInfos: DefaultCoverOrderInfo[], 
    disableModification: boolean, 
    isAsyncRefreshAlbum: boolean): Promise<void>
```

修改隐藏相册的默认封面选择顺序

**起始版本：** 26.0.0

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| coverOrderInfos | [DefaultCoverOrderInfo](arkts-medialibrary-photoaccesshelper-defaultcoverorderinfo-c-sys.md)[] | 是 |
| disableModification | boolean | 是 |
| isAsyncRefreshAlbum | boolean | 是 |

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

## moveAssetsByPath

```TypeScript
moveAssetsByPath(assets: string[], target: Album, option?: BatchOperationOptions): Promise<string[]>
```

将文件管理中的资产移动到目标相册中。使用Promise异步回调。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | string[] | 是 |
| target | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i.md) | 是 |
| option | [BatchOperationOptions](arkts-medialibrary-photoaccesshelper-batchoperationoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## moveAssetsToDir

```TypeScript
moveAssetsToDir(assets: string[], target: string, option?: BatchOperationOptions): Promise<string[]>
```

移动资产到文件管理目录中。使用Promise异步回调。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assets | string[] | 是 |
| target | string | 是 |
| option | [BatchOperationOptions](arkts-medialibrary-photoaccesshelper-batchoperationoptions-i-sys.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## off('hiddenPhotoChange')

```TypeScript
off(type: 'hiddenPhotoChange', callback?: Callback<PhotoAssetChangeInfos>): void
```

取消对'hiddenPhotoChange'隐藏资产的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'hiddenPhotoChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## off('trashedPhotoChange')

```TypeScript
off(type: 'trashedPhotoChange', callback?: Callback<PhotoAssetChangeInfos>): void
```

取消对'trashedPhotoChange'回收站资产的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'trashedPhotoChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## off('hiddenAlbumChange')

```TypeScript
off(type: 'hiddenAlbumChange', callback?: Callback<AlbumChangeInfos>): void
```

取消对'hiddenAlbumChange'隐藏相册的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'hiddenAlbumChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## off('trashedAlbumChange')

```TypeScript
off(type: 'trashedAlbumChange', callback?: Callback<AlbumChangeInfos>): void
```

取消对'trashedAlbumChange'回收站相册的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'trashedAlbumChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## offAnalysisAlbumChange

```TypeScript
offAnalysisAlbumChange(callback?: Callback<AlbumChangeInfos>): void
```

取消对智慧分析相册的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## offAnalysisPhotoChange

```TypeScript
offAnalysisPhotoChange(callback?: Callback<PhotoAssetChangeInfos>): void
```

取消对与智慧分析相册相关的媒体资产变更的监听。存在多个callback监听时，可以取消指定注册的callback监听；不指定callback时取消所有监听。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## offShareAlbumChange

```TypeScript
offShareAlbumChange(callback?: Callback<AlbumChangeInfos>): void
```

注销共享相册的监听

**起始版本：** 26.1.0

**需要权限：** ohos.permission.MANAGE_SHARE_PHOTO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## offSharePhotoChange

```TypeScript
offSharePhotoChange(callback?: Callback<PhotoAssetChangeInfos>): void
```

注销共享相册图片和视频的监听

**起始版本：** 26.1.0

**需要权限：** ohos.permission.MANAGE_SHARE_PHOTO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## on('hiddenPhotoChange')

```TypeScript
on(type: 'hiddenPhotoChange', callback: Callback<PhotoAssetChangeInfos>): void
```

注册'hiddenPhotoChange'监听隐藏的媒体资产，并通过callback方式返回隐藏资产变化结果，可以注册多个callback。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'hiddenPhotoChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## on('trashedPhotoChange')

```TypeScript
on(type: 'trashedPhotoChange', callback: Callback<PhotoAssetChangeInfos>): void
```

注册'trashedPhotoChange'监听回收站的媒体资产，并通过callback方式返回回收站资产变化结果，可以注册多个callback。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'trashedPhotoChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## on('hiddenAlbumChange')

```TypeScript
on(type: 'hiddenAlbumChange', callback: Callback<AlbumChangeInfos>): void
```

注册'hiddenAlbumChange'监听隐藏相册，并通过callback方式返回相册变化结果，可以注册多个callback。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'hiddenAlbumChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## on('trashedAlbumChange')

```TypeScript
on(type: 'trashedAlbumChange', callback: Callback<AlbumChangeInfos>): void
```

注册'trashedAlbumChange'监听回收站相册，并通过callback方式返回相册变化结果，可以注册多个callback。

**起始版本：** 20

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'trashedAlbumChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## onAnalysisAlbumChange

```TypeScript
onAnalysisAlbumChange(callback: Callback<AlbumChangeInfos>): void
```

监听智慧分析相册，并通过callback方式返回相册变化结果，可以注册多个callback。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## onAnalysisPhotoChange

```TypeScript
onAnalysisPhotoChange(callback: Callback<PhotoAssetChangeInfos>): void
```

监听与智慧分析相册相关的媒体资产的变更情况，该变更携带智慧分析相册变更信息，当且仅当资产变更涉及智慧分析相册信息变更时，才会发送该资产变更通知， 通过callback返回资产变化结果，可以注册多个callback。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## onShareAlbumChange

```TypeScript
onShareAlbumChange(callback: Callback<AlbumChangeInfos>): void
```

监听共享相册的变化

**起始版本：** 26.1.0

**需要权限：** ohos.permission.MANAGE_SHARE_PHOTO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AlbumChangeInfos](arkts-medialibrary-photoaccesshelper-albumchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## onSharePhotoChange

```TypeScript
onSharePhotoChange(callback: Callback<PhotoAssetChangeInfos>): void
```

共享相册资产的监听

**起始版本：** 26.1.0

**需要权限：** ohos.permission.MANAGE_SHARE_PHOTO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PhotoAssetChangeInfos](arkts-medialibrary-photoaccesshelper-photoassetchangeinfos-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## query

```TypeScript
query(sql: string): Promise<ResultSet>
```

根据指定的SQL语句查询数据库数据，不支持写操作和多级查询。使用Promise异步回调。

**起始版本：** 22

**需要权限：** ohos.permission.ACCESS_MEDIALIB_THUMB_DB

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sql | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;ResultSet & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## releaseDebugDatabase

```TypeScript
releaseDebugDatabase(betaIssueId: string, dbFd: number): Promise<void>
```

Release medialibrary database backup resources incluses closing backup database fd and deleting temporary backup database file which only works on beta device.

**起始版本：** 23

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| betaIssueId | string | 是 |
| dbFd | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800201](../errorcode-medialibrary.md#23800201-不支持的操作类型) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## removeFormInfo

```TypeScript
removeFormInfo(info: FormInfo, callback: AsyncCallback<void>): void
```

从数据库中删除绑定单个图片的图库卡片信息。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [FormInfo](../../apis-form-kit/arkts-apis/arkts-form-forminfo-forminfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## removeFormInfo

```TypeScript
removeFormInfo(info: FormInfo): Promise<void>
```

从数据库中删除绑定单个图片的图库卡片信息。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [FormInfo](../../apis-form-kit/arkts-apis/arkts-form-forminfo-forminfo-i.md) | 是 |

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

## removeGalleryFormInfo

```TypeScript
removeGalleryFormInfo(info: GalleryFormInfo): Promise<void>
```

从数据库中删除绑定一组图片的图库卡片信息。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [GalleryFormInfo](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | 是 |

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

## saveFormInfo

```TypeScript
saveFormInfo(info: FormInfo, callback: AsyncCallback<void>): void
```

将绑定单个图片的图库卡片信息保存到数据库中。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [FormInfo](../../apis-form-kit/arkts-apis/arkts-form-forminfo-forminfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## saveFormInfo

```TypeScript
saveFormInfo(info: FormInfo): Promise<void>
```

将绑定单个图片的图库卡片信息保存到数据库中。使用Promise异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [FormInfo](../../apis-form-kit/arkts-apis/arkts-form-forminfo-forminfo-i.md) | 是 |

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

## saveGalleryFormInfo

```TypeScript
saveGalleryFormInfo(info: GalleryFormInfo): Promise<void>
```

将绑定一组图片的图库卡片信息保存到数据库中。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [GalleryFormInfo](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | 是 |

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

## setAssetCompatibleCapability

```TypeScript
setAssetCompatibleCapability(bundleName: string, capability: AssetCompatibleCapability): Promise<void>
```

根据bundleName配置资产兼容能力。开发者可以获取兼容性能力，并决定是否根据兼容性能力进行兼容性转换。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| capability | [AssetCompatibleCapability](arkts-medialibrary-photoaccesshelper-assetcompatiblecapability-i.md) | 是 |

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

## setPhotoAlbumOrder

```TypeScript
setPhotoAlbumOrder(orderStyle: number, albumOrders: Array<AlbumOrder>): Promise<void>
```

设置系统、用户和来源相册的排序。使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| orderStyle | number | 是 |
| albumOrders | Array&lt;[AlbumOrder](arkts-medialibrary-photoaccesshelper-albumorder-i-sys.md)&gt; | 是 |

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

## setPreferredCompatibleMode

```TypeScript
setPreferredCompatibleMode(bundleName: string, compatibleMode: PreferredCompatibleMode): Promise<void>
```

根据bundleName配置应用程序设置的首选兼容模式。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| [compatibleMode](arkts-medialibrary-photoaccesshelper-requestoptions-i.md) | [PreferredCompatibleMode](arkts-medialibrary-photoaccesshelper-preferredcompatiblemode-e.md) | 是 |

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

## startAssetAnalysis

```TypeScript
startAssetAnalysis(type: AnalysisType, assetUris?: Array<string>): Promise<number>
```

启动资产分析服务。

**起始版本：** 18

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [AnalysisType](arkts-medialibrary-photoaccesshelper-analysistype-e-sys.md) | 是 |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | Array & lt;string & gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## startAssetAnalysisAsync

```TypeScript
startAssetAnalysisAsync(config: AnalysisConfig, callback: Callback<AnalysisResult>): Promise<number>
```

启动异步资产分析。使用callback异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [AnalysisConfig](arkts-medialibrary-photoaccesshelper-analysisconfig-i-sys.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AnalysisResult](arkts-medialibrary-photoaccesshelper-analysisresult-i-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## startDeepOptimizeSpace

```TypeScript
startDeepOptimizeSpace(callback?: Callback<DeepOptimizeSpaceProgress>): Promise<void>
```

开启深度优化存储空间。使用Promise异步回调。建议先调用[canPerformDeepOptimizeSpace](#canperformdeepoptimizespace)确认当前系统状态是否允许执行，仅在返回true时调用此接口。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeepOptimizeSpaceProgress](arkts-medialibrary-photoaccesshelper-deepoptimizespaceprogress-i-sys.md)&gt; | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800201](../errorcode-medialibrary.md#23800201-不支持的操作类型) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## startThumbnailCreationTask

```TypeScript
startThumbnailCreationTask(predicate: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>): number
```

按指定规则生成缩略图。

**起始版本：** 13

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | dataSharePredicates.DataSharePredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## startThumbnailCreationTask

```TypeScript
startThumbnailCreationTask(predicate: dataSharePredicates.DataSharePredicates, callback: AsyncCallback<void>, response: AsyncCallback<number>): number
```

根据指定规则生成缩略图。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [predicate](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-cloudsyncconfig-i.md) | dataSharePredicates.DataSharePredicates | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
| response | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## stopAssetAnalysis

```TypeScript
stopAssetAnalysis(config: AnalysisConfig): void
```

停止资产分析。

**起始版本：** 24

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [AnalysisConfig](arkts-medialibrary-photoaccesshelper-analysisconfig-i-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## stopDeepOptimizeSpace

```TypeScript
stopDeepOptimizeSpace(): Promise<void>
```

停止深度优化存储空间。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## stopThumbnailCreationTask

```TypeScript
stopThumbnailCreationTask(taskId: number): void
```

停止生成缩略图。

**起始版本：** 13

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| taskId | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## updateGalleryFormInfo

```TypeScript
updateGalleryFormInfo(info: GalleryFormInfo): Promise<void>
```

更新既存的图库卡片的相关信息，并保存到数据库中。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [GalleryFormInfo](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | 是 |

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
