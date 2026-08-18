# PlaybackPosition

Playback position definition

**Since:** 23

<!--Device-avSession-interface PlaybackPosition--><!--Device-avSession-interface PlaybackPosition-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from '@kit.AVSessionKit';
```

## elapsedTime

```TypeScript
elapsedTime: long
```

Elapsed time(position) of this media set by the app, described by milliseconds.

**Type:** long

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PlaybackPosition-elapsedTime: long--><!--Device-PlaybackPosition-elapsedTime: long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## updateTime

```TypeScript
updateTime: long
```

Record the system time when elapsedTime is set, described by milliseconds.

**Type:** long

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PlaybackPosition-updateTime: long--><!--Device-PlaybackPosition-updateTime: long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

