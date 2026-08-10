# OnPasteCallback

```TypeScript
export type OnPasteCallback = (content: string, event: PasteEvent) => void
```

粘贴回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type OnPasteCallback = (content: string, event: PasteEvent) => void--><!--Device-unnamed-export type OnPasteCallback = (content: string, event: PasteEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content | string | Yes | 粘贴的文本内容。 |
| event | [PasteEvent](../arkts-components/arkts-arkui-pasteevent-i.md) | Yes | 用户自定义的粘贴事件。 |

