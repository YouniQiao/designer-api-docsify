# AVMetadata

媒体元数据的相关属性。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-interface AVMetadata--><!--Device-avSession-interface AVMetadata-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## album

```TypeScript
album?: string
```

专辑名称。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-album?: string--><!--Device-AVMetadata-album?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## artist

```TypeScript
artist?: string
```

艺术家。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-artist?: string--><!--Device-AVMetadata-artist?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## assetId

```TypeScript
assetId: string
```

媒体ID。媒体信息的唯一标识，由应用自定义。

- 该属性发生变化则其他元数据属性都将被刷新。  
- 若该属性维持不变，且不设置相应的媒体元数据信息，那么将不会更新对应的媒体元数据信息。  
- 当该属性设为空值时，调用[setAVMetadata](arkts-avsession-avsession-avsession-i.md#setavmetadata)方法将失败，返回错误码6600101。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-assetId: string--><!--Device-AVMetadata-assetId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## author

```TypeScript
author?: string
```

专辑作者。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-author?: string--><!--Device-AVMetadata-author?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## avQueueId

```TypeScript
avQueueId?: string
```

歌单（歌曲列表）唯一标识Id。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVMetadata-avQueueId?: string--><!--Device-AVMetadata-avQueueId?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## avQueueImage

```TypeScript
avQueueImage?: image.PixelMap | string
```

歌单（歌曲列表）封面图。

图片的像素数据或者图片路径地址（本地路径或网络路径）。应用通过setAVMetadata设置图片数据。

- 设置的数据类型为PixelMap时，通过getAVMetadata获取的将为PixelMap。  
- 设置为url图片路径，获取的为url图片路径。

**Type:** image.PixelMap \| string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVMetadata-avQueueImage?: image.PixelMap | string--><!--Device-AVMetadata-avQueueImage?: image.PixelMap | string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## avQueueName

```TypeScript
avQueueName?: string
```

歌单（歌曲列表）名称。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVMetadata-avQueueName?: string--><!--Device-AVMetadata-avQueueName?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## bundleIcon

```TypeScript
readonly bundleIcon?: image.PixelMap
```

应用图标图片的像素数据。只读类型，不从应用侧设置。

**Type:** image.PixelMap

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AVMetadata-readonly bundleIcon?: image.PixelMap--><!--Device-AVMetadata-readonly bundleIcon?: image.PixelMap-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## composer

```TypeScript
composer?: string
```

作曲者。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AVMetadata-composer?: string--><!--Device-AVMetadata-composer?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## description

```TypeScript
description?: string
```

媒体描述。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-description?: string--><!--Device-AVMetadata-description?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## displayTags

```TypeScript
displayTags?: int
```

媒体资源的金标类型，取值参考[DisplayTag](arkts-avsession-avsession-displaytag-e.md)。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVMetadata-displayTags?: int--><!--Device-AVMetadata-displayTags?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## drmSchemes

```TypeScript
drmSchemes?: Array<string>
```

当前session支持的DRM方案，取值为DRM方案uuid。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVMetadata-drmSchemes?: Array<string>--><!--Device-AVMetadata-drmSchemes?: Array<string>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## duration

```TypeScript
duration?: long
```

媒体时长，单位毫秒（ms）。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-duration?: long--><!--Device-AVMetadata-duration?: long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## fastForwardSkipIntervals

```TypeScript
fastForwardSkipIntervals?: SkipIntervals
```

快进支持的时间间隔。默认为SECONDS_15，即15秒。

系统会使用此值作为快进操作的时间间隔，而非skipIntervals的值。

若未设置此参数，快进操作的时间间隔仍会沿用skipIntervals的值。

**起始版本**：26.0.0

**Type:** [SkipIntervals](arkts-avsession-avsession-skipintervals-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMetadata-fastForwardSkipIntervals?: SkipIntervals--><!--Device-AVMetadata-fastForwardSkipIntervals?: SkipIntervals-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## filter

```TypeScript
filter?: int
```

当前会话支持的协议，默认为TYPE_CAST_PLUS_STREAM。具体取值参考[ProtocolType](arkts-avsession-avsession-protocoltype-e.md)。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-filter?: int--><!--Device-AVMetadata-filter?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## lyric

```TypeScript
lyric?: string
```

媒体歌词内容。应用需将歌词内容拼接为一个字符串传入。

字符串长度需小于40960字节。

**说明：** 系统支持简单版的LRC格式（Simple LRC format）的歌词文本内容。当传入的歌词内容不规范（例如：出现重复的时间戳等），将导致解析失败，并在系统中显示异常。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AVMetadata-lyric?: string--><!--Device-AVMetadata-lyric?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## mediaImage

```TypeScript
mediaImage?: image.PixelMap | string
```

图片的像素数据或者图片路径地址（本地路径或网络路径）。应用通过setAVMetadata设置图片数据。

- 设置的数据类型为PixelMap时，通过getAVMetadata获取的将为PixelMap。  
- 设置为url图片路径，获取的为url图片路径。

**Type:** image.PixelMap \| string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-mediaImage?: image.PixelMap | string--><!--Device-AVMetadata-mediaImage?: image.PixelMap | string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## nextAssetId

```TypeScript
nextAssetId?: string
```

下一首媒体ID。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-nextAssetId?: string--><!--Device-AVMetadata-nextAssetId?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## previousAssetId

```TypeScript
previousAssetId?: string
```

上一首媒体ID。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-previousAssetId?: string--><!--Device-AVMetadata-previousAssetId?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## publishDate

```TypeScript
publishDate?: Date
```

发行日期。

**Type:** Date

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-AVMetadata-publishDate?: Date--><!--Device-AVMetadata-publishDate?: Date-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## rewindSkipIntervals

```TypeScript
rewindSkipIntervals?: SkipIntervals
```

快退支持的时间间隔。默认为SECONDS_15，即15秒。

系统会使用此值作为快退操作的时间间隔，而非skipIntervals的值。

若未设置此参数，快退操作的时间间隔仍会沿用skipIntervals的值。

**起始版本**：26.0.0

**Type:** [SkipIntervals](arkts-avsession-avsession-skipintervals-e.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AVMetadata-rewindSkipIntervals?: SkipIntervals--><!--Device-AVMetadata-rewindSkipIntervals?: SkipIntervals-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## singleLyricText

```TypeScript
singleLyricText?: string
```

单条媒体歌词内容。应用需将歌词内容拼接为一个字符串传入（不包含时间戳）。

字符串长度小于40960字节。

**Type:** string

**Since:** 17

**ArkTS mode:** ArkTS-Dyn since version 17; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AVMetadata-singleLyricText?: string--><!--Device-AVMetadata-singleLyricText?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## skipIntervals

```TypeScript
skipIntervals?: SkipIntervals
```

快进快退支持的时间间隔。默认为SECONDS_15，即15秒。

**Type:** [SkipIntervals](arkts-avsession-avsession-skipintervals-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AVMetadata-skipIntervals?: SkipIntervals--><!--Device-AVMetadata-skipIntervals?: SkipIntervals-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## subtitle

```TypeScript
subtitle?: string
```

子标题。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-subtitle?: string--><!--Device-AVMetadata-subtitle?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## title

```TypeScript
title?: string
```

标题。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-title?: string--><!--Device-AVMetadata-title?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## writer

```TypeScript
writer?: string
```

词作者。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVMetadata-writer?: string--><!--Device-AVMetadata-writer?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

