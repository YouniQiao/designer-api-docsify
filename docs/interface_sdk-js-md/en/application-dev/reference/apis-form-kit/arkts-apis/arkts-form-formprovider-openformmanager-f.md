# openFormManager

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## openFormManager

```TypeScript
function openFormManager(want: Want): void
```

Opens the Widget Manager page of the current application.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-formProvider-function openFormManager(want: Want): void--><!--Device-formProvider-function openFormManager(want: Want): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Parameter that must contain the following fields:&lt;br&gt;**bundleName**: bundle name of widget.&lt;br&gt; **abilityName**: ability name of the widget.&lt;br&gt;**parameters**:&lt;br&gt;- **ohos.extra.param.key.form_dimension**: [Widget dimension](arkts-form-forminfo-formdimension-e.md).&lt;br&gt;- **ohos.extra.param.key.form_name**: Widget name.&lt;br&gt;- **ohos.extra.param.key.module_name**: module name of the widget. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [16501000](../errorcode-form.md#16501000-internal-function-error) | An internal functional error occurred. |
| [16500050](../errorcode-form.md#16500050-ipc-failure) | IPC connection error. |
| [16500100](../errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) | Failed to obtain the configuration information. |

## Examples

```TypeScript
import { formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

const want: Want = {
  bundleName: 'com.example.formbutton',
  abilityName: 'EntryFormAbility',
  parameters: {
    'ohos.extra.param.key.form_dimension': 2,
    'ohos.extra.param.key.form_name': 'widget',
    'ohos.extra.param.key.module_name': 'entry'
  },
};
try {
  formProvider.openFormManager(want);
} catch (error) {
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
}
```

