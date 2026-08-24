# WindowSizeLayoutBreakpointInfo

Defines the window size layout breakpoint information. This interface provides the current breakpoint classification of the window's width and height based on the configured breakpoint thresholds.@interface WindowSizeLayoutBreakpointInfo

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

<!--Device-uiObserver-export interface WindowSizeLayoutBreakpointInfo--><!--Device-uiObserver-export interface WindowSizeLayoutBreakpointInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## heightBreakpoint

```TypeScript
readonly heightBreakpoint: HeightBreakpoint
```

The height breakpoint classification of the current window. This value indicates which height category the window currently falls into based on the configured height breakpoint thresholds and aspect ratio.

**Type:** HeightBreakpoint

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowSizeLayoutBreakpointInfo-readonly heightBreakpoint: HeightBreakpoint--><!--Device-WindowSizeLayoutBreakpointInfo-readonly heightBreakpoint: HeightBreakpoint-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## widthBreakpoint

```TypeScript
readonly widthBreakpoint: WidthBreakpoint
```

The width breakpoint classification of the current window. This value indicates which width category the window currently falls into based on the configured width breakpoint thresholds.

**Type:** WidthBreakpoint

**Since:** 24

**ArkTS mode:** ArkTS-Sta since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowSizeLayoutBreakpointInfo-readonly widthBreakpoint: WidthBreakpoint--><!--Device-WindowSizeLayoutBreakpointInfo-readonly widthBreakpoint: WidthBreakpoint-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

