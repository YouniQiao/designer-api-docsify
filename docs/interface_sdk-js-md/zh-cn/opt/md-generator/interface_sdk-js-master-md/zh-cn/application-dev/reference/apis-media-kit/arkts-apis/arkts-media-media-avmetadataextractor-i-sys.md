# AVMetadataExtractor

元数据获取类，用于从媒体资源中获取元数据、缩略图。在调用AVMetadataExtractor的方法前，需要先通过 [media.createAVMetadataExtractor](arkts-media-media-createavmetadataextractor-f.md#createavmetadataextractor) 构建一个AVMetadataExtractor实例。 获取音频或视频元数据、视频缩略图的demo可参考：[使用AVMetadataExtractor提取音视频元数据信息(ArkTS)](../../../media/media/avmetadataextractor.md)。 > **说明：** > > - 本Interface首批接口从API version 11开始支持。

**起始版本：** 23

<!--Device-media-interface AVMetadataExtractor--><!--Device-media-interface AVMetadataExtractor-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

## 导入模块

```TypeScript
```

## getFrameIndexByTime

```TypeScript
getFrameIndexByTime(timeUs: number): Promise<number>
```

Obtains the video frame number corresponding to a video timestamp. Only MP4 video files are supported.

**起始版本：** 23

<!--Device-AVMetadataExtractor-getFrameIndexByTime(timeUs: long): Promise<int>--><!--Device-AVMetadataExtractor-getFrameIndexByTime(timeUs: long): Promise<int>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeUs | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |

**示例**

```TypeScript
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';

avMetadataExtractor.getFrameIndexByTime(0).then((index: number) => {
  console.info(`Succeeded getFrameIndexByTime index: ${index}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getFrameIndexByTime ${err.message}`);
})
```

## getTimeByFrameIndex

```TypeScript
getTimeByFrameIndex(index: number): Promise<number>
```

Obtains the video timestamp corresponding to a video frame number. Only MP4 video files are supported.

**起始版本：** 23

<!--Device-AVMetadataExtractor-getTimeByFrameIndex(index: int): Promise<long>--><!--Device-AVMetadataExtractor-getTimeByFrameIndex(index: int): Promise<long>-End-->

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [5400102](../errorcode-media.md#5400102-当前状态不支持此操作) |
| [5400106](../errorcode-media.md#5400106-不支持的规格) |

**示例**

```TypeScript
import { media } from '@kit.MediaKit';
import { BusinessError } from '@kit.BasicServicesKit';

avMetadataExtractor.getTimeByFrameIndex(0).then((timeUs: number) => {
  console.info(`Succeeded getTimeByFrameIndex timeUs: ${timeUs}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getTimeByFrameIndex ${err.message}`);
})
```
