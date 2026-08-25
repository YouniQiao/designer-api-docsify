# createSystemSoundPlayer

## Modules to Import

```TypeScript
import { systemSoundManager } from 'kits/@kit.AudioKit';
```

## createSystemSoundPlayer

```TypeScript
function createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>
```

Creates a SystemSoundPlayer instance. This function uses a promise to return the result. This player can be used to play some system sounds for media or camera actions.

**Since:** 23

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;SystemSoundPlayer \ | null & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../../apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |
