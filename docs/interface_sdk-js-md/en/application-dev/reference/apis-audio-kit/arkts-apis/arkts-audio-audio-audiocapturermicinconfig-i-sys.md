# AudioCapturerMicInConfig (System API)

Describes audio capturer configuration options that can capture microphone input (mic-in) audio data before any processing.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-audio-interface AudioCapturerMicInConfig--><!--Device-audio-interface AudioCapturerMicInConfig-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## capturerInfo

```TypeScript
capturerInfo: AudioCapturerInfo
```

Capturer attribute information.

**Type:** [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInConfig-capturerInfo: AudioCapturerInfo--><!--Device-AudioCapturerMicInConfig-capturerInfo: AudioCapturerInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## ecStreamInfo

```TypeScript
ecStreamInfo?: AudioStreamInfo
```

Stream information that describe echo reference signal.If not set this attribute, the capturer will only record Mic-In audio stream.

**Type:** [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInConfig-ecStreamInfo?: AudioStreamInfo--><!--Device-AudioCapturerMicInConfig-ecStreamInfo?: AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## micInStreamInfo

```TypeScript
micInStreamInfo: AudioStreamInfo
```

Stream information that describe Mic-In audio stream.

**Type:** [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInConfig-micInStreamInfo: AudioStreamInfo--><!--Device-AudioCapturerMicInConfig-micInStreamInfo: AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## processedStreamInfo

```TypeScript
processedStreamInfo?: AudioStreamInfo
```

描述处理后的音频流的流信息。

**Type:** [AudioStreamInfo](arkts-audio-audio-audiostreaminfo-i.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AudioCapturerMicInConfig-processedStreamInfo?: AudioStreamInfo--><!--Device-AudioCapturerMicInConfig-processedStreamInfo?: AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

