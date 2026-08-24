# MixedMode

The Web's behavior to load from HTTP or HTTPS. Defaults to MixedMode.None.@enum { number }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare enum MixedMode--><!--Device-unnamed-export declare enum MixedMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ALL

```TypeScript
ALL = 0
```

Loose Mode: HTTP and HTTPS hybrid content can be loaded. This means that all insecure content can be loaded.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-MixedMode-ALL = 0--><!--Device-MixedMode-ALL = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## COMPATIBLE

```TypeScript
COMPATIBLE = 1
```

Compatibility Modes: HTTP and HTTPS hybrid content can be loaded in compatibility mode. This means that some insecure content may be loaded.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-MixedMode-COMPATIBLE = 1--><!--Device-MixedMode-COMPATIBLE = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## NONE

```TypeScript
NONE = 2
```

Strict Mode: HTTP and HTTPS hybrid content cannot be loaded.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-MixedMode-NONE = 2--><!--Device-MixedMode-NONE = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

