# getSystemSoundManager

## Modules to Import

```TypeScript
import { systemSoundManager } from '@kit.AudioKit';
```

## getSystemSoundManager

```TypeScript
function getSystemSoundManager(): SystemSoundManager
```

Gets system sound manager for all type sound.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-systemSoundManager-function getSystemSoundManager(): SystemSoundManager--><!--Device-systemSoundManager-function getSystemSoundManager(): SystemSoundManager-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| Type | Description |
| --- | --- |
| [SystemSoundManager](arkts-audio-systemsoundmanager-systemsoundmanager-i.md) | SystemSoundManager instance. |

## Examples

```TypeScript
let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
```

