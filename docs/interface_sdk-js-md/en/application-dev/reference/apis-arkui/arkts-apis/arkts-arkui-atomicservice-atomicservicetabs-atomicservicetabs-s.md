# AtomicServiceTabs

**AtomicServiceTabs** is an advanced component designed to streamline the use of the **Tabs** component by limiting customization options. It restricts the display to a maximum of five tabs, with fixed styles, positions, and sizes for the tabs.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare struct AtomicServiceTabs--><!--Device-unnamed-export declare struct AtomicServiceTabs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { TabBarPosition, TabBarOptions, AtomicServiceTabs, TabContentBuilder, OnContentWillChangeCallback } from '@kit.ArkUI';
```

## barBackgroundColor

```TypeScript
@Prop
  barBackgroundColor?: ResourceColor
```

Sets the barBackgroundColor of tabs.

**Type:** ResourceColor

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-@Prop  barBackgroundColor?: ResourceColor--><!--Device-AtomicServiceTabs-@Prop  barBackgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## barOverlap

```TypeScript
@Prop
  barOverlap?: boolean
```

set if need overlap, default value is true.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-@Prop  barOverlap?: boolean--><!--Device-AtomicServiceTabs-@Prop  barOverlap?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: TabsController
```

Provide methods for switching tabs.

**Type:** TabsController

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-controller?: TabsController--><!--Device-AtomicServiceTabs-controller?: TabsController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
@Prop
  index?: number
```

Sets the index of tabs.

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-@Prop  index?: number--><!--Device-AtomicServiceTabs-@Prop  index?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutMode

```TypeScript
@Prop
  layoutMode?: LayoutMode
```

Sets the layout mode of the bottom tab bar

**Type:** LayoutMode

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceTabs-@Prop  layoutMode?: LayoutMode--><!--Device-AtomicServiceTabs-@Prop  layoutMode?: LayoutMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: Callback<number>
```

onChange callback of tabs when tabs changed.

**Type:** Callback&lt;number&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-onChange?: Callback<number>--><!--Device-AtomicServiceTabs-onChange?: Callback<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onContentWillChange

```TypeScript
onContentWillChange?: OnContentWillChangeCallback
```

onContentWillChange callback of tabs when tabbar is clicked.

**Type:** [OnContentWillChangeCallback](arkts-arkui-oncontentwillchangecallback-t.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-onContentWillChange?: OnContentWillChangeCallback--><!--Device-AtomicServiceTabs-onContentWillChange?: OnContentWillChangeCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onTabBarClick

```TypeScript
onTabBarClick?: Callback<number>
```

onTabBarClick callback of tabs when tabbar is clicked.

**Type:** Callback&lt;number&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-onTabBarClick?: Callback<number>--><!--Device-AtomicServiceTabs-onTabBarClick?: Callback<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tabBarOptionsArray

```TypeScript
@Prop
  tabBarOptionsArray: [
    TabBarOptions,
    TabBarOptions,
    TabBarOptions?,
    TabBarOptions?,
    TabBarOptions?
  ]
```

The tabBar array of tabs.

**Type:** [     TabBarOptions,     TabBarOptions,     TabBarOptions?,     TabBarOptions?,     TabBarOptions?   ]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-@Prop  tabBarOptionsArray: [    TabBarOptions,    TabBarOptions,    TabBarOptions?,    TabBarOptions?,    TabBarOptions?  ]--><!--Device-AtomicServiceTabs-@Prop  tabBarOptionsArray: [    TabBarOptions,    TabBarOptions,    TabBarOptions?,    TabBarOptions?,    TabBarOptions?  ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tabBarPosition

```TypeScript
@Prop
  tabBarPosition?: TabBarPosition
```

set the positions of tabbar.

**Type:** [TabBarPosition](arkts-arkui-atomicservice-atomicservicetabs-tabbarposition-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-@Prop  tabBarPosition?: TabBarPosition--><!--Device-AtomicServiceTabs-@Prop  tabBarPosition?: TabBarPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tabContents

```TypeScript
@BuilderParam
  tabContents?: [ 
    TabContentBuilder?,
    TabContentBuilder?,
    TabContentBuilder?,
    TabContentBuilder?,
    TabContentBuilder?
  ]
```

The TabContent array of tabs.

**Type:** [      TabContentBuilder?,     TabContentBuilder?,     TabContentBuilder?,     TabContentBuilder?,     TabContentBuilder?   ]

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-@BuilderParam  tabContents?: [     TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?  ]--><!--Device-AtomicServiceTabs-@BuilderParam  tabContents?: [     TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?  ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

