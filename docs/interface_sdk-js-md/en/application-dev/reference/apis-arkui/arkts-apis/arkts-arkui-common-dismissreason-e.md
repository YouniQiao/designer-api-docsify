# DismissReason

关闭原因类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum DismissReason--><!--Device-unnamed-export declare enum DismissReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## PRESS_BACK

```TypeScript
PRESS_BACK = 0
```

点击三键back、侧滑（左滑/右滑）、键盘ESC。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissReason-PRESS_BACK = 0--><!--Device-DismissReason-PRESS_BACK = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## TOUCH_OUTSIDE

```TypeScript
TOUCH_OUTSIDE = 1
```

点击遮障层时。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissReason-TOUCH_OUTSIDE = 1--><!--Device-DismissReason-TOUCH_OUTSIDE = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## CLOSE_BUTTON

```TypeScript
CLOSE_BUTTON = 2
```

点击关闭按钮。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissReason-CLOSE_BUTTON = 2--><!--Device-DismissReason-CLOSE_BUTTON = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SLIDE_DOWN

```TypeScript
SLIDE_DOWN = 3
```

下拉关闭。

**说明：**

该接口仅支持在[半模态转场](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)中使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissReason-SLIDE_DOWN = 3--><!--Device-DismissReason-SLIDE_DOWN = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SLIDE

```TypeScript
SLIDE = 4
```

侧滑（左滑/右滑）关闭。默认表示向右滑动关闭，镜像场景表示向左滑动关闭，不支持选择向左或向右滑动。

**说明：**

该接口仅支持在[半模态转场](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)中使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DismissReason-SLIDE = 4--><!--Device-DismissReason-SLIDE = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

