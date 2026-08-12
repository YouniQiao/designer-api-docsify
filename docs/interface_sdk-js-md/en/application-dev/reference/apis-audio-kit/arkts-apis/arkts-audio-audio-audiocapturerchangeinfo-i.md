# AudioCapturerChangeInfo

Describes the audio capturer change event.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioCapturerChangeInfo--><!--Device-audio-interface AudioCapturerChangeInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
```

## capturerInfo

```TypeScript
readonly capturerInfo: AudioCapturerInfo
```

Audio capturer information.

**Type:** [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioCapturerChangeInfo-readonly capturerInfo: AudioCapturerInfo--><!--Device-AudioCapturerChangeInfo-readonly capturerInfo: AudioCapturerInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## deviceDescriptors

```TypeScript
readonly deviceDescriptors: AudioDeviceDescriptors
```

Audio device information.

**Type:** [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioCapturerChangeInfo-readonly deviceDescriptors: AudioDeviceDescriptors--><!--Device-AudioCapturerChangeInfo-readonly deviceDescriptors: AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## muted

```TypeScript
readonly muted?: boolean
```

Whether the audio capturer is muted. **true** if muted, **false** otherwise.

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioCapturerChangeInfo-readonly muted?: boolean--><!--Device-AudioCapturerChangeInfo-readonly muted?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## streamId

```TypeScript
readonly streamId: int
```

Unique ID of an audio stream.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioCapturerChangeInfo-readonly streamId: int--><!--Device-AudioCapturerChangeInfo-readonly streamId: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

