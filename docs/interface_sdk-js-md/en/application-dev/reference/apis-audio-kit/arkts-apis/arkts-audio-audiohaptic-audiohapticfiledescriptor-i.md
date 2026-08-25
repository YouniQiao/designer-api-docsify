# AudioHapticFileDescriptor

Describes the audio-haptic file descriptor.

> **NOTE：**&gt;
> Ensure that **fd** is an available file descriptor and the values of **offset** and **length** are correct.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

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

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## length

```TypeScript
length?: long
```

Number of bytes to read. By default, the length is the number of bytes remaining in the file from the offset position.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## offset

```TypeScript
offset?: long
```

Offset for reading data from the file, in bytes. By default, the offset is 0.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core
