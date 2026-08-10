# CacheStrategy

表示缓存刷新策略的枚举。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-cacheDownload-enum CacheStrategy--><!--Device-cacheDownload-enum CacheStrategy-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## FORCE

```TypeScript
FORCE = 0
```

强制更新缓存，无论缓存是否已经存在。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CacheStrategy-FORCE = 0--><!--Device-CacheStrategy-FORCE = 0-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## LAZY

```TypeScript
LAZY = 1
```

延迟更新缓存，只有当缓存不存在时才会更新。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-CacheStrategy-LAZY = 1--><!--Device-CacheStrategy-LAZY = 1-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

