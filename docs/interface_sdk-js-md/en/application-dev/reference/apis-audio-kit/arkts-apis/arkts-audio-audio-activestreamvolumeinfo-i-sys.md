# ActiveStreamVolumeInfo (System API)

用于激活音频流的音量信息。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-audio-interface ActiveStreamVolumeInfo--><!--Device-audio-interface ActiveStreamVolumeInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## appVolume

```TypeScript
appVolume: int
```

应用的音量。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActiveStreamVolumeInfo-appVolume: int--><!--Device-ActiveStreamVolumeInfo-appVolume: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

## clientUid

```TypeScript
clientUid: int
```

音频应用的Uid。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActiveStreamVolumeInfo-clientUid: int--><!--Device-ActiveStreamVolumeInfo-clientUid: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

## volumeType

```TypeScript
volumeType: AudioVolumeType
```

当前音频流的音量类型。

**Type:** [AudioVolumeType](arkts-audio-audio-audiovolumetype-e-sys.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ActiveStreamVolumeInfo-volumeType: AudioVolumeType--><!--Device-ActiveStreamVolumeInfo-volumeType: AudioVolumeType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

**System API:** This is a system API.

