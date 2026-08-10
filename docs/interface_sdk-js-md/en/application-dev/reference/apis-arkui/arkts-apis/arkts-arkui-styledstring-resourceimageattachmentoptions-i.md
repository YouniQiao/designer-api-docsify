# ResourceImageAttachmentOptions

ResourceStr类型图片设置项。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ResourceImageAttachmentOptions--><!--Device-unnamed-export declare interface ResourceImageAttachmentOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colorFilter

```TypeScript
colorFilter?: ColorFilterType
```

设置属性字符串的图片颜色滤镜效果。

**Type:** [ColorFilterType](arkts-arkui-colorfiltertype-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResourceImageAttachmentOptions-colorFilter?: ColorFilterType--><!--Device-ResourceImageAttachmentOptions-colorFilter?: ColorFilterType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutStyle

```TypeScript
layoutStyle?: ImageAttachmentLayoutStyle
```

设置图片布局。

**Type:** [ImageAttachmentLayoutStyle](arkts-arkui-imageattachmentlayoutstyle-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResourceImageAttachmentOptions-layoutStyle?: ImageAttachmentLayoutStyle--><!--Device-ResourceImageAttachmentOptions-layoutStyle?: ImageAttachmentLayoutStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## objectFit

```TypeScript
objectFit?: ImageFit
```

设置图片的缩放类型，当前枚举类型不支持ImageFit.MATRIX。

默认值：ImageFit.Cover

**Type:** [ImageFit](arkts-arkui-imagefit-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResourceImageAttachmentOptions-objectFit?: ImageFit--><!--Device-ResourceImageAttachmentOptions-objectFit?: ImageFit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## resourceValue

```TypeScript
resourceValue: ResourceStr | undefined
```

设置图片数据源。

取值为undefined时，按空处理。

**Type:** [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResourceImageAttachmentOptions-resourceValue: ResourceStr | undefined--><!--Device-ResourceImageAttachmentOptions-resourceValue: ResourceStr | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: SizeOptions
```

设置图片大小。

**Type:** [SizeOptions](arkts-arkui-sizeoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResourceImageAttachmentOptions-size?: SizeOptions--><!--Device-ResourceImageAttachmentOptions-size?: SizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## supportSvg2

```TypeScript
supportSvg2?: boolean
```

控制是否开启[SVG标签解析能力增强功能](../../../reference/apis-arkui/arkui-ts/ts-image-svg2-capabilities.md)。

true：支持SVG解析新能力；false：保持原有SVG解析能力。

默认值：false

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResourceImageAttachmentOptions-supportSvg2?: boolean--><!--Device-ResourceImageAttachmentOptions-supportSvg2?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## syncLoad

```TypeScript
syncLoad?: boolean
```

是否同步加载图片，默认是异步加载。同步加载时阻塞UI线程，不会显示占位图。

true：同步加载；false：异步加载。

默认值：false

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResourceImageAttachmentOptions-syncLoad?: boolean--><!--Device-ResourceImageAttachmentOptions-syncLoad?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## verticalAlign

```TypeScript
verticalAlign?: ImageSpanAlignment
```

设置图片基于文本的对齐方式。

默认值：ImageSpanAlignment.BOTTOM

**Type:** [ImageSpanAlignment](arkts-arkui-imagespanalignment-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ResourceImageAttachmentOptions-verticalAlign?: ImageSpanAlignment--><!--Device-ResourceImageAttachmentOptions-verticalAlign?: ImageSpanAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

