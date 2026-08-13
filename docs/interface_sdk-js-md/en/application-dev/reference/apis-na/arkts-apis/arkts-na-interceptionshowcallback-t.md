# InterceptionShowCallback

```TypeScript
export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void
```

navigation interception callback using in willShow and didShow

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void--><!--Device-unnamed-export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [NavDestinationContext](arkts-na-navdestination-navdestinationcontext-i.md) \| [NavBar](arkts-na-navbar-t.md) | Yes | Indicates the starting NavDestination or NavBar. <br>Value constraint:If the parameter value is navBar, the navigation home page is displayed. |
| to | [NavDestinationContext](arkts-na-navdestination-navdestinationcontext-i.md) \| [NavBar](arkts-na-navbar-t.md) | Yes | Indicates the destination NavDestination or NavBar. <br>Value constraint:If the parameter value is navBar, the navigation home page is displayed. |
| operation | [NavigationOperation](arkts-na-navigation-navigationoperation-e.md) | Yes | Indicates the type of stack operation. |
| isAnimated | boolean | Yes | Indicates whether the transition is animated. |

