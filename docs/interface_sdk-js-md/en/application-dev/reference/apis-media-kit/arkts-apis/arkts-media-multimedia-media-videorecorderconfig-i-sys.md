# VideoRecorderConfig (System API)

视频录制配置定义。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-interface VideoRecorderConfig--><!--Device-unnamed-interface VideoRecorderConfig-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## audioSourceType

```TypeScript
audioSourceType?: AudioSourceType
```

音频源类型，详见AudioSourceType。

**Type:** [AudioSourceType](arkts-media-multimedia-media-audiosourcetype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorderConfig-audioSourceType?: AudioSourceType--><!--Device-VideoRecorderConfig-audioSourceType?: AudioSourceType-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

## location

```TypeScript
location?: Location
```

地理位置信息。

**Type:** [Location](../../apis-location-kit/arkts-apis/arkts-location-geolocationmanager-location-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorderConfig-location?: Location--><!--Device-VideoRecorderConfig-location?: Location-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

## profile

```TypeScript
profile: VideoRecorderProfile
```

视频录制配置参数，可通过getVideoRecorderProfile获取，详见VideoRecorderProfile。

**Type:** [VideoRecorderProfile](arkts-media-multimedia-media-videorecorderprofile-i-sys.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorderConfig-profile: VideoRecorderProfile--><!--Device-VideoRecorderConfig-profile: VideoRecorderProfile-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

## rotation

```TypeScript
rotation?: int
```

设置视频输出文件中的旋转角度，用于文件播放。仅mp4格式支持。旋转角度取值为{0, 90, 180, 270}，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorderConfig-rotation?: int--><!--Device-VideoRecorderConfig-rotation?: int-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

## url

```TypeScript
url: string
```

视频输出URI。支持两种URI格式。格式：scheme + "://" + "context"。fd格式：fd://fd

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorderConfig-url: string--><!--Device-VideoRecorderConfig-url: string-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

## videoSourceType

```TypeScript
videoSourceType: VideoSourceType
```

视频源类型，详见VideoSourceType。

**Type:** [VideoSourceType](arkts-media-multimedia-media-videosourcetype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VideoRecorderConfig-videoSourceType: VideoSourceType--><!--Device-VideoRecorderConfig-videoSourceType: VideoSourceType-End-->

**System capability:** SystemCapability.Multimedia.Media.VideoRecorder

**System API:** This is a system API.

