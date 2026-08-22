# WebDestroyMode

Enum type supplied to SetWebDestroyMode for indicating the web component destroy mode. @enum { number }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-webview-enum WebDestroyMode--><!--Device-webview-enum WebDestroyMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## NORMAL_MODE

```TypeScript
NORMAL_MODE = 0
```

The normal destroy mode, when the web component triggers destroy, the resources will be released at the appropriate time.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebDestroyMode-NORMAL_MODE = 0--><!--Device-WebDestroyMode-NORMAL_MODE = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## FAST_MODE

```TypeScript
FAST_MODE = 1
```

The fast destroy mode, when the web component triggers destroy, the resources will be immediately released.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebDestroyMode-FAST_MODE = 1--><!--Device-WebDestroyMode-FAST_MODE = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

