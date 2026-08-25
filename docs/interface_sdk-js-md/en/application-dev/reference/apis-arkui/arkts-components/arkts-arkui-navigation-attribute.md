# Navigation properties/events

In addition to the universal attributes, the following attributes are supported.

**Inheritance/Implementation:** NavigationAttribute extends CommonMethod<NavigationAttribute>

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## backButtonIcon

```TypeScript
backButtonIcon(value: string | PixelMap | Resource | SymbolGlyphModifier)
```

Sets the icon of the back button in the title bar.

> **NOTE：**&gt;
> The following are not allowed: modify the icon size through the **fontSize** attribute of the
> **SymbolGlyphModifier** object, change the animation effects through the **effectStrategy** attribute, or change
> the type of animation effects through the **symbolEffect** attribute.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| PixelMap \| Resource \| [SymbolGlyphModifier](../arkts-apis/arkts-arkui-symbolglyphmodifier-c.md) | Yes |

## backButtonIcon

```TypeScript
backButtonIcon(icon: string | PixelMap | Resource | SymbolGlyphModifier, accessibilityText?: ResourceStr)
```

Sets the icon and accessibility text for the back button on the title bar.

> **NOTE：**&gt;
> This API cannot be called within attributeModifier.&gt;
> The following are not allowed: modify the icon size through the **fontSize** attribute of the
> **SymbolGlyphModifier** object, change the animation effects through the **effectStrategy** attribute, or change
> the type of animation effects through the **symbolEffect** attribute.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| icon | string \| PixelMap \| Resource \| [SymbolGlyphModifier](../arkts-apis/arkts-arkui-symbolglyphmodifier-c.md) | Yes |
| accessibilityText | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) | No |

## configuration

```TypeScript
configuration(config: NavigationConfiguration)
```

Sets Navigation configuration.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [NavigationConfiguration](arkts-arkui-navigationconfiguration-i.md) | Yes |

## customNavContentTransition

```TypeScript
customNavContentTransition(delegate: (from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation)
    => NavigationAnimatedTransition | undefined)
```

Defines the callback of the custom transition animation.

> **NOTE：**&gt;
> This API can be called in attributeModifier since API version 20.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| delegate | (from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation)     = & gt; NavigationAnimatedTransition \ | undefined | Yes |

## divider

```TypeScript
divider(style: NavigationDividerStyle | null)
```

Sets the divider style in the split-column mode of the **Navigation** component.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [NavigationDividerStyle](arkts-arkui-navigationdividerstyle-i.md) \| null | Yes |

## enableDragBar

```TypeScript
enableDragBar(isEnabled: Optional<boolean>)
```

Sets whether to display a drag bar in split-column scenarios. This attribute has no effect on PCs/2-in-1 devices.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## enableModeChangeAnimation

```TypeScript
enableModeChangeAnimation(isEnabled: Optional<boolean>)
```

Sets whether to enable the animation for switching between single- and split-column modes.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## enableToolBarAdaptation

```TypeScript
enableToolBarAdaptation(enable: Optional<boolean>)
```

Sets whether to enable toolbar adaptation ([toolbarConfiguration](#toolbarconfiguration)) for the **Navigation** and **NavDestination** components. If this feature is disabled, the bottom toolbar ([toolbarConfiguration](#toolbarconfiguration)) will no longer be moved into the menu in the upper right corner of the page. This API does not apply to custom menus; using it requires defining the [menu](#menus) via the [NavigationMenuItem](arkts-arkui-navigationmenuitem-i.md) API.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## enableVisibilityLifecycleWithContentCover

```TypeScript
enableVisibilityLifecycleWithContentCover(isEnabled: Optional<boolean>)
```

Sets whether to enable the linkage between the [onShown](arkts-arkui-navdestination-attribute.md#onshown) and onHidden lifecycle callbacks of the NavDestination page and the full-modal triggering.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isEnabled | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## hideBackButton

```TypeScript
hideBackButton(value: boolean)
```

Sets whether to hide the back button in the title bar. The back button takes effect only when [titleMode](#titlemode) is set to **NavigationTitleMode.Mini**.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## hideNavBar

```TypeScript
hideNavBar(value: boolean)
```

Sets whether to hide the navigation page. If the value is set to **true**, the navigation bar, including the title bar, content area, and toolbar, will be hidden. In this case, if the navigation destination page is in the routing stack, it is moved to the top of the stack and displayed. Otherwise, a blank page is displayed.From API version 9 to API version 10, this attribute takes effect only in split-column mode. Since API version 11, this attribute takes effect in all display modes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## hideTitleBar

```TypeScript
hideTitleBar(value: boolean)
```

Specifies whether to hide the title bar.

**Since:** 8

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
hideToolBar(value: boolean)
```

Specifies whether to hide the toolbar.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## hideToolBar

```TypeScript
hideToolBar(hide: boolean, animated: boolean)
```

Specifies whether to hide the toolbar. Compared with [hideToolBar](#hidetoolbar), this API adds the capability to control whether to animate the visibility change of the toolbar.

**Since:** 13

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 13.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| hide | boolean | Yes |
| animated | boolean | Yes |

## ignoreLayoutSafeArea

```TypeScript
ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>)
```

Ignores the layout safe area by allowing the component to extend into the non-safe areas of the screen.

> **NOTE：**&gt;
> - Prerequisites for the **ignoreLayoutSafeArea** attribute to take effect:
> 
> When **LayoutSafeAreaType.SYSTEM** is set, the component can extend into the non-safe area if its boundaries
> overlap with it.&gt;
> - If the component extends into the non-safe area, events triggered within that area (such as click events) might
> be intercepted by the system. This allows the system to prioritize responses to system components such as the
> status bar.&gt;
> - To allow a component to extend into non-safe areas, the title bar and toolbar must be hidden or set to
> [STACK](arkts-arkui-barstyle-e.md) mode.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [types](../../apis-arkts/arkts-apis/arkts-arkts-util-types-c.md) | Array&lt;[LayoutSafeAreaType](arkts-arkui-layoutsafeareatype-e.md)&gt; | No |
| edges | Array&lt;[LayoutSafeAreaEdge](arkts-arkui-layoutsafeareaedge-e.md)&gt; | No |

## menus

```TypeScript
menus(value: Array<NavigationMenuItem> | CustomBuilder)
```

Sets the menu items in the upper right corner of the page. If this attribute is not set, no menu item is displayed. When the value type is Array&lt;[NavigationMenuItem](arkts-arkui-navigationmenuitem-i.md)&gt;, the menu shows a maximum of three icons in portrait mode and a maximum of five icons in landscape mode, with excess icons (if any) placed under the automatically generated **More** icon.

&gt; **NOTE：**&gt;
> The following are not allowed: modify the icon size through the **fontSize** attribute of the
> **SymbolGlyphModifier** object, change the animation effects through the **effectStrategy** attribute, or change
> the type of animation effects through the **symbolEffect** attribute.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array&lt;[NavigationMenuItem](arkts-arkui-navigationmenuitem-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |

## menus

```TypeScript
menus(items: Array<NavigationMenuItem> | CustomBuilder, options?: NavigationMenuOptions)
```

Sets the menu items in the upper right corner of the page. If this attribute is not set, no menu item is displayed. Compared with [menus](#menus), this API adds menu options. When the value type is Array&lt;[NavigationMenuItem](arkts-arkui-navigationmenuitem-i.md)&gt;, the menu shows a maximum of three icons in portrait mode and a maximum of five icons in landscape mode, with excess icons (if any) placed under the automatically generated **More** icon.

&gt; **NOTE：**&gt;
> This API cannot be called within attributeModifier.&gt;
> The following are not allowed: modify the icon size through the **fontSize** attribute of the
> **SymbolGlyphModifier** object, change the animation effects through the **effectStrategy** attribute, or change
> the type of animation effects through the **symbolEffect** attribute.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| items | Array&lt;[NavigationMenuItem](arkts-arkui-navigationmenuitem-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| options | [NavigationMenuOptions](arkts-arkui-navigationmenuoptions-i.md) | No |

## minContentWidth

```TypeScript
minContentWidth(value: Dimension)
```

Minimum width of the navigation bar content area (effective in split-column mode).

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension](../arkts-apis/arkts-arkui-dimension-t.md) | Yes |

## mode

```TypeScript
mode(value: NavigationMode)
```

Sets the display mode of the navigation page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [NavigationMode](arkts-arkui-navigationmode-e.md) | Yes |

## navBarPosition

```TypeScript
navBarPosition(value: NavBarPosition)
```

Sets the position of the navigation page. It takes effect only when [mode](#mode) is set to **NavigationMode.Auto** or **NavigationMode.Split**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [NavBarPosition](arkts-arkui-navbarposition-e.md) | Yes |

## navBarWidth

```TypeScript
navBarWidth(value: Length)
```

Set the width of the navigation page. It takes effect only when [mode](#mode) is set to **NavigationMode.Auto** or **NavigationMode.Split**.Since API version 18, this attribute supports two-way binding through [!!](../../../ui/state-management/arkts-new-binding.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes |

## navBarWidthRange

```TypeScript
navBarWidthRange(value: [Dimension, Dimension])
```

Sets the minimum and maximum widths of the navigation page (effective in split-column mode). When this API is not used, the minimum width defaults to 240 vp, and the maximum width defaults to 40% of the component width (not exceeding 432 vp). When dragging the divider changes the navigation page width, the content area will be compressed.Divider dragging range:  
| Condition| Dragging Range | | ----| ----------- | |Both **navBarWidthRange** and **minContentWidth** are set.| Range set by **navBarWidthRange** if the value set by **minContentWidth** is satisfied| |Neither **navBarWidthRange** nor **minContentWidth** is set.| Default minimum and maximum ranges of **navBarWidthRange**| |Only the **navBarWidthRange** attribute is set.| Range set by **navBarWidthRange**, where the maximum dragging range cannot exceed the default value of **minContentWidth**| |Only the **minContentWidth** attribute is set.| Default minimum and maximum ranges of **navBarWidthRange**| |Only the **navBarWidth** attribute is set.|

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [Dimension, Dimension] | Yes |

## navDestination

```TypeScript
navDestination(builder: (name: string, param: unknown) => void)
```

Creates a **NavDestination** component. The builder receives the **name** and **param** parameters for constructing the **NavDestination** component. The builder must return a single root node. The builder can have only one root node. In the builder, a layer of custom components can wrap the **NavDestination** component. However, no attributes or events can be set for these custom components. Otherwise, only blank content is displayed.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| builder | (name: string, param: unknown) = & gt; void | Yes |

## onNavBarStateChange

```TypeScript
onNavBarStateChange(callback: (isVisible: boolean) => void)
```

Callback invoked when the navigation page visibility status changes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (isVisible: boolean) = & gt; void | Yes |

## onNavigationModeChange

```TypeScript
onNavigationModeChange(callback: (mode: NavigationMode) => void)
```

Triggered when the **Navigation** component is displayed for the first time or its display mode switches between single-column and split-column.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (mode: NavigationMode) = & gt; void | Yes |

## onTitleModeChange

```TypeScript
onTitleModeChange(callback: (titleMode: NavigationTitleMode) => void)
```

Triggered when [titleMode](#titlemode) is set to **NavigationTitleMode.Free** and the title bar mode changes as content scrolls.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (titleMode: NavigationTitleMode) = & gt; void | Yes |

## recoverable

```TypeScript
recoverable(recoverable: Optional<boolean>)
```

Sets whether the **Navigation** component is recoverable. If set to recoverable, when the application process exits unexpectedly and restarts, the **Navigation** component can be automatically re-created and its routing stack restored to the state at the time of the unexpected exit.

> **NOTE：**&gt;
> 1. For this API to work properly, you must first set the universal attribute id of the
> **Navigation** component.&gt;
> 2. This API must be used together with the recoverable API of
> **NavDestination**.&gt;
> 3. Non-serializable information, such as non-serializable parameters and custom **onPop**, is discarded and
> cannot be restored during the recovery process.&gt;
> 4. If an application is terminated due to insufficient system resources after it is switched to the background,
> any page configured as recoverable will be automatically restored when the application is revived to the
> foreground. For details, see
> [UIAbility Backup and Restore](../../../application-models/ability-recover-guideline.md). For the usage example,
> see
> [Example 18: Setting Navigation as Recoverable](../../../reference/apis-arkui/arkui-ts/ts-basic-components-navigation.md#example-18-setting-navigation-as-recoverable).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [recoverable](#recoverable) | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## splitPlaceholder

```TypeScript
splitPlaceholder(placeholder: ComponentContent)
```

Sets a default placeholder page for the right column in the **Navigation** component's split-column mode. The placeholder page is for UI display only and cannot receive focus or respond to events.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| placeholder | [ComponentContent](../arkts-apis/arkts-arkui-componentcontent-c.md) | Yes |

## subTitle

```TypeScript
subTitle(value: string)
```

Sets the page subtitle.

> **NOTE：**

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [title](#title)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string | Yes |

## systemBarStyle

```TypeScript
systemBarStyle(style: Optional<SystemBarStyle>)
```

Sets the style of the system status bar when the home page of the **Navigation** component is displayed.

> **NOTE：**&gt;
> 1. Avoid using the **systemBarStyle** attribute in conjunction with the status bar style APIs in the **Window**
> module, such as
> [setWindowSystemBarProperties](../../../reference/apis-arkui/arkts-apis-window-Window.md#setwindowsystembarproperties).&gt;>
> 2. When you first set the **systemBarStyle** attribute for a **Navigation** or **NavDestination** component, the
> current status bar style is saved for potential future restoration.&gt;
> 3. **Navigation** always uses the status bar style defined by the home page (when no **NavDestination** exists in
> the routing stack) or the top **NavDestination** in the stack.&gt;
> 4. If the home page or any top **NavDestination** page has a valid **systemBarStyle** set, that style will be
> used. If no style is set, and there is a previously saved style available, the saved style will be used. If no
> style has been set or saved, no changes will be made.&gt;
> 5. In [Split](arkts-arkui-navigationmode-e.md) mode, if there is no **NavDestination** in the content area, the settings of
> the **Navigation** home page will apply. Otherwise, the settings of the top **NavDestination** page on the
> routing stack will apply.&gt;
> 6. The **systemBarStyle** attribute is effective only for the main page of the main window.&gt;
> 7. The set style will only take effect if the **Navigation** component spans the entire page. If it does not, and
> there is a previously saved style available, the saved style will be used instead.&gt;
> 8. When different styles are set for pages, the new style takes effect at the start of the page transition.&gt;
> 9. The status bar style set by **Navigation** or **NavDestination** does not apply in non-fullscreen windows.&gt;
> This API can be called in attributeModifier since API version 20.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| style | [Optional](arkts-arkui-optional-t.md)&lt;[SystemBarStyle](arkts-arkui-systembarstyle-t.md)&gt; | Yes |

## title

```TypeScript
title(value: ResourceStr | CustomBuilder | NavigationCommonTitle | NavigationCustomTitle, options?: NavigationTitleOptions)
```

Sets the page title.

> **NOTE：**&gt;
> This API can be called within attributeModifier since API version 12.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| [CustomBuilder](arkts-arkui-custombuilder-t.md) \| [NavigationCommonTitle](arkts-arkui-navigationcommontitle-i.md) \| [NavigationCustomTitle](arkts-arkui-navigationcustomtitle-i.md) | Yes |
| options | [NavigationTitleOptions](arkts-arkui-navigationtitleoptions-i.md) | No |

## titleMode

```TypeScript
titleMode(value: NavigationTitleMode)
```

Sets the display mode of the page title bar.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [NavigationTitleMode](arkts-arkui-navigationtitlemode-e.md) | Yes |

## toolBar

```TypeScript
toolBar(value: object | CustomBuilder)
```

Sets the content of the toolbar. If this attribute is not set, no toolbar is displayed. Toolbar items are evenly distributed on the bottom toolbar, with text and icons evenly spaced in each content area. If any item contains overlong text and there are fewer than five items, the toolbar will reduce the text size progressively, wrap the text over two lines if necessary, and then clip the text to fit.  
**object**

**Since:** 8

**Deprecated since:** 10

**Substitutes:** [toolbarConfiguration](#toolbarconfiguration)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | object \| [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |

## toolbarConfiguration

```TypeScript
toolbarConfiguration(value: Array<ToolbarItem> | CustomBuilder, options?: NavigationToolbarOptions)
```

Sets the content of the toolbar. If this attribute is not set, no toolbar is displayed.

> **NOTE：**&gt;
> This API can be called in attributeModifier since API version 20.&gt;
> The following are not allowed: modify the icon size through the **fontSize** attribute of the
> **SymbolGlyphModifier** object, change the animation effects through the **effectStrategy** attribute, or change
> the type of animation effects through the **symbolEffect** attribute.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | Array&lt;[ToolbarItem](arkts-arkui-toolbaritem-i.md)&gt; \| [CustomBuilder](arkts-arkui-custombuilder-t.md) | Yes |
| options | [NavigationToolbarOptions](arkts-arkui-navigationtoolbaroptions-i.md) | No |
