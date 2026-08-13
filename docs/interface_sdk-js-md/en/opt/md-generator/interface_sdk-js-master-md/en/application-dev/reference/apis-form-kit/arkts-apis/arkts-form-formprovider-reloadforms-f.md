# reloadForms

## Modules to Import

```TypeScript
import { formProvider } from '@kit.FormKit';
```

## reloadForms

```TypeScript
function reloadForms(context: UIAbilityContext, moduleName: string, abilityName: string, formName: string): Promise<number>
```

Reloads widgets. For widgets with the same **moduleName**, **abilityName**, and **formName** of the current application, each widget has a different widget ID after being added to the home screen for multiple times. Widget providers can use this API to batch update widgets that have different IDs but share the same **moduleName**, **abilityName**, and **formName**. Invoked in the main process of the application, this API notifies the FormExtension process to perform batch updates. It can only be called within a [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility) and uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-formProvider-function reloadForms(context: UIAbilityContext, moduleName: string, abilityName: string, formName: string): Promise<int>--><!--Device-formProvider-function reloadForms(context: UIAbilityContext, moduleName: string, abilityName: string, formName: string): Promise<int>-End-->

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

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { formProvider } from '@kit.FormKit';

try {
  // Obtain the context from the component and ensure that the return value of this.getUIContext().getHostContext() is UIAbilityContext.
  let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // Replace the information with the actual widget information to be updated.
  let moduleName: string = 'entry';
  let abilityName: string = 'EntryFormAbility';
  let formName: string = 'formName';
  formProvider.reloadForms(context, moduleName, abilityName, formName).then((reloadNum: number) => {
    console.info(`reloadForms success, reload number: ${reloadNum}`);
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
