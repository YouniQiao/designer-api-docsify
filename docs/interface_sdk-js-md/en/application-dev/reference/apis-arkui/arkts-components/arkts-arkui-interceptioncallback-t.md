# InterceptionCallback

```TypeScript
declare type InterceptionCallback = (from: NavPathInfo|NavBar, to: NavPathInfo|NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void
```

Navigation页面跳转前的拦截回调。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-unnamed-declare type InterceptionCallback = (from: NavPathInfo|NavBar, to: NavPathInfo|NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void--><!--Device-unnamed-declare type InterceptionCallback = (from: NavPathInfo|NavBar, to: NavPathInfo|NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [NavPathInfo](arkts-arkui-navpathinfo-c.md) \| NavBar | Yes | 退场页面信息。参数值为navBar，则表示跳转前的页面为Navigation首页。 |
| to | [NavPathInfo](arkts-arkui-navpathinfo-c.md) \| NavBar | Yes | 进场页面信息。参数值为navBar，则表示跳转的目标页面为Navigation首页。 |
| pathStack | [NavPathStack](../arkts-apis/arkts-arkui-navigation-navpathstack-c.md) | Yes | 页面栈。 |
| operation | [NavigationOperation](arkts-arkui-navigationoperation-e.md) | Yes | 当前页面跳转类型。 |
| isAnimated | boolean | Yes | 页面跳转是否有动画。<br/>true：页面跳转有动画。<br/>false：页面跳转没有动画。 |

