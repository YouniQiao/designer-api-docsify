# AVMetadataExtractor

元数据获取类，用于从媒体资源中获取元数据、缩略图。在调用AVMetadataExtractor的方法前，需要先通过 [media.createAVMetadataExtractor](arkts-media-media-createavmetadataextractor-f.md) 构建一个AVMetadataExtractor实例。获取音频或视频元数据、视频缩略图的demo可参考：[使用AVMetadataExtractor提取音视频元数据信息(ArkTS)](../../../media/media/avmetadataextractor.md)。

> **说明：**&gt;
> - 本Interface首批接口从API version 11开始支持。

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

## 导入模块

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## getFrameIndexByTime

```TypeScript
getFrameIndexByTime(timeUs: number): Promise<number>
```

获取目标视频时间戳对应的视频帧号（仅支持MP4视频文件）。使用Promise异步回调。

**起始版本：** 12

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

## getTimeByFrameIndex

```TypeScript
getTimeByFrameIndex(index: number): Promise<number>
```

获取目标视频帧号对应的视频时间戳（仅支持MP4视频文件）。使用Promise异步回调。

**起始版本：** 12

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
