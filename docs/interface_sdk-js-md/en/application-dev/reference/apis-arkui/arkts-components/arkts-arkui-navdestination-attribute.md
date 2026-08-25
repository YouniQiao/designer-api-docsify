# NavDestination properties/events

The universal attributes are supported.In addition to the universal events, the following events are supported.

**Inheritance/Implementation:** NavDestinationAttribute extends CommonMethod<NavDestinationAttribute>

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## backButtonIcon

```TypeScript
backButtonIcon(value: ResourceStr | PixelMap | SymbolGlyphModifier)
```

Sets the icon of the back button on the title bar.

> **NOTE：**

> - This API can be called within attributeModifier since API version 12.&gt;
> - The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the
> **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or
> changing the animation effect type through the **symbolEffect** attribute.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | ResourceStr \| PixelMap \| [SymbolGlyphModifier](../arkts-apis/arkts-arkui-symbolglyphmodifier-c.md) | Yes |

## backButtonIcon

```TypeScript
backButtonIcon(icon: ResourceStr | PixelMap | SymbolGlyphModifier, accessibilityText?: ResourceStr)
```

Sets the icon and accessibility text for the back button on the title bar.

> **NOTE：**

> - This API cannot be called within attributeModifier.&gt;
> - The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the
> **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or
> changing the animation effect type through the **symbolEffect** attribute.

**Since:** 19

**ArkTS mode:** Supports only ArkTS-Dyn, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| icon | ResourceStr \| PixelMap \| [SymbolGlyphModifier](../arkts-apis/arkts-arkui-symbolglyphmodifier-c.md) | Yes |
| accessibilityText | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | No |

## bindToNestedScrollable

```TypeScript
bindToNestedScrollable(scrollInfos: Array<NestedScrollInfo>)
```

Binds the **NavDestination** component with a nested scrollable container, which can be a List, Scroll, Grid, or WaterFlow component. This way, scrolling in the scrollable container triggers the display and hide animations of the title bar and toolbar of all **NavDestination** components that are bound to it �C scrolling up triggers the hide animation, and scrolling down triggers the show animation. A single **NavDestination** component can be bound to multiple nested scrollable containers, and a single nested scrollable container can be bound to multiple **NavDestination** components. For details, see [Example 1](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#example-1-linking-the-title-bar-and-toolbar-with-scrollable-components).

> **NOTE：**

> - The connection between the scrolling actions and the animations for showing or hiding the title bar and toolbar
> of the **NavDestination** component takes effect only when the title bar or toolbar is visible.&gt;
> - If a **NavDestination** component is bound to multiple scrollable containers, scrolling in any of these
> containers triggers the display or hiding animations of the title bar and toolbar. Specifically, when any
> scrollable container reaches either the bottom or the top, the display animation for the title bar and toolbar is
> triggered without delay. As such, to ensure the optimal user experience, avoid triggering scroll events of
> multiple scrollable containers simultaneously.&gt;
> - This API can be called in attributeModifier since API version 22.

**Since:** 14

**ArkTS mode:** Supports only ArkTS-Dyn, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scrollInfos | Array&lt;[NestedScrollInfo](arkts-arkui-nestedscrollinfo-i.md)&gt; | Yes |

## bindToScrollable

```TypeScript
bindToScrollable(scrollers: Array<Scroller>)
```

Binds the **NavDestination** component with a scrollable container, which can be a List, Scroll, Grid, or WaterFlow component. This way, scrolling in the scrollable container triggers the display and hide animations of the title bar and toolbar of all **NavDestination** components that are bound to it �C scrolling up triggers the hide animation, and scrolling down triggers the show animation. A single **NavDestination** component can be bound to multiple scrollable containers, and a single scrollable container can be bound to multiple **NavDestination** components. For details, see [Example 1](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#example-1-linking-the-title-bar-and-toolbar-with-scrollable-components).

> **NOTE：**

> - The connection between the scrolling actions and the animations for showing or hiding the title bar and toolbar
> of the **NavDestination** component takes effect only when the title bar or toolbar is visible.&gt;
> - If a **NavDestination** component is bound to multiple scrollable containers, scrolling in any of these
> containers triggers the display or hiding animations of the title bar and toolbar. Specifically, when any
> scrollable container reaches either the bottom or the top, the display animation for the title bar and toolbar is
> triggered without delay. As such, to ensure the optimal user experience, avoid triggering scroll events of
> multiple scrollable containers simultaneously.&gt;
> - This API can be called in attributeModifier since API version 22.

**Since:** 14

**ArkTS mode:** Supports only ArkTS-Dyn, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scrollers | Array & lt;Scroller & gt; | Yes |

## customTransition

```TypeScript
customTransition(delegate: NavDestinationTransitionDelegate)
```

Sets a custom transition animation for the **NavDestination** component.

> **NOTE：**

> - This API cannot be called within attributeModifier.&gt;
> - If both this attribute and [systemTransition](#systemtransition) are set,
> whichever is set later takes effect.

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| delegate | [NavDestinationTransitionDelegate](arkts-arkui-navdestinationtransitiondelegate-t.md) | Yes |

## enableNavigationIndicator

```TypeScript
enableNavigationIndicator(enabled: Optional<boolean>)
```

Sets whether to show or hide the system navigation bar when entering this **NavDestination** component.

> **NOTE：**

> This attribute is effective only if the following conditions are all met:

> The actual effect of setting the system navigation bar depends on the specific device support. For details, see
> [setSpecificSystemBarEnabled](../../../reference/apis-arkui/arkts-apis-window-Window.md#setspecificsystembarenabled).

**Since:** 19

**ArkTS mode:** Supports only ArkTS-Dyn, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | Optional & lt;boolean & gt; | Yes |

## enableStatusBar

```TypeScript
enableStatusBar(enabled: Optional<boolean>, animated?: boolean)
```

Sets whether to show or hide the system status bar when entering this **NavDestination** component.

> **NOTE：**

> - This attribute is effective only if the following conditions are all met:
> 
> 1. The **NavDestination** component belongs to the application's main window page, and the main window is a
> full-screen window.
> 
> 2. The **Navigation** container containing the **NavDestination** component occupies the entire page area.
> 
> 3. The **NavDestination** component occupies the entire **Navigation** container.
> 
> 4. The type of **NavDestination** is [NavDestinationMode](arkts-arkui-navdestinationmode-e.md).STANDARD.&gt;
> - The actual effect of setting the system status bar depends on the specific device support. For details, see
> [setSpecificSystemBarEnabled](../../../reference/apis-arkui/arkts-apis-window-Window.md#setspecificsystembarenabled).

**Since:** 19

**ArkTS mode:** Supports only ArkTS-Dyn, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enabled | Optional & lt;boolean & gt; | Yes |
| animated | boolean | No |

## fullScreenOverlay

```TypeScript
fullScreenOverlay(fullScreenOverlay: Optional<boolean>)
```

Sets whether the NavDestination should cover the entire navigation container.When set to true, in split navigation mode, the page covers both the NavBar and content area, displaying in full screen overlay mode. This setting applies to all instances of this NavDestination whenever it is pushed onto the stack, unless overridden by the fullScreen option in the push operation.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [fullScreenOverlay](#fullscreenoverlay) | Optional & lt;boolean & gt; | Yes |

## hideBackButton

```TypeScript
hideBackButton(hide: Optional<boolean>)
```

Sets whether to hide the back button in the title bar.

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hide | Optional & lt;boolean & gt; | Yes |

## hideTitleBar

```TypeScript
hideTitleBar(value: boolean)
```

Specifies whether to hide the title bar.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## hideTitleBar

```TypeScript
hideTitleBar(hide: boolean, animated: boolean)
```

Specifies whether to hide the title bar. Compared with [hideTitleBar](#hidetitlebar), this API adds the capability to control whether to animate the visibility change of the title bar.

**Since:** 13

**ArkTS mode:** Supports only ArkTS-Dyn, since version 13.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hide | boolean | Yes |
| animated | boolean | Yes |

## hideToolBar

```TypeScript
hideToolBar(hide: boolean, animated?: boolean)
```

Specifies whether to hide the toolbar.

**Since:** 13

**ArkTS mode:** Supports only ArkTS-Dyn, since version 13.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hide | boolean | Yes |
| animated | boolean | No |

## ignoreLayoutSafeArea

```TypeScript
ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)
```

Ignores the layout safe area by allowing the component to extend into the non-safe areas of the screen.

> **NOTE：**

> - Prerequisites for the **ignoreLayoutSafeArea** attribute to take effect:
> 
> When **LayoutSafeAreaType.SYSTEM** is set, the component can extend into the non-safe area if its boundaries
> overlap with the non-safe area.&gt;
> - If the component extends into the non-safe area, events triggered within that area (such as click events) might
> be intercepted by the system. This allows the system to prioritize responses to system components such as the
> status bar.&gt;
> - To allow a component to extend into non-safe areas, the title bar and toolbar must be hidden or set to
> STACK mode.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array & lt;LayoutSafeAreaType & gt; | No |
| edges | Array & lt;LayoutSafeAreaEdge & gt; | No |

## menus

```TypeScript
menus(value: Array<NavigationMenuItem> | CustomBuilder)
```

Sets the menu items in the upper right corner of the page. If this attribute is not set, no menu item is displayed. When the value type is Array&lt;NavigationMenuItem&gt;, the menu shows a maximum of three icons in portrait mode and a maximum of five icons in landscape mode, with excess icons (if any) placed under the automatically generated **More** icon.

&gt; **NOTE：**

> - This API can be called within attributeModifier since API version 14.&gt;
> - The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the
> **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or
> changing the animation effect type through the **symbolEffect** attribute.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array & lt;NavigationMenuItem & gt; \ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |

## menus

```TypeScript
menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions)
```

Sets the menu items in the upper right corner of the page. If this attribute is not set, no menu item is displayed. Compared with [menus](#menus), this API adds menu options. When the value type is Array&lt;NavigationMenuItem&gt;, the menu shows a maximum of three icons in portrait mode and a maximum of five icons in landscape mode, with excess icons (if any) placed under the automatically generated **More** icon.

&gt; **NOTE：**

> - This API cannot be called within attributeModifier.&gt;
> - The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the
> **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or
> changing the animation effect type through the **symbolEffect** attribute.

**Since:** 19

**ArkTS mode:** Supports only ArkTS-Dyn, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | Array & lt;NavigationMenuItem & gt; \ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| options | [NavigationMenuOptions](arkts-arkui-navigationmenuoptions-i.md) | No |

## mode

```TypeScript
mode(value: NavDestinationMode)
```

Sets the mode of the **NavDestination** component. Dynamic modification is not supported.

> **NOTE：**

> This API can be called within attributeModifier since API version 12.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [NavDestinationMode](arkts-arkui-navdestinationmode-e.md) | Yes |

## onActive

```TypeScript
onActive(callback: Optional<Callback<NavDestinationActiveReason>>)
```

Triggered when the **NavDestination** component becomes active (on top of the stack and operable, with no special components blocking it). For details, see [Example 5](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#example-5-handling-navdestination-onactive-and-oninactive-lifecycle-events).

> **NOTE：**

> This API can be called in attributeModifier since API version 22.

**Since:** 17

**ArkTS mode:** Supports only ArkTS-Dyn, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Optional&lt;Callback&lt;[NavDestinationActiveReason](arkts-arkui-navdestinationactivereason-e.md)&gt;&gt; | Yes |

## onBackPressed

```TypeScript
onBackPressed(callback: () => boolean)
```

This callback takes effect when content exists in the navigation controller bound to the **Navigation** component. Triggered when the back button is pressed.The value **true** means that the back button logic is overridden, and **false** means that the previous page is displayed.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | () = & gt; boolean | Yes |

## onHidden

```TypeScript
onHidden(callback: Callback<VisibilityChangeReason>)
```

Triggered when the navigation destination page is hidden. Starting from API version 21, the callback includes a **VisibilityChangeReason** parameter indicating the cause of the visibility change.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[VisibilityChangeReason](arkts-arkui-visibilitychangereason-e.md)&gt; | Yes |

## onInactive

```TypeScript
onInactive(callback: Optional<Callback<NavDestinationActiveReason>>)
```

Triggered when the **NavDestination** component becomes inactive (not on top of the stack and inoperable, or on top but blocked by special components). For details, see [Example 5](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navdestination.md#example-5-handling-navdestination-onactive-and-oninactive-lifecycle-events).

> **NOTE：**

> This API can be called in attributeModifier since API version 22.

**Since:** 17

**ArkTS mode:** Supports only ArkTS-Dyn, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Optional&lt;Callback&lt;[NavDestinationActiveReason](arkts-arkui-navdestinationactivereason-e.md)&gt;&gt; | Yes |

## onNewParam

```TypeScript
onNewParam(callback: Optional<Callback<ESObject>>)
```

Triggered when a **NavDestination** page that already exists in the stack is moved to the top using launchMode.MOVE_TO_TOP_SINGLETON or launchMode.POP_TO_SINGLETON.

> **NOTE：**

> - This callback is not triggered by
> replacePath or
> replaceDestination.&gt;
> - This API can be called in attributeModifier since API version 22.

**Since:** 19

**ArkTS mode:** Supports only ArkTS-Dyn, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Optional&lt;Callback&lt;[ESObject](../../apis-default/arkts-apis/arkts-esobject-t.md)&gt;&gt; | Yes |

## onReady

```TypeScript
onReady(callback: import('../api/@ohos.base').Callback<NavDestinationContext>)
```

Triggered when the **NavDestination** component is about to build a child component.

> **NOTE：**

> This API can be called within attributeModifier since API version 20.

**Since:** 11

**ArkTS mode:** Supports only ArkTS-Dyn, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | import('../api/@ohos.base').Callback&lt;[NavDestinationContext](arkts-arkui-navdestinationcontext-i.md)&gt; | Yes |

## onRestoreState

```TypeScript
onRestoreState(callback: Optional<RestoreStateCallback>)
```

Sets custom page state restore callback.Triggered when page is reconstructed. The custom state saved by onSaveState is passed to this callback. Null is passed if no custom state was saved.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Optional&lt;[RestoreStateCallback](arkts-arkui-restorestatecallback-t.md)&gt; | Yes |

## onResult

```TypeScript
onResult(callback: Optional<Callback<ESObject>>)
```

Triggered when the **NavDestination** component returns.

> **NOTE：**

> This API can be called in attributeModifier since API version 22.

**Since:** 15

**ArkTS mode:** Supports only ArkTS-Dyn, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Optional&lt;Callback&lt;[ESObject](../../apis-default/arkts-apis/arkts-esobject-t.md)&gt;&gt; | Yes |

## onSaveState

```TypeScript
onSaveState(callback: Optional<SaveStateCallback>)
```

Sets custom page state save callback.Triggered when page becomes hidden. Save custom page state for potential restoration. The initial param used to create the page is preserved by Navigation separately. State object must be serializable.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Optional&lt;[SaveStateCallback](arkts-arkui-savestatecallback-t.md)&gt; | Yes |

## onShown

```TypeScript
onShown(callback: Callback<VisibilityChangeReason>)
```

Triggered when the navigation destination page is displayed. Starting from API version 21, the callback includes a **VisibilityChangeReason** parameter indicating the cause of the visibility change.

**Since:** 10

**ArkTS mode:** Supports only ArkTS-Dyn, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback&lt;[VisibilityChangeReason](arkts-arkui-visibilitychangereason-e.md)&gt; | Yes |

## onWillAppear

```TypeScript
onWillAppear(callback: Callback<void>)
```

Called when the **NavDestination** component is about to be mounted. The routing stack can be modified in the callback, and the modification takes effect in the current frame.

> **NOTE：**

> This API can be called within attributeModifier since API version 20.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;void & gt; | Yes |

## onWillDisappear

```TypeScript
onWillDisappear(callback: Callback<void>)
```

Called when the the **NavDestination** component is about to be unmounted (or when the transition animation, if any, is about to start).

> **NOTE：**

> This API can be called within attributeModifier since API version 20.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;void & gt; | Yes |

## onWillHide

```TypeScript
onWillHide(callback: Callback<void>)
```

Called when the **NavDestination** component is about to be hidden.

> **NOTE：**

> This API can be called within attributeModifier since API version 20.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;void & gt; | Yes |

## onWillShow

```TypeScript
onWillShow(callback: Callback<void>)
```

Called when the **NavDestination** component is about to display.

> **NOTE：**

> This API can be called within attributeModifier since API version 20.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | Callback & lt;void & gt; | Yes |

## preferredOrientation

```TypeScript
preferredOrientation(orientation: Optional<Orientation>)
```

Sets the display orientation for the **NavDestination** component. After the transition to the NavDestination, the system also switches the application's main window to the specified display orientation.

> **NOTE：**

> - This attribute is effective only if the following conditions are all met:
> 
> 1. The **NavDestination** component belongs to the application's main window page, and the main window is a
> full-screen window.
> 
> 2. The **Navigation** container containing the **NavDestination** component occupies the entire application
> page area.
> 
> 3. The type of **NavDestination** is [NavDestinationMode](arkts-arkui-navdestinationmode-e.md).STANDARD.&gt;
> - The actual effect of setting the display orientation depends on the specific device support. For details, see
> [setPreferredOrientation](../../../reference/apis-arkui/arkts-apis-window-Window.md#setpreferredorientation9-1).

**Since:** 19

**ArkTS mode:** Supports only ArkTS-Dyn, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| orientation | Optional&lt;[Orientation](arkts-arkui-orientation-t.md)&gt; | Yes |

## recoverable

```TypeScript
recoverable(recoverable: Optional<boolean>)
```

Sets whether the **NavDestination** component is recoverable. If set to recoverable, when the application process exits unexpectedly and restarts, the **NavDestination** component will be automatically re-created. To use this feature, ensure that the recoverable attribute is set for the **Navigation** component associated with the **NavDestination** component.

> **NOTE：**

> This API must be used together with the recoverable API of
> **Navigation**.

**Since:** 14

**ArkTS mode:** Supports only ArkTS-Dyn, since version 14.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [recoverable](#recoverable) | Optional & lt;boolean & gt; | Yes |

## systemBarStyle

```TypeScript
systemBarStyle(style: Optional<SystemBarStyle>)
```

Sets the style of the system status bar when this **NavDestination** page is displayed in the **Navigation** component.

> **NOTE：**

> - The setting takes effect only when the **NavDestination** component is used in conjunction with the
> **Navigation** component.&gt;
> - For other usage restrictions, see the description of systemBarStyle
> for the **Navigation** component.&gt;
> - This API can be called within attributeModifier since API version 20.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | Optional & lt;SystemBarStyle & gt; | Yes |

## systemTransition

```TypeScript
systemTransition(type: NavigationSystemTransitionType)
```

Sets the system transition animation of the **NavDestination** component. System transition animations for the title bar and content area can be configured separately.

**Since:** 14

**ArkTS mode:** Supports only ArkTS-Dyn, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [NavigationSystemTransitionType](arkts-arkui-navigationsystemtransitiontype-e.md) | Yes |

## title

```TypeScript
title(value: string | CustomBuilder | NavDestinationCommonTitle | NavDestinationCustomTitle | Resource,
          options?: NavigationTitleOptions)
```

Sets the page title. When the title string is too long: (1) If no subtitle is set, the string is scaled down, wrapped in two lines, and then clipped with an ellipsis (...) if it is still overlong. (2) If a subtitle is set, the subtitle is scaled down and then truncated with an ellipsis (...) if it is still overlong.

> **NOTE：**

> This API can be called within attributeModifier since API version 12.

**Since:** 9

**ArkTS mode:** Supports only ArkTS-Dyn, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| CustomBuilder \| [NavDestinationCommonTitle](arkts-arkui-navdestinationcommontitle-i.md) \| [NavDestinationCustomTitle](arkts-arkui-navdestinationcustomtitle-i.md) \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |
| options | [NavigationTitleOptions](../arkts-apis/arkts-arkui-navigation-navigationtitleoptions-i.md) | No |

## toolbarConfiguration

```TypeScript
toolbarConfiguration(toolbarParam: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)
```

Sets the content of the toolbar. If this API is not called, the toolbar remains hidden.

> **NOTE：**

> - This API can be called within attributeModifier since API version 20.&gt;
> - The following operations are not allowed: modifying the icon size through the **fontSize** attribute of the
> **SymbolGlyphModifier** object, changing the animation effects through the **effectStrategy** attribute, or
> changing the animation effect type through the **symbolEffect** attribute.

**Since:** 13

**ArkTS mode:** Supports only ArkTS-Dyn, since version 13.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| toolbarParam | Array & lt;ToolbarItem & gt; \ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| options | [NavigationToolbarOptions](../arkts-apis/arkts-arkui-navigation-navigationtoolbaroptions-i.md) | No |
