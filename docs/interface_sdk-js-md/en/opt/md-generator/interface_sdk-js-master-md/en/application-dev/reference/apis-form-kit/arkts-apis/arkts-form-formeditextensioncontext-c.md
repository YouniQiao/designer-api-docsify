# FormEditExtensionContext

**FormEditExtensionContext**, inherited from   
[UIExtensionContext](./application/UIExtensionContext:UIExtensionContext), is the context of   
[FormEditExtensionAbility](arkts-form-app-form-formeditextensionability-formeditextensionability-c.md#FormEditExtensionAbility).

> **NOTE：**

> - The APIs of this module can be used only in the stage model.

**Inheritance/Implementation:** FormEditExtensionContext extends [UIExtensionContext](UIExtensionContext)

**Since:** 18

<!--Device-unnamed-declare class FormEditExtensionContext extends UIExtensionContext--><!--Device-unnamed-declare class FormEditExtensionContext extends UIExtensionContext-End-->

**System capability:** SystemCapability.Ability.Form

## startSecondPage

```TypeScript
startSecondPage(want: Want): Promise<AbilityResult>
```

Starts the widget provider page to be edited. This API uses a promise to return the result.

**Since:** 18

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormEditExtensionContext-startSecondPage(want: Want): Promise<AbilityResult>--><!--Device-FormEditExtensionContext-startSecondPage(want: Want): Promise<AbilityResult>-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[AbilityResult](../../apis-ability-kit/arkts-apis/arkts-ability-abilityresult-abilityresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) |
| [16500050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |

## startUIAbility

```TypeScript
startUIAbility(want: Want): Promise<void>
```

Starts UIAbility of the application to which a widget belongs. This API uses a promise to return the result.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormEditExtensionContext-startUIAbility(want: Want): Promise<void>--><!--Device-FormEditExtensionContext-startUIAbility(want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16000130](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000130-uiability-does-not-belong-to-the-caller) |
| [16500050](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500050-ipc-failure) |
| [16501014](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501014-semimodal-widget-editing-page-not-in-foreground) |
| [16000121](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ability-kit/errorcode-ability.md#16000121-target-component-is-not-a-uiability) |
| [16500100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |

## Examples

```TypeScript
import { FormEditExtensionAbility } from '@kit.FormKit'
import { Want, UIExtensionContentSession } from '@kit.AbilityKit';

const TAG: string = '[testTag] ExampleFormEditExtensionAbility'

export default class ExampleFormEditAbility extends FormEditExtensionAbility {
  abilityName: string = 'FormEditSecPageAbility'

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    try {
      this.context.startUIAbility({
        abilityName: 'EntryAbility1',
      }).then(() => {
        console.info(TAG, `startUIAbility success`);
      });
    } catch (e) {
      console.error(TAG, `startUIAbility failed, code: ${e.code}, message: ${e.message}`);
      return
    }
  }
}
```
