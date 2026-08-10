# RichEditorImageSpanStyleResult

后端返回的图片样式信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface RichEditorImageSpanStyleResult--><!--Device-unnamed-declare interface RichEditorImageSpanStyleResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutStyle

```TypeScript
layoutStyle?: RichEditorLayoutStyle
```

图片布局样式。

**Type:** [RichEditorLayoutStyle](arkts-arkui-richeditorlayoutstyle-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorImageSpanStyleResult-layoutStyle?: RichEditorLayoutStyle--><!--Device-RichEditorImageSpanStyleResult-layoutStyle?: RichEditorLayoutStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## objectFit

```TypeScript
objectFit: ImageFit
```

图片缩放类型。

**Type:** [ImageFit](../arkts-apis/arkts-arkui-imagefit-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorImageSpanStyleResult-objectFit: ImageFit--><!--Device-RichEditorImageSpanStyleResult-objectFit: ImageFit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size: [number, number]
```

图片的宽度和高度，单位为px。默认值：size的默认值与objectFit的值有关，不同的objectFit值对应的size默认值也不同。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，图片宽度为组件宽度减去组件左右内边距。

**Type:** [number, number]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorImageSpanStyleResult-size: [number, number]--><!--Device-RichEditorImageSpanStyleResult-size: [number, number]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## verticalAlign

```TypeScript
verticalAlign: ImageSpanAlignment
```

图片垂直对齐方式。

**Type:** [ImageSpanAlignment](../arkts-apis/arkts-arkui-enums-imagespanalignment-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorImageSpanStyleResult-verticalAlign: ImageSpanAlignment--><!--Device-RichEditorImageSpanStyleResult-verticalAlign: ImageSpanAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

