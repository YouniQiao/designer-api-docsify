# BarrierStyle

barrier参数，用于定义一条barrier的id、方向和生成时所依赖的组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface BarrierStyle--><!--Device-unnamed-export declare interface BarrierStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction: BarrierDirection
```

指定barrier的方向。垂直方向（TOP，BOTTOM）的barrier仅能作为组件的水平方向锚点，用作垂直方向锚点时值为0；水平方向（LEFT，RIGHT）的barrier仅能作为组件的垂直方向锚点，用作水平方向锚点时值为0。默认值：BarrierDirection.LEFT，非法值：按默认值处理。

**Type:** [BarrierDirection](arkts-arkui-relativecontainer-barrierdirection-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarrierStyle-direction: BarrierDirection--><!--Device-BarrierStyle-direction: BarrierDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id: string
```

barrier的id，必须是唯一的并且不可与容器内组件重名。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarrierStyle-id: string--><!--Device-BarrierStyle-id: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## referencedId

```TypeScript
referencedId: Array<string>
```

指定生成barrier所依赖的组件。

**Type:** Array&lt;string&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BarrierStyle-referencedId: Array<string>--><!--Device-BarrierStyle-referencedId: Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

