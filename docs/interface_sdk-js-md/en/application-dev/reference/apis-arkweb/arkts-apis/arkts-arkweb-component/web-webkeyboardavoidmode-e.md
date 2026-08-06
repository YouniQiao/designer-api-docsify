# WebKeyboardAvoidMode

Enum type supplied to \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ for setting the web keyboard avoid mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum WebKeyboardAvoidMode--><!--Device-unnamed-export declare enum WebKeyboardAvoidMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## RESIZE_VISUAL

```TypeScript
RESIZE_VISUAL = 0
```

When the soft keyboard avoids, only the size of the visual viewport is adjusted, not the size of the layout viewport.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebKeyboardAvoidMode-RESIZE_VISUAL = 0--><!--Device-WebKeyboardAvoidMode-RESIZE_VISUAL = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## RESIZE_CONTENT

```TypeScript
RESIZE_CONTENT = 1
```

By default, when the soft keyboard avoids,the sizes of the visual viewport and the layout viewport are adjusted at the same time.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebKeyboardAvoidMode-RESIZE_CONTENT = 1--><!--Device-WebKeyboardAvoidMode-RESIZE_CONTENT = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## OVERLAYS_CONTENT

```TypeScript
OVERLAYS_CONTENT = 2
```

Without adjusting any viewport size, soft keyboard avoidance will not be triggered.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebKeyboardAvoidMode-OVERLAYS_CONTENT = 2--><!--Device-WebKeyboardAvoidMode-OVERLAYS_CONTENT = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## RETURN_TO_UICONTEXT

```TypeScript
RETURN_TO_UICONTEXT = 3
```

When the soft keyboard avoid, follow the avoid result of UIContext.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-WebKeyboardAvoidMode-RETURN_TO_UICONTEXT = 3--><!--Device-WebKeyboardAvoidMode-RETURN_TO_UICONTEXT = 3-End-->

**System capability:** SystemCapability.Web.Webview.Core

