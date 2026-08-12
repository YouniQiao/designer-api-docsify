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

**Substitutes:** [NavPathInfo](NavPathInfo)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigatorInterface-(value?: { target: string; type?: NavigationType }): NavigatorAttribute--><!--Device-NavigatorInterface-(value?: { target: string; type?: NavigationType }): NavigatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { target: string; type?: NavigationType } | No | Information about the page to be redirected to.<br/>target: Path of the target page to be redirected to. <br/>type: Navigation type.<br>Default value: **NavigationType.Push |

## Navigator

```TypeScript
Navigator()
```

Called when using the navigator.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 13

**Substitutes:** [NavigationAttribute](NavigationAttribute)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-NavigatorInterface-(): NavigatorAttribute--><!--Device-NavigatorInterface-(): NavigatorAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

- [NavigationType](arkts-arkui-navigator-navigationtype-e.md)
