# AudioTimestampInfo

Describes the information about the audio stream timestamp and the current data frame position.

**Since:** 23

<!--Device-audio-interface AudioTimestampInfo--><!--Device-audio-interface AudioTimestampInfo-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## Modules to Import

```TypeScript
import { audio } from '@kit.AudioKit';
import { audioHaptic } from '@kit.AudioKit';
```

## framePos

```TypeScript
readonly framePos: long
```

Position of the current data frame for playback or recording.

**Type:** long

**Since:** 23

<!--Device-AudioTimestampInfo-readonly framePos: long--><!--Device-AudioTimestampInfo-readonly framePos: long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

## timestamp

```TypeScript
readonly timestamp: long
```

Timestamp corresponding to the current data frame position during playback or recording, in nanoseconds.

**Type:** long

**Since:** 23

<!--Device-AudioTimestampInfo-readonly timestamp: long--><!--Device-AudioTimestampInfo-readonly timestamp: long-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

