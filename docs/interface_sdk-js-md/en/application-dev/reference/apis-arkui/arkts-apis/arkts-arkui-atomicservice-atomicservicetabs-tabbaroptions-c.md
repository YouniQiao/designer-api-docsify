# TabBarOptions

Array of tab bar container configurations.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

<!--Device-unnamed-export declare class TabBarOptions--><!--Device-unnamed-export declare class TabBarOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { AtomicServiceTabs } from 'AtomicServiceTabs';
import { TabBarOptions } from 'TabBarOptions';
import { TabBarPosition } from 'TabBarPosition';
import { TabContentBuilder } from 'TabContentBuilder';
import { OnContentWillChangeCallback } from 'OnContentWillChangeCallback';
```

## constructor

```TypeScript
constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr,
    unselectedColor?: ResourceColor, selectedColor?: ResourceColor)
```

A constructor used to create a **TabBarOptions** instance.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-TabBarOptions-constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr,    unselectedColor?: ResourceColor, selectedColor?: ResourceColor)--><!--Device-TabBarOptions-constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr,    unselectedColor?: ResourceColor, selectedColor?: ResourceColor)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| icon | ResourceStr \| TabBarSymbol | Yes | Image for the tab. |
| text | ResourceStr | Yes | Text of the tab. |
| unselectedColor | ResourceColor | No | Color of the tab when it is not selected. <br>Default value: **#99182431 |
| selectedColor | ResourceColor | No | Color of the tab when it is selected. <br>Default value: **#FF007DFF |

