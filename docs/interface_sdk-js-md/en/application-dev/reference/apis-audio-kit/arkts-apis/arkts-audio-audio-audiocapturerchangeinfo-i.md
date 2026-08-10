# AudioCapturerChangeInfo

描述音频采集器更改信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioCapturerChangeInfo--><!--Device-audio-interface AudioCapturerChangeInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## capturerInfo

```TypeScript
readonly capturerInfo: AudioCapturerInfo
```

音频采集器信息。

**Type:** [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioCapturerChangeInfo-readonly capturerInfo: AudioCapturerInfo--><!--Device-AudioCapturerChangeInfo-readonly capturerInfo: AudioCapturerInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## deviceDescriptors

```TypeScript
readonly deviceDescriptors: AudioDeviceDescriptors
```

音频设备信息。

**Type:** [AudioDeviceDescriptors](arkts-audio-audio-audiodevicedescriptors-t.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioCapturerChangeInfo-readonly deviceDescriptors: AudioDeviceDescriptors--><!--Device-AudioCapturerChangeInfo-readonly deviceDescriptors: AudioDeviceDescriptors-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## muted

```TypeScript
readonly muted?: boolean
```

音频采集器是否处于静音状态。true表示静音，false表示非静音。

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-AudioCapturerChangeInfo-readonly muted?: boolean--><!--Device-AudioCapturerChangeInfo-readonly muted?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

## streamId

```TypeScript
readonly streamId: int
```

音频流唯一id。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AudioCapturerChangeInfo-readonly streamId: int--><!--Device-AudioCapturerChangeInfo-readonly streamId: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

