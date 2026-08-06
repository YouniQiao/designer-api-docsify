# NavDestinationTransitionDelegate

```TypeScript
declare type NavDestinationTransitionDelegate =
    (operation: NavigationOperation, isEnter: boolean) => Array<NavDestinationTransition> | undefined
```

Defines the delegate function for custom transition animations of the **NavDestination** component.

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-unnamed-declare type NavDestinationTransitionDelegate =    (operation: NavigationOperation, isEnter: boolean) => Array<NavDestinationTransition> | undefined--><!--Device-unnamed-declare type NavDestinationTransitionDelegate =    (operation: NavigationOperation, isEnter: boolean) => Array<NavDestinationTransition> | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| operation | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Type of navigation operation for the current page transition.  |
| isEnter | boolean | Yes | Whether the current page is an entry page.\_\_\_HTML\_TAG\_USD\_0\_\_\_**true**: The current page is an entry page.\_\_\_HTML\_TAG\_USD\_1\_\_\_**false**: The current page is not an entry page.  |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;NavDestinationTransition&gt; \| undefined | Array of custom animations for the **NavDestination** page. If **undefined** is returned, the default system animation is used.  |

