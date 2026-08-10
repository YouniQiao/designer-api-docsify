# OnFoldStatusChangeCallback

```TypeScript
declare type OnFoldStatusChangeCallback = (event: OnFoldStatusChangeInfo) => void
```

当折叠状态改变时触发的回调&lt;!--RP4--&gt;，仅在横屏状态下生效&lt;!--RP4End--&gt;。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type OnFoldStatusChangeCallback = (event: OnFoldStatusChangeInfo) => void--><!--Device-unnamed-declare type OnFoldStatusChangeCallback = (event: OnFoldStatusChangeInfo) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [OnFoldStatusChangeInfo](../arkts-apis/arkts-arkui-folderstack-onfoldstatuschangeinfo-i.md) | Yes | 折叠状态改变时的信息，仅在横屏状态下生效。 |

