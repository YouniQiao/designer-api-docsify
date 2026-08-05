# createAudioRecorder

## createAudioRecorder

```TypeScript
function createAudioRecorder(): AudioRecorder
```

Creates an AudioRecorder instance to control audio recording. Only one AudioRecorder instance can be created per device.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [media.createAVRecorder](arkts-media-media-createavrecorder-f.md#createavrecorder)(callback:

<!--Device-media-function createAudioRecorder(): AudioRecorder--><!--Device-media-function createAudioRecorder(): AudioRecorder-End-->

**System capability:** SystemCapability.Multimedia.Media.AudioRecorder

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | If the operation is successful, an AudioRecorder instance is returned; otherwise, |

**Example**

```TypeScript
let audioRecorder: media.AudioRecorder = media.createAudioRecorder();
```

