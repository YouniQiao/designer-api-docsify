# RawFileDescriptor

本模块提供rawfile文件所在HAP包的文件描述符信息，包括文件描述符、rawfile文件的起始偏移和文件长度。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface RawFileDescriptor--><!--Device-unnamed-export interface RawFileDescriptor-End-->

**System capability:** SystemCapability.Global.ResourceManager

## fd

```TypeScript
fd: int
```

文件描述符。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RawFileDescriptor-fd: int--><!--Device-RawFileDescriptor-fd: int-End-->

**System capability:** SystemCapability.Global.ResourceManager

## length

```TypeScript
length: long
```

文件长度，表示rawfile文件的大小。单位为Byte。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RawFileDescriptor-length: long--><!--Device-RawFileDescriptor-length: long-End-->

**System capability:** SystemCapability.Global.ResourceManager

## offset

```TypeScript
offset: long
```

起始偏移量，表示rawfile文件在HAP包中的起始位置。单位为Byte。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RawFileDescriptor-offset: long--><!--Device-RawFileDescriptor-offset: long-End-->

**System capability:** SystemCapability.Global.ResourceManager

