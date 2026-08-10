# VolumeEvent

音量改变时，应用接收到的事件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-audio-interface VolumeEvent--><!--Device-audio-interface VolumeEvent-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## updateUi

```TypeScript
updateUi: boolean
```

是否在UI中显示音量变化。true表示显示，false表示不显示。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VolumeEvent-updateUi: boolean--><!--Device-VolumeEvent-updateUi: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volume

```TypeScript
volume: int
```

音量等级，可设置范围通过调用getMinVolume和getMaxVolume方法获取。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VolumeEvent-volume: int--><!--Device-VolumeEvent-volume: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeMode

```TypeScript
volumeMode?: AudioVolumeMode
```

音频的音量模式。默认值为SYSTEM_GLOBAL。

**Type:** [AudioVolumeMode](arkts-audio-audio-audiovolumemode-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-VolumeEvent-volumeMode?: AudioVolumeMode--><!--Device-VolumeEvent-volumeMode?: AudioVolumeMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeType

```TypeScript
volumeType: AudioVolumeType
```

音频音量类型。

**Type:** [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VolumeEvent-volumeType: AudioVolumeType--><!--Device-VolumeEvent-volumeType: AudioVolumeType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

