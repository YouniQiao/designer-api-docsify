# RenderStrategy

RenderStrategy 的枚举。定义图形渲染策略。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

<!--Device-unnamed-declare enum RenderStrategy--><!--Device-unnamed-declare enum RenderStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FAST

```TypeScript
FAST = 0
```

当前组件及其子组件将直接绘制到画布上，并应用圆角效果。

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

当前组件及其子组件会先被画到一个离屏画布上，然后进行一些图形渲染操作，最后绘制到主画布上。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

<!--Device-RenderStrategy-OFFSCREEN = 1--><!--Device-RenderStrategy-OFFSCREEN = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

