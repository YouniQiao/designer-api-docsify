# GestureStyleInterface

Defines the Gesture Events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface GestureStyleInterface--><!--Device-unnamed-export declare interface GestureStyleInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onClick

```TypeScript
onClick?: Callback<ClickEvent>
```

设置点击事件。

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[ClickEvent](../arkts-components/arkts-arkui-clickevent-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureStyleInterface-onClick?: Callback<ClickEvent>--><!--Device-GestureStyleInterface-onClick?: Callback<ClickEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onLongPress

```TypeScript
onLongPress?: Callback<GestureEvent>
```

设置长按事件。

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[GestureEvent](arkts-arkui-gestureevent-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureStyleInterface-onLongPress?: Callback<GestureEvent>--><!--Device-GestureStyleInterface-onLongPress?: Callback<GestureEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTouch

```TypeScript
onTouch?: Callback<TouchEvent>
```

设置触摸事件。

取值为undefined时，不使用回调函数。

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[TouchEvent](../arkts-components/arkts-arkui-touchevent-i.md)&gt;

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GestureStyleInterface-onTouch?: Callback<TouchEvent>--><!--Device-GestureStyleInterface-onTouch?: Callback<TouchEvent>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

