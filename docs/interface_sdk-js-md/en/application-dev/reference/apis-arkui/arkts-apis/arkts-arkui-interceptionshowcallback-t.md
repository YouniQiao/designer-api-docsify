# InterceptionShowCallback

```TypeScript
export type InterceptionShowCallback = (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar, operation: NavigationOperation, isAnimated: boolean) => void
```

navigation interception callback using in willShow and didShow

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [NavDestinationContext](arkts-arkui-navdestination-navdestinationcontext-i.md) \| [NavBar](arkts-arkui-navbar-t.md) | Yes |
| to | [NavDestinationContext](arkts-arkui-navdestination-navdestinationcontext-i.md) \| [NavBar](arkts-arkui-navbar-t.md) | Yes |
| operation | [NavigationOperation](arkts-arkui-navigation-navigationoperation-e.md) | Yes |
| isAnimated | boolean | Yes |
