# NavDestinationTransitionDelegate

```TypeScript
declare type NavDestinationTransitionDelegate =
    (operation: NavigationOperation, isEnter: boolean) => Array<NavDestinationTransition> | undefined
```

NavDestination自定义转场动画的代理函数。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-unnamed-declare type NavDestinationTransitionDelegate =    (operation: NavigationOperation, isEnter: boolean) => Array<NavDestinationTransition> | undefined--><!--Device-unnamed-declare type NavDestinationTransitionDelegate =    (operation: NavigationOperation, isEnter: boolean) => Array<NavDestinationTransition> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| operation | [NavigationOperation](arkts-arkui-navigationoperation-e.md) | Yes | 当前页面转场的操作类型。 |
| isEnter | boolean | Yes | 当前页面是否为入场页面。<br/>true：当前页面是入场页面；false：当前页面不是入场页面。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;NavDestinationTransition&gt; \| undefined | Array of custom animations for the **NavDestination** page. If **undefined** is returned, the default system animation is used. |

