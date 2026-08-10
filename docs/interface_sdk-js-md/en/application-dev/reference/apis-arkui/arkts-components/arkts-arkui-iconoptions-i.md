# IconOptions

定义图标选项。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-interface IconOptions--><!--Device-unnamed-interface IconOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

图标颜色。不传入时使用默认颜色（浅色模式为'#99182431'，表示深灰色，60%不透明度，深色模式为'#99ffffff'，表示白色，60%不透明度）。

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-IconOptions-color?: ResourceColor--><!--Device-IconOptions-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: Length
```

图标尺寸，不传入单位时默认单位为vp，不支持百分比。传入百分比时，不生效。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-IconOptions-size?: Length--><!--Device-IconOptions-size?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## src

```TypeScript
src?: ResourceStr
```

图标/图片源。不传入时使用系统默认图标。

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-IconOptions-src?: ResourceStr--><!--Device-IconOptions-src?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

