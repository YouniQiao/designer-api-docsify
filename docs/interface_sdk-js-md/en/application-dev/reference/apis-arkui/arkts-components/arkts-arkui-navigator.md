# Navigator

The **Navigator** component provides redirection.

## Child Components

Supported

## Navigator

```TypeScript
Navigator(value?: { target: string; type?: NavigationType })
```

Called when the route jumps.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 13

**Substitutes:** <!--SUBSTITUTE_API-->NavPathInfo<!--/SUBSTITUTE_API-->

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigatorInterface-(value?: { target: string; type?: NavigationType }): NavigatorAttribute--><!--Device-NavigatorInterface-(value?: { target: string; type?: NavigationType }): NavigatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { target: string; type?: NavigationType } | No | Information about the page to be redirected to.\_\_\_HTML\_TAG\_USD\_0\_\_\_target: Path of the target page to be redirected to. \_\_\_HTML\_TAG\_USD\_1\_\_\_type: Navigation type.\_\_\_HTML\_TAG\_USD\_2\_\_\_Default value: **NavigationType.Push**  |

## Navigator

```TypeScript
Navigator()
```

Called when using the navigator.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 13

**Substitutes:** <!--SUBSTITUTE_API-->NavigationAttribute<!--/SUBSTITUTE_API-->

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigatorInterface-(): NavigatorAttribute--><!--Device-NavigatorInterface-(): NavigatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

