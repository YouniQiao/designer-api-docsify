# createAudioPlayer

## createAudioPlayer

```TypeScript
function createAudioPlayer(): AudioPlayer
```

Creates an AudioPlayer instance in synchronous mode.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [media.createAVPlayer](arkts-media-media-createavplayer-f.md#createavplayer)(callback:

<!--Device-media-function createAudioPlayer(): AudioPlayer--><!--Device-media-function createAudioPlayer(): AudioPlayer-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioPlayer

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | If the operation is successful, an AudioPlayer instance is returned; otherwise, **null** |

**Example**

```TypeScript
let audioPlayer: media.AudioPlayer = media.createAudioPlayer();
```

