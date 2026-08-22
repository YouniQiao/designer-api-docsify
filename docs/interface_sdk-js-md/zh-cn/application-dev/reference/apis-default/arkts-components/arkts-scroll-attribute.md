# ScrollAttribute

除支持通用属性和[滚动组件通用属性](../../../reference/apis-arkui/arkui-ts/ts-container-scrollable-common.md#属性)外，还支持 以下属性：

**继承/实现关系：** ScrollAttribute extends ScrollableCommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface ScrollAttribute--><!--Device-unnamed-export declare interface ScrollAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ScrollAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-attributeModifier(modifier: AttributeModifier<ScrollAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ScrollAttribute-attributeModifier(modifier: AttributeModifier<ScrollAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ScrollAttribute](arkts-scroll-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## edgeEffect

```TypeScript
edgeEffect(edgeEffect: EdgeEffect | undefined, options?: EdgeEffectOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-edgeEffect(edgeEffect: EdgeEffect | undefined, options?: EdgeEffectOptions | undefined): this--><!--Device-ScrollAttribute-edgeEffect(edgeEffect: EdgeEffect | undefined, options?: EdgeEffectOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| edgeEffect | [EdgeEffect](../../apis-arkui/arkts-apis/arkts-arkui-edgeeffect-e.md) \| undefined | 是 |  |
| options | [EdgeEffectOptions](../../apis-arkui/arkts-components/arkts-arkui-edgeeffectoptions-i.md) \| undefined | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableBouncesZoom

```TypeScript
enableBouncesZoom(enable: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-enableBouncesZoom(enable: boolean | undefined): this--><!--Device-ScrollAttribute-enableBouncesZoom(enable: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enablePaging

```TypeScript
enablePaging(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-enablePaging(value: boolean | undefined): this--><!--Device-ScrollAttribute-enablePaging(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableScrollInteraction

```TypeScript
enableScrollInteraction(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-enableScrollInteraction(value: boolean | undefined): this--><!--Device-ScrollAttribute-enableScrollInteraction(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## friction

```TypeScript
friction(value: double | Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-friction(value: double | Resource | undefined): this--><!--Device-ScrollAttribute-friction(value: double | Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## initialOffset

```TypeScript
initialOffset(value: OffsetOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-initialOffset(value: OffsetOptions | undefined): this--><!--Device-ScrollAttribute-initialOffset(value: OffsetOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [OffsetOptions](arkts-scroll-offsetoptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## maxZoomScale

```TypeScript
maxZoomScale(scale: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-maxZoomScale(scale: double | undefined): this--><!--Device-ScrollAttribute-maxZoomScale(scale: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## minZoomScale

```TypeScript
minZoomScale(scale: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-minZoomScale(scale: double | undefined): this--><!--Device-ScrollAttribute-minZoomScale(scale: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-nestedScroll(value: NestedScrollOptions | undefined): this--><!--Device-ScrollAttribute-nestedScroll(value: NestedScrollOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](../../apis-arkui/arkts-components/arkts-arkui-nestedscrolloptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onDidScroll

```TypeScript
onDidScroll(handler: ScrollOnScrollCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-onDidScroll(handler: ScrollOnScrollCallback | undefined): this--><!--Device-ScrollAttribute-onDidScroll(handler: ScrollOnScrollCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [ScrollOnScrollCallback](arkts-scrollonscrollcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onDidZoom

```TypeScript
onDidZoom(event: ScrollOnDidZoomCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-onDidZoom(event: ScrollOnDidZoomCallback | undefined): this--><!--Device-ScrollAttribute-onDidZoom(event: ScrollOnDidZoomCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ScrollOnDidZoomCallback](arkts-scrollondidzoomcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollEdge

```TypeScript
onScrollEdge(event: OnScrollEdgeCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-onScrollEdge(event: OnScrollEdgeCallback | undefined): this--><!--Device-ScrollAttribute-onScrollEdge(event: OnScrollEdgeCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnScrollEdgeCallback](arkts-onscrolledgecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollFrameBegin

```TypeScript
onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this--><!--Device-ScrollAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [OnScrollFrameBeginCallback](arkts-onscrollframebegincallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollStart

```TypeScript
onScrollStart(event: VoidCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-onScrollStart(event: VoidCallback | undefined): this--><!--Device-ScrollAttribute-onScrollStart(event: VoidCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onScrollStop

```TypeScript
onScrollStop(event: VoidCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-onScrollStop(event: VoidCallback | undefined): this--><!--Device-ScrollAttribute-onScrollStop(event: VoidCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onWillScroll

```TypeScript
onWillScroll(handler: ScrollOnWillScrollCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-onWillScroll(handler: ScrollOnWillScrollCallback | undefined): this--><!--Device-ScrollAttribute-onWillScroll(handler: ScrollOnWillScrollCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [ScrollOnWillScrollCallback](arkts-scrollonwillscrollcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onZoomStart

```TypeScript
onZoomStart(event: VoidCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-onZoomStart(event: VoidCallback | undefined): this--><!--Device-ScrollAttribute-onZoomStart(event: VoidCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onZoomStop

```TypeScript
onZoomStop(event: VoidCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-onZoomStop(event: VoidCallback | undefined): this--><!--Device-ScrollAttribute-onZoomStop(event: VoidCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollBar

```TypeScript
scrollBar(barState: BarState | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-scrollBar(barState: BarState | undefined): this--><!--Device-ScrollAttribute-scrollBar(barState: BarState | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| barState | [BarState](../../apis-arkui/arkts-apis/arkts-arkui-barstate-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollBarColor

```TypeScript
scrollBarColor(color: Color | int | string | Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-scrollBarColor(color: Color | int | string | Resource | undefined): this--><!--Device-ScrollAttribute-scrollBarColor(color: Color | int | string | Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Color](../../apis-arkui/arkts-apis/arkts-arkui-color-e.md) \| int \| string \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollBarWidth

```TypeScript
scrollBarWidth(value: double | string | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-scrollBarWidth(value: double | string | undefined): this--><!--Device-ScrollAttribute-scrollBarWidth(value: double | string | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| string \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollBarWidth

```TypeScript
scrollBarWidth(value: Resource | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-scrollBarWidth(value: Resource | undefined): this--><!--Device-ScrollAttribute-scrollBarWidth(value: Resource | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollSnap

```TypeScript
scrollSnap(value: ScrollSnapOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-scrollSnap(value: ScrollSnapOptions | undefined): this--><!--Device-ScrollAttribute-scrollSnap(value: ScrollSnapOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScrollSnapOptions](arkts-scroll-scrollsnapoptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## scrollable

```TypeScript
scrollable(value: ScrollDirection | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-scrollable(value: ScrollDirection | undefined): this--><!--Device-ScrollAttribute-scrollable(value: ScrollDirection | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScrollDirection](arkts-scroll-scrolldirection-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setScrollOptions

```TypeScript
setScrollOptions(scroller?: Scroller): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-setScrollOptions(scroller?: Scroller): this--><!--Device-ScrollAttribute-setScrollOptions(scroller?: Scroller): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scroller | [Scroller](arkts-scroll-scroller-c.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## zoomScale

```TypeScript
zoomScale(scale: double | Bindable<double> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-ScrollAttribute-zoomScale(scale: double | Bindable<double> | undefined): this--><!--Device-ScrollAttribute-zoomScale(scale: double | Bindable<double> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | double \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;double&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

动态设置Scroll组件的属性方法。

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ScrollAttribute-default--><!--Device-ScrollAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

