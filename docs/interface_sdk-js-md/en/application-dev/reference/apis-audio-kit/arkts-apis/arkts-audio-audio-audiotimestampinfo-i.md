# AudioTimestampInfo

音频流时间戳和当前数据帧位置信息。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-audio-interface AudioTimestampInfo--><!--Device-audio-interface AudioTimestampInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## framePos

```TypeScript
readonly framePos: long
```

当前播放或者录制的数据帧位置。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-AudioTimestampInfo-readonly framePos: long--><!--Device-AudioTimestampInfo-readonly framePos: long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## timestamp

```TypeScript
readonly timestamp: long
```

播放或者录制到当前数据帧位置时对应的时间戳，单位为纳秒。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 19

**ArkTS mode:** ArkTS-Dyn since version 19; ArkTS-Sta since version 23.

<!--Device-AudioTimestampInfo-readonly timestamp: long--><!--Device-AudioTimestampInfo-readonly timestamp: long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

