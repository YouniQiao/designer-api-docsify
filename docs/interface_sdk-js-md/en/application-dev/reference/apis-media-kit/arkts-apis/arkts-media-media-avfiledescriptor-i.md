# AVFileDescriptor

Media file descriptor. The caller needs to ensure that the fd is valid and the offset and length are correct.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-media-interface AVFileDescriptor--><!--Device-media-interface AVFileDescriptor-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## Modules to Import

```TypeScript
import { media } from '@kit.MediaKit';
```

## fd

```TypeScript
fd: int
```

The file descriptor of audio or video source from file system. The caller is responsible to close the file descriptor.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVFileDescriptor-fd: int--><!--Device-AVFileDescriptor-fd: int-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## length

```TypeScript
length?: long
```

The length in bytes of the data to be read. By default, the length is the rest of bytes in the file from the offset.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVFileDescriptor-length?: long--><!--Device-AVFileDescriptor-length?: long-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

## offset

```TypeScript
offset?: long
```

The offset into the file where the data to be read, in bytes. By default,the offset is zero.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-AVFileDescriptor-offset?: long--><!--Device-AVFileDescriptor-offset?: long-End-->

**System capability:** SystemCapability.Multimedia.Media.Core

