# CacheMode

Enum type supplied to {@link cacheMode} for setting the Web cache mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum CacheMode--><!--Device-unnamed-export declare enum CacheMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## DEFAULT

```TypeScript
DEFAULT = 0
```

load cache when they are available and not expired, otherwise load online.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CacheMode-DEFAULT = 0--><!--Device-CacheMode-DEFAULT = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## NONE

```TypeScript
NONE = 1
```

load cache when they are available, otherwise load online.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CacheMode-NONE = 1--><!--Device-CacheMode-NONE = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ONLINE

```TypeScript
ONLINE = 2
```

Load online and not cache.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CacheMode-ONLINE = 2--><!--Device-CacheMode-ONLINE = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ONLY

```TypeScript
ONLY = 3
```

load cache and not online.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-CacheMode-ONLY = 3--><!--Device-CacheMode-ONLY = 3-End-->

**System capability:** SystemCapability.Web.Webview.Core

