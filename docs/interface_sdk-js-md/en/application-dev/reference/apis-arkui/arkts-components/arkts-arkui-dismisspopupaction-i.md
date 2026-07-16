# DismissPopupAction

Provides information about the dismissal of the popup.

**Since:** 12

<!--Device-unnamed-declare interface DismissPopupAction--><!--Device-unnamed-declare interface DismissPopupAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dismiss

```TypeScript
dismiss: Callback<void>
```

Callback for dismissing the popup. This API is called only when the popup needs to be dismissed.

**Type:** Callback<void>

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissPopupAction-dismiss: Callback<void>--><!--Device-DismissPopupAction-dismiss: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## reason

```TypeScript
reason: DismissReason
```

Reason why the popup is dismissed.

**Type:** DismissReason

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DismissPopupAction-reason: DismissReason--><!--Device-DismissPopupAction-reason: DismissReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

