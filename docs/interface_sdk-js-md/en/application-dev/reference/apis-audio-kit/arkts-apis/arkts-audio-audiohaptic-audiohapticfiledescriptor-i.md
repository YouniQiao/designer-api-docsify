# AudioHapticFileDescriptor

描述音振文件描述符。

> **注意：**
> 
> 开发者需要确保fd是可用的文件描述符，且offset和length的值都是正确的。

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

音振资源文件的文件描述符，通常大于等于0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticFileDescriptor-fd: int--><!--Device-AudioHapticFileDescriptor-fd: int-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## length

```TypeScript
length?: long
```

读取数据的字节长度。默认情况下，长度为文件中从偏移量位置开始的剩余字节数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticFileDescriptor-length?: long--><!--Device-AudioHapticFileDescriptor-length?: long-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

## offset

```TypeScript
offset?: long
```

文件中数据读取的偏移量，单位为字节。默认情况下，偏移量为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-AudioHapticFileDescriptor-offset?: long--><!--Device-AudioHapticFileDescriptor-offset?: long-End-->

**System capability:** SystemCapability.Multimedia.AudioHaptic.Core

