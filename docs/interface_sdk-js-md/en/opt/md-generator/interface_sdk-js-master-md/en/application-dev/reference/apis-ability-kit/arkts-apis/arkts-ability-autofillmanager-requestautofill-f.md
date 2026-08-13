# requestAutoFill

## Modules to Import

```TypeScript
import { autoFillManager } from '@kit.AbilityKit';
```

## requestAutoFill

```TypeScript
export function requestAutoFill(context: UIContext, request: FillRequest, callback?: AutoFillCallback): void
```

Trigger an auto fill request.

**Since:** 26.0.0

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-autoFillManager-export function requestAutoFill(context: UIContext, request: FillRequest, callback?: AutoFillCallback): void--><!--Device-autoFillManager-export function requestAutoFill(context: UIContext, request: FillRequest, callback?: AutoFillCallback): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| request | [FillRequest](arkts-ability-autofillrequest-fillrequest-i-sys.md) | Yes |
| callback | [AutoFillCallback](arkts-ability-autofillmanager-autofillcallback-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
