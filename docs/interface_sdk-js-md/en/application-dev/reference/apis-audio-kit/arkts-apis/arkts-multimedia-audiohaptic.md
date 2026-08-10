# @ohos.multimedia.audioHaptic

音振协同


**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace audioHaptic--><!--Device-unnamed-declare namespace audioHaptic-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## Modules to Import

```TypeScript
import { audioHaptic } from 'kits/@kit.AudioKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAudioHapticManager](arkts-audio-audiohaptic-getaudiohapticmanager-f.md#getaudiohapticmanager) | 获取音振管理器。 |

### Interfaces

| Name | Description |
| --- | --- |
| [AudioHapticFileDescriptor](arkts-audio-audiohaptic-audiohapticfiledescriptor-i.md) | 描述音振文件描述符。  > **注意：** >  > 开发者需要确保fd是可用的文件描述符，且offset和length的值都是正确的。 |
| [AudioHapticManager](arkts-audio-audiohaptic-audiohapticmanager-i.md) | 管理音振协同功能。在调用AudioHapticManager的接口前，需要先通过[getAudioHapticManager](arkts-audio-audiohaptic-getaudiohapticmanager-f.md#getaudiohapticmanager)创建实例。 |
| [AudioHapticPlayer](arkts-audio-audiohaptic-audiohapticplayer-i.md) | 音振播放器，提供音振协同播放功能。在调用AudioHapticPlayer的接口前，需要先通过  [createPlayer](arkts-audio-audiohaptic-audiohapticmanager-i.md#createplayer)创建实例。 |
| [AudioHapticPlayerOptions](arkts-audio-audiohaptic-audiohapticplayeroptions-i.md) | 音振播放器选项。 |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [AudioHapticPlayer](arkts-audio-audiohaptic-audiohapticplayer-i-sys.md) | 音振播放器，提供音振协同播放功能。在调用AudioHapticPlayer的接口前，需要先通过  [createPlayer](arkts-audio-audiohaptic-audiohapticmanager-i.md#createplayer)创建实例。 |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AudioHapticType](arkts-audio-audiohaptic-audiohaptictype-e.md) | 枚举，音振类型。 |
| [AudioLatencyMode](arkts-audio-audiohaptic-audiolatencymode-e.md) | 枚举，音频时延模式。 |

