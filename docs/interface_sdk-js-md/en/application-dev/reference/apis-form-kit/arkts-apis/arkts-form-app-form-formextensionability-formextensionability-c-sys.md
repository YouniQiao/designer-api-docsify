# FormExtensionAbility

Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed.

**Since:** 23

<!--Device-unnamed-declare class FormExtensionAbility--><!--Device-unnamed-declare class FormExtensionAbility-End-->

**System capability:** SystemCapability.Ability.Form

## Modules to Import

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';
```

## onAcquireFormData

```TypeScript
onAcquireFormData?(formId: string): Record<string, Object>
```

Called when the system acquire the form data.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormExtensionAbility-onAcquireFormData?(formId: string): Record<string, Object>--><!--Device-FormExtensionAbility-onAcquireFormData?(formId: string): Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Indicates the ID of the form. |

**Return value:**

| Type | Description |
| --- | --- |
| object | Returns the wantParams object.<br>**Applicable version:** 10 |
| Record&lt;string, Object&gt; | Returns the wantParams object.<br>**Applicable version:** 11 and later |

**Examples**

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAcquireFormData(formId: string) {
    console.info(`FormExtensionAbility onAcquireFormData, formId: ${formId}`);
    let wantParams: Record<string, Object> = {
      'temperature': '20',
      'time': '2022-8-8 09:59',
    };
    return wantParams;
  }
};
```

## onShareForm

```TypeScript
onShareForm?(formId: string): Record<string, Object>
```

Called when the system shares the form.

**Since:** 9

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormExtensionAbility-onShareForm?(formId: string): Record<string, Object>--><!--Device-FormExtensionAbility-onShareForm?(formId: string): Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Indicates the ID of the form. |

**Return value:**

| Type | Description |
| --- | --- |
| object | Returns the wantParams object.<br>**Applicable version:** 9 - 10 |
| Record&lt;string, Object&gt; | Returns the wantParams object.<br>**Applicable version:** 11 and later |

**Examples**

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onShareForm(formId: string) {
    console.info(`FormExtensionAbility onShareForm, formId: ${formId}`);
    let wantParams: Record<string, Object> = {
      'temperature': '20',
      'time': '2022-8-8 09:59',
    };
    return wantParams;
  }
};
```

## onAcquireFormData

```TypeScript
onAcquireFormData?: OnAcquireFormDataFn
```

Called when the system acquire the form data.

**Type:** [OnAcquireFormDataFn](arkts-form-onacquireformdatafn-t-sys.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormExtensionAbility-onAcquireFormData?: OnAcquireFormDataFn--><!--Device-FormExtensionAbility-onAcquireFormData?: OnAcquireFormDataFn-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## onShareForm

```TypeScript
onShareForm?: OnShareFormFn
```

Called when the system shares the form.

**Type:** [OnShareFormFn](arkts-form-onshareformfn-t-sys.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormExtensionAbility-onShareForm?: OnShareFormFn--><!--Device-FormExtensionAbility-onShareForm?: OnShareFormFn-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

