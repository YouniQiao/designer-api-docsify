# OnPasteCallback

```TypeScript
export type OnPasteCallback = (content: string, event: PasteEvent) => void
```

Defines a TextInput callback when onPaste. Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnPasteCallback = (content: string, event: PasteEvent) => void--><!--Device-unnamed-export type OnPasteCallback = (content: string, event: PasteEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string | Yes | The text content of the paste. |
| event | [PasteEvent](arkts-arkui-richeditor-pasteevent-i.md) | Yes | User-defined paste event. |

