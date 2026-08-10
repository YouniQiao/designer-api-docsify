# createAudioRecorder

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createAudioRecorder

```TypeScript
function createAudioRecorder(): AudioRecorder
```

创建音频录制的实例来控制音频的录制。一台设备只允许创建一个录制实例。

> **说明：**
> > 从API version 6开始支持，从API version 9开始废弃，建议使用
> [createAVRecorder](arkts-media-media-createavrecorder-f.md#createavrecorder)替代。

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [media.createAVRecorder](arkts-media-media-createavrecorder-f.md#createavrecorder)(callback:

<!--Device-media-function createAudioRecorder(): AudioRecorder--><!--Device-media-function createAudioRecorder(): AudioRecorder-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Return value:**

| Type | Description |
| --- | --- |
| [AudioRecorder](arkts-media-multimedia-media-audiorecorder-i.md) | 返回AudioRecorder类实例，失败时返回null。可用于录制音频媒体。 |

## Examples

```TypeScript
let audioRecorder: media.AudioRecorder = media.createAudioRecorder();
```

