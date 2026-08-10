# GuideLineStyle

guideLine参数，用于定义一条guideLine的id、方向和位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface GuideLineStyle--><!--Device-unnamed-export declare interface GuideLineStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction: Axis
```

指定guideLine的方向。垂直方向的guideLine仅能作为组件水平方向的锚点，作为垂直方向的锚点时值为0；水平方向的guideLine仅能作为组件垂直方向的锚点，作为水平方向的锚点时值为0。默认值：Axis.Vertical，非法值：按默认值处理。

**Type:** [Axis](arkts-arkui-axis-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GuideLineStyle-direction: Axis--><!--Device-GuideLineStyle-direction: Axis-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id: string
```

guideLine的id，必须是唯一的并且不可与容器内组件重名。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GuideLineStyle-id: string--><!--Device-GuideLineStyle-id: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position: GuideLinePosition
```

指定guideLine的位置。当未声明或声明异常值（如undefined）时，guideLine的位置默认为start: 0。start和end两种声明方式选择一种即可。若同时声明，仅start生效。若容器在某个方向的size被声明为"auto"，则该方向上guideLine的位置只能使用start方式声明（不允许使用百分比）。默认值：{start: 0}，非法值：按默认值处理。

**Type:** [GuideLinePosition](arkts-arkui-relativecontainer-guidelineposition-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GuideLineStyle-position: GuideLinePosition--><!--Device-GuideLineStyle-position: GuideLinePosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

