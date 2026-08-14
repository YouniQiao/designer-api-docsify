# VolumeEvent

Describes the event received by the application when the volume is changed.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-audio-interface VolumeEvent--><!--Device-audio-interface VolumeEvent-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## Modules to Import

```TypeScript
import { audio } from 'audio';
```

## updateUi

```TypeScript
updateUi: boolean
```

Whether to show the volume change in UI. **true** to show, **false** otherwise.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-VolumeEvent-updateUi: boolean--><!--Device-VolumeEvent-updateUi: boolean-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volume

```TypeScript
volume: int
```

Volume to set. The value range can be obtained by calling **getMinVolume** and **getMaxVolume**.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-VolumeEvent-volume: int--><!--Device-VolumeEvent-volume: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeMode

```TypeScript
volumeMode?: AudioVolumeMode
```

Audio volume mode. The default value is **SYSTEM_GLOBAL**.

**Type:** [AudioVolumeMode](arkts-audio-audio-audiovolumemode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-VolumeEvent-volumeMode?: AudioVolumeMode--><!--Device-VolumeEvent-volumeMode?: AudioVolumeMode-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

## volumeType

```TypeScript
volumeType: AudioVolumeType
```

Audio volume type.

**Type:** [AudioVolumeType](arkts-audio-audio-audiovolumetype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-VolumeEvent-volumeType: AudioVolumeType--><!--Device-VolumeEvent-volumeType: AudioVolumeType-End-->

**System capability:** SystemCapability.Multimedia.Audio.Volume

