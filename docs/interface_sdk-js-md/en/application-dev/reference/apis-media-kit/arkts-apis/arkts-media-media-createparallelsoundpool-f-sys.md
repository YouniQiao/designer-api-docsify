# createParallelSoundPool (System API)

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## createParallelSoundPool

```TypeScript
function createParallelSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>
```

Creates a **SoundPool** instance. This API uses a promise to return the result.If a **SoundPool** instance created using [createSoundPool](arkts-media-media-createsoundpool-f.md) is used to play the same sound again, it stops the current audio and restarts the audio. However, if the instance is created using **createParallelSoundPool**, it keeps playing the first audio and starts the new one alongside it.

**Since:** 20

**System capability:** SystemCapability.Multimedia.Media.SoundPool

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| maxStreams | number | Yes |
| audioRenderInfo | audio.AudioRendererInfo | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;SoundPool & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [5400101](../errorcode-media.md#5400101-memory-allocation-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
