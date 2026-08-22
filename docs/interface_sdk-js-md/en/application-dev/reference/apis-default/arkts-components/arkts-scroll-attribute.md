# ScrollAttribute

The ScrollAttribute

**Inheritance/Implementation:** ScrollAttribute extends ScrollableCommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface ScrollAttribute--><!--Device-unnamed-export declare interface ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ScrollAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-attributeModifier(modifier: AttributeModifier<ScrollAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ScrollAttribute-attributeModifier(modifier: AttributeModifier<ScrollAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ScrollAttribute](arkts-scroll-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## edgeEffect

```TypeScript
edgeEffect(edgeEffect: EdgeEffect | undefined, options?: EdgeEffectOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-edgeEffect(edgeEffect: EdgeEffect | undefined, options?: EdgeEffectOptions | undefined): this--><!--Device-ScrollAttribute-edgeEffect(edgeEffect: EdgeEffect | undefined, options?: EdgeEffectOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| edgeEffect | [EdgeEffect](../../apis-arkui/arkts-apis/arkts-arkui-edgeeffect-e.md) \| undefined | Yes |  |
| options | [EdgeEffectOptions](../../apis-arkui/arkts-components/arkts-arkui-edgeeffectoptions-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableBouncesZoom

```TypeScript
enableBouncesZoom(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-enableBouncesZoom(enable: boolean | undefined): this--><!--Device-ScrollAttribute-enableBouncesZoom(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enablePaging

```TypeScript
enablePaging(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-enablePaging(value: boolean | undefined): this--><!--Device-ScrollAttribute-enablePaging(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableScrollInteraction

```TypeScript
enableScrollInteraction(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-enableScrollInteraction(value: boolean | undefined): this--><!--Device-ScrollAttribute-enableScrollInteraction(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## friction

```TypeScript
friction(value: double | Resource | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-friction(value: double | Resource | undefined): this--><!--Device-ScrollAttribute-friction(value: double | Resource | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## initialOffset

```TypeScript
initialOffset(value: OffsetOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-initialOffset(value: OffsetOptions | undefined): this--><!--Device-ScrollAttribute-initialOffset(value: OffsetOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [OffsetOptions](arkts-scroll-offsetoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## maxZoomScale

```TypeScript
maxZoomScale(scale: double | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-maxZoomScale(scale: double | undefined): this--><!--Device-ScrollAttribute-maxZoomScale(scale: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## minZoomScale

```TypeScript
minZoomScale(scale: double | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-minZoomScale(scale: double | undefined): this--><!--Device-ScrollAttribute-minZoomScale(scale: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-nestedScroll(value: NestedScrollOptions | undefined): this--><!--Device-ScrollAttribute-nestedScroll(value: NestedScrollOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](../../apis-arkui/arkts-components/arkts-arkui-nestedscrolloptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onDidScroll

```TypeScript
onDidScroll(handler: ScrollOnScrollCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-onDidScroll(handler: ScrollOnScrollCallback | undefined): this--><!--Device-ScrollAttribute-onDidScroll(handler: ScrollOnScrollCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [ScrollOnScrollCallback](arkts-scrollonscrollcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onDidZoom

```TypeScript
onDidZoom(event: ScrollOnDidZoomCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-onDidZoom(event: ScrollOnDidZoomCallback | undefined): this--><!--Device-ScrollAttribute-onDidZoom(event: ScrollOnDidZoomCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [ScrollOnDidZoomCallback](arkts-scrollondidzoomcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onScrollEdge

```TypeScript
onScrollEdge(event: OnScrollEdgeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-onScrollEdge(event: OnScrollEdgeCallback | undefined): this--><!--Device-ScrollAttribute-onScrollEdge(event: OnScrollEdgeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [OnScrollEdgeCallback](arkts-onscrolledgecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onScrollFrameBegin

```TypeScript
onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this--><!--Device-ScrollAttribute-onScrollFrameBegin(event: OnScrollFrameBeginCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [OnScrollFrameBeginCallback](arkts-onscrollframebegincallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onScrollStart

```TypeScript
onScrollStart(event: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-onScrollStart(event: VoidCallback | undefined): this--><!--Device-ScrollAttribute-onScrollStart(event: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onScrollStop

```TypeScript
onScrollStop(event: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-onScrollStop(event: VoidCallback | undefined): this--><!--Device-ScrollAttribute-onScrollStop(event: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onWillScroll

```TypeScript
onWillScroll(handler: ScrollOnWillScrollCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-onWillScroll(handler: ScrollOnWillScrollCallback | undefined): this--><!--Device-ScrollAttribute-onWillScroll(handler: ScrollOnWillScrollCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [ScrollOnWillScrollCallback](arkts-scrollonwillscrollcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onZoomStart

```TypeScript
onZoomStart(event: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-onZoomStart(event: VoidCallback | undefined): this--><!--Device-ScrollAttribute-onZoomStart(event: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onZoomStop

```TypeScript
onZoomStop(event: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-onZoomStop(event: VoidCallback | undefined): this--><!--Device-ScrollAttribute-onZoomStop(event: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## scrollable

```TypeScript
scrollable(value: ScrollDirection | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-scrollable(value: ScrollDirection | undefined): this--><!--Device-ScrollAttribute-scrollable(value: ScrollDirection | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScrollDirection](arkts-scroll-scrolldirection-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## scrollBar

```TypeScript
scrollBar(barState: BarState | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-scrollBar(barState: BarState | undefined): this--><!--Device-ScrollAttribute-scrollBar(barState: BarState | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| barState | [BarState](../../apis-arkui/arkts-apis/arkts-arkui-barstate-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## scrollBarColor

```TypeScript
scrollBarColor(color: Color | int | string | Resource | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-scrollBarColor(color: Color | int | string | Resource | undefined): this--><!--Device-ScrollAttribute-scrollBarColor(color: Color | int | string | Resource | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| color | [Color](../../apis-arkui/arkts-apis/arkts-arkui-color-e.md) \| int \| string \| [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## scrollBarWidth

```TypeScript
scrollBarWidth(value: double | string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-scrollBarWidth(value: double | string | undefined): this--><!--Device-ScrollAttribute-scrollBarWidth(value: double | string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## scrollBarWidth

```TypeScript
scrollBarWidth(value: Resource | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-scrollBarWidth(value: Resource | undefined): this--><!--Device-ScrollAttribute-scrollBarWidth(value: Resource | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Resource](../../apis-arkui/arkts-apis/arkts-arkui-resource-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## scrollSnap

```TypeScript
scrollSnap(value: ScrollSnapOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-scrollSnap(value: ScrollSnapOptions | undefined): this--><!--Device-ScrollAttribute-scrollSnap(value: ScrollSnapOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ScrollSnapOptions](arkts-scroll-scrollsnapoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setScrollOptions

```TypeScript
setScrollOptions(scroller?: Scroller): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-setScrollOptions(scroller?: Scroller): this--><!--Device-ScrollAttribute-setScrollOptions(scroller?: Scroller): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scroller | [Scroller](arkts-scroll-scroller-c.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## zoomScale

```TypeScript
zoomScale(scale: double | Bindable<double> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-ScrollAttribute-zoomScale(scale: double | Bindable<double> | undefined): this--><!--Device-ScrollAttribute-zoomScale(scale: double | Bindable<double> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scale | double \| [Bindable](../arkts-apis/arkts-common-bindable-i.md)&lt;double&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Called attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ScrollAttribute-default--><!--Device-ScrollAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

