# reloadForms

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## reloadForms

```TypeScript
function reloadForms(context: UIAbilityContext, moduleName: string, abilityName: string, formName: string): Promise<number>
```

Reloads widgets. For widgets with the same **moduleName**, **abilityName**, and **formName** of the current application, each widget has a different widget ID after being added to the home screen for multiple times. Widget providers can use this API to batch update widgets that have different IDs but share the same **moduleName**, **abilityName**, and **formName**. Invoked in the main process of the application, this API notifies the FormExtension process to perform batch updates. It can only be called within a [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md) and uses a promise to return the result.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | Yes |
| moduleName | string | Yes |
| abilityName | string | Yes |
| formName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
