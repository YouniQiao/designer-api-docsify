# CacheMode

Enum type supplied to {@link cacheMode} for setting the Web cache mode.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare enum CacheMode--><!--Device-unnamed-declare enum CacheMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Default

```TypeScript
Default = 0
```

优先使用未过期cache加载资源，无效或无cache时从网络获取。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CacheMode-Default = 0--><!--Device-CacheMode-Default = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## None

```TypeScript
None = 1
```

优先使用cache（含过期）加载资源，无cache时从网络获取。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CacheMode-None = 1--><!--Device-CacheMode-None = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Online

```TypeScript
Online = 2
```

强制从网络获取最新资源，不使用任何cache。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CacheMode-Online = 2--><!--Device-CacheMode-Online = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Only

```TypeScript
Only = 3
```

仅使用本地cache加载资源。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-CacheMode-Only = 3--><!--Device-CacheMode-Only = 3-End-->

**System capability:** SystemCapability.Web.Webview.Core

