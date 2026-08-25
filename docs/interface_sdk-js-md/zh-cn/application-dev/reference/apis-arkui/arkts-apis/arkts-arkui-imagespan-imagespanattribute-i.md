# ImageSpanAttribute

属性继承自BaseSpan，通用属性方法支持 [尺寸设置](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-size.md)、 [背景设置](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-background.md)、 [边框设置](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-border.md)。

**继承/实现关系：** ImageSpanAttribute extends BaseSpan

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alt

```TypeScript
default alt(value: PixelMap | undefined): this
```

设置图片加载过程中显示的占位图。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSpanAttribute](arkts-arkui-imagespan-imagespanattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ImageSpanAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ImageSpanAttribute](arkts-arkui-imagespan-imagespanattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSpanAttribute](arkts-arkui-imagespan-imagespanattribute-i.md) |

## colorFilter

```TypeScript
default colorFilter(filter: ColorFilter | DrawingColorFilter | undefined): this
```

为图像设置颜色滤镜效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| filter | [ColorFilter](arkts-arkui-colorfilter-c.md) \| [DrawingColorFilter](../arkts-components/arkts-arkui-drawingcolorfilter-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSpanAttribute](arkts-arkui-imagespan-imagespanattribute-i.md) |

## objectFit

```TypeScript
default objectFit(value: ImageFit | undefined): this
```

设置图片的缩放类型。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageFit](arkts-arkui-imagefit-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSpanAttribute](arkts-arkui-imagespan-imagespanattribute-i.md) |

## onComplete

```TypeScript
default onComplete(callback: ImageCompleteCallback | undefined): this
```

图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ImageCompleteCallback](arkts-arkui-imagecompletecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSpanAttribute](arkts-arkui-imagespan-imagespanattribute-i.md) |

## onError

```TypeScript
default onError(callback: ImageErrorCallback | undefined): this
```

图片加载异常时触发该回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ImageErrorCallback](../arkts-components/arkts-arkui-imageerrorcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSpanAttribute](arkts-arkui-imagespan-imagespanattribute-i.md) |

## setImageSpanOptions

```TypeScript
default setImageSpanOptions(value: ResourceStr | PixelMap): this
```

设置ImageSpan选项。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceStr](arkts-arkui-resourcestr-t.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSpanAttribute](arkts-arkui-imagespan-imagespanattribute-i.md) |

## supportSvg2

```TypeScript
default supportSvg2(enable: boolean | undefined) : this
```

开启或关闭SVG标签解析能力增强功能，开启后相关SVG图片显示效果会有变化。ImageSpan组件创建后，不支持动态修改该属性的值。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSpanAttribute](arkts-arkui-imagespan-imagespanattribute-i.md) |

## verticalAlign

```TypeScript
default verticalAlign(value: ImageSpanAlignment | undefined): this
```

设置图片基于行高的对齐方式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageSpanAlignment](arkts-arkui-imagespanalignment-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageSpanAttribute](arkts-arkui-imagespan-imagespanattribute-i.md) |
