# reloadAllForms

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## reloadAllForms

```TypeScript
function reloadAllForms(context: UIAbilityContext): Promise<number>
```

Reloads all widgets. Invoked in the main process of the application, this API notifies the FormExtension process to  perform batch updates of all widgets added to the current application. It can only be called within a   
[UIAbility](../../apis-ability-kit/arkts-apis/arkts-app-ability-uiability.md/arkts-app-ability-uiability.md) and uses a promise to return the result.

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-formProvider-function reloadAllForms(context: UIAbilityContext): Promise<int>--><!--Device-formProvider-function reloadAllForms(context: UIAbilityContext): Promise<int>-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [UIAbilityContext](../../apis-ability-kit/arkts-apis/arkts-ability-uiabilitycontext-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

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
  formProvider.reloadAllForms(context).then((reloadNum: number) => {
    console.info(`reloadAllForms success, reload number: ${reloadNum}`);
  }).catch((error: BusinessError) => {
    console.error(`promise error, code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```
