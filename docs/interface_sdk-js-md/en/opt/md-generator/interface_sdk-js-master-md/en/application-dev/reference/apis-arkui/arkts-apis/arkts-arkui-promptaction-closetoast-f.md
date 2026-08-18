# closeToast

## Modules to Import

```TypeScript
```

## closeToast

```TypeScript
function closeToast(toastId: number): void
```

Closes the specified toast. > **NOTE：**> > Directly using **closeToast** can lead to the issue of > [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain the > **PromptAction** object using the **getPromptAction** API in **UIContext** and then call the > [closeToast](arkts-arkui-arkui-uicontext-promptaction-c.md#closetoast) API through this object.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-promptAction-function closeToast(toastId: number): void--><!--Device-promptAction-function closeToast(toastId: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| toastId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [103401](../errorcode-promptAction.md#103401-toast-not-found) |
