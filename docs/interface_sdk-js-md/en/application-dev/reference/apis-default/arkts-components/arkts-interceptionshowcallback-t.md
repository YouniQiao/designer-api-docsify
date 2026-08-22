# InterceptionShowCallback

```TypeScript
export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void
```

navigation interception callback using in willShow and didShow

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void--><!--Device-unnamed-export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [NavDestinationContext](arkts-navdestination-navdestinationcontext-i.md) \| [NavBar](arkts-navbar-t.md) | Yes | Indicates the starting NavDestination or NavBar. <br>Value constraint:If the parameter value is navBar, the navigation home page is displayed. |
| to | [NavDestinationContext](arkts-navdestination-navdestinationcontext-i.md) \| [NavBar](arkts-navbar-t.md) | Yes | Indicates the destination NavDestination or NavBar. <br>Value constraint:If the parameter value is navBar, the navigation home page is displayed. |
| operation | [NavigationOperation](arkts-navigation-navigationoperation-e.md) | Yes | Indicates the type of stack operation. |
| isAnimated | boolean | Yes | Indicates whether the transition is animated. |

