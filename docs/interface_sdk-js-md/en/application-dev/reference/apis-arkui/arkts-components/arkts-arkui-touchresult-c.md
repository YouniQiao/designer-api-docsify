# TouchResult

自定义事件分发结果，开发者通过返回结果来影响事件分发。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare class TouchResult--><!--Device-unnamed-declare class TouchResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id?: string
```

子组件的唯一标识。

当strategy为TouchTestStrategy.DEFAULT时，id是可选的；当strategy是TouchTestStrategy.FORWARD_COMPETITION或TouchTestStrategy.FORWARD时，id是必需的（如果没有返回id，则当成TouchTestStrategy.DEFAULT处理）。

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TouchResult-id?: string--><!--Device-TouchResult-id?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strategy

```TypeScript
strategy: TouchTestStrategy
```

事件派发策略。

**Type:** [TouchTestStrategy](../arkts-apis/arkts-arkui-common-touchteststrategy-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TouchResult-strategy: TouchTestStrategy--><!--Device-TouchResult-strategy: TouchTestStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

