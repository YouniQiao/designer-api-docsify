# RichEditorImageSpanStyle

图片样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RichEditorImageSpanStyle--><!--Device-unnamed-export declare interface RichEditorImageSpanStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutStyle

```TypeScript
layoutStyle?: RichEditorLayoutStyle
```

图片布局风格。

**Type:** [RichEditorLayoutStyle](../arkts-components/arkts-arkui-richeditorlayoutstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorImageSpanStyle-layoutStyle?: RichEditorLayoutStyle--><!--Device-RichEditorImageSpanStyle-layoutStyle?: RichEditorLayoutStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## objectFit

```TypeScript
objectFit?: ImageFit
```

图片缩放类型。

**Type:** [ImageFit](arkts-arkui-imagefit-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorImageSpanStyle-objectFit?: ImageFit--><!--Device-RichEditorImageSpanStyle-objectFit?: ImageFit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: [
        Dimension,
        Dimension
    ]
```

图片的宽度和高度，单位为px。默认值：size的默认值与objectFit的值有关，不同的objectFit值对应的size默认值也不同。objectFit的值为Cover时，图片高度为组件高度减去组件上下内边距，图片宽度为组件宽度减去组件左右内边距。

**Type:** [         Dimension,         Dimension     ]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorImageSpanStyle-size?: [        Dimension,        Dimension    ]--><!--Device-RichEditorImageSpanStyle-size?: [        Dimension,        Dimension    ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## verticalAlign

```TypeScript
verticalAlign?: ImageSpanAlignment
```

图片垂直对齐方式。

**Type:** [ImageSpanAlignment](arkts-arkui-imagespanalignment-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorImageSpanStyle-verticalAlign?: ImageSpanAlignment--><!--Device-RichEditorImageSpanStyle-verticalAlign?: ImageSpanAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

