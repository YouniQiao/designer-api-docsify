# getSystemSoundManager

## Modules to Import

```TypeScript
import { systemSoundManager } from 'kits/@kit.AudioKit';
```

## getSystemSoundManager

```TypeScript
function getSystemSoundManager(): SystemSoundManager
```

Gets system sound manager for all type sound.

**Since:** 10

<!--Device-systemSoundManager-function getSystemSoundManager(): SystemSoundManager--><!--Device-systemSoundManager-function getSystemSoundManager(): SystemSoundManager-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SystemSoundManager](arkts-audio-systemsoundmanager-systemsoundmanager-i.md) |

## Examples

```TypeScript
let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
```
