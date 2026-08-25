# CloudMediaAssetManager（系统接口）

云端媒体资产管理类，该类用于管理云端资产的下载任务，以及删除云端资产在本地的数据和文件。

**起始版本：** 14

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## cancelDownloadCloudMedia

```TypeScript
cancelDownloadCloudMedia(): Promise<void>
```

取消云端媒体资产下载任务。

**起始版本：** 14

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

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
| 14000011 |

## cancelDownloadSpecificCloudMedia

```TypeScript
cancelDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>
```

取消云端媒体资产批量下载任务。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | string[] \| null | 是 |

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

## getCloudMediaAssetManagerInstance

```TypeScript
static getCloudMediaAssetManagerInstance(context: Context): CloudMediaAssetManager
```

获取云端媒体资产管理类实例。

**起始版本：** 14

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [CloudMediaAssetManager](arkts-medialibrary-photoaccesshelper-cloudmediaassetmanager-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## getCloudMediaAssetStatus

```TypeScript
getCloudMediaAssetStatus(): Promise<CloudMediaAssetStatus>
```

查询云端媒体资产下载任务状态。

**起始版本：** 14

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CloudMediaAssetStatus](arkts-medialibrary-photoaccesshelper-cloudmediaassetstatus-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 14000011 |

## offDownloadProgressChange

```TypeScript
offDownloadProgressChange(callback?: Callback<CloudAssetDownloadProgressInfo>): void
```

取消监听云端媒体资产批量下载进度相关通知。

**起始版本：** 21

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CloudAssetDownloadProgressInfo](arkts-medialibrary-photoaccesshelper-cloudassetdownloadprogressinfo-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## onDownloadProgressChange

```TypeScript
onDownloadProgressChange(callback: Callback<CloudAssetDownloadProgressInfo>): void
```

监听云端媒体资产批量下载进度。

**起始版本：** 21

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CloudAssetDownloadProgressInfo](arkts-medialibrary-photoaccesshelper-cloudassetdownloadprogressinfo-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## pauseDownloadCloudMedia

```TypeScript
pauseDownloadCloudMedia(): Promise<void>
```

暂停云端媒体资产下载任务。

**起始版本：** 14

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

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
| 14000011 |

## pauseDownloadSpecificCloudMedia

```TypeScript
pauseDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>
```

暂停云端媒体资产批量下载任务。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | string[] \| null | 是 |

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

## queryDownloadSpecificCloudMediaDetails

```TypeScript
queryDownloadSpecificCloudMediaDetails(predicates: dataSharePredicates.DataSharePredicates): Promise<CloudAssetDownloadStatus>
```

查询云端媒体资产批量下载任务信息。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[CloudAssetDownloadStatus](arkts-medialibrary-photoaccesshelper-cloudassetdownloadstatus-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |

## queryDownloadSpecificCloudMediaTaskCount

```TypeScript
queryDownloadSpecificCloudMediaTaskCount(predicates: dataSharePredicates.DataSharePredicates): Promise<number>
```

查询云端媒体资产批量下载任务总量。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| predicates | dataSharePredicates.DataSharePredicates | 是 |

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

## resumeDownloadSpecificCloudMedia

```TypeScript
resumeDownloadSpecificCloudMedia(assetUris: string[] | null): Promise<void>
```

恢复云端媒体资产批量下载任务。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | string[] \| null | 是 |

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

## retainCloudMediaAsset

```TypeScript
retainCloudMediaAsset(retainType: CloudMediaRetainType): Promise<void>
```

删除云端媒体资产在本地的元数据和文件。

**起始版本：** 14

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| retainType | [CloudMediaRetainType](arkts-medialibrary-photoaccesshelper-cloudmediaretaintype-e-sys.md) | 是 |

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

## startDownloadCloudMedia

```TypeScript
startDownloadCloudMedia(downloadType: CloudMediaDownloadType): Promise<void>
```

开始或恢复云端媒体资产下载任务。

**起始版本：** 14

**需要权限：** ohos.permission.CLOUDFILE_SYNC_MANAGER

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| downloadType | [CloudMediaDownloadType](arkts-medialibrary-photoaccesshelper-cloudmediadownloadtype-e-sys.md) | 是 |

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

## startDownloadSpecificCloudMedia

```TypeScript
startDownloadSpecificCloudMedia(assetUris: string[]): Promise<Map<string, CloudAssetDownloadCode>>
```

开始云端媒体资产批量下载任务。使用Promise异步回调。

**起始版本：** 21

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [assetUris](arkts-medialibrary-photoaccesshelper-galleryforminfo-i-sys.md) | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Map&lt;string, [CloudAssetDownloadCode](arkts-medialibrary-photoaccesshelper-cloudassetdownloadcode-e-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
