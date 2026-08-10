# ZStream

处理所有用于压缩和解压缩所需的信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-zlib-interface ZStream--><!--Device-zlib-interface ZStream-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## adler

```TypeScript
adler?: long
```

未压缩数据的Adler-32或CRC-32值。

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

nextIn可用的字节数。

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

nextOut的剩余可用字节数。

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

关于数据类型的最佳猜测：deflate的二进制或文本，或inflate的解码状态。

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

需要压缩的输入字节。

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

压缩后的输出字节。

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

到目前为止读取的输入字节总数。

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

到目前为止输出字节总数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ZStream-totalOut?: long--><!--Device-ZStream-totalOut?: long-End-->

**System capability:** SystemCapability.BundleManager.Zlib

