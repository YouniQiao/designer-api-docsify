# MediaAnalysisAlbumChangeRequest（系统接口）

Provides APIs for managing the analysis album change request.

**继承/实现关系：** MediaAnalysisAlbumChangeRequest extends [MediaAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-class MediaAnalysisAlbumChangeRequest extends MediaAlbumChangeRequest--><!--Device-photoAccessHelper-class MediaAnalysisAlbumChangeRequest extends MediaAlbumChangeRequest-End-->

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

Constructor.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-MediaAnalysisAlbumChangeRequest-constructor(album: Album)--><!--Device-MediaAnalysisAlbumChangeRequest-constructor(album: Album)-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| album | [Album](arkts-medialibrary-sendablephotoaccesshelper-album-i-sys.md) | 是 | Highlights** album. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 202 | Called by non-system application |

## 示例

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('MediaAnalysisAlbumChangeRequest constructorDemo');
  let helper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
  let albumFetchOption: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: new dataSharePredicates.DataSharePredicates()
  };
  let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
    await helper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.HIGHLIGHT, albumFetchOption);
  if (albumFetchResult.getCount() === 0) {
    console.error('No album');
    return;
  }
  let highlightAlbum: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
  albumFetchResult.close();
  let changeRequest: photoAccessHelper.MediaAnalysisAlbumChangeRequest =
    new photoAccessHelper.MediaAnalysisAlbumChangeRequest(highlightAlbum);
}
```

## createAnalysisAlbumRequest

```TypeScript
static createAnalysisAlbumRequest(
      context:Context,
      name: string,
      subtype: AlbumSubtype
    ): MediaAnalysisAlbumChangeRequest | null
```

Creates a MediaAnalysisAlbumChangeRequest instance.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MediaAnalysisAlbumChangeRequest-static createAnalysisAlbumRequest(      context:Context,      name: string,      subtype: AlbumSubtype    ): MediaAnalysisAlbumChangeRequest | null--><!--Device-MediaAnalysisAlbumChangeRequest-static createAnalysisAlbumRequest(      context:Context,      name: string,      subtype: AlbumSubtype    ): MediaAnalysisAlbumChangeRequest | null-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c-sys.md) | 是 | Context of the ability instance. |
| name | string | 是 | Name of the album. |
| subtype | [AlbumSubtype](arkts-medialibrary-photoaccesshelper-albumsubtype-e-sys.md) | 是 | Subtype of the album. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaAnalysisAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaanalysisalbumchangerequest-c-sys.md) | Returns a MediaAnalysisAlbumChangeRequest instance. If the operation fails, returns null. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application. |
| 23800151 | The scenario parameter verification fails. &lt;br&gt;Possible causes: &lt;br&gt;1. The input parameter is not within the valid range. |

## createAnalysisAlbumRequest

```TypeScript
static createAnalysisAlbumRequest(
      context:Context,
      name: string,
      subtype: AlbumSubtype
    ): MediaAnalysisAlbumChangeRequest
```

Creates a change request for the **Analysis** album.

> **NOTE：**
> 
> The album name must meet the following requirements:
> 
> - The album name string length ranges from 1 to 255.
> 
> - The album name cannot contain any of the following characters:.. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MediaAnalysisAlbumChangeRequest-static createAnalysisAlbumRequest(      context:Context,      name: string,      subtype: AlbumSubtype    ): MediaAnalysisAlbumChangeRequest--><!--Device-MediaAnalysisAlbumChangeRequest-static createAnalysisAlbumRequest(      context:Context,      name: string,      subtype: AlbumSubtype    ): MediaAnalysisAlbumChangeRequest-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c-sys.md) | 是 | Context of the ability instance. |
| name | string | 是 | Name of the album. |
| subtype | [AlbumSubtype](arkts-medialibrary-photoaccesshelper-albumsubtype-e-sys.md) | 是 | Subtype of the album. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MediaAnalysisAlbumChangeRequest](arkts-medialibrary-photoaccesshelper-mediaanalysisalbumchangerequest-c-sys.md) | MediaAnalysisAlbumChangeRequest instance created. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application |
| 23800151 | The scenario parameter verification fails. &lt;br&gt;Possible causes: &lt;br&gt;1. The input parameter is not within the valid range. |

## 示例

photoAccessHelper的创建请参考[photoAccessHelper.getPhotoAccessHelper](arkts-apis-photoAccessHelper-f.md#photoaccesshelpergetphotoaccesshelper)的示例使用。

```TypeScript
async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper, context: Context) {
  console.info('createAlbumRequestDemo');
  try {
    let albumName: string = 'newAlbumName' + new Date().getTime();
    let albumChangeRequest: photoAccessHelper.MediaAnalysisAlbumChangeRequest = photoAccessHelper.MediaAnalysisAlbumChangeRequest.createAnalysisAlbumRequest(context, albumName, photoAccessHelper.AlbumSubtype.PORTRAIT);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('apply createAlbumRequest successfully');
  } catch (err) {
    console.error(`createAlbumRequestDemo failed with error: ${err.code}, ${err.message}`);
  }
}
```

## setDefaultCoverUri

```TypeScript
setDefaultCoverUri(coverUri: string): void
```

Sets the default cover image for the smart album.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MediaAnalysisAlbumChangeRequest-setDefaultCoverUri(coverUri: string): void--><!--Device-MediaAnalysisAlbumChangeRequest-setDefaultCoverUri(coverUri: string): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| coverUri | string | 是 | URI of the file to be set as the default cover image of the smart album. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 202 | Called by non-system application. |
| 23800151 | The scenario parameter verification fails. &lt;br&gt;Possible causes: &lt;br&gt;1. The input parameter is not within the valid range. |

## 示例

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  console.info('setDefaultCoverUri');
  try {
    let helper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let albumFetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: new dataSharePredicates.DataSharePredicates()
    };
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
      await helper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.PORTRAIT, albumFetchOption);
    if (albumFetchResult.getCount() === 0) {
      console.error('No album');
      return;
    }
    let portraitAlbum: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    albumFetchResult.close();
    // 获取相册中的资源。
    let fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: new dataSharePredicates.DataSharePredicates()
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
      await portraitAlbum.getAssets(fetchOption);
    if (fetchResult.getCount() === 0) {
      console.error('No asset in album');
      fetchResult.close();
      return;
    }
    let asset: photoAccessHelper.PhotoAsset = await fetchResult.getFirstObject();
    let coverUri: string = asset.uri;
    fetchResult.close();
    // 设置默认封面。
    let changeRequest: photoAccessHelper.MediaAnalysisAlbumChangeRequest =
      new photoAccessHelper.MediaAnalysisAlbumChangeRequest(portraitAlbum);
    changeRequest.setDefaultCoverUri(coverUri);
    await helper.applyChanges(changeRequest);
    console.info('setDefaultCoverUri success');
  } catch (err) {
    console.error(`setDefaultCoverUri error: ${err}`);
  }
}
```

## setOrderPosition

ArkTS-Dyn:
```TypeScript
setOrderPosition(assets: Array<PhotoAsset>, position: Array<number>): void
```

ArkTS-Sta:
```TypeScript
setOrderPosition(assets: Array<PhotoAsset>, position: Array<int>): void
```

Sets the sequence of assets in the **Analysis** album.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaAnalysisAlbumChangeRequest-setOrderPosition(assets: Array<PhotoAsset>, position: Array<int>): void--><!--Device-MediaAnalysisAlbumChangeRequest-setOrderPosition(assets: Array<PhotoAsset>, position: Array<int>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| assets | Array&lt;PhotoAsset&gt; | 是 | Assets in the album for which the sequence needs to be set. |
| position | ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt; | 是 | Sequence of assets in the album. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; &lt;br&gt;3. Parameter verification failed. |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 14000011 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |

## 示例

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function example(context: Context) {
  try {
    console.info('setOrderPosition');
    let helper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let albumFetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: new dataSharePredicates.DataSharePredicates()
    };
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> = 
      await helper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.HIGHLIGHT, albumFetchOption);
    if (albumFetchResult.getCount() === 0) {
      console.error('No album');
      return;
    }
    let highlightAlbum: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    albumFetchResult.close();
    let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
    const fetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: predicates
    };
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
      await highlightAlbum.getAssets(fetchOption);
    let assets: photoAccessHelper.PhotoAsset[] = await fetchResult.getAllObjects();
    let indexes: number[] = [];
    for (let i = 0; i < assets.length; i++) {
      indexes.push(i);
    }
    let changeRequest: photoAccessHelper.MediaAnalysisAlbumChangeRequest =
      new photoAccessHelper.MediaAnalysisAlbumChangeRequest(highlightAlbum);
    changeRequest.setOrderPosition(assets, indexes);
    await helper.applyChanges(changeRequest);
    console.info(`setOrderPosition ${indexes}`);
  } catch (err) {
    console.error(`setOrderPosition error: ${err}`);
  }
}
```

## setRelationship

```TypeScript
setRelationship(relationship: string): Promise<void>
```

Sets the relationships of a person in the portrait album.

The supported relationship names include:  
| Unique ID | Description |  
| ---------- | ------- |  
| me | Me|  
| son | Son|  
| daughter | Daughter|  
| wife | Wife|  
| husband | Husband|  
| father | Father|  
| mother | Mother|  
| colleague | Colleague|  
| friend | Friend|  
| classmate | Classmate|  
| best_friend_female | Best female friend|  
| boyfriend | Boyfriend|  
| girlfriend | Girlfriend|  
| family | Family|  
| maternal_grandfather | Maternal grandfather|  
| maternal_grandmother | Maternal grandmother|  
| paternal_grandfather | Paternal grandfather|  
| paternal_grandmother | Paternal grandmother|  
| older_brother | Older brother|  
| older_sister | Older sister|  
| younger_brother | Younger brother|  
| younger_sister | Younger sister|  
| relative | Relative|  
| other | Other|

**起始版本：** 21

**ArkTS模式：** ArkTS-Dyn起始版本为21；ArkTS-Sta起始版本为26.0.0。

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-MediaAnalysisAlbumChangeRequest-setRelationship(relationship: string): Promise<void>--><!--Device-MediaAnalysisAlbumChangeRequest-setRelationship(relationship: string): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| relationship | string | 是 | Name of the relationship to set. &lt;br&gt;You can set it to an empty string to remove the current relationship setting. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 201 | Permission denied |
| 202 | Called by non-system application |
| 23800151 | The scenario parameter verification fails. &lt;br&gt;Possible causes: &lt;br&gt;1. The input parameter is not within the valid range. |

## 示例

```TypeScript
import { dataSharePredicates } from '@kit.ArkData';

async function SetRelationshipExample(context: Context, relationship: string) {
  try {
    console.info('setRelationship');
    let helper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
    let albumFetchOption: photoAccessHelper.FetchOptions = {
      fetchColumns: [],
      predicates: new dataSharePredicates.DataSharePredicates()
    };
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
      await helper.getAlbums(photoAccessHelper.AlbumType.SMART, photoAccessHelper.AlbumSubtype.PORTRAIT, albumFetchOption);
    if (albumFetchResult.getCount() === 0) {
      console.error('No album');
      return;
    }
    let portraitAlbum: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    albumFetchResult.close();
    let changeRequest: photoAccessHelper.MediaAnalysisAlbumChangeRequest =
      new photoAccessHelper.MediaAnalysisAlbumChangeRequest(portraitAlbum);
    changeRequest.setRelationship(relationship);
    await helper.applyChanges(changeRequest);
    console.info(`setRelationship ${relationship}`);
  } catch (err) {
    console.error(`setRelationship error: ${err}`);
  }
}
```

