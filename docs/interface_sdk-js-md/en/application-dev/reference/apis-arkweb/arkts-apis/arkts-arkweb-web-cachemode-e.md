# CacheMode

Enum type supplied to [cacheMode](arkts-arkweb-web-webattribute-i.md#cachemode) for setting the Web cache mode.@enum { number }

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## DEFAULT

```TypeScript
DEFAULT = 0
```

load cache when they are available and not expired, otherwise load online.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## NONE

```TypeScript
NONE = 1
```

load cache when they are available, otherwise load online.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## ONLINE

```TypeScript
ONLINE = 2
```

Load online and not cache.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## ONLY

```TypeScript
ONLY = 3
```

load cache and not online.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core
