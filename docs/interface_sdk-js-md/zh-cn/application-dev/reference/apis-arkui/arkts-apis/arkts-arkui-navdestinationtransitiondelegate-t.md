# NavDestinationTransitionDelegate

```TypeScript
export type NavDestinationTransitionDelegate = (operation: NavigationOperation, isEnter: boolean) => (Array<NavDestinationTransition> | undefined)
```

NavDestination自定义转场动画的代理函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| operation | [NavigationOperation](../arkts-components/arkts-arkui-navigationoperation-e.md) | 是 |
| isEnter | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| (Array&lt;[NavDestinationTransition](arkts-arkui-navdestination-navdestinationtransition-i.md)&gt; \| undefined) |
