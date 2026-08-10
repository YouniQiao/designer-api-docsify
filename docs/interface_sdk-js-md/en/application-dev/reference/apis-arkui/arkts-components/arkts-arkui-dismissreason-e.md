# DismissReason

关闭原因类型。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare enum DismissReason--><!--Device-unnamed-declare enum DismissReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PRESS_BACK

```TypeScript
PRESS_BACK = 0
```

点击三键back、侧滑（左滑/右滑）、键盘ESC。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissReason-PRESS_BACK = 0--><!--Device-DismissReason-PRESS_BACK = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TOUCH_OUTSIDE

```TypeScript
TOUCH_OUTSIDE = 1
```

点击遮障层时。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissReason-TOUCH_OUTSIDE = 1--><!--Device-DismissReason-TOUCH_OUTSIDE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CLOSE_BUTTON

```TypeScript
CLOSE_BUTTON = 2
```

点击关闭按钮。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissReason-CLOSE_BUTTON = 2--><!--Device-DismissReason-CLOSE_BUTTON = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SLIDE_DOWN

```TypeScript
SLIDE_DOWN = 3
```

下拉关闭。

**说明：**

该接口仅支持在[半模态转场](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md)中使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissReason-SLIDE_DOWN = 3--><!--Device-DismissReason-SLIDE_DOWN = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SLIDE

```TypeScript
SLIDE = 4
```

滑动交互，不是向下滑动。默认表示向右滑动，镜像操作后表示向左滑动。不支持选择向左或向右滑动。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-DismissReason-SLIDE = 4--><!--Device-DismissReason-SLIDE = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

