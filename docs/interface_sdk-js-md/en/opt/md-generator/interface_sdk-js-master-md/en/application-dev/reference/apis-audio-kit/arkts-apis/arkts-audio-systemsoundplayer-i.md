# SystemSoundPlayer

Implements a system sound player that provides functions for loading, unloading, playing system sounds. Before using these functions, application must call [createSystemSoundPlayer](arkts-audio-systemsoundmanager-createsystemsoundplayer-f.md#createSystemSoundPlayer) to create a SystemSoundPlayer instance first.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-export interface SystemSoundPlayer--><!--Device-unnamed-export interface SystemSoundPlayer-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

## load

```TypeScript
load(soundType: systemSoundManager.SystemSoundType): Promise<void>
```

Loads a system sound.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemSoundPlayer-load(soundType: systemSoundManager.SystemSoundType): Promise<void>--><!--Device-SystemSoundPlayer-load(soundType: systemSoundManager.SystemSoundType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| soundType | systemSoundManager.SystemSoundType | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |
| [5400108](../../apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

systemSoundPlayer?.load(systemSoundManager.SystemSoundType.PHOTO_SHUTTER).then(() => {
  console.info('Succeeded in calling the load method.');
}).catch((err: BusinessError) => {
  console.error(`Failed to call the load method. Code: ${err.code}, message: ${err.message}`);
});
```

## play

```TypeScript
play(soundType: systemSoundManager.SystemSoundType): Promise<void>
```

Plays a system sound.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemSoundPlayer-play(soundType: systemSoundManager.SystemSoundType): Promise<void>--><!--Device-SystemSoundPlayer-play(soundType: systemSoundManager.SystemSoundType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| soundType | systemSoundManager.SystemSoundType | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |
| [5400108](../../apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

systemSoundPlayer?.play(systemSoundManager.SystemSoundType.PHOTO_SHUTTER).then(() => {
  console.info('Succeeded in calling the play method.');
}).catch((err: BusinessError) => {
  console.error(`Failed to call the play method. Code: ${err.code}, message: ${err.message}`);
});
```

## release

```TypeScript
release(): Promise<void>
```

Releases this system sound player instance.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemSoundPlayer-release(): Promise<void>--><!--Device-SystemSoundPlayer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

systemSoundPlayer?.release().then(() => {
  console.info('Succeeded in calling the release method.');
}).catch((err: BusinessError) => {
  console.error(`Failed to call the release method. Code: ${err.code}, message: ${err.message}`);
});
```

## unload

```TypeScript
unload(soundType: systemSoundManager.SystemSoundType): Promise<void>
```

Unloads a system sound that has been loaded before.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemSoundPlayer-unload(soundType: systemSoundManager.SystemSoundType): Promise<void>--><!--Device-SystemSoundPlayer-unload(soundType: systemSoundManager.SystemSoundType): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| soundType | systemSoundManager.SystemSoundType | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |
| [5400108](../../apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

systemSoundPlayer?.unload(systemSoundManager.SystemSoundType.PHOTO_SHUTTER).then(() => {
  console.info('Succeeded in calling the unload method.');
}).catch((err: BusinessError) => {
  console.error(`Failed to call the unload method. Code: ${err.code}, message: ${err.message}`);
});
```
