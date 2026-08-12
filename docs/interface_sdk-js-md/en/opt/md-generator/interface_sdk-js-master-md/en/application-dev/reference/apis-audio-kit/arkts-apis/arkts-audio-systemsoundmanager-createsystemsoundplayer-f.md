# createSystemSoundPlayer

## Modules to Import

```TypeScript
import { systemSoundManager } from '@kit.AudioKit';
```

## createSystemSoundPlayer

```TypeScript
function createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>
```

Creates a SystemSoundPlayer instance. This function uses a promise to return the result.This player can be used to play some system sounds for media or camera actions.

**Since:** 23

<!--Device-systemSoundManager-function createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>--><!--Device-systemSoundManager-function createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;SystemSoundPlayer \ | null & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-media-kit/errorcode-media.md#5400101-memory-allocation-failed) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let systemSoundPlayer: systemSoundManager.SystemSoundPlayer | null = null;

systemSoundManager.createSystemSoundPlayer().then((systemSoundPlayerInstance) => {
  console.info('Succeeded in creating the system sound player.');
  systemSoundPlayer = systemSoundPlayerInstance;
}).catch((err: BusinessError) => {
  console.error(`Failed to create the system sound player. Code: ${err.code}, message: ${err.message}`);
});
```
