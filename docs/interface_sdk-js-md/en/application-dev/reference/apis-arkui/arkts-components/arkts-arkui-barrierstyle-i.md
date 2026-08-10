# BarrierStyle

barrier参数，用于定义一条barrier的id、方向和生成时所依赖的组件，子组件可通过barrier的id引用屏障作为锚点进行对齐定位。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface BarrierStyle--><!--Device-unnamed-declare interface BarrierStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## direction

```TypeScript
direction : BarrierDirection
```

指定barrier的方向。

水平屏障线（TOP/BOTTOM）仅能作为组件垂直方向锚点（top或bottom），用于水平方向锚点时位置视为0。垂直屏障线（LEFT/RIGHT）仅能作为组件水平方向锚点（left或right），用于垂直方向锚点时位置视为0。

默认值：BarrierDirection.LEFT

非法值：按默认值处理。

**Type:** [BarrierDirection](../arkts-apis/arkts-arkui-relativecontainer-barrierdirection-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BarrierStyle-direction : BarrierDirection--><!--Device-BarrierStyle-direction : BarrierDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id : string
```

barrier的id，用于标识屏障，子组件可通过此id引用该屏障作为锚点。必须是唯一的并且不可与容器内组件重名。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BarrierStyle-id : string--><!--Device-BarrierStyle-id : string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## referencedId

```TypeScript
referencedId : Array<string>
```

指定生成barrier所依赖的组件。将需要作为屏障基准的组件id放入数组，至少包含一个有效组件ID，不存在的ID会被忽略。barrier根据组件边界计算位置：LEFT取最左侧，RIGHT取最右侧，TOP取最上方，BOTTOM取最下方。

**Type:** Array&lt;string&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BarrierStyle-referencedId : Array<string>--><!--Device-BarrierStyle-referencedId : Array<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

