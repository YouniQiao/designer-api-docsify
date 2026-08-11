# AudioHapticFileDescriptor

Describes the audio-haptic file descriptor.

> **NOTE：**
> 
> Ensure that **fd** is an available file descriptor and the values of **offset** and **length** are correct.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-audioHaptic-interface AudioHapticFileDescriptor--><!--Device-audioHaptic-interface AudioHapticFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## Modules to Import

```TypeScript
import { audioHaptic } from 'kits/@kit.AudioKit';
```

## fd

```TypeScript
fd: int
```

File descriptor of the audio-haptic file, which is generally greater than or equal to 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticFileDescriptor-fd: int--><!--Device-AudioHapticFileDescriptor-fd: int-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## length

```TypeScript
length?: long
```

Number of bytes to read. By default, the length is the number of bytes remaining in the file from the offset position.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticFileDescriptor-length?: long--><!--Device-AudioHapticFileDescriptor-length?: long-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## offset

```TypeScript
offset?: long
```

Offset for reading data from the file, in bytes. By default, the offset is 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticFileDescriptor-offset?: long--><!--Device-AudioHapticFileDescriptor-offset?: long-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

