# InterceptionShowCallback

```TypeScript
declare type InterceptionShowCallback = (from: NavDestinationContext|NavBar, to: NavDestinationContext|NavBar, operation: NavigationOperation, isAnimated: boolean) => void
```

Represents the interception callback invoked before and after page redirection.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | [NavDestinationContext](arkts-arkui-navdestinationcontext-i.md) \| [NavBar](arkts-arkui-navbar-t.md) | Yes |
| to | [NavDestinationContext](arkts-arkui-navdestinationcontext-i.md) \| [NavBar](arkts-arkui-navbar-t.md) | Yes |
| operation | [NavigationOperation](arkts-arkui-navigationoperation-e.md) | Yes |
| isAnimated | boolean | Yes |
