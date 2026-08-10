# ColorStop

颜色断点类型，用于描述渐进色颜色断点。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ColorStop--><!--Device-unnamed-export declare interface ColorStop-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color: ResourceColor
```

渐变色断点处的颜色值。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorStop-color: ResourceColor--><!--Device-ColorStop-color: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset: Length
```

渐变色断点（0~1之间的比例值，若数据值小于0则置为0，若数据值大于1则置为1）。

**说明：**

若传入字符串类型且内容为数字，则转换为对应的数值。

例如'10vp'转换为10，'10%'转换为0.1。

**Type:** [Length](arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColorStop-offset: Length--><!--Device-ColorStop-offset: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

