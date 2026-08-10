# CompressFlushMode

压缩刷新模式。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-zlib-export enum CompressFlushMode--><!--Device-zlib-export enum CompressFlushMode-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## NO_FLUSH

```TypeScript
NO_FLUSH = 0
```

默认值，表示正常操作。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompressFlushMode-NO_FLUSH = 0--><!--Device-CompressFlushMode-NO_FLUSH = 0-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## PARTIAL_FLUSH

```TypeScript
PARTIAL_FLUSH = 1
```

在流中生成部分刷新点。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompressFlushMode-PARTIAL_FLUSH = 1--><!--Device-CompressFlushMode-PARTIAL_FLUSH = 1-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## SYNC_FLUSH

```TypeScript
SYNC_FLUSH = 2
```

在保持压缩流状态的同时强制输出所有压缩数据。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompressFlushMode-SYNC_FLUSH = 2--><!--Device-CompressFlushMode-SYNC_FLUSH = 2-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## FULL_FLUSH

```TypeScript
FULL_FLUSH = 3
```

重置压缩状态。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompressFlushMode-FULL_FLUSH = 3--><!--Device-CompressFlushMode-FULL_FLUSH = 3-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## FINISH

```TypeScript
FINISH = 4
```

压缩或解压缩过程结束。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompressFlushMode-FINISH = 4--><!--Device-CompressFlushMode-FINISH = 4-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## BLOCK

```TypeScript
BLOCK = 5
```

允许更精确的控制。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompressFlushMode-BLOCK = 5--><!--Device-CompressFlushMode-BLOCK = 5-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## TREES

```TypeScript
TREES = 6
```

实施过程中有特殊目的。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-CompressFlushMode-TREES = 6--><!--Device-CompressFlushMode-TREES = 6-End-->

**System capability:** SystemCapability.BundleManager.Zlib

