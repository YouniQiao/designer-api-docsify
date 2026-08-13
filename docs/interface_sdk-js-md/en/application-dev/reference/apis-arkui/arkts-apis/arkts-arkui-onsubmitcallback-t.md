# OnSubmitCallback

```TypeScript
export type OnSubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void
```

Defines a TextInput callback when onSubmit. Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnSubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void--><!--Device-unnamed-export type OnSubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enterKey | [EnterKeyType](arkts-arkui-textinput-enterkeytype-e.md) | Yes | Input method Enter key type. |
| event | [SubmitEvent](arkts-arkui-textinput-submitevent-i.md) | Yes | The event submitted. |

