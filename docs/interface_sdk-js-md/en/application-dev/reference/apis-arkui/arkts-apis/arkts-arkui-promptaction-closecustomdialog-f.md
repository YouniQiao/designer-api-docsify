# closeCustomDialog

## Modules to Import

```TypeScript
import { LevelMode } from 'LevelMode';
import { ImmersiveMode } from 'ImmersiveMode';
import { LevelOrder } from 'LevelOrder';
```

## closeCustomDialog

```TypeScript
function closeCustomDialog(dialogId: number): void
```

Closes the specified custom dialog box. > **NOTE：**> > - This API is supported since API version 11 and deprecated since API version 18. You are advised to use closeCustomDialog instead. Before calling this API, you need to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object using the [getPromptAction](arkts-arkui-arkui-uicontext-uicontext-c.md#getPromptAction) method in [UIContext](arkts-apis-uicontext-uicontext.md). Directly using **closeCustomDialog** can lead to the issue of [ambiguous UI context](../../../ui/arkts-global-interface.md#ambiguous-ui-context). > > - Since API version 12, you can use the [getPromptAction](arkts-arkui-arkui-uicontext-uicontext-c.md#getPromptAction) API in [UIContext](arkts-apis-uicontext-uicontext.md) to obtain the [PromptAction](arkts-apis-uicontext-promptaction.md) object associated with the current UI context.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 18

**Substitutes:** closeCustomDialog

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-promptAction-function closeCustomDialog(dialogId: number): void--><!--Device-promptAction-function closeCustomDialog(dialogId: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| dialogId | number | Yes | ID of the custom dialog box to close. It is returned from **openCustomDialog**. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../errorcode-internal.md#100001-internal-error) | Internal error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |

