# SwiperAttribute

Defines the swiper attribute functions.

**Inheritance/Implementation:** SwiperAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface SwiperAttribute extends CommonMethod--><!--Device-unnamed-export declare interface SwiperAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SwiperAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of swiper.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default attributeModifier(modifier: AttributeModifier<SwiperAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-SwiperAttribute-default attributeModifier(modifier: AttributeModifier<SwiperAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md)&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | The attribute modifier of swiper. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## autoPlay

```TypeScript
default autoPlay(value: boolean | undefined): this
```

Sets whether to enable automatic playback for child component switching.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default autoPlay(value: boolean | undefined): this--><!--Device-SwiperAttribute-default autoPlay(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Whether to enable automatic playback for child component switching, default value is false, undefined means setting to default value. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## autoPlay

```TypeScript
default autoPlay(autoPlay: boolean | undefined, options: AutoPlayOptions | undefined): this
```

Set whether the subcomponent plays automatically.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default autoPlay(autoPlay: boolean | undefined, options: AutoPlayOptions | undefined): this--><!--Device-SwiperAttribute-default autoPlay(autoPlay: boolean | undefined, options: AutoPlayOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| autoPlay | boolean \| undefined | Yes | whether the subcomponent plays automatically |
| options | [AutoPlayOptions](arkts-arkui-swiper-autoplayoptions-i.md) \| undefined | Yes | autoPlay related options |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## cachedCount

```TypeScript
default cachedCount(value: int | undefined): this
```

Sets the number of child components to be preloaded(cached).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default cachedCount(value: int | undefined): this--><!--Device-SwiperAttribute-default cachedCount(value: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## cachedCount

```TypeScript
default cachedCount(count: int | undefined, isShown: boolean | undefined): this
```

Sets the number of child components to be preloaded(cached).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default cachedCount(count: int | undefined, isShown: boolean | undefined): this--><!--Device-SwiperAttribute-default cachedCount(count: int | undefined, isShown: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | int \| undefined | Yes | Number of child components to be preloaded (cached). |
| isShown | boolean \| undefined | Yes | whether to show the nodes in the cache. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the swiper. |

## cachedCount

```TypeScript
default cachedCount(count: int | undefined, options: CachedCountOptions | undefined): this
```

Sets the number of child components to be preloaded(cached).

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default cachedCount(count: int | undefined, options: CachedCountOptions | undefined): this--><!--Device-SwiperAttribute-default cachedCount(count: int | undefined, options: CachedCountOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | int \| undefined | Yes | Number of child components to be preloaded (cached). |
| options | [CachedCountOptions](arkts-arkui-swiper-cachedcountoptions-i.md) \| undefined | Yes | Options for controlling cached count behavior. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the swiper. |

## curve

```TypeScript
default curve(value: Curve | string | ICurve | undefined): this
```

Sets the animation curve Curve is an enumeration type for common curves ICurve is a curve object

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default curve(value: Curve | string | ICurve | undefined): this--><!--Device-SwiperAttribute-default curve(value: Curve | string | ICurve | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Curve](arkts-arkui-curve-e.md) \| string \| ICurve \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## customContentTransition

```TypeScript
default customContentTransition(transition: SwiperContentAnimatedTransition | undefined): this
```

Custom swiper content transition animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default customContentTransition(transition: SwiperContentAnimatedTransition | undefined): this--><!--Device-SwiperAttribute-default customContentTransition(transition: SwiperContentAnimatedTransition | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| transition | [SwiperContentAnimatedTransition](../arkts-components/arkts-arkui-swipercontentanimatedtransition-i.md) \| undefined | Yes | custom content transition animation. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the swiper. |

## disableSwipe

```TypeScript
default disableSwipe(value: boolean | undefined): this
```

Sets whether to disable the swipe feature

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default disableSwipe(value: boolean | undefined): this--><!--Device-SwiperAttribute-default disableSwipe(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## displayArrow

```TypeScript
default displayArrow(value: ArrowStyle | boolean | undefined, isHoverShow?: boolean | undefined): this
```

Set arrow is enabled, or set the arrow style.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default displayArrow(value: ArrowStyle | boolean | undefined, isHoverShow?: boolean | undefined): this--><!--Device-SwiperAttribute-default displayArrow(value: ArrowStyle | boolean | undefined, isHoverShow?: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ArrowStyle](arkts-arkui-swiper-arrowstyle-i.md) \| boolean \| undefined | Yes | arrow is displayed or set the arrow style. |
| isHoverShow | boolean \| undefined | No | arrow is display when mouse hover in indicator hotspot. |

**Return value:**

| Type | Description |
| --- | --- |
| this | return the component attribute. |

## displayCount

```TypeScript
default displayCount(value: int | string | SwiperAutoFill | ItemFillPolicy | undefined, swipeByGroup?: boolean | undefined): this
```

Sets the number of elements to display per page.

If swipeByGroup is set to true:1.All sub-items are grouped from index 0.2.The number of sub-items in each group is the value of displayCount.3.If the number of sub-items in the last group is less than displayCount,placeholder items are added to supplement the number of last group.4.Placeholder items do not display any content and are only used as placeholders.5.When turning pages, turn pages by group.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default displayCount(value: int | string | SwiperAutoFill | ItemFillPolicy | undefined, swipeByGroup?: boolean | undefined): this--><!--Device-SwiperAttribute-default displayCount(value: int | string | SwiperAutoFill | ItemFillPolicy | undefined, swipeByGroup?: boolean | undefined): this-End-->

**System capability:** 
- API version 23 and later: SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| string \| SwiperAutoFill \| ItemFillPolicy \| undefined | Yes | The number of elements to display per page.<br>**Since:** 26.0.0 |
| swipeByGroup | boolean \| undefined | No | if swipe by group. &lt;br&gt;Default value: false &lt;br&gt;true: The page is turned by group. The number of subelements in each group is the value of displayCount. false: The default page turning behavior is used. That is, pages are turned based on subelements.<br>**Since:** 23 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## displayMode

```TypeScript
default displayMode(value: SwiperDisplayMode | undefined): this
```

Called when setting the size of the swiper container on the spindle.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default displayMode(value: SwiperDisplayMode | undefined): this--><!--Device-SwiperAttribute-default displayMode(value: SwiperDisplayMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SwiperDisplayMode](arkts-arkui-swiper-swiperdisplaymode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## duration

```TypeScript
default duration(value: int | undefined): this
```

Called when the animation duration of the switch is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default duration(value: int | undefined): this--><!--Device-SwiperAttribute-default duration(value: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## effectMode

```TypeScript
default effectMode(value: EdgeEffect | undefined): this
```

Invoked when setting the sliding effect

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default effectMode(value: EdgeEffect | undefined): this--><!--Device-SwiperAttribute-default effectMode(value: EdgeEffect | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [EdgeEffect](arkts-arkui-edgeeffect-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## index

```TypeScript
default index(value: int | Bindable<int> | undefined): this
```

Called when the index value of the displayed subcomponent is set in the container.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default index(value: int | Bindable<int> | undefined): this--><!--Device-SwiperAttribute-default index(value: int | Bindable<int> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| Bindable&lt;int&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## indicator

```TypeScript
default indicator(indicator: IndicatorComponentController | DotIndicator | DigitIndicator | boolean | undefined): this
```

Use indicator component controller.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default indicator(indicator: IndicatorComponentController | DotIndicator | DigitIndicator | boolean | undefined): this--><!--Device-SwiperAttribute-default indicator(indicator: IndicatorComponentController | DotIndicator | DigitIndicator | boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| indicator | [IndicatorComponentController](../arkts-components/arkts-arkui-indicatorcomponentcontroller-c.md) \| DotIndicator \| DigitIndicator \| boolean \| undefined | Yes | the style value or show indicator of the swiper indicator. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## indicatorInteractive

```TypeScript
default indicatorInteractive(value: boolean | undefined): this
```

Setting whether the indicator is interactive.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default indicatorInteractive(value: boolean | undefined): this--><!--Device-SwiperAttribute-default indicatorInteractive(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes | Whether the indicator is interactive. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## interval

```TypeScript
default interval(value: int | undefined): this
```

Called when the time interval for automatic playback is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default interval(value: int | undefined): this--><!--Device-SwiperAttribute-default interval(value: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## itemSpace

```TypeScript
default itemSpace(value: double | string | undefined): this
```

Sets the space between child components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default itemSpace(value: double | string | undefined): this--><!--Device-SwiperAttribute-default itemSpace(value: double | string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## loop

```TypeScript
default loop(value: boolean | undefined): this
```

Called when setting whether to turn on cyclic sliding.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default loop(value: boolean | undefined): this--><!--Device-SwiperAttribute-default loop(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## maintainVisibleContentPosition

```TypeScript
default maintainVisibleContentPosition(enabled: boolean | undefined): this
```

Sets whether to keep the position of the visible content unchanged when data is inserted or deleted above or in front of the display area.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default maintainVisibleContentPosition(enabled: boolean | undefined): this--><!--Device-SwiperAttribute-default maintainVisibleContentPosition(enabled: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes | Maintaining Visible Content Positions Default value: false |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of swiper. |

## nestedScroll

```TypeScript
default nestedScroll(value: SwiperNestedScrollMode | undefined): this
```

Called to setting the nested scroll mode.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default nestedScroll(value: SwiperNestedScrollMode | undefined): this--><!--Device-SwiperAttribute-default nestedScroll(value: SwiperNestedScrollMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [SwiperNestedScrollMode](../arkts-components/arkts-arkui-swipernestedscrollmode-e.md) \| undefined | Yes | mode for nested scrolling. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the swiper. |

## nextMargin

```TypeScript
default nextMargin(value: Length | undefined, ignoreBlank?: boolean | undefined): this
```

The next margin which can be used to expose a small portion of the latter item.When the next item is empty, do not display blank space.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default nextMargin(value: Length | undefined, ignoreBlank?: boolean | undefined): this--><!--Device-SwiperAttribute-default nextMargin(value: Length | undefined, ignoreBlank?: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | The length of next margin. |
| ignoreBlank | boolean \| undefined | No | Whether to hide(ignore) the next margin on the last page in non-loop scenarios &lt;br&gt;Default value: false. |

**Return value:**

| Type | Description |
| --- | --- |
| this | The attribute of the swiper. |

## onAnimationEnd

```TypeScript
default onAnimationEnd(event: OnSwiperAnimationEndCallback | undefined): this
```

Called when the swiper animation end.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default onAnimationEnd(event: OnSwiperAnimationEndCallback | undefined): this--><!--Device-SwiperAttribute-default onAnimationEnd(event: OnSwiperAnimationEndCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [OnSwiperAnimationEndCallback](arkts-arkui-onswiperanimationendcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onAnimationStart

```TypeScript
default onAnimationStart(event: OnSwiperAnimationStartCallback | undefined): this
```

Called when the swiper animation start.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default onAnimationStart(event: OnSwiperAnimationStartCallback | undefined): this--><!--Device-SwiperAttribute-default onAnimationStart(event: OnSwiperAnimationStartCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [OnSwiperAnimationStartCallback](../arkts-components/arkts-arkui-onswiperanimationstartcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(event: Callback<int> | undefined): this
```

Called when the index value changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default onChange(event: Callback<int> | undefined): this--><!--Device-SwiperAttribute-default onChange(event: Callback<int> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onContentDidScroll

```TypeScript
default onContentDidScroll(handler: ContentDidScrollCallback | undefined): this
```

Called when the swiper content did scroll.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default onContentDidScroll(handler: ContentDidScrollCallback | undefined): this--><!--Device-SwiperAttribute-default onContentDidScroll(handler: ContentDidScrollCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [ContentDidScrollCallback](arkts-arkui-contentdidscrollcallback-t.md) \| undefined | Yes | callback of scroll, selectedIndex is the index value of the swiper content selected before animation start. index is the index value of the swiper content. position is the moving ratio of the swiper content from the start position of the swiper main axis. mainAxisLength is the swiper main axis length for calculating position. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the swiper. |

## onContentWillScroll

```TypeScript
default onContentWillScroll(handler: ContentWillScrollCallback | undefined): this
```

Called when the swiper content will scroll.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default onContentWillScroll(handler: ContentWillScrollCallback | undefined): this--><!--Device-SwiperAttribute-default onContentWillScroll(handler: ContentWillScrollCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handler | [ContentWillScrollCallback](arkts-arkui-contentwillscrollcallback-t.md) \| undefined | Yes | callback of will scroll. |

**Return value:**

| Type | Description |
| --- | --- |
| this | the attribute of the swiper. |

## onGestureSwipe

```TypeScript
default onGestureSwipe(event: OnSwiperGestureSwipeCallback | undefined): this
```

Called when the swiper swipe with the gesture.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default onGestureSwipe(event: OnSwiperGestureSwipeCallback | undefined): this--><!--Device-SwiperAttribute-default onGestureSwipe(event: OnSwiperGestureSwipeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [OnSwiperGestureSwipeCallback](../arkts-components/arkts-arkui-onswipergestureswipecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onScrollStateChanged

```TypeScript
default onScrollStateChanged(event: Callback<ScrollState> | undefined): this
```

Called when the scroll state of the swiper changed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default onScrollStateChanged(event: Callback<ScrollState> | undefined): this--><!--Device-SwiperAttribute-default onScrollStateChanged(event: Callback<ScrollState> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[ScrollState](../arkts-components/arkts-arkui-scrollstate-e.md)&gt; \| undefined | Yes | callback to notify the change of the scroll state. |

**Return value:**

| Type | Description |
| --- | --- |
| this | this |

## onSelected

```TypeScript
default onSelected(event: Callback<int> | undefined): this
```

Called when a new index becomes selected. Animation is not necessarily complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default onSelected(event: Callback<int> | undefined): this--><!--Device-SwiperAttribute-default onSelected(event: Callback<int> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | Yes | callback to notify which index has been selected |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onUnselected

```TypeScript
default onUnselected(event: Callback<int> | undefined): this
```

Called when a new index becomes unselected. Animation is not necessarily complete.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default onUnselected(event: Callback<int> | undefined): this--><!--Device-SwiperAttribute-default onUnselected(event: Callback<int> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | Yes | callback to notify which index has been unselected |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## pageFlipMode

```TypeScript
default pageFlipMode(mode: PageFlipMode | undefined): this
```

Setting page flip mode on mouse wheel event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default pageFlipMode(mode: PageFlipMode | undefined): this--><!--Device-SwiperAttribute-default pageFlipMode(mode: PageFlipMode | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [PageFlipMode](arkts-arkui-pageflipmode-e.md) \| undefined | Yes | page flip mode on mouse wheel event. The default value is PageFlipMode.CONTINUOUS. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## prevMargin

```TypeScript
default prevMargin(value: Length | undefined, ignoreBlank?: boolean | undefined): this
```

The previous margin which can be used to expose a small portion of the previous item.When the previous item is empty, do not display blank space.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default prevMargin(value: Length | undefined, ignoreBlank?: boolean | undefined): this--><!--Device-SwiperAttribute-default prevMargin(value: Length | undefined, ignoreBlank?: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes | The length of previous margin. |
| ignoreBlank | boolean \| undefined | No | Whether to hide(ignore) the previous margin on the first page in non -loop scenarios &lt;br&gt;Default value: false. |

**Return value:**

| Type | Description |
| --- | --- |
| this | The attribute of the swiper. |

## setSwiperOptions

```TypeScript
default setSwiperOptions(controller?: SwiperController): this
```

Set swiper options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default setSwiperOptions(controller?: SwiperController): this--><!--Device-SwiperAttribute-default setSwiperOptions(controller?: SwiperController): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [SwiperController](arkts-arkui-swiper-swipercontroller-c.md) | No | Swiper options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the SwiperAttribute. |

## vertical

```TypeScript
default vertical(value: boolean | undefined): this
```

Called when setting whether to slide vertically.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperAttribute-default vertical(value: boolean | undefined): this--><!--Device-SwiperAttribute-default vertical(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

