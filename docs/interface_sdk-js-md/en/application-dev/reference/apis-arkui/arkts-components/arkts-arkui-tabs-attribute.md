# Tabs properties/events

In addition to the universal attributes, the following attributes are supported.In addition to the universal events, the following events are supported.

**Inheritance/Implementation:** TabsAttribute extends CommonMethod<TabsAttribute>

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## animationCurve

```TypeScript
animationCurve(curve: Curve | ICurve)
```

Sets the tab switching animation curve for the **Tabs** component. For details about commonly used curves, refer to the Curve enum. Custom interpolation curve objects can also be created using the APIs provided in the [interpolation calculation](../arkts-apis/arkts-curves.md) module.

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| curve | Curve \| [ICurve](../arkts-apis/arkts-arkui-curves-icurve-i.md) | Yes |

## animationDuration

```TypeScript
animationDuration(value: number)
```

Sets the duration of the tab switching animation for the **Tabs** component.If **animationCurve** is not set, **animationDuration** only controls the duration of tab switching animations triggered by tapping a tab or calling the **changeIndex** API, and page-turning animations triggered by swiping in **TabContent**, the duration is determined by the intrinsic parameters of the default curve **interpolatingSpring(-1, 1, 228, 30)**.For details about curves unaffected by **animationDuration**, see [Interpolation Calculation](../arkts-apis/arkts-curves.md). These curves include curves of type [springMotion](../arkts-apis/arkts-arkui-curves-springmotion-f.md), [responsiveSpringMotion](../arkts-apis/arkts-arkui-curves-responsivespringmotion-f.md), and [interpolatingSpring](../arkts-apis/arkts-arkui-curves-interpolatingspring-f.md).

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## animationMode

```TypeScript
animationMode(mode: Optional<AnimationMode>)
```

Sets the animation mode for tab switching initiated by clicking a specific tab or by calling the **changeIndex** API of **TabsController**.

> **NOTE：**&gt;
> This attribute cannot be called within [attributeModifier.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | Optional&lt;[AnimationMode](arkts-arkui-animationmode-e.md)&gt; | Yes |

## barBackgroundBlurStyle

```TypeScript
barBackgroundBlurStyle(value: BlurStyle)
```

Sets the background blur style of the tab bar.

> **NOTE：**&gt;
> This API can be called within attributeModifier since API version 12.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BlurStyle](arkts-arkui-blurstyle-e.md) | Yes |

## barBackgroundBlurStyle

```TypeScript
barBackgroundBlurStyle(style: BlurStyle, options: BackgroundBlurStyleOptions)
```

Defines the blur style to apply between the background and content of a tab bar. It encapsulates various blur radius, mask color, mask opacity, saturation, and brightness values through enum values.

**Since:** 18

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [BlurStyle](arkts-arkui-blurstyle-e.md) | Yes |
| options | [BackgroundBlurStyleOptions](../arkts-apis/arkts-arkui-common-backgroundblurstyleoptions-i.md) | Yes |

## barBackgroundColor

```TypeScript
barBackgroundColor(value: ResourceColor)
```

Sets the background color of the tab bar.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## barBackgroundEffect

```TypeScript
barBackgroundEffect(options: BackgroundEffectOptions)
```

Sets the background effect of the tab bar, including the blur radius, brightness, saturation, and color.

**Since:** 18

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [BackgroundEffectOptions](arkts-arkui-backgroundeffectoptions-i.md) | Yes |

## barDisplayModeBreakpoint

```TypeScript
barDisplayModeBreakpoint(style: Optional<TabsBreakpointType<TabBarDisplayMode>>)
```

Sets the display mode of the tab bar for different Tabs container sizes.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | Optional&lt;[TabsBreakpointType](arkts-arkui-tabsbreakpointtype-i.md)&lt;[TabBarDisplayMode](arkts-arkui-tabbardisplaymode-e.md)&gt;&gt; | Yes |

## barFloatingStyle

```TypeScript
barFloatingStyle(style: Optional<FloatingTabBarStyle>)
```

Enable floating style for bar.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | Optional&lt;[FloatingTabBarStyle](arkts-arkui-floatingtabbarstyle-i.md)&gt; | Yes |

## barGridAlign

```TypeScript
barGridAlign(value: BarGridColumnOptions)
```

Sets the visible area of the tab bar in grid mode. For details, see **BarGridColumnOptions**. This attribute is effective only in horizontal mode. It is not applicable to [XS, XL, and XXL devices](../../../ui/arkts-layout-development-grid-layout.md#breakpoints).

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BarGridColumnOptions](arkts-arkui-bargridcolumnoptions-i.md) | Yes |

## barHeight

```TypeScript
barHeight(value: Length)
```

Sets the height of the tab bar. For horizontal **Tabs** components, you can set the height to **'auto'** to allow the tab bar to automatically adapt to the height of its child components. If the height is set to a value less than 0 or greater than the height of the **Tabs** component, the default value is used.In versions earlier than API version 14, setting **barHeight** to a fixed value prevents the tab bar from extending beyond the bottom safe area. Since API version 14, the safeAreaPadding attribute is supported. When **safeAreaPadding** is set to 0 or is not explicitly set, the tab bar is allowed to extend beyond the bottom safe area.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

## barHeight

```TypeScript
barHeight(height: Length, noMinHeightLimit: boolean)
```

Sets the height of the tab bar. For horizontal **Tabs** components, you can set the height to **'auto'** to allow the tab bar to automatically adapt to the height of its child components; you can also set **noMinHeightLimit** to **true** so that the adaptive height can be less than the default tab bar height. If the height is set to a value less than 0 or greater than the height of the **Tabs** component, the default value is used.

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| height | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |
| noMinHeightLimit | boolean | Yes |

## barMode

```TypeScript
barMode(value: BarMode.Fixed)
```

Sets the tab bar layout mode to **BarMode.Fixed**.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BarMode.Fixed](arkts-arkui-barmode-e.md) | Yes |

## barMode

```TypeScript
barMode(value: BarMode.Scrollable, options: ScrollableBarModeOptions)
```

Sets the tab bar layout mode to **BarMode.Scrollable**.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BarMode.Scrollable](arkts-arkui-barmode-e.md) | Yes |
| options | [ScrollableBarModeOptions](arkts-arkui-scrollablebarmodeoptions-i.md) | Yes |

## barMode

```TypeScript
barMode(value: BarMode, options?: ScrollableBarModeOptions)
```

Sets the tab bar layout mode.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BarMode](arkts-arkui-barmode-e.md) | Yes |
| options | [ScrollableBarModeOptions](arkts-arkui-scrollablebarmodeoptions-i.md) | No |

## barOverlap

```TypeScript
barOverlap(value: boolean)
```

Sets whether the tab bar overlaps the **TabContent** component with a blurred background effect.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## barPosition

```TypeScript
barPosition(value: BarPosition)
```

Sets the position of the **Tabs** component.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BarPosition](arkts-arkui-barposition-e.md) | Yes |

## barStyle

```TypeScript
barStyle(style: Optional<TabBarStyle>)
```

Sets the display style of the tab bar.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | Optional&lt;[TabBarStyle](arkts-arkui-tabbarstyle-e.md)&gt; | Yes |

## barWidth

```TypeScript
barWidth(value: Length)
```

Sets the width of the tab bar. If the set value is less than 0 or greater than the width of the **Tabs** component, the default value is used.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

## cachedMaxCount

```TypeScript
cachedMaxCount(count: number, mode: TabsCacheMode)
```

Sets the maximum number of child components to cache and the caching mode. If this attribute is not set, all child components are cached by default and are not released after being cached.

**Since:** 19

**ArkTS mode:** Supports only ArkTS-Dyn, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| count | number | Yes |
| mode | [TabsCacheMode](arkts-arkui-tabscachemode-e.md) | Yes |

## customContentTransition

```TypeScript
customContentTransition(delegate: TabsCustomContentTransitionCallback)
```

Defines a custom tab page transition animation.Instructions:
1. When a custom animation is used, the default transition animation of the **Tabs** component is disabled,
and the tab pages cannot be switched by swipe gestures.
2. Setting this attribute to **undefined** disables the custom transition animation and reverts to the component's
default transition animation.
3. Currently, the custom animation cannot be interrupted.
4. Currently, the custom animation can be triggered only in two scenarios: clicking a tab and
calling the TabsController.changeIndex() API.
5. When a custom animation is used, all events except **onGestureSwipe** of the **Tabs** component are supported.
6. The triggering time of the **onChange** and **onAnimationEnd** events needs to be specified.
If the second custom animation is triggered during the execution of the first custom animation, the **onChange** and **onAnimationEnd** events of the first custom animation are triggered when the second custom animation starts.
7. When a custom animation is used, the layout mode of the page involved in the animation is changed to **Stack**.
If the **zIndex** attribute is not set for related pages, the **zIndex** values of all pages are the same. In this case, the pages are rendered in the order in which they are added to the component tree (that is, the sequence of page indexes). In light of this, to control the rendering levels of pages, set the **zIndex** attribute of the pages.
8. This attribute cannot be called within attributeModifier.

> **NOTE：**&gt;
> This API can be called in attributeModifier since API version 20.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| delegate | [TabsCustomContentTransitionCallback](arkts-arkui-tabscustomcontenttransitioncallback-t.md) | Yes |

## divider

```TypeScript
divider(value: DividerStyle | null)
```

Sets the divider between the **TabBar** and **TabContent** components.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [DividerStyle](arkts-arkui-dividerstyle-i.md) \| null | Yes |

## edgeEffect

```TypeScript
edgeEffect(edgeEffect: Optional<EdgeEffect>)
```

Sets the edge effect used when the boundary of the scrolling area is reached.

> **NOTE：**&gt;
> This API can be called within attributeModifier since API version 17.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [edgeEffect](#edgeeffect) | Optional & lt;EdgeEffect & gt; | Yes |

## fadingEdge

```TypeScript
fadingEdge(value: boolean)
```

Sets whether the tabs fade out when they exceed the container width. It is recommended that this attribute be used together with the **barBackgroundColor** attribute. If **barBackgroundColor** is not defined, the default fade effect shows a white gradient at the container's edge.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## nestedScroll

```TypeScript
nestedScroll(value: TabsNestedScrollMode | undefined)
```

Sets the nested scrolling mode of the **Tabs** component and its parent component. If this API is not called, the default nested scrolling mode is [SELF_ONLY](arkts-arkui-tabsnestedscrollmode-e.md).  
**Model constraint**: This API can be used only in the stage model.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Dyn, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TabsNestedScrollMode](arkts-arkui-tabsnestedscrollmode-e.md) \| undefined | Yes |

## onAnimationEnd

```TypeScript
onAnimationEnd(handler: OnTabsAnimationEndCallback)
```

Triggered when the tab switching animation is completed, including cases where the gesture is interrupted during animation. This event is not triggered when **animationDuration** is set to **0**, which effectively disables the animation.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnTabsAnimationEndCallback](arkts-arkui-ontabsanimationendcallback-t.md) | Yes |

## onAnimationStart

```TypeScript
onAnimationStart(handler: OnTabsAnimationStartCallback)
```

Triggered when the transition animation starts. If [animationDuration](#animationduration) is set to **0** and [scrollable](#scrollable) is set to **false**, this callback is not triggered.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnTabsAnimationStartCallback](arkts-arkui-ontabsanimationstartcallback-t.md) | Yes |

## onChange

```TypeScript
onChange(event: Callback<number>)
```

Triggered after the active tab changes.This event is triggered when any of the following occurs:
1. After completing a swipe-triggered tab switching animation.
2. After the active tab changes by calling the [changeIndex](arkts-arkui-tabscontroller-c.md#changeindex) API of [Controller](arkts-arkui-tabscontroller-c.md).
3. After the active tab changes by updating the index through the bound [state variable](../../../ui/state-management/arkts-state.md).
4. After the active tab changes by tapping a tab in the tab bar.

> **NOTE：**&gt;
> When a custom tab is used, relying solely on the **onChange** event for synchronization between tabs and swipe
> gestures may result in delayed visual updates, since it is triggered after the swipe-triggered tab switching
> animation is completed. For smooth animations, listen for the active tab index in
> [onAnimationStart](#onanimationstart) and update the tab index accordingly. For details about
> the implementation, see
> [Example 3](../../../reference/apis-arkui/arkui-ts/ts-container-tabs.md#example-3-implementing-custom-tab-switching-synchronization).

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback & lt;number & gt; | Yes |

## onContentDidScroll

```TypeScript
onContentDidScroll(handler: OnTabsContentDidScrollCallback | undefined)
```

Triggered when content in the **Tabs** component scrolls.During page scrolling, the [OnTabsContentDidScrollCallback](arkts-arkui-ontabscontentdidscrollcallback-t.md) callback is invoked for all pages in the viewport on a frame-by-frame basis. For example, when there are two pages whose subscripts are 0 and 1 in the viewport, two callbacks whose indexes are 0 and 1 are invoked in each frame.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Dyn, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnTabsContentDidScrollCallback](arkts-arkui-ontabscontentdidscrollcallback-t.md) \| undefined | Yes |

## onContentWillChange

```TypeScript
onContentWillChange(handler: OnTabsContentWillChangeCallback)
```

Triggered when a new page is about to be displayed.This event is triggered when any of the following occurs:
1. When the user swipes through the **TabContent** to switch to a new page.
2. When **TabsController.changeIndex** is called to switch to a new page.
3. When the **index** attribute is changed to switch to a new page.
4. When the user taps a tab on the tab bar to switch to a new page.
5. When the user presses the left or
right arrow key on the keyboard to switch to a new page while the tab bar has focus.

> **NOTE：**&gt;
> This API can be called in attributeModifier since API version 20.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnTabsContentWillChangeCallback](arkts-arkui-ontabscontentwillchangecallback-t.md) | Yes |

## onGestureSwipe

```TypeScript
onGestureSwipe(handler: OnTabsGestureSwipeCallback)
```

Triggered on a frame-by-frame basis during swipe gestures for tab switching.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnTabsGestureSwipeCallback](arkts-arkui-ontabsgestureswipecallback-t.md) | Yes |

## onSelected

```TypeScript
onSelected(event: Callback<number>)
```

Triggered when the selected element changes. The index of the currently selected element is returned.This event is triggered when any of the following occurs:
1. When the swipe gesture is released and the tab switching threshold is met, triggering the switching animation.
2. When the [changeIndex](arkts-arkui-tabscontroller-c.md#changeindex) API of [TabsController](arkts-arkui-tabscontroller-c.md)
is called, triggering the switching animation.
3. When the index of the active tab is changed through the bound  
[state variable](../../../ui/state-management/arkts-state.md).
4. When a tab is tapped.

> **NOTE：**&gt;
> In the **onSelected** callback, the index of the current displayed page cannot be set using **index** of
> [TabsOptions](arkts-arkui-tabsoptions-i.md), and **TabsController.changeIndex()** cannot be called.

**Since:** 18

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback & lt;number & gt; | Yes |

## onTabBarClick

```TypeScript
onTabBarClick(event: Callback<number>)
```

Triggered when a tab is clicked.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback & lt;number & gt; | Yes |

## onUnselected

```TypeScript
onUnselected(event: Callback<number>)
```

Triggered when the selected element changes. The index of the element that is about to be hidden is returned.This event is triggered when any of the following occurs:
1. When the swipe gesture is released and the tab switching threshold is met, triggering the switching animation.
2. When the [changeIndex](arkts-arkui-tabscontroller-c.md#changeindex) API of [TabsController](arkts-arkui-tabscontroller-c.md) is called, triggering the switching animation.
3. When the index of the active tab is changed through the bound [state variable](../../../ui/state-management/arkts-state.md).
4. When a tab is tapped.

**Since:** 18

**ArkTS mode:** Supports only ArkTS-Dyn, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | Callback & lt;number & gt; | Yes |

## pageFlipMode

```TypeScript
pageFlipMode(mode: Optional<PageFlipMode>)
```

Sets the mode for flipping pages using the mouse wheel.

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | Optional & lt;PageFlipMode & gt; | Yes |

## scrollable

```TypeScript
scrollable(value: boolean)
```

Sets whether the tabs are scrollable.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## sidebarHeader

```TypeScript
sidebarHeader(header: ComponentContent)
```

Sets the header content of the sidebar tab bar.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| header | [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md) | Yes |

## sidebarPosition

```TypeScript
sidebarPosition(position: Optional<BarPosition>)
```

Sets the position of the sidebar tab bar. The sidebar tab bar position is not affected by the **vertical** attribute. It is always on the start or end side of the Tabs container, regardless of the **vertical** setting.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | Optional&lt;[BarPosition](arkts-arkui-barposition-e.md)&gt; | Yes |

## sidebarSearchable

```TypeScript
sidebarSearchable(searchOptions?: TabsSidebarSearchableOptions)
```

Sets the search options for the sidebar tab bar.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchOptions | [TabsSidebarSearchableOptions](arkts-arkui-tabssidebarsearchableoptions-i.md) | No |

## vertical

```TypeScript
vertical(value: boolean)
```

Sets whether to use vertical tabs.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |
