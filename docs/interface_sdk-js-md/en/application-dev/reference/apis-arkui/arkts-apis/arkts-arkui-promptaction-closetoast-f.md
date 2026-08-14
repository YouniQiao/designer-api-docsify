# closeToast

## Modules to Import

```TypeScript
import { LevelMode } from 'LevelMode';
import { ImmersiveMode } from 'ImmersiveMode';
import { LevelOrder } from 'LevelOrder';
```

## closeToast

```TypeScript
function closeToast(toastId: number): void
```

Closes the specified toast. > **NOTE：**> > Directly using **closeToast** can lead to the issue of > [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). To avoid this, obtain the > **PromptAction** object using the **getPromptAction** API in **UIContext** and then call the > [closeToast](arkts-arkui-arkui-uicontext-promptaction-c.md#closeToast) API through this object.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-promptAction-function closeToast(toastId: number): void--><!--Device-promptAction-function closeToast(toastId: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| toastId | number | Yes | Toast ID returned from **openToast**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../errorcode-internal.md#100001-internal-error) | Internal error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103401](../errorcode-promptAction.md#103401-toast-not-found) | Cannot find the toast. |

