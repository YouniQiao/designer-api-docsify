# FocusPriority

设置组件焦点的优先级。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare enum FocusPriority--><!--Device-unnamed-declare enum FocusPriority-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO

```TypeScript
AUTO = 0
```

默认的优先级，缺省时组件的获焦优先级。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FocusPriority-AUTO = 0--><!--Device-FocusPriority-AUTO = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PRIOR

```TypeScript
PRIOR = 2000
```

容器内优先获焦的优先级。优先级高于AUTO。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FocusPriority-PRIOR = 2000--><!--Device-FocusPriority-PRIOR = 2000-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PREVIOUS

```TypeScript
PREVIOUS = 3000
```

上一次容器整体失焦时获焦节点的优先级。优先级高于PRIOR。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FocusPriority-PREVIOUS = 3000--><!--Device-FocusPriority-PREVIOUS = 3000-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

