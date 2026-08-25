# InterceptionCallback

```TypeScript
declare type InterceptionCallback = (from: NavPathInfo|NavBar, to: NavPathInfo|NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void
```

Defines the callback triggered before a navigation page is redirected.

**Since:** 22

**ArkTS mode:** Supports only ArkTS-Dyn, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [NavPathInfo](arkts-arkui-navpathinfo-c.md) \| [NavBar](arkts-arkui-navbar-t.md) | Yes |
| to | [NavPathInfo](arkts-arkui-navpathinfo-c.md) \| [NavBar](arkts-arkui-navbar-t.md) | Yes |
| pathStack | [NavPathStack](arkts-arkui-navpathstack-c.md) | Yes |
| operation | [NavigationOperation](arkts-arkui-navigationoperation-e.md) | Yes |
| isAnimated | boolean | Yes |
