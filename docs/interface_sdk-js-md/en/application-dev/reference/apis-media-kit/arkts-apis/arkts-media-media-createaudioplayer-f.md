# createAudioPlayer

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## createAudioPlayer

```TypeScript
function createAudioPlayer(): AudioPlayer
```

Creates an AudioPlayer instance in synchronous mode.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** [createAVPlayer](arkts-media-media-createavplayer-f.md)(callback: AsyncCallback&lt;AVPlayer&gt;)

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioPlayer](arkts-media-media-audioplayer-i.md) |

**Examples**

```TypeScript
let audioPlayer: media.AudioPlayer = media.createAudioPlayer();
```
