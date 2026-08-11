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

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-audioHaptic-function getAudioHapticManager(): AudioHapticManager--><!--Device-audioHaptic-function getAudioHapticManager(): AudioHapticManager-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AudioHapticManager](arkts-audio-audiohaptic-audiohapticmanager-i.md) | AudioHapticManager instance. |

## Examples

```TypeScript
let audioHapticManagerInstance: audioHaptic.AudioHapticManager = audioHaptic.getAudioHapticManager();
```

