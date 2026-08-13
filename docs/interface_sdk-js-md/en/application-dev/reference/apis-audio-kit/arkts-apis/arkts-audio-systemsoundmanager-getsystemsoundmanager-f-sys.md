# getSystemSoundManager (System API)

## Modules to Import

```TypeScript
import { systemSoundManager } from '@kit.AudioKit';
```

## getSystemSoundManager

```TypeScript
function getSystemSoundManager(): SystemSoundManager
```

Gets system sound manager for all type sound.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-systemSoundManager-function getSystemSoundManager(): SystemSoundManager--><!--Device-systemSoundManager-function getSystemSoundManager(): SystemSoundManager-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| [SystemSoundManager](arkts-audio-systemsoundmanager-systemsoundmanager-i-sys.md) | SystemSoundManager instance. |

## Examples

```TypeScript
let systemSoundManagerInstance: systemSoundManager.SystemSoundManager = systemSoundManager.getSystemSoundManager();
```

