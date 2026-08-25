# InterceptionCallback

```TypeScript
export type InterceptionCallback = (from: NavPathInfo | NavBar, to: NavPathInfo | NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void
```

navigation interception callback.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) \| [NavBar](arkts-arkui-navbar-t.md) | Yes |
| to | [NavPathInfo](arkts-arkui-navigation-navpathinfo-c.md) \| [NavBar](arkts-arkui-navbar-t.md) | Yes |
| pathStack | [NavPathStack](arkts-arkui-navigation-navpathstack-c.md) | Yes |
| operation | [NavigationOperation](arkts-arkui-navigation-navigationoperation-e.md) | Yes |
| isAnimated | boolean | Yes |
