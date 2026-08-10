# MixedMode

混合内容模式。默认设置为 MixedMode.None。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare enum MixedMode--><!--Device-unnamed-declare enum MixedMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## All

```TypeScript
All = 0
```

宽松模式：允许加载HTTP和HTTPS混合内容。所有不安全的内容都可以被加载。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MixedMode-All = 0--><!--Device-MixedMode-All = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Compatible

```TypeScript
Compatible = 1
```

兼容模式：混合内容兼容性模式，部分不安全的内容可能被加载。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MixedMode-Compatible = 1--><!--Device-MixedMode-Compatible = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## None

```TypeScript
None = 2
```

严格模式：不允许加载HTTP和HTTPS混合内容。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MixedMode-None = 2--><!--Device-MixedMode-None = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

