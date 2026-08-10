# InterceptionShowCallback

```TypeScript
export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void
```

Navigation页面跳转前和页面跳转后的拦截回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void--><!--Device-unnamed-export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | [NavDestinationContext](../arkts-components/arkts-arkui-navdestinationcontext-i.md) \| NavBar | Yes | 页面跳转之前的栈顶页面信息。 <br>取值约束:参数值为navBar，则表示跳转前的页面为Navigation首页。 |
| to | [NavDestinationContext](../arkts-components/arkts-arkui-navdestinationcontext-i.md) \| NavBar | Yes | 页面跳转之后的栈顶页面信息。 <br>取值约束:参数值为navBar，则表示跳转的目标页面为Navigation首页。 |
| operation | [NavigationOperation](../arkts-components/arkts-arkui-navigationoperation-e.md) | Yes | 当前页面跳转类型。 |
| isAnimated | boolean | Yes | 页面跳转是否有动画。 <br>true：页面跳转有动画。 false：页面跳转没有动画。 |

