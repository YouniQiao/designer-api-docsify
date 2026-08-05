# InterceptionCallback

```TypeScript
export type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void
```

navigation interception callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void--><!--Device-unnamed-export type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| NavBar | Yes | Indicates the info of NavDestination or NavBar. \_\_\_HTML\_TAG\_USD\_0\_\_\_Value constraint:If the parameter value is navBar, the navigation home page is displayed.  |
| to | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| NavBar | Yes | Indicates the info of NavDestination or NavBar. \_\_\_HTML\_TAG\_USD\_0\_\_\_Value constraint:If the parameter value is navBar, the navigation home page is displayed.  |
| pathStack | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The NavPathStack of current Navigation.  |
| operation | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the type of navigation operation.  |
| isAnimated | boolean | Yes | Indicates whether the transition is animated.  |

