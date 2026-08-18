# getAudioHapticManager

## Modules to Import

```TypeScript
```

## getAudioHapticManager

```TypeScript
function getAudioHapticManager(): AudioHapticManager
```

Obtains an [AudioHapticManager](arkts-audio-audiohaptic-audiohapticmanager-i.md#audiohapticmanager) instance. This object is singleton in one process.

**Since:** 23

<!--Device-audioHaptic-function getAudioHapticManager(): AudioHapticManager--><!--Device-audioHaptic-function getAudioHapticManager(): AudioHapticManager-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioHapticManager](arkts-audio-audiohaptic-audiohapticmanager-i.md) |

**Examples**

```TypeScript
let audioHapticManagerInstance: audioHaptic.AudioHapticManager = audioHaptic.getAudioHapticManager();
```
