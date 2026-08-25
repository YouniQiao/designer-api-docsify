# TabsAttribute

The TabsAttribute.

**Inheritance/Implementation:** TabsAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## animationCurve

```TypeScript
default animationCurve(curve: Curve | ICurve| undefined): this
```

Sets the animation curve

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| curve | [Curve](arkts-arkui-curve-e.md) \| [ICurve](../arkts-components/arkts-arkui-icurve-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| this |

## animationDuration

```TypeScript
default animationDuration(value: int | undefined): this
```

Sets the length of time required to complete the tab switching animation, which is initiated by clicking a specific tab or by calling the changeIndex API of TabsController.

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## animationMode

```TypeScript
default animationMode(mode: AnimationMode | undefined): this
```

Sets the animation mode for tab switching initiated by clicking a specific tab or by calling the changeIndex API of TabsController.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| mode | [AnimationMode](arkts-arkui-tabs-animationmode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<TabsAttribute> |
        AttributeModifier<CommonMethod> | undefined): this
```

Sets the attribute modifier to Tabs.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barBackgroundBlurStyle

```TypeScript
default barBackgroundBlurStyle(value: BlurStyle | undefined): this
```

Sets the background blur style of the tab bar.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barBackgroundBlurStyle

```TypeScript
default barBackgroundBlurStyle(style: BlurStyle | undefined, options: BackgroundBlurStyleOptions | undefined): this
```

Set the BlurStyle of the tab bar.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [BlurStyle](../arkts-components/arkts-arkui-blurstyle-e.md) \| undefined | Yes |
| options | [BackgroundBlurStyleOptions](../arkts-components/arkts-arkui-backgroundblurstyleoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barBackgroundColor

```TypeScript
default barBackgroundColor(value: ResourceColor | undefined): this
```

Set the background color of the tab bar.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barBackgroundEffect

```TypeScript
default barBackgroundEffect(options: BackgroundEffectOptions | undefined): this
```

Set the BackgroundEffect of the tab bar.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [BackgroundEffectOptions](../arkts-components/arkts-arkui-backgroundeffectoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barFloatingStyle

```TypeScript
default barFloatingStyle(style: FloatingTabBarStyle | undefined): this
```

Enable floating style for bar.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [FloatingTabBarStyle](arkts-arkui-tabs-floatingtabbarstyle-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barGridAlign

```TypeScript
default barGridAlign(value: BarGridColumnOptions | undefined): this
```

Sets the visible area of the tab bar in grid mode.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute is effective only in horizontal mode. It is not applicable to XS, XL, and XXL devices. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BarGridColumnOptions](arkts-arkui-tabs-bargridcolumnoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barHeight

```TypeScript
default barHeight(value: Length | undefined): this
```

Sets the height of the tab bar. Default value: When the vertical attribute of tabs is set to false, and no tabBar style is set for the tabs or a custom style is set using CustomBuilder, the default value is 56vp. When the vertical attribute of tabs is set to true, and no tabBar style is set for the tabs or a custom style is set using CustomBuilder, the default value is the height of the tabs. When the vertical attribute of tabs is set to false, and tabBar style is SubTabBarStyle, the default value is 56vp. When the vertical attribute of tabs is set to true, and tabBar style is SubTabBarStyle, the default value is the height of the tabs. When the vertical attribute of tabs is set to false, and tabBar style is BottomTabBarStyle, the default value is 48vp. When the vertical attribute of tabs is set to true, and tabBar style is BottomTabBarStyle, the default value is the height of the tabs.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barHeight

```TypeScript
default barHeight(value: Length | undefined, noMinHeightLimit: boolean| undefined): this
```

Sets the height of the tab bar. Default value: When the vertical attribute of tabs is set to false, and no tabBar style is set for the tabs or a custom style is set using CustomBuilder, the default value is 56vp. When the vertical attribute of tabs is set to true, and no tabBar style is set for the tabs or a custom style is set using CustomBuilder, the default value is the height of the tabs. When the vertical attribute of tabs is set to false, and tabBar style is SubTabBarStyle, the default value is 56vp. When the vertical attribute of tabs is set to true, and tabBar style is SubTabBarStyle, the default value is the height of the tabs. When the vertical attribute of tabs is set to false, and tabBar style is BottomTabBarStyle, the default value is 48vp. When the vertical attribute of tabs is set to true, and tabBar style is BottomTabBarStyle, the default value is the height of the tabs.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |
| noMinHeightLimit | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barMode

```TypeScript
default barMode(value: BarMode | undefined, options?: ScrollableBarModeOptions | undefined): this
```

Sets the tab bar layout mode.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BarMode](arkts-arkui-tabs-barmode-e.md) \| undefined | Yes |
| options | [ScrollableBarModeOptions](arkts-arkui-tabs-scrollablebarmodeoptions-i.md) \| undefined | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barOverlap

```TypeScript
default barOverlap(value: boolean | undefined): this
```

Sets whether the tab bar is superimposed on the TabContent component after having its background blurred.

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barPosition

```TypeScript
default barPosition(value: BarPosition | undefined): this
```

Sets the position of the Tabs component.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BarPosition](arkts-arkui-tabs-barposition-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## barWidth

```TypeScript
default barWidth(value: Length | undefined): this
```

Sets the width of the tab bar.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](arkts-arkui-length-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## cachedMaxCount

```TypeScript
default cachedMaxCount(count: int | undefined, mode: TabsCacheMode | undefined): this
```

Sets the maximum number of child components to be cached.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| count | int \| undefined | Yes |
| mode | [TabsCacheMode](arkts-arkui-tabs-tabscachemode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## customContentTransition

```TypeScript
default customContentTransition(delegate: TabsCustomContentTransitionCallback | undefined): this
```

Custom tab content transition animation. When undefined is set, this interface does not take effect. Anonymous Object Rectification<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Instructions: <br>1. When the custom tab switching animation is used, the default switching animation of the Tabs component is disabled, and tabs cannot be switched through swiping. <br>2. The value undefined means not to use the custom tab switching animation, in which case the default switching animation is used. <br>3. The custom tab switching animation cannot be interrupted. <br>4. Currently, the custom tab switching animation can be triggered only by clicking a tab or by calling the TabsController.changeIndex() API. <br>5. When the custom tab switching animation is used, the Tabs component supports all events except onGestureSwipe. <br>6. Notes about the onChange and onAnimationEnd events: If the second custom animation is triggered during the execution of the first custom animation, the onChange and onAnimationEnd events of the first custom animation will be triggered when the second custom animation starts. <br>7. When the custom animation is used, the stack layout is used for pages involved in the animation. If the zIndex attribute is not set for related pages, the zIndex values of all pages are the same. In this case, the pages are rendered in the order in which they are added to the component tree(that is, the sequence of page indexes). In light of this, to control the rendering levels of pages, set the zIndex attribute of the pages. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| delegate | [TabsCustomContentTransitionCallback](arkts-arkui-tabscustomcontenttransitioncallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## divider

```TypeScript
default divider(value: DividerStyle | null | undefined): this
```

Set the divider between tab bar and tab content.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | DividerStyle \| null \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## edgeEffect

```TypeScript
default edgeEffect(edgeEffect: EdgeEffect | undefined): this
```

Sets the edge effect used when the boundary of the scrolling area is reached.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [edgeEffect](#edgeeffect) | [EdgeEffect](arkts-arkui-edgeeffect-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## fadingEdge

```TypeScript
default fadingEdge(value: boolean | undefined): this
```

Sets whether the tab fades out when it exceeds the container width.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>It is recommended that this attribute be used together with the barBackgroundColor attribute. If the barBackgroundColor attribute is not defined, the tab fades out in white when it exceeds the container width by default. </p>

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## nestedScroll

```TypeScript
default nestedScroll(value: TabsNestedScrollMode | undefined): this
```

Sets the nested scrolling mode of the tabs component and its parent container.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [TabsNestedScrollMode](arkts-arkui-tabs-tabsnestedscrollmode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onAnimationEnd

```TypeScript
default onAnimationEnd(handler: OnTabsAnimationEndCallback | undefined): this
```

Triggered when the tab switching animation ends. Anonymous Object Rectification

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnTabsAnimationEndCallback](arkts-arkui-ontabsanimationendcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onAnimationStart

```TypeScript
default onAnimationStart(handler: OnTabsAnimationStartCallback | undefined): this
```

Triggered when the tab switching animation starts. Anonymous Object Rectification

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnTabsAnimationStartCallback](arkts-arkui-ontabsanimationstartcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onChange

```TypeScript
default onChange(event: Callback<int> | undefined): this
```

Triggered when a tab is switched. Anonymous Object Rectification<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This event is triggered when any of the following conditions is met:
1. The swiping animation is completed, followed by tab switching.
2. The Controller API is called.
3. The attribute value is updated using a state variable.
4. A tab is clicked.
</p>

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onContentDidScroll

```TypeScript
default onContentDidScroll(handler: OnTabsContentDidScrollCallback | undefined): this
```

Triggered when scrolling content within the Tabs component.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>During page scrolling, the OnTabsContentDidScrollCallback callback is invoked for all pages in the viewport on a frame-by-frame basis. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnTabsContentDidScrollCallback](arkts-arkui-ontabscontentdidscrollcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| this |

## onContentWillChange

```TypeScript
default onContentWillChange(handler: OnTabsContentWillChangeCallback | undefined): this
```

Triggered when a new page is about to be displayed. Anonymous Object Rectification<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This event is triggered when any of the following conditions is met:
1. When the user swipes on the TabContent component (provided that it supports swiping) to switch to a new page.
2. When TabsController.changeIndex is called to switch to a new page.
3. When the **index** attribute is changed to switch to a new page.
4. When the user clicks a tab on the tab bar to switch to a new page.
5. When the user presses the left or right arrow key on the keyboard to switch to a new page
while the tab bar is focused. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnTabsContentWillChangeCallback](arkts-arkui-ontabscontentwillchangecallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onGestureSwipe

```TypeScript
default onGestureSwipe(handler: OnTabsGestureSwipeCallback | undefined): this
```

Triggered on a frame-by-frame basis when the tab is switched by a swipe. Anonymous Object Rectification

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| handler | [OnTabsGestureSwipeCallback](arkts-arkui-ontabsgestureswipecallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onSelected

```TypeScript
default onSelected(event: Callback<int> | undefined): this
```

Called when a new tab becomes selected. Animation is not necessarily complete.

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onTabBarClick

```TypeScript
default onTabBarClick(event: Callback<int> | undefined): this
```

Triggered when a tab is clicked. Anonymous Object Rectification

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## onUnselected

```TypeScript
default onUnselected(event: Callback<int> | undefined): this
```

Called when a new tab becomes unselected. Animation is not necessarily complete.

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## scrollable

```TypeScript
default scrollable(value: boolean | undefined): this
```

Sets whether the tabs are scrollable.

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## setTabsOptions

```TypeScript
default setTabsOptions(options?: TabsOptions): this
```

Set tabs options.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [TabsOptions](arkts-arkui-tabs-tabsoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |

## vertical

```TypeScript
default vertical(value: boolean | undefined): this
```

Sets whether to use vertical tabs.

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
| [TabsAttribute](arkts-arkui-tabs-tabsattribute-i.md) |
