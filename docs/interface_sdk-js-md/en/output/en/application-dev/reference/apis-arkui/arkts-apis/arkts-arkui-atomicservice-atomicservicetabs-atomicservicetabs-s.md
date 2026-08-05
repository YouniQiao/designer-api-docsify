# AtomicServiceTabs

**AtomicServiceTabs** is an advanced component designed to streamline the use of the **Tabs** component by limiting customization options. It restricts the display to a maximum of five tabs, with fixed styles, positions, and sizes for the tabs.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Component

<!--Device-unnamed-/** Copyright (C) 2024 Huawei Device Co., Ltd.* Licensed under the Apache License, Version 2.0 (the "License");* you may not use this file except in compliance with the License.* You may obtain a copy of the License at** http://www.apache.org/licenses/LICENSE-2.0** Unless required by applicable law or agreed to in writing, software* distributed under the License is distributed on an "AS IS" BASIS,* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.* See the License for the specific language governing permissions and* limitations under the License.*/export declare struct AtomicServiceTabs--><!--Device-unnamed-/** Copyright (C) 2024 Huawei Device Co., Ltd.* Licensed under the Apache License, Version 2.0 (the "License");* you may not use this file except in compliance with the License.* You may obtain a copy of the License at** http://www.apache.org/licenses/LICENSE-2.0** Unless required by applicable law or agreed to in writing, software* distributed under the License is distributed on an "AS IS" BASIS,* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.* See the License for the specific language governing permissions and* limitations under the License.*/export declare struct AtomicServiceTabs-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## barBackgroundColor

```TypeScript
barBackgroundColor?: ResourceColor
```

Sets the barBackgroundColor of tabs.

**Type:** ResourceColor

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-barBackgroundColor?: ResourceColor--><!--Device-AtomicServiceTabs-barBackgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## barOverlap

```TypeScript
barOverlap?: boolean
```

set if need overlap, default value is true.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-barOverlap?: boolean--><!--Device-AtomicServiceTabs-barOverlap?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## controller

```TypeScript
controller?: TabsController
```

Provide methods for switching tabs.

**Type:** TabsController

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-controller?: TabsController--><!--Device-AtomicServiceTabs-controller?: TabsController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## index

```TypeScript
index?: number
```

Sets the index of tabs.

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-index?: number--><!--Device-AtomicServiceTabs-index?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutMode

```TypeScript
layoutMode?: LayoutMode
```

Sets the layout mode of the bottom tab bar

**Type:** LayoutMode

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-AtomicServiceTabs-layoutMode?: LayoutMode--><!--Device-AtomicServiceTabs-layoutMode?: LayoutMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onChange

```TypeScript
onChange?: Callback<number>
```

onChange callback of tabs when tabs changed.

**Type:** Callback&lt;number&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-onChange?: Callback<number>--><!--Device-AtomicServiceTabs-onChange?: Callback<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onContentWillChange

```TypeScript
onContentWillChange?: OnContentWillChangeCallback
```

onContentWillChange callback of tabs when tabbar is clicked.

**Type:** OnContentWillChangeCallback

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

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

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-onTabBarClick?: Callback<number>--><!--Device-AtomicServiceTabs-onTabBarClick?: Callback<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tabBarOptionsArray

```TypeScript
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

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-tabBarOptionsArray: [    TabBarOptions,    TabBarOptions,    TabBarOptions?,    TabBarOptions?,    TabBarOptions?  ]--><!--Device-AtomicServiceTabs-tabBarOptionsArray: [    TabBarOptions,    TabBarOptions,    TabBarOptions?,    TabBarOptions?,    TabBarOptions?  ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tabBarPosition

```TypeScript
tabBarPosition?: TabBarPosition
```

set the positions of tabbar.

**Type:** TabBarPosition

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Decorator:** @Prop

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-tabBarPosition?: TabBarPosition--><!--Device-AtomicServiceTabs-tabBarPosition?: TabBarPosition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tabContents

```TypeScript
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

**Decorator:** @BuilderParam

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-AtomicServiceTabs-tabContents?: [     TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?  ]--><!--Device-AtomicServiceTabs-tabContents?: [     TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?,    TabContentBuilder?  ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

