# requestAutoSave

## Modules to Import

```TypeScript
import { autoFillManager } from 'kits/@kit.AbilityKit';
```

## requestAutoSave

```TypeScript
export function requestAutoSave(context: UIContext, callback?: AutoSaveCallback): void
```

Requests to automatically save the widget data. This API uses an asynchronous callback to return the result. If the current widget does not support widget switching, you can call this API to save historical widget input data. The callback is triggered when the auto-save request is complete.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| callback | [AutoSaveCallback](arkts-ability-autofillmanager-autosavecallback-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |


## requestAutoSave

```TypeScript
export function requestAutoSave(context: UIContext, request: SaveRequest, callback?: AutoSaveCallback): void
```

Trigger an auto save request.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| request | [SaveRequest](arkts-ability-autofillrequest-saverequest-i.md) | Yes |
| callback | [AutoSaveCallback](arkts-ability-autofillmanager-autosavecallback-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
