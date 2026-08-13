# createAudioRecorder

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## createAudioRecorder

```TypeScript
function createAudioRecorder(): AudioRecorder
```

Creates an AudioRecorder instance to control audio recording. Only one AudioRecorder instance can be created per device.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [createAVRecorder](arkts-media-media-createavrecorder-f.md#createAVRecorder)(callback: AsyncCallback&lt;AVRecorder&gt;)

<!--Device-media-function createAudioRecorder(): AudioRecorder--><!--Device-media-function createAudioRecorder(): AudioRecorder-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AudioRecorder](arkts-media-media-audiorecorder-i.md) |

## Examples

```TypeScript
let audioRecorder: media.AudioRecorder = media.createAudioRecorder();
```
