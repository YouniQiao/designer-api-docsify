# ScrollbarMode

Enum type supplied to [setScrollbarMode](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#setscrollbarmode) for indicating the web component scrollbar mode.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-webview-enum ScrollbarMode--><!--Device-webview-enum ScrollbarMode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## OVERLAY_LAYOUT_SCROLLBAR

```TypeScript
OVERLAY_LAYOUT_SCROLLBAR = 0
```

The normal scrollbar mode, A scrollbar suspended above the content, appearing when scrolling and automatically hiding when stationary. Draw using layout viewport, which can be dragged and dropped.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ScrollbarMode-OVERLAY_LAYOUT_SCROLLBAR = 0--><!--Device-ScrollbarMode-OVERLAY_LAYOUT_SCROLLBAR = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## FORCE_DISPLAY_SCROLLBAR

```TypeScript
FORCE_DISPLAY_SCROLLBAR = 1
```

The Resident scrollbar mode, Always display a fixed position scrollbar in the content area.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-ScrollbarMode-FORCE_DISPLAY_SCROLLBAR = 1--><!--Device-ScrollbarMode-FORCE_DISPLAY_SCROLLBAR = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## OVERLAY_VISUAL_SCROLLBAR

```TypeScript
OVERLAY_VISUAL_SCROLLBAR = 2
```

Overlay VisualViewport scrollbars: appear on scroll, hide when idle. Rendered via Visual Viewport, non-draggable.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollbarMode-OVERLAY_VISUAL_SCROLLBAR = 2--><!--Device-ScrollbarMode-OVERLAY_VISUAL_SCROLLBAR = 2-End-->

**System capability:** SystemCapability.Web.Webview.Core

