# PasteEventCallback

```TypeScript
declare type PasteEventCallback = (event?: PasteEvent) => void
```

粘贴完成前，触发回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-declare type PasteEventCallback = (event?: PasteEvent) => void--><!--Device-unnamed-declare type PasteEventCallback = (event?: PasteEvent) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [PasteEvent](../arkts-apis/arkts-arkui-richeditor-pasteevent-i.md) | No | 定义用户粘贴事件。省略时，不接收粘贴事件信息。 |

