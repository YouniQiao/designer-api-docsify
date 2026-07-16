# Options

Defines options used to compress or decompress a ZIP file.

**Since:** 7

<!--Device-zlib-interface Options--><!--Device-zlib-interface Options-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from '@kit.BasicServicesKit';
```

## keepTopLevelFolder

```TypeScript
keepTopLevelFolder?: boolean
```

Indicates whether to keep the top-level source folder in the compressed file.The default value is false.

**Type:** boolean

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Options-keepTopLevelFolder?: boolean--><!--Device-Options-keepTopLevelFolder?: boolean-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## level

```TypeScript
level?: CompressLevel
```

Compression level specified for compression or decompression.

**Type:** CompressLevel

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Options-level?: CompressLevel--><!--Device-Options-level?: CompressLevel-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## memLevel

```TypeScript
memLevel?: MemLevel
```

Memory level specified for compression.

**Type:** MemLevel

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Options-memLevel?: MemLevel--><!--Device-Options-memLevel?: MemLevel-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## parallel

```TypeScript
parallel?: ParallelStrategy
```

Serial or parallel strategy specified for compression or decompression.

**Type:** ParallelStrategy

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Options-parallel?: ParallelStrategy--><!--Device-Options-parallel?: ParallelStrategy-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## pathSeparatorStrategy

```TypeScript
pathSeparatorStrategy?: PathSeparatorStrategy
```

Separator strategy for the file path in the compressed package specified for decompression.

**Type:** PathSeparatorStrategy

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Options-pathSeparatorStrategy?: PathSeparatorStrategy--><!--Device-Options-pathSeparatorStrategy?: PathSeparatorStrategy-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## strategy

```TypeScript
strategy?: CompressStrategy
```

Compression strategy specified for compression.

**Type:** CompressStrategy

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Options-strategy?: CompressStrategy--><!--Device-Options-strategy?: CompressStrategy-End-->

**System capability:** SystemCapability.BundleManager.Zlib

