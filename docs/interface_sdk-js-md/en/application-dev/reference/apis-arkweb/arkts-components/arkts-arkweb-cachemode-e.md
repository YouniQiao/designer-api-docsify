# CacheMode

Enum type supplied to {@link cacheMode} for setting the Web cache mode.

**Since:** 8

<!--Device-unnamed-declare enum CacheMode--><!--Device-unnamed-declare enum CacheMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Default

```TypeScript
Default = 0
```

load cache when they are available and not expired, otherwise load online.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CacheMode-Default = 0--><!--Device-CacheMode-Default = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## None

```TypeScript
None = 1
```

load cache when they are available, otherwise load online.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CacheMode-None = 1--><!--Device-CacheMode-None = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Online

```TypeScript
Online = 2
```

Load online and not cache.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CacheMode-Online = 2--><!--Device-CacheMode-Online = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Only

```TypeScript
Only = 3
```

load cache and not online.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CacheMode-Only = 3--><!--Device-CacheMode-Only = 3-End-->

**System capability:** SystemCapability.Web.Webview.Core

