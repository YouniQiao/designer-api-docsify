# GzHeader

Gzip header information passed to and from zlib routines.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-zlib-interface GzHeader--><!--Device-zlib-interface GzHeader-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from '@kit.BasicServicesKit';
```

## comment

```TypeScript
comment?: ArrayBuffer
```

Comment.

**Type:** ArrayBuffer

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GzHeader-comment?: ArrayBuffer--><!--Device-GzHeader-comment?: ArrayBuffer-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## done

```TypeScript
done?: boolean
```

Returns **True** after reading the gzip file header.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GzHeader-done?: boolean--><!--Device-GzHeader-done?: boolean-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## extra

```TypeScript
extra?: ArrayBuffer
```

Extra field.

**Type:** ArrayBuffer

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GzHeader-extra?: ArrayBuffer--><!--Device-GzHeader-extra?: ArrayBuffer-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## extraLen

```TypeScript
extraLen?: int
```

Length of the extra field.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GzHeader-extraLen?: int--><!--Device-GzHeader-extraLen?: int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## hcrc

```TypeScript
hcrc?: boolean
```

Returns **True** if the **crc** header exists.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GzHeader-hcrc?: boolean--><!--Device-GzHeader-hcrc?: boolean-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## isText

```TypeScript
isText?: boolean
```

Returns **True** if the compressed data is considered text.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GzHeader-isText?: boolean--><!--Device-GzHeader-isText?: boolean-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## name

```TypeScript
name?: ArrayBuffer
```

File name.

**Type:** ArrayBuffer

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GzHeader-name?: ArrayBuffer--><!--Device-GzHeader-name?: ArrayBuffer-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## os

```TypeScript
os?: int
```

Operating system.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GzHeader-os?: int--><!--Device-GzHeader-os?: int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## time

```TypeScript
time?: long
```

Modification time.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GzHeader-time?: long--><!--Device-GzHeader-time?: long-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## xflags

```TypeScript
xflags?: int
```

Extra flag.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-GzHeader-xflags?: int--><!--Device-GzHeader-xflags?: int-End-->

**System capability:** SystemCapability.BundleManager.Zlib

