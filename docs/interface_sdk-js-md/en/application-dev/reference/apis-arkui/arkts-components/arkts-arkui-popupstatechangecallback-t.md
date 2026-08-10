# PopupStateChangeCallback

```TypeScript
declare type PopupStateChangeCallback = (event: PopupStateChangeParam) => void
```

气泡状态变化事件回调。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-unnamed-declare type PopupStateChangeCallback = (event: PopupStateChangeParam) => void--><!--Device-unnamed-declare type PopupStateChangeCallback = (event: PopupStateChangeParam) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [PopupStateChangeParam](../arkts-apis/arkts-arkui-common-popupstatechangeparam-i.md) | Yes | 气泡当前的显示状态。 |

