# InterceptionShowCallback

```TypeScript
export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void
```

Navigation页面跳转前和页面跳转后的拦截回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [NavDestinationContext](arkts-arkui-navdestination-navdestinationcontext-i.md) \| [NavBar](arkts-arkui-navbar-t.md) | 是 |
| to | [NavDestinationContext](arkts-arkui-navdestination-navdestinationcontext-i.md) \| [NavBar](arkts-arkui-navbar-t.md) | 是 |
| operation | [NavigationOperation](arkts-arkui-navigation-navigationoperation-e.md) | 是 |
| isAnimated | boolean | 是 |
