# NavDestinationTransitionDelegate

```TypeScript
export type NavDestinationTransitionDelegate = (operation: NavigationOperation, isEnter: boolean) => (Array<NavDestinationTransition> | undefined)
```

Delegate function for NavDestination custom animation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type NavDestinationTransitionDelegate = (operation: NavigationOperation, isEnter: boolean) => (Array<NavDestinationTransition> | undefined)--><!--Device-unnamed-export type NavDestinationTransitionDelegate = (operation: NavigationOperation, isEnter: boolean) => (Array<NavDestinationTransition> | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| operation | [NavigationOperation](../arkts-components/arkts-arkui-navigationoperation-e.md) | Yes | the operation type of current Navigation animation. |
| isEnter | boolean | Yes | whether current NavDestination will do enter-type transition. |

**Return value:**

| Type | Description |
| --- | --- |
| (Array&lt;[NavDestinationTransition](arkts-arkui-navdestination-navdestinationtransition-i.md)&gt; \| undefined) | user-set custom navDestination transitions. |

