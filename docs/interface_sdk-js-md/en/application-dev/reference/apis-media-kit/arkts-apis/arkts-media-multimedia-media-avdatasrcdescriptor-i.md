# AVDataSrcDescriptor

Defines the descriptor of an audio and video file, which is used in DataSource playback mode.Use scenario: An application can create a playback instance and start playback before it finishes downloading the audio and video resources.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-interface AVDataSrcDescriptor--><!--Device-unnamed-interface AVDataSrcDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

## Modules to Import

```TypeScript
import { media } from 'kits/@kit.MediaKit';
```

## callback

ArkTS-Dyn:
```TypeScript
callback: (buffer: ArrayBuffer, length: number, pos?: number) => number
```

ArkTS-Sta:
```TypeScript
callback: (buffer: ArrayBuffer, length: long, pos?: long) => int
```

Callback function implemented by users, which is used to fill data.buffer - The buffer need to fill.length - The stream length player want to get.pos - The stream position player want get start, and is an optional parameter.When fileSize set to -1, this parameter is not used.Returns length of the data to be filled, Return -1 to indicate that the end of the stream is reached,Return -2 to indicate that an unrecoverable error has been encountered.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVDataSrcDescriptor-callback: (buffer: ArrayBuffer, length: long, pos?: long) => int--><!--Device-AVDataSrcDescriptor-callback: (buffer: ArrayBuffer, length: long, pos?: long) => int-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| buffer | ArrayBuffer | Yes |  |
| length | ArkTS-Dyn: number  <br>ArkTS-Sta：long | Yes |  |
| pos | ArkTS-Dyn: number  <br>ArkTS-Sta：long | No |  |

## fileSize

```TypeScript
fileSize: long
```

Size of the file, -1 means the file size is unknown, in this case,seek and setSpeed can't be executed, loop can't be set, and can't replay.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVDataSrcDescriptor-fileSize: long--><!--Device-AVDataSrcDescriptor-fileSize: long-End-->

**System capability:** SystemCapability.Multimedia.Media.AVPlayer

