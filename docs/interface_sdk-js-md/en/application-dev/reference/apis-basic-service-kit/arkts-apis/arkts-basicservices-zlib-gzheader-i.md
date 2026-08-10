# GzHeader

传递从zlib例程中获取的Gzip头部信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-zlib-interface GzHeader--><!--Device-zlib-interface GzHeader-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## comment

```TypeScript
comment?: ArrayBuffer
```

注释。

**Type:** ArrayBuffer

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzHeader-comment?: ArrayBuffer--><!--Device-GzHeader-comment?: ArrayBuffer-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## done

```TypeScript
done?: boolean
```

读取gzip标头后为True。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzHeader-done?: boolean--><!--Device-GzHeader-done?: boolean-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## extra

```TypeScript
extra?: ArrayBuffer
```

额外字段。

**Type:** ArrayBuffer

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzHeader-extra?: ArrayBuffer--><!--Device-GzHeader-extra?: ArrayBuffer-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## extraLen

```TypeScript
extraLen?: int
```

额外字段的长度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzHeader-extraLen?: int--><!--Device-GzHeader-extraLen?: int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## hcrc

```TypeScript
hcrc?: boolean
```

如果存在crc标头，则为True。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzHeader-hcrc?: boolean--><!--Device-GzHeader-hcrc?: boolean-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## isText

```TypeScript
isText?: boolean
```

如果压缩数据被认为是文本，则为True。

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzHeader-isText?: boolean--><!--Device-GzHeader-isText?: boolean-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## name

```TypeScript
name?: ArrayBuffer
```

文件名。

**Type:** ArrayBuffer

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzHeader-name?: ArrayBuffer--><!--Device-GzHeader-name?: ArrayBuffer-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## os

```TypeScript
os?: int
```

操作系统。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzHeader-os?: int--><!--Device-GzHeader-os?: int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## time

```TypeScript
time?: long
```

修改时间。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzHeader-time?: long--><!--Device-GzHeader-time?: long-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## xflags

```TypeScript
xflags?: int
```

额外标志。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-GzHeader-xflags?: int--><!--Device-GzHeader-xflags?: int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

