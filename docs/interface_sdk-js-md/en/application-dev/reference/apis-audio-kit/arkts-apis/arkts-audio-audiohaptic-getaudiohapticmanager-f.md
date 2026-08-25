# getAudioHapticManager

## Modules to Import

```TypeScript
import { audioHaptic } from '@kit.AudioKit';
```

## getAudioHapticManager

```TypeScript
function getAudioHapticManager(): AudioHapticManager
```

Obtains an [AudioHapticManager](arkts-audio-audiohaptic-audiohapticmanager-i.md) instance. This object is singleton in one process.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioHapticManager](arkts-audio-audiohaptic-audiohapticmanager-i.md) |

**Examples**

```TypeScript
let audioHapticManagerInstance: audioHaptic.AudioHapticManager = audioHaptic.getAudioHapticManager();
```
