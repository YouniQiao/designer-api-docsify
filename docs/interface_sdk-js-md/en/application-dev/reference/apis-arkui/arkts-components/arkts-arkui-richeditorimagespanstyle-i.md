# RichEditorImageSpanStyle

图片样式。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface RichEditorImageSpanStyle--><!--Device-unnamed-declare interface RichEditorImageSpanStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutStyle

```TypeScript
layoutStyle?: RichEditorLayoutStyle
```

图片布局样式。默认值：{"borderRadius":"","margin":""}

**Type:** [RichEditorLayoutStyle](arkts-arkui-richeditorlayoutstyle-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorImageSpanStyle-layoutStyle?: RichEditorLayoutStyle--><!--Device-RichEditorImageSpanStyle-layoutStyle?: RichEditorLayoutStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## objectFit

```TypeScript
objectFit?: ImageFit
```

图片缩放类型。

默认值：ImageFit.Cover。

**Type:** [ImageFit](../arkts-apis/arkts-arkui-imagefit-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorImageSpanStyle-objectFit?: ImageFit--><!--Device-RichEditorImageSpanStyle-objectFit?: ImageFit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: [Dimension, Dimension]
```

图片宽度和高度，默认单位为vp。默认值：与objectFit的值相关，不同的objectFit值有不同的默认尺寸。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，宽度为组件宽度减去组件左右内边距。不支持以Percentage形式设置。

**Type:** [Dimension, Dimension]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorImageSpanStyle-size?: [Dimension, Dimension]--><!--Device-RichEditorImageSpanStyle-size?: [Dimension, Dimension]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## verticalAlign

```TypeScript
verticalAlign?: ImageSpanAlignment
```

图片垂直对齐方式。

默认值：ImageSpanAlignment.BOTTOM

**Type:** [ImageSpanAlignment](../arkts-apis/arkts-arkui-enums-imagespanalignment-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorImageSpanStyle-verticalAlign?: ImageSpanAlignment--><!--Device-RichEditorImageSpanStyle-verticalAlign?: ImageSpanAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

