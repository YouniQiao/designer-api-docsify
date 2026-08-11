# SystemSoundPlayer

Implements a system sound player that provides functions for loading, unloading, playing system sounds.Before using these functions, application must call  
[createSystemSoundPlayer](#systemSoundManager.createSystemSoundPlayer) to create a SystemSoundPlayer instance first.

**Since:** 23

<!--Device-unnamed-export interface SystemSoundPlayer--><!--Device-unnamed-export interface SystemSoundPlayer-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

## load

```TypeScript
load(soundType: systemSoundManager.SystemSoundType): Promise<void>
```

Loads a system sound.

**Since:** 23

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
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |
| [5400108](../../apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## play

```TypeScript
play(soundType: systemSoundManager.SystemSoundType): Promise<void>
```

Plays a system sound.

**Since:** 23

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
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400103](../../apis-media-kit/errorcode-media.md#5400103-io-error) |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |
| [5400108](../../apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |

## release

```TypeScript
release(): Promise<void>
```

Releases this system sound player instance.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-SystemSoundPlayer-release(): Promise<void>--><!--Device-SystemSoundPlayer-release(): Promise<void>-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |

## unload

```TypeScript
unload(soundType: systemSoundManager.SystemSoundType): Promise<void>
```

Unloads a system sound that has been loaded before.

**Since:** 23

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
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400105](../../apis-media-kit/errorcode-media.md#5400105-play-service-dead) |
| [5400108](../../apis-media-kit/errorcode-media.md#5400108-parameter-value-out-of-range) |
