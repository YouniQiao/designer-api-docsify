# Options

Options用于指定在压缩或解压Zip文件时的选项。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-zlib-interface Options--><!--Device-zlib-interface Options-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## level

```TypeScript
level?: CompressLevel
```

压缩或解压时指定的压缩等级。

**Type:** [CompressLevel](arkts-basicservices-zlib-compresslevel-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Options-level?: CompressLevel--><!--Device-Options-level?: CompressLevel-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## memLevel

```TypeScript
memLevel?: MemLevel
```

压缩时指定的使用内存等级。

**Type:** [MemLevel](arkts-basicservices-zlib-memlevel-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Options-memLevel?: MemLevel--><!--Device-Options-memLevel?: MemLevel-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## parallel

```TypeScript
parallel?: ParallelStrategy
```

压缩策略。

**Type:** [ParallelStrategy](arkts-basicservices-zlib-parallelstrategy-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-Options-parallel?: ParallelStrategy--><!--Device-Options-parallel?: ParallelStrategy-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## pathSeparatorStrategy

```TypeScript
pathSeparatorStrategy?: PathSeparatorStrategy
```

并行策略。

**Type:** [PathSeparatorStrategy](arkts-basicservices-zlib-pathseparatorstrategy-e.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-Options-pathSeparatorStrategy?: PathSeparatorStrategy--><!--Device-Options-pathSeparatorStrategy?: PathSeparatorStrategy-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## strategy

```TypeScript
strategy?: CompressStrategy
```

压缩时指定的压缩策略。

**Type:** [CompressStrategy](arkts-basicservices-zlib-compressstrategy-e.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Options-strategy?: CompressStrategy--><!--Device-Options-strategy?: CompressStrategy-End-->

**System capability:** SystemCapability.BundleManager.Zlib

