# getAudioHapticManager

## Modules to Import

```TypeScript
import { audioHaptic } from 'kits/@kit.AudioKit';
```

## getAudioHapticManager

```TypeScript
function getAudioHapticManager(): AudioHapticManager
```

Obtains an {@link AudioHapticManager} instance. This object is singleton in one process.

**Since:** 11

<!--Device-audioHaptic-function getAudioHapticManager(): AudioHapticManager--><!--Device-audioHaptic-function getAudioHapticManager(): AudioHapticManager-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioHapticManager](arkts-audio-audiohaptic-audiohapticmanager-i.md) |

## Examples

```TypeScript
let audioHapticManagerInstance: audioHaptic.AudioHapticManager = audioHaptic.getAudioHapticManager();
```
