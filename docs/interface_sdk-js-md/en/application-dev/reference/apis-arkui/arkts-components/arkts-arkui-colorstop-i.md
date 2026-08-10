# ColorStop

颜色断点类型，用于描述渐变色颜色断点。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface ColorStop--><!--Device-unnamed-declare interface ColorStop-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color: ResourceColor
```

渐变色断点处的颜色值。

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ColorStop-color: ResourceColor--><!--Device-ColorStop-color: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset: Length
```

渐变色断点（0~1之间的比例值，若该值小于0则置为0，若该值大于1则置为1）。

**说明：**

若传入字符串类型且内容为数字，则转换为对应的数值。

例如'10vp'转换为10，'10%'转换为0.1。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ColorStop-offset: Length--><!--Device-ColorStop-offset: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

