# TouchTestStrategy

事件派发策略。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare enum TouchTestStrategy--><!--Device-unnamed-declare enum TouchTestStrategy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DEFAULT

```TypeScript
DEFAULT = 0
```

自定义分发不产生影响，系统按当前节点命中状态分发事件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-TouchTestStrategy-DEFAULT = 0--><!--Device-TouchTestStrategy-DEFAULT = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FORWARD_COMPETITION

```TypeScript
FORWARD_COMPETITION = 1
```

应用指定分发事件到某个子节点，其他兄弟节点是否分发事件交由系统决定。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-TouchTestStrategy-FORWARD_COMPETITION = 1--><!--Device-TouchTestStrategy-FORWARD_COMPETITION = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## FORWARD

```TypeScript
FORWARD = 2
```

应用指定分发事件到某个子节点，系统不再分发事件到其他兄弟节点。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-TouchTestStrategy-FORWARD = 2--><!--Device-TouchTestStrategy-FORWARD = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

