# getAudioManager

## getAudioManager

```TypeScript
function getAudioManager(): AudioManager
```

Obtains an AudioManager instance.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-audio-function getAudioManager(): AudioManager--><!--Device-audio-function getAudioManager(): AudioManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | AudioManager instance. |

**Example**

```TypeScript
import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
```

