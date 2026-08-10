# WindowSizeLayoutBreakpointInfo

定义窗口大小断点信息。这个接口定义了当前窗口长宽的断点信息，基于配置好的断点阈值。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-uiObserver-export interface WindowSizeLayoutBreakpointInfo--><!--Device-uiObserver-export interface WindowSizeLayoutBreakpointInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiObserver } from 'kits/@kit.ArkUI';
```

## heightBreakpoint

```TypeScript
readonly heightBreakpoint: HeightBreakpoint
```

当前窗口的高度断点分类。该值根据已配置的高度断点阈值和宽高比，指示窗口当前所处的高度类别。

**Type:** [HeightBreakpoint](arkts-arkui-heightbreakpoint-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowSizeLayoutBreakpointInfo-readonly heightBreakpoint: HeightBreakpoint--><!--Device-WindowSizeLayoutBreakpointInfo-readonly heightBreakpoint: HeightBreakpoint-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## widthBreakpoint

```TypeScript
readonly widthBreakpoint: WidthBreakpoint
```

当前窗口的宽度断点分类。该值根据已配置的宽度断点阈值，指示窗口当前处于哪个宽度类别。

**Type:** [WidthBreakpoint](arkts-arkui-widthbreakpoint-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowSizeLayoutBreakpointInfo-readonly widthBreakpoint: WidthBreakpoint--><!--Device-WindowSizeLayoutBreakpointInfo-readonly widthBreakpoint: WidthBreakpoint-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

