# InterceptionShowCallback

```TypeScript
export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void
```

navigation interception callback using in willShow and didShow

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void--><!--Device-unnamed-export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| NavBar | Yes | Indicates the starting NavDestination or NavBar. \_\_\_HTML\_TAG\_USD\_0\_\_\_Value constraint:If the parameter value is navBar, the navigation home page is displayed.  |
| to | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| NavBar | Yes | Indicates the destination NavDestination or NavBar. \_\_\_HTML\_TAG\_USD\_0\_\_\_Value constraint:If the parameter value is navBar, the navigation home page is displayed.  |
| operation | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the type of stack operation.  |
| isAnimated | boolean | Yes | Indicates whether the transition is animated.  |

