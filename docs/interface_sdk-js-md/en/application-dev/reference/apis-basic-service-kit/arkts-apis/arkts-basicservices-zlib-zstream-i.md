# ZStream

Process all the information required for compression and decompression.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-zlib-interface ZStream--><!--Device-zlib-interface ZStream-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from '@kit.BasicServicesKit';
```

## adler

```TypeScript
adler?: long
```

Adler-32 or CRC-32 value of uncompressed data.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ZStream-adler?: long--><!--Device-ZStream-adler?: long-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## availableIn

```TypeScript
availableIn?: int
```

Number of bytes available for **nextIn**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ZStream-availableIn?: int--><!--Device-ZStream-availableIn?: int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## availableOut

```TypeScript
availableOut?: int
```

Number of remaining bytes available for **nextOut**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ZStream-availableOut?: int--><!--Device-ZStream-availableOut?: int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## dataType

```TypeScript
dataType?: int
```

Binary or text of **deflate**, or decoding state of **inflate**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ZStream-dataType?: int--><!--Device-ZStream-dataType?: int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## nextIn

```TypeScript
nextIn?: ArrayBuffer
```

Input bytes to be compressed.

**Type:** ArrayBuffer

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ZStream-nextIn?: ArrayBuffer--><!--Device-ZStream-nextIn?: ArrayBuffer-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## nextOut

```TypeScript
nextOut?: ArrayBuffer
```

Output bytes after compression.

**Type:** ArrayBuffer

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ZStream-nextOut?: ArrayBuffer--><!--Device-ZStream-nextOut?: ArrayBuffer-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## totalIn

```TypeScript
totalIn?: long
```

Total number of input bytes read so far.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ZStream-totalIn?: long--><!--Device-ZStream-totalIn?: long-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## totalOut

```TypeScript
totalOut?: long
```

Total number of output bytes.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ZStream-totalOut?: long--><!--Device-ZStream-totalOut?: long-End-->

**System capability:** SystemCapability.BundleManager.Zlib

