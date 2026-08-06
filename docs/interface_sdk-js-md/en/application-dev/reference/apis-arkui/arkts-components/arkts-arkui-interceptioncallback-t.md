# InterceptionCallback

```TypeScript
declare type InterceptionCallback = (from: NavPathInfo|NavBar, to: NavPathInfo|NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void
```

Defines the callback triggered before a navigation page is redirected.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-unnamed-declare type InterceptionCallback = (from: NavPathInfo|NavBar, to: NavPathInfo|NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void--><!--Device-unnamed-declare type InterceptionCallback = (from: NavPathInfo|NavBar, to: NavPathInfo|NavBar, pathStack: NavPathStack, operation: NavigationOperation, isAnimated: boolean) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| NavBar | Yes | Information about the exit page. The value **navBar** indicates that the top page is the home page.  |
| to | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| NavBar | Yes | Information about the enter page. The value **navBar** indicates that the top page is the home page.  |
| pathStack | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Page stack.  |
| operation | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Current page redirection type.  |
| isAnimated | boolean | Yes | Whether to enable the transition animation. \_\_\_HTML\_TAG\_USD\_0\_\_\_**true**: Enable the transition animation.\_\_\_HTML\_TAG\_USD\_1\_\_\_**false**: Disable the transition animation.  |

