# StateChangeCallback

```TypeScript
type StateChangeCallback = (state: PiPState, reason: string) => void
```

Describe picture-in-picture stage change event callback.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-PiPWindow-type StateChangeCallback = (state: PiPState, reason: string) => void--><!--Device-PiPWindow-type StateChangeCallback = (state: PiPState, reason: string) => void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [PiPState](arkts-arkui-pipwindow-pipstate-e.md) | Yes | pip window state |
| reason | string | Yes | the reason of state change |

