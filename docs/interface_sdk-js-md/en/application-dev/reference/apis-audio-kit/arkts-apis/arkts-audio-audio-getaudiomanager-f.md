# getAudioManager

## Modules to Import

```TypeScript
import { audio } from 'kits/@kit.AudioKit';
```

## getAudioManager

```TypeScript
function getAudioManager(): AudioManager
```

获取音频管理器。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-audio-function getAudioManager(): AudioManager--><!--Device-audio-function getAudioManager(): AudioManager-End-->

**System capability:** SystemCapability.Multimedia.Audio.Core

**Return value:**

| Type | Description |
| --- | --- |
| [AudioManager](arkts-audio-audio-audiomanager-i.md) | 音频管理器对象。 |

## Examples

```TypeScript
import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
```

