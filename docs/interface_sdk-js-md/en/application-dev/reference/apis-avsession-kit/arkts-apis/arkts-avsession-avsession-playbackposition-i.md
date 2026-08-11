# PlaybackPosition

Playback position definition

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-avSession-interface PlaybackPosition--><!--Device-avSession-interface PlaybackPosition-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## elapsedTime

```TypeScript
elapsedTime: long
```

Elapsed time(position) of this media set by the app, described by milliseconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PlaybackPosition-elapsedTime: long--><!--Device-PlaybackPosition-elapsedTime: long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## updateTime

```TypeScript
updateTime: long
```

Record the system time when elapsedTime is set, described by milliseconds.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PlaybackPosition-updateTime: long--><!--Device-PlaybackPosition-updateTime: long-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

