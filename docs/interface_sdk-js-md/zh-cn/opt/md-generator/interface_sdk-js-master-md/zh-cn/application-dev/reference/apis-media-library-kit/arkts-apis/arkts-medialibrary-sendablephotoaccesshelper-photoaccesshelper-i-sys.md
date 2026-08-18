# PhotoAccessHelper

提供操作系统媒体资源能力的接口。

**继承/实现关系：** PhotoAccessHelper extends lang.ISendable

**起始版本：** 12

<!--Device-sendablePhotoAccessHelper-interface PhotoAccessHelper--><!--Device-sendablePhotoAccessHelper-interface PhotoAccessHelper-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
```

## createAsset

```TypeScript
createAsset(displayName: string): Promise<PhotoAsset>
```

指定待创建的图片或者视频的文件名，创建图片或视频资源。使用Promise异步回调。 待创建的文件名参数规格为： - 应包含有效文件主名和图片或视频扩展名。 - 文件名字符串长度为1~255。 - 文件主名中不允许出现的非法英文字符。 API18开始，非法字符包括：\ / : * ? " &lt; &gt; | API10-17，非法字符包括：. .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**起始版本：** 12

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAsset(displayName: string): Promise<PhotoAsset>--><!--Device-PhotoAccessHelper-createAsset(displayName: string): Promise<PhotoAsset>-End-->

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
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000001 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

**示例**

phAccessHelper的创建请参考[@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)](arkts-file-sendablephotoaccesshelper.md#ohosfilesendablephotoaccesshelper)的示例使用。

```TypeScript
async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  try {
    let testFileName: string = 'testFile' + Date.now() + '.jpg';
    let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await phAccessHelper.createAsset(testFileName);
    console.info('createAsset file displayName' + photoAsset.displayName);
    console.info('createAsset successfully');
  } catch (err) {
    console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
  }
}
```

## createAsset

```TypeScript
createAsset(displayName: string, options: photoAccessHelper.PhotoCreateOptions): Promise<PhotoAsset>
```

指定待创建的图片或者视频的文件名和创建选项，创建图片或视频资源。使用Promise异步回调。 待创建的文件名参数规格为： - 应包含有效文件主名和图片或视频扩展名。 - 文件名字符串长度为1~255。 - 文件主名中不允许出现的非法英文字符。 API18开始，非法字符包括： \ / : * ? " &lt; &gt; | API10-17，非法字符包括： . .. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**起始版本：** 12

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAccessHelper-createAsset(displayName: string, options: photoAccessHelper.PhotoCreateOptions): Promise<PhotoAsset>--><!--Device-PhotoAccessHelper-createAsset(displayName: string, options: photoAccessHelper.PhotoCreateOptions): Promise<PhotoAsset>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayName | string | 是 |
| options | photoAccessHelper.PhotoCreateOptions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PhotoAsset & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000001 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

**示例**

phAccessHelper的创建请参考[@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)](arkts-file-sendablephotoaccesshelper.md#ohosfilesendablephotoaccesshelper)的示例使用。

```TypeScript
async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper) {
  console.info('createAssetDemo');
  try {
    let testFileName:string = 'testFile' + Date.now() + '.jpg';
    let createOption: photoAccessHelper.PhotoCreateOptions = {
      subtype: photoAccessHelper.PhotoSubtype.DEFAULT
    }
    let photoAsset: sendablePhotoAccessHelper.PhotoAsset = await phAccessHelper.createAsset(testFileName, createOption);
    console.info('createAsset file displayName' + photoAsset.displayName);
    console.info('createAsset successfully');
  } catch (err) {
    console.error(`createAsset failed, error: ${err.code}, ${err.message}`);
  }
}
```

## getHiddenAlbums

```TypeScript
getHiddenAlbums(
      mode: photoAccessHelper.HiddenPhotosDisplayMode,
      options?: photoAccessHelper.FetchOptions
    ): Promise<FetchResult<Album>>
```

根据隐藏文件显示模式和检索选项获取系统中的隐藏相册。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.READ_IMAGEVIDEO and ohos.permission.MANAGE_PRIVATE_PHOTOS

<!--Device-PhotoAccessHelper-getHiddenAlbums(      mode: photoAccessHelper.HiddenPhotosDisplayMode,      options?: photoAccessHelper.FetchOptions    ): Promise<FetchResult<Album>>--><!--Device-PhotoAccessHelper-getHiddenAlbums(      mode: photoAccessHelper.HiddenPhotosDisplayMode,      options?: photoAccessHelper.FetchOptions    ): Promise<FetchResult<Album>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | photoAccessHelper.HiddenPhotosDisplayMode | 是 |
| options | photoAccessHelper.FetchOptions | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;FetchResult & lt;Album & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

## getPhotoAssets

```TypeScript
getPhotoAssets(assetsData: photoAccessHelper.ValuesBucket[]): Promise<PhotoAsset[]>
```

将ValuesBucket记录转换为PhotoAsset对象。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoAccessHelper-getPhotoAssets(assetsData: photoAccessHelper.ValuesBucket[]): Promise<PhotoAsset[]>--><!--Device-PhotoAccessHelper-getPhotoAssets(assetsData: photoAccessHelper.ValuesBucket[]): Promise<PhotoAsset[]>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| assetsData | photoAccessHelper.ValuesBucket[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PhotoAsset[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

**示例**

phAccessHelper的创建请参考[@ohos.file.sendablePhotoAccessHelper (基于Sendable对象的相册管理模块)](arkts-file-sendablephotoaccesshelper.md#ohosfilesendablephotoaccesshelper)的示例使用。

```TypeScript
async function example(phAccessHelper: sendablePhotoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('getPhotoAssets demo');
  let valuesArr: photoAccessHelper.ValuesBucket[] = [];
  let resultSet: photoAccessHelper.ResultSet | undefined = undefined;
  let photoAssetArr: sendablePhotoAccessHelper.PhotoAsset[] = [];
  let QUERY_SQL = 'SELECT file_id,data,display_name,media_type,subtype from Photos limit 100';
  try {
    resultSet = await photoAccessHelper.getPhotoAccessHelper(context).query(QUERY_SQL);
    let index: number = 0;
    while(resultSet && index < resultSet.rowCount){
      resultSet.goToRow(index);
      valuesArr.push(resultSet.getRow());
      index++;
    }
    photoAssetArr = await phAccessHelper.getPhotoAssets(valuesArr);
    console.info('getPhotoAssets successfully');
  } catch (err) {
    console.error(`valuesArr failed: ${err.code}, ${err.message}`);
  }
}
```

## getSharedPhotoAssets

```TypeScript
getSharedPhotoAssets(options: photoAccessHelper.FetchOptions): Array<SharedPhotoAsset>
```

Fetch shared photo assets.

**起始版本：** 14

**需要权限：** ohos.permission.ACCESS_MEDIALIB_THUMB_DB

<!--Device-PhotoAccessHelper-getSharedPhotoAssets(options: photoAccessHelper.FetchOptions): Array<SharedPhotoAsset>--><!--Device-PhotoAccessHelper-getSharedPhotoAssets(options: photoAccessHelper.FetchOptions): Array<SharedPhotoAsset>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | photoAccessHelper.FetchOptions | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;SharedPhotoAsset & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |
