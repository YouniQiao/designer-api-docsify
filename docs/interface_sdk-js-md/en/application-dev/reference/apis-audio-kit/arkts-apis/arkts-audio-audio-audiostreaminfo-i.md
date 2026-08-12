# AudioStreamInfo

Describes audio stream information.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioStreamInfo--><!--Device-audio-interface AudioStreamInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## channelLayout

```TypeScript
channelLayout?: AudioChannelLayout
```

Audio channel layout. The default value is **0x0**.

**Type:** [AudioChannelLayout](arkts-audio-audio-audiochannellayout-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioStreamInfo-channelLayout?: AudioChannelLayout--><!--Device-AudioStreamInfo-channelLayout?: AudioChannelLayout-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## channels

```TypeScript
channels: AudioChannel
```

Number of audio channels.

**Type:** [AudioChannel](arkts-audio-audio-audiochannel-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioStreamInfo-channels: AudioChannel--><!--Device-AudioStreamInfo-channels: AudioChannel-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## encodingType

```TypeScript
encodingType: AudioEncodingType
```

Audio encoding type.

**Type:** [AudioEncodingType](arkts-audio-audio-audioencodingtype-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioStreamInfo-encodingType: AudioEncodingType--><!--Device-AudioStreamInfo-encodingType: AudioEncodingType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## sampleFormat

```TypeScript
sampleFormat: AudioSampleFormat
```

Audio sample format.

**Type:** [AudioSampleFormat](arkts-audio-audio-audiosampleformat-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-AudioStreamInfo-sampleFormat: AudioSampleFormat--><!--Device-AudioStreamInfo-sampleFormat: AudioSampleFormat-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## samplingRate

```TypeScript
samplingRate: AudioSamplingRate | int
```

Audio sampling rate.

**Type:** ArkTS-Dyn: [AudioSamplingRate](arkts-audio-audio-audiosamplingrate-e.md) \| number  <br>ArkTS-Sta：[AudioSamplingRate](arkts-audio-audio-audiosamplingrate-e.md) \| int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Model restriction:** 
- API version 26.0.0 and later: This API can be used in both the stage model and FA model.

<!--Device-AudioStreamInfo-samplingRate: AudioSamplingRate | int--><!--Device-AudioStreamInfo-samplingRate: AudioSamplingRate | int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

