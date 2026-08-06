# RenderStrategy

Enumerates rendering strategies for drawing rounded corners.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-unnamed-declare enum RenderStrategy--><!--Device-unnamed-declare enum RenderStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FAST

```TypeScript
FAST = 0
```

Online rendering mode. The content to be rendered is clipped with rounded corners and directly rendered to the main canvas.

Note: Online rendering may cause display anomalies in certain scenarios. For example, when blur effects are applied within rounded corner components, background colors may interact and create gradient overlay effects. For detailed behavior, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-RenderStrategy-FAST = 0--><!--Device-RenderStrategy-FAST = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## OFFSCREEN

```TypeScript
OFFSCREEN = 1
```

Offscreen rendering mode. The content to be rendered is first rendered to the offscreen canvas without rounded corners, and then clipped with rounded corners and rendered to the main canvas.

**NOTE**

1. Compared with online rendering, offscreen rendering requires additional performance overhead.2. In offscreen rendering, the content is first rendered on an additional canvas, and then rendered on the main canvas.3. Use offscreen rendering primarily for multi-layer components requiring rounded corners. For single components,it has effect only when the [clip]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ attribute, [background]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_,or [foreground color]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ is configured.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-RenderStrategy-OFFSCREEN = 1--><!--Device-RenderStrategy-OFFSCREEN = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

