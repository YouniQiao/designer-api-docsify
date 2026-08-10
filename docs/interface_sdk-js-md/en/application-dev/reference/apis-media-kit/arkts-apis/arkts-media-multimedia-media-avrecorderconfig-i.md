# AVRecorderConfig

音视频录制的参数。

audioSourceType和videoSourceType参数用于区分纯音频录制、纯视频录制和音视频录制。纯音频录制仅设置audioSourceType。纯视频录制仅设置videoSourceType。音视频录制需同时设置audioSourceType和videoSourceType。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-interface AVRecorderConfig--><!--Device-unnamed-interface AVRecorderConfig-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## audioSourceType

```TypeScript
audioSourceType?: AudioSourceType
```

录制的音频源类型。录制音频时该参数为必填参数。&lt;br&gt;**原子化服务API**：从API version 12开始，该接口支持在原子化服务中使用。

**Type:** [AudioSourceType](arkts-media-multimedia-media-audiosourcetype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderConfig-audioSourceType?: AudioSourceType--><!--Device-AVRecorderConfig-audioSourceType?: AudioSourceType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## fileGenerationMode

```TypeScript
fileGenerationMode?: FileGenerationMode
```

文件创建模式，与on('photoAssetAvailable')配合使用。

**Type:** [FileGenerationMode](arkts-media-multimedia-media-filegenerationmode-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVRecorderConfig-fileGenerationMode?: FileGenerationMode--><!--Device-AVRecorderConfig-fileGenerationMode?: FileGenerationMode-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## location

```TypeScript
location?: Location
```

录制视频的地理位置。默认不记录地理位置信息。&lt;br&gt;此接口从API version 6开始支持，从API version 12开始废弃，建议使用**AVMetadata.location**替代。如果同时设置了两个参数，将使用**AVMetadata.location**。

**Type:** [Location](../../apis-location-kit/arkts-apis/arkts-location-geolocationmanager-location-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Substitutes:** ohos.multimedia.media/media.AVMetadata#location

<!--Device-AVRecorderConfig-location?: Location--><!--Device-AVRecorderConfig-location?: Location-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## maxDuration

```TypeScript
maxDuration?: int
```

最大录制时长，单位为秒。取值范围为[1, 2^31-1]。如果提供了无效值，将重置为最大允许时长。一旦录制达到指定时长，将自动停止并通过**stateChange**回调通知录制已停止：AVRecorderState = 'stopped'，StateChangeReason = BACKGROUND。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-AVRecorderConfig-maxDuration?: int--><!--Device-AVRecorderConfig-maxDuration?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## metadata

```TypeScript
metadata?: AVMetadata
```

元数据。详见AVMetadata。

**Type:** [AVMetadata](../../apis-avsession-kit/arkts-apis/arkts-avsession-avsession-avmetadata-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AVRecorderConfig-metadata?: AVMetadata--><!--Device-AVRecorderConfig-metadata?: AVMetadata-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## profile

```TypeScript
profile: AVRecorderProfile
```

录制配置参数。此参数为必填参数。&lt;br&gt;**原子化服务API**：从API version 12开始，该接口支持在原子化服务中使用。

**Type:** [AVRecorderProfile](arkts-media-multimedia-media-avrecorderprofile-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderConfig-profile: AVRecorderProfile--><!--Device-AVRecorderConfig-profile: AVRecorderProfile-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## rotation

```TypeScript
rotation?: number
```

录制视频的旋转角度。MP4视频取值可为0（默认）、90、180或270。&lt;br&gt;此接口从API version 6开始支持，从API version 12开始废弃，建议使用**AVMetadata.videoOrientation**替代。如果同时设置了两个参数，将使用**AVMetadata.videoOrientation**。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 12

**Substitutes:** ohos.multimedia.media/media.AVMetadata#videoOrientation

<!--Device-AVRecorderConfig-rotation?: number--><!--Device-AVRecorderConfig-rotation?: number-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## url

```TypeScript
url: string
```

录制输出URL：fd://xx（fd句柄）。&lt;br&gt;此参数为必填参数。&lt;br&gt;**原子化服务API**：从API version 12开始，该接口支持在原子化服务中使用。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AVRecorderConfig-url: string--><!--Device-AVRecorderConfig-url: string-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

## videoSourceType

```TypeScript
videoSourceType?: VideoSourceType
```

录制的视频源类型。录制视频时该参数为必填参数。

**Type:** [VideoSourceType](arkts-media-multimedia-media-videosourcetype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AVRecorderConfig-videoSourceType?: VideoSourceType--><!--Device-AVRecorderConfig-videoSourceType?: VideoSourceType-End-->

**System capability:** SystemCapability.Multimedia.Media.AVRecorder

