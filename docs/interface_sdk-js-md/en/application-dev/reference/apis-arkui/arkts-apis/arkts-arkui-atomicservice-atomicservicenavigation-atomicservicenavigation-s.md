# AtomicServiceNavigation

*AtomicServiceNavigation** is a component that serves as the root container of a page. By default, it includes a title bar, content area, and toolbar. The content area switches between the home page content (child components of NavDestination) and non-home page content through routing.

**Since:** 12

<!--Device-unnamed-export declare struct AtomicServiceNavigation--><!--Device-unnamed-export declare struct AtomicServiceNavigation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceNavigation, NavDestinationBuilder, MixMode, GradientAlpha, BackgroundTheme, TitleBarType, SideBarOptions, TitleOptions, GradientBackground } from '@kit.ArkUI';
```

## gradientBackground

```TypeScript
@Prop
  gradientBackground?: GradientBackground
```

The background with gradient colors of Navigation.

**Type:** [GradientBackground](arkts-arkui-atomicservice-atomicservicenavigation-gradientbackground-i.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceNavigation-@Prop  gradientBackground?: GradientBackground--><!--Device-AtomicServiceNavigation-@Prop  gradientBackground?: GradientBackground-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hideTitleBar

```TypeScript
@Prop
  hideTitleBar?: boolean
```

Hide navigation title bar.

**Type:** boolean

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-@Prop  hideTitleBar?: boolean--><!--Device-AtomicServiceNavigation-@Prop  hideTitleBar?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## menus

```TypeScript
@BuilderParam
  menus?: CustomBuilder | Array<NavigationMenuItem>
```

The layout style users defined and inserted.

**Type:** CustomBuilder \| Array&lt;NavigationMenuItem&gt;

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceNavigation-@BuilderParam  menus?: CustomBuilder | Array<NavigationMenuItem>--><!--Device-AtomicServiceNavigation-@BuilderParam  menus?: CustomBuilder | Array<NavigationMenuItem>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minContentWidth

```TypeScript
@Prop
  minContentWidth?: Dimension
```

Sets the minimum width of content.

**Type:** Dimension

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-@Prop  minContentWidth?: Dimension--><!--Device-AtomicServiceNavigation-@Prop  minContentWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
@Prop
  mode?: NavigationMode
```

Sets the mode of navigation.

**Type:** NavigationMode

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-@Prop  mode?: NavigationMode--><!--Device-AtomicServiceNavigation-@Prop  mode?: NavigationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## modeChangeCallback

```TypeScript
modeChangeCallback?: Callback<NavigationMode>
```

Trigger callback when navigation mode changes.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;NavigationMode&gt;

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-modeChangeCallback?: Callback<NavigationMode>--><!--Device-AtomicServiceNavigation-modeChangeCallback?: Callback<NavigationMode>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navBarWidth

```TypeScript
@Prop
  navBarWidth?: Length
```

Sets the width of navigation bar.

**Type:** Length

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-@Prop  navBarWidth?: Length--><!--Device-AtomicServiceNavigation-@Prop  navBarWidth?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navBarWidthRange

```TypeScript
@Prop
  navBarWidthRange?: [
    Dimension,
    Dimension
  ]
```

Sets the minimum width and the maximum width of navigation bar.

**Type:** [     Dimension,     Dimension   ]

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-@Prop  navBarWidthRange?: [    Dimension,    Dimension  ]--><!--Device-AtomicServiceNavigation-@Prop  navBarWidthRange?: [    Dimension,    Dimension  ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navDestinationBuilder

```TypeScript
@BuilderParam
  navDestinationBuilder?: NavDestinationBuilder
```

The builder of navDestination.

**Type:** [NavDestinationBuilder](arkts-arkui-navdestinationbuilder-t.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-@BuilderParam  navDestinationBuilder?: NavDestinationBuilder--><!--Device-AtomicServiceNavigation-@BuilderParam  navDestinationBuilder?: NavDestinationBuilder-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navPathStack

```TypeScript
@State
  navPathStack?: NavPathStack
```

the information of route page.Providers methods for controlling destination page in the stack.

**Type:** NavPathStack

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-@State  navPathStack?: NavPathStack--><!--Device-AtomicServiceNavigation-@State  navPathStack?: NavPathStack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## navigationContent

```TypeScript
@BuilderParam
  navigationContent?: Callback<void>
```

the content of Navigation.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-@BuilderParam  navigationContent?: Callback<void>--><!--Device-AtomicServiceNavigation-@BuilderParam  navigationContent?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sideBarContent

```TypeScript
@BuilderParam
  sideBarContent?: Callback<void>
```

Set side bar content.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceNavigation-@BuilderParam  sideBarContent?: Callback<void>--><!--Device-AtomicServiceNavigation-@BuilderParam  sideBarContent?: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sideBarOptions

```TypeScript
@Prop
  sideBarOptions?: SideBarOptions
```

Set side bar options.

**Type:** [SideBarOptions](arkts-arkui-atomicservice-atomicservicenavigation-sidebaroptions-i.md)

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceNavigation-@Prop  sideBarOptions?: SideBarOptions--><!--Device-AtomicServiceNavigation-@Prop  sideBarOptions?: SideBarOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stateChangeCallback

```TypeScript
stateChangeCallback?: Callback<boolean>
```

Trigger callback when the visibility of navigation bar change.

**Type:** [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt;

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-stateChangeCallback?: Callback<boolean>--><!--Device-AtomicServiceNavigation-stateChangeCallback?: Callback<boolean>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## title

```TypeScript
@Prop
  title?: ResourceStr
```

Sets the Navigation title.

**Type:** ResourceStr

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-@Prop  title?: ResourceStr--><!--Device-AtomicServiceNavigation-@Prop  title?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## titleOptions

```TypeScript
@Prop
  titleOptions?: TitleOptions
```

The color of Navigation's TitleBar.

**Type:** [TitleOptions](arkts-arkui-atomicservice-atomicservicenavigation-titleoptions-i.md)

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceNavigation-@Prop  titleOptions?: TitleOptions--><!--Device-AtomicServiceNavigation-@Prop  titleOptions?: TitleOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

