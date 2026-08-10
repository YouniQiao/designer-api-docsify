# SliderChangeMode

滑块的状态值。包括按下、拖动、离开以及点击滑动条使滑块位置时。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare enum SliderChangeMode--><!--Device-unnamed-export declare enum SliderChangeMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Begin

```TypeScript
Begin
```

手势/鼠标接触或者按下滑块。

**ArkTS-Dyn起始版本：** 7

**ArkTS-Sta起始版本：** 23

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderChangeMode-Begin--><!--Device-SliderChangeMode-Begin-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Moving

```TypeScript
Moving
```

正在拖动滑块过程中。

**ArkTS-Dyn起始版本：** 7

**ArkTS-Sta起始版本：** 23

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderChangeMode-Moving--><!--Device-SliderChangeMode-Moving-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## End

```TypeScript
End
```

手势/鼠标离开滑块。

**说明：**

异常值恢复成默认值时触发，即value设置小于min或大于max。

**ArkTS-Dyn起始版本：** 7

**ArkTS-Sta起始版本：** 23

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderChangeMode-End--><!--Device-SliderChangeMode-End-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Click

```TypeScript
Click
```

点击滑动条使滑块位置移动。

**ArkTS-Dyn起始版本：** 8

**ArkTS-Sta起始版本：** 23

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SliderChangeMode-Click--><!--Device-SliderChangeMode-Click-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

