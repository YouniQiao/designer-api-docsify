# MarqueeAttribute

除支持通用属性外，还支持以下属性：

**继承/实现关系：** MarqueeAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## allowScale

```TypeScript
default allowScale(value: boolean | undefined): this
```

设置是否允许文本缩放。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<MarqueeAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置组件的动态属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## fontColor

```TypeScript
default fontColor(value: ResourceColor | undefined): this
```

设置字体颜色。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## fontFamily

```TypeScript
default fontFamily(value: string | Resource | undefined): this
```

设置字体列表。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## fontSize

```TypeScript
default fontSize(value: Length | undefined): this
```

设置字体大小。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## fontWeight

```TypeScript
default fontWeight(value: int | FontWeight | ResourceStr | undefined): this
```

设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | int \| [FontWeight](arkts-arkui-fontweight-e.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## marqueeUpdateStrategy

```TypeScript
default marqueeUpdateStrategy(value: MarqueeUpdateStrategy | undefined): this
```

跑马灯组件属性更新后，跑马灯的滚动策略。(当跑马灯为播放状态，且文本内容宽度超过跑马灯组件宽度时，该属性生效。)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [MarqueeUpdateStrategy](arkts-arkui-marqueeupdatestrategy-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## onBounce

```TypeScript
default onBounce(event: (() => void) | undefined): this
```

完成一次滚动时触发，若循环次数不为1，则该事件会多次触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## onFinish

```TypeScript
default onFinish(event: (() => void) | undefined): this
```

滚动全部循环次数完成时触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## onStart

```TypeScript
default onStart(event: (() => void) | undefined): this
```

当滚动的文本内容变化或者开始滚动时触发回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## onStop

```TypeScript
default onStop(event: VoidCallback | undefined): this
```

跑马灯滚动结束或停止时触发回调。跑马灯停止表示跑马灯将从开始位置，重新开始循环，不包含暂停场景，暂停不会触发该回调。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |

## setMarqueeOptions

```TypeScript
default setMarqueeOptions(options: MarqueeOptions): this
```

设置Marquee组件选项。

**起始版本：** 26.1.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [MarqueeOptions](arkts-arkui-marquee-marqueeoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [MarqueeAttribute](arkts-arkui-marquee-marqueeattribute-i.md) |
