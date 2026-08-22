# AudioCapturerFilter (System API)

Describe audio capturer filter.

**Since:** 23

<!--Device-audio-interface AudioCapturerFilter--><!--Device-audio-interface AudioCapturerFilter-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
import { audioHaptic } from '@kit.AudioKit';
```

## capturerInfo

```TypeScript
capturerInfo?: AudioCapturerInfo
```

Capturer information.

**Type:** [AudioCapturerInfo](arkts-audio-audio-audiocapturerinfo-i.md)

**Since:** 23

<!--Device-AudioCapturerFilter-capturerInfo?: AudioCapturerInfo--><!--Device-AudioCapturerFilter-capturerInfo?: AudioCapturerInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Capturer

**System API:** This is a system API.

## uid

```TypeScript
uid?: int
```

Application uid.

**Type:** int

**Since:** 23

<!--Device-AudioCapturerFilter-uid?: int--><!--Device-AudioCapturerFilter-uid?: int-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**System API:** This is a system API.

**Examples**

```TypeScript
import { audio } from '@kit.AudioKit';

let inputAudioCapturerFilter: audio.AudioCapturerFilter = {
    uid : 20010041,
    capturerInfo : {
        source: audio.SourceType.SOURCE_TYPE_MIC,
        capturerFlags: 0
    }
};
```

