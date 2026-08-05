# InterceptionShowCallback

```TypeScript
declare type InterceptionShowCallback = (from: NavDestinationContext|NavBar, to: NavDestinationContext|NavBar, operation: NavigationOperation, isAnimated: boolean) => void
```

Represents the interception callback invoked before and after page redirection.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type InterceptionShowCallback = (from: NavDestinationContext|NavBar, to: NavDestinationContext|NavBar, operation: NavigationOperation, isAnimated: boolean) => void--><!--Device-unnamed-declare type InterceptionShowCallback = (from: NavDestinationContext|NavBar, to: NavDestinationContext|NavBar, operation: NavigationOperation, isAnimated: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| NavBar | Yes | Information about the top page in the routing stack after page redirection. The value **navBar** indicates that the top page is the home page.  |
| to | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| NavBar | Yes | Information about the top page in the routing stack after page redirection. The value **navBar** indicates that the top page is the home page.  |
| operation | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Current page redirection type.  |
| isAnimated | boolean | Yes | Whether to enable the transition animation. \_\_\_HTML\_TAG\_USD\_0\_\_\_**true**: Enable the transition animation.\_\_\_HTML\_TAG\_USD\_1\_\_\_**false**: Disable the transition animation.  |

