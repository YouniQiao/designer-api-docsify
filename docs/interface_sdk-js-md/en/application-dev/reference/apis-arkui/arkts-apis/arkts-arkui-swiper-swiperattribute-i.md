# SwiperAttribute

Defines the swiper attribute functions.

**Inheritance/Implementation:** SwiperAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<SwiperAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of swiper.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## autoPlay

```TypeScript
default autoPlay(value: boolean | undefined): this
```

Sets whether to enable automatic playback for child component switching.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## autoPlay

```TypeScript
default autoPlay(autoPlay: boolean | undefined, options: AutoPlayOptions | undefined): this
```

Set whether the subcomponent plays automatically.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [autoPlay](#autoplay) | boolean \| undefined | Yes |
| options | [AutoPlayOptions](arkts-arkui-swiper-autoplayoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## cachedCount

```TypeScript
default cachedCount(value: int | undefined): this
```

Sets the number of child components to be preloaded(cached).

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## cachedCount

```TypeScript
default cachedCount(count: int | undefined, isShown: boolean | undefined): this
```

Sets the number of child components to be preloaded(cached).

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| count | int \| undefined | Yes |
| isShown | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## cachedCount

```TypeScript
default cachedCount(count: int | undefined, options: CachedCountOptions | undefined): this
```

Sets the number of child components to be preloaded(cached).

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| count | int \| undefined | Yes |
| options | [CachedCountOptions](arkts-arkui-swiper-cachedcountoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## curve

```TypeScript
default curve(value: Curve | string | ICurve | undefined): this
```

Sets the animation curve Curve is an enumeration type for common curves ICurve is a curve object

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Curve](arkts-arkui-curve-e.md) \| string \| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## customContentTransition

```TypeScript
default customContentTransition(transition: SwiperContentAnimatedTransition | undefined): this
```

Custom swiper content transition animation.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transition | [SwiperContentAnimatedTransition](arkts-arkui-swiper-swipercontentanimatedtransition-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## disableSwipe

```TypeScript
default disableSwipe(value: boolean | undefined): this
```

Sets whether to disable the swipe feature

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## displayArrow

```TypeScript
default displayArrow(value: ArrowStyle | boolean | undefined, isHoverShow?: boolean | undefined): this
```

Set arrow is enabled, or set the arrow style.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ArrowStyle](arkts-arkui-swiper-arrowstyle-i.md) \| boolean \| undefined | Yes |
| isHoverShow | boolean \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## displayCount

```TypeScript
default displayCount(value: int | string | SwiperAutoFill | ItemFillPolicy | undefined, swipeByGroup?: boolean | undefined): this
```

Sets the number of elements to display per page.If swipeByGroup is set to true: 1.All sub-items are grouped from index 0. 2.The number of sub-items in each group is the value of displayCount. 3.If the number of sub-items in the last group is less than displayCount, placeholder items are added to supplement the number of last group. 4.Placeholder items do not display any content and are only used as placeholders. 5.When turning pages, turn pages by group.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** 
- API version 23 and later: SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| string \| [SwiperAutoFill](arkts-arkui-swiper-swiperautofill-i.md) \| [ItemFillPolicy](arkts-arkui-itemfillpolicy-i.md) \| undefined | Yes |
| swipeByGroup | boolean \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## displayMode

```TypeScript
default displayMode(value: SwiperDisplayMode | undefined): this
```

Called when setting the size of the swiper container on the spindle.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SwiperDisplayMode](arkts-arkui-swiper-swiperdisplaymode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## duration

```TypeScript
default duration(value: int | undefined): this
```

Called when the animation duration of the switch is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## effectMode

```TypeScript
default effectMode(value: EdgeEffect | undefined): this
```

Invoked when setting the sliding effect

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [EdgeEffect](arkts-arkui-edgeeffect-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## index

```TypeScript
default index(value: int | Bindable<int> | undefined): this
```

Called when the index value of the displayed subcomponent is set in the container.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| [Bindable](arkts-arkui-common-bindable-i.md)&lt;int&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## indicator

```TypeScript
default indicator(indicator: IndicatorComponentController | DotIndicator | DigitIndicator | boolean | undefined): this
```

Use indicator component controller.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [indicator](#indicator) | [IndicatorComponentController](../arkts-components/arkts-arkui-indicatorcomponentcontroller-c.md) \| [DotIndicator](arkts-arkui-swiper-dotindicator-c.md) \| [DigitIndicator](arkts-arkui-swiper-digitindicator-c.md) \| boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## indicatorInteractive

```TypeScript
default indicatorInteractive(value: boolean | undefined): this
```

Setting whether the indicator is interactive.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## interval

```TypeScript
default interval(value: int | undefined): this
```

Called when the time interval for automatic playback is set.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | int \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## itemSpace

```TypeScript
default itemSpace(value: double | string | undefined): this
```

Sets the space between child components.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | double \| string \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## loop

```TypeScript
default loop(value: boolean | undefined): this
```

Called when setting whether to turn on cyclic sliding.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## maintainVisibleContentPosition

```TypeScript
default maintainVisibleContentPosition(enabled: boolean | undefined): this
```

Sets whether to keep the position of the visible content unchanged when data is inserted or deleted above or in front of the display area.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## nestedScroll

```TypeScript
default nestedScroll(value: SwiperNestedScrollMode | undefined): this
```

Called to setting the nested scroll mode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [SwiperNestedScrollMode](arkts-arkui-swiper-swipernestedscrollmode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## nextMargin

```TypeScript
default nextMargin(value: Length | undefined, ignoreBlank?: boolean | undefined): this
```

The next margin which can be used to expose a small portion of the latter item. When the next item is empty, do not display blank space.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |
| ignoreBlank | boolean \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onAnimationEnd

```TypeScript
default onAnimationEnd(event: OnSwiperAnimationEndCallback | undefined): this
```

Called when the swiper animation end.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [OnSwiperAnimationEndCallback](arkts-arkui-onswiperanimationendcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onAnimationStart

```TypeScript
default onAnimationStart(event: OnSwiperAnimationStartCallback | undefined): this
```

Called when the swiper animation start.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [OnSwiperAnimationStartCallback](arkts-arkui-onswiperanimationstartcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onChange

```TypeScript
default onChange(event: Callback<int> | undefined): this
```

Called when the index value changes.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onContentDidScroll

```TypeScript
default onContentDidScroll(handler: ContentDidScrollCallback | undefined): this
```

Called when the swiper content did scroll.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [ContentDidScrollCallback](arkts-arkui-contentdidscrollcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onContentWillScroll

```TypeScript
default onContentWillScroll(handler: ContentWillScrollCallback | undefined): this
```

Called when the swiper content will scroll.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [ContentWillScrollCallback](arkts-arkui-contentwillscrollcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onGestureSwipe

```TypeScript
default onGestureSwipe(event: OnSwiperGestureSwipeCallback | undefined): this
```

Called when the swiper swipe with the gesture.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [OnSwiperGestureSwipeCallback](arkts-arkui-onswipergestureswipecallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onScrollStateChanged

```TypeScript
default onScrollStateChanged(event: Callback<ScrollState> | undefined): this
```

Called when the scroll state of the swiper changed.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;[ScrollState](../arkts-components/arkts-arkui-scrollstate-e.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onSelected

```TypeScript
default onSelected(event: Callback<int> | undefined): this
```

Called when a new index becomes selected. Animation is not necessarily complete.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## onUnselected

```TypeScript
default onUnselected(event: Callback<int> | undefined): this
```

Called when a new index becomes unselected. Animation is not necessarily complete.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;int&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## pageFlipMode

```TypeScript
default pageFlipMode(mode: PageFlipMode | undefined): this
```

Setting page flip mode on mouse wheel event.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [PageFlipMode](arkts-arkui-pageflipmode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## prevMargin

```TypeScript
default prevMargin(value: Length | undefined, ignoreBlank?: boolean | undefined): this
```

The previous margin which can be used to expose a small portion of the previous item. When the previous item is empty, do not display blank space.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |
| ignoreBlank | boolean \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## setSwiperOptions

```TypeScript
default setSwiperOptions(controller?: SwiperController): this
```

Set swiper options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| controller | [SwiperController](arkts-arkui-swiper-swipercontroller-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |

## vertical

```TypeScript
default vertical(value: boolean | undefined): this
```

Called when setting whether to slide vertically.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |
