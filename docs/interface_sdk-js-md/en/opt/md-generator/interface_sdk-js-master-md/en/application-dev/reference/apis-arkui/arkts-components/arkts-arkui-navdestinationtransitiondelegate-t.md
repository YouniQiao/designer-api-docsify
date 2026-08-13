# NavDestinationTransitionDelegate

```TypeScript
declare type NavDestinationTransitionDelegate =
    (operation: NavigationOperation, isEnter: boolean) => Array<NavDestinationTransition> | undefined
```

Defines the delegate function for custom transition animations of the **NavDestination** component.

**Since:** 15

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-unnamed-declare type NavDestinationTransitionDelegate =    (operation: NavigationOperation, isEnter: boolean) => Array<NavDestinationTransition> | undefined--><!--Device-unnamed-declare type NavDestinationTransitionDelegate =    (operation: NavigationOperation, isEnter: boolean) => Array<NavDestinationTransition> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| operation | [NavigationOperation](arkts-arkui-navigationoperation-e.md) | Yes |
| isEnter | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[NavDestinationTransition](arkts-arkui-navdestinationtransition-i.md)&gt; \| undefined |
