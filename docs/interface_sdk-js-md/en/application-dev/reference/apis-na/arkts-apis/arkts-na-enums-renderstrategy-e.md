# RenderStrategy

Enum for RenderStrategy. Define Graphics Rendering Strategy.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare enum RenderStrategy--><!--Device-unnamed-export declare enum RenderStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FAST

```TypeScript
FAST = 0
```

The current component and its child components will be drawn directly onto the screen canvas.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderStrategy-FAST = 0--><!--Device-RenderStrategy-FAST = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## OFFSCREEN

```TypeScript
OFFSCREEN = 1
```

The current component and its child components will first be drawn onto an off-screen canvas, then undergo some graphic rendering operations, and finally be drawn onto the main canvas.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-RenderStrategy-OFFSCREEN = 1--><!--Device-RenderStrategy-OFFSCREEN = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

