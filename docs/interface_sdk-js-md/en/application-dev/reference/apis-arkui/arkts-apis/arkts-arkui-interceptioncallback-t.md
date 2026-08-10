# InterceptionCallback

```TypeScript
export type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void
```

Navigation页面跳转前的拦截回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void--><!--Device-unnamed-export type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) \| NavBar | Yes | Navigation页面跳转前的拦截回调。 <br>取值约束:参数值为navBar，则表示跳转前的页面为Navigation首页。 |
| to | [NavPathInfo](../arkts-components/arkts-arkui-navpathinfo-c.md) \| NavBar | Yes | Navigation页面跳转前的拦截回调。 <br>取值约束:参数值为navBar，则表示跳转前的页面为Navigation首页。 |
| pathStack | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | Yes | 页面栈。 |
| operation | [NavigationOperation](../arkts-components/arkts-arkui-navigationoperation-e.md) | Yes | 当前页面跳转类型。 |
| isAnimated | boolean | Yes | 页面跳转是否有动画。 |

