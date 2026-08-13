# InterceptionShowCallback

```TypeScript
declare type InterceptionShowCallback = (from: NavDestinationContext|NavBar, to: NavDestinationContext|NavBar, operation: NavigationOperation, isAnimated: boolean) => void
```

Navigation页面跳转前和页面跳转后的拦截回调。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type InterceptionShowCallback = (from: NavDestinationContext|NavBar, to: NavDestinationContext|NavBar, operation: NavigationOperation, isAnimated: boolean) => void--><!--Device-unnamed-declare type InterceptionShowCallback = (from: NavDestinationContext|NavBar, to: NavDestinationContext|NavBar, operation: NavigationOperation, isAnimated: boolean) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [NavDestinationContext](arkts-arkui-navdestinationcontext-i.md) \| [NavBar](arkts-arkui-navbar-t.md) | 是 |
| to | [NavDestinationContext](arkts-arkui-navdestinationcontext-i.md) \| [NavBar](arkts-arkui-navbar-t.md) | 是 |
| operation | [NavigationOperation](arkts-arkui-navigationoperation-e.md) | 是 |
| isAnimated | boolean | 是 |
