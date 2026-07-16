# ScrollDirectionalLockType

Enum defining the scope of directional lock behavior in the WebView, used with {@link enableScrollDirectionalLock}.

**Since:** 26.0.0

<!--Device-unnamed-declare enum ScrollDirectionalLockType--><!--Device-unnamed-declare enum ScrollDirectionalLockType-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ALL

```TypeScript
ALL = 0
```

Applies directional lock across all scroll contexts.This includes both nested and flat scroll scenarios.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollDirectionalLockType-ALL = 0--><!--Device-ScrollDirectionalLockType-ALL = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## NESTED_SCROLL

```TypeScript
NESTED_SCROLL = 1
```

Applies directional lock only within nested scroll scenarios.This is the default behavior in ArkWeb to improve UX in complex scroll hierarchies.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollDirectionalLockType-NESTED_SCROLL = 1--><!--Device-ScrollDirectionalLockType-NESTED_SCROLL = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

