# AudioHapticFileDescriptor

Describes the audio-haptic file descriptor.

> **NOTE：**&gt;
> Ensure that **fd** is an available file descriptor and the values of **offset** and **length** are correct.

**Since:** 23

<!--Device-audioHaptic-interface AudioHapticFileDescriptor--><!--Device-audioHaptic-interface AudioHapticFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## Modules to Import

```TypeScript
import { audioHaptic } from '@kit.AudioKit';
```

## fd

```TypeScript
fd: int
```

File descriptor of the audio-haptic file, which is generally greater than or equal to 0.

**Type:** int

**Since:** 23

<!--Device-AudioHapticFileDescriptor-fd: int--><!--Device-AudioHapticFileDescriptor-fd: int-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## length

```TypeScript
length?: long
```

Number of bytes to read. By default, the length is the number of bytes remaining in the file from the offset position.

**Type:** long

**Since:** 23

<!--Device-AudioHapticFileDescriptor-length?: long--><!--Device-AudioHapticFileDescriptor-length?: long-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## offset

```TypeScript
offset?: long
```

Offset for reading data from the file, in bytes. By default, the offset is 0.

**Type:** long

**Since:** 23

<!--Device-AudioHapticFileDescriptor-offset?: long--><!--Device-AudioHapticFileDescriptor-offset?: long-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

