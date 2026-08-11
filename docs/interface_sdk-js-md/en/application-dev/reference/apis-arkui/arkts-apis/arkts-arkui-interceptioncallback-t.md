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
| from | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) \| NavBar | Yes | Indicates the info of NavDestination or NavBar. <br>Value constraint:If the parameter value is navBar, the navigation home page is displayed. |
| to | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) \| NavBar | Yes | Indicates the info of NavDestination or NavBar. <br>Value constraint:If the parameter value is navBar, the navigation home page is displayed. |
| pathStack | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | Yes | The NavPathStack of current Navigation. |
| operation | [NavigationOperation](../arkts-components/arkts-arkui-navigationoperation-e.md) | Yes | Indicates the type of navigation operation. |
| isAnimated | boolean | Yes | Indicates whether the transition is animated. |

