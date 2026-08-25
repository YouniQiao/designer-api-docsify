# InterceptionCallback

```TypeScript
declare type InterceptionCallback = (from: NavPathInfo|NavBar, to: NavPathInfo|NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void
```

Navigation页面跳转前的拦截回调。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| from | [NavPathInfo](arkts-arkui-navpathinfo-c.md) \| [NavBar](arkts-arkui-navbar-t.md) | 是 |
| to | [NavPathInfo](arkts-arkui-navpathinfo-c.md) \| [NavBar](arkts-arkui-navbar-t.md) | 是 |
| pathStack | [NavPathStack](arkts-arkui-navpathstack-c.md) | 是 |
| operation | [NavigationOperation](arkts-arkui-navigationoperation-e.md) | 是 |
| isAnimated | boolean | 是 |
