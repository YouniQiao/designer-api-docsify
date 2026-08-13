# FormExtensionAbility

Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare class FormExtensionAbility--><!--Device-unnamed-declare class FormExtensionAbility-End-->

**System capability:** SystemCapability.Ability.Form

## Modules to Import

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';
```

## onAcquireFormState

```TypeScript
onAcquireFormState?(want: Want): formInfo.FormState
```

Called to notify the widget provider that the widget host is requesting the widget state. By default, the initial widget state is returned. (You can override this API as required.)

**Since:** 9

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onAcquireFormState?(want: Want): formInfo.FormState--><!--Device-FormExtensionAbility-onAcquireFormState?(want: Want): formInfo.FormState-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| formInfo.FormState |

## Examples

```TypeScript
import { FormExtensionAbility, formInfo } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAcquireFormState(want: Want) {
    console.info(`FormExtensionAbility onAcquireFormState, want: ${want}`);
    return formInfo.FormState.UNKNOWN;
  }
}
```

## onAddForm

```TypeScript
onAddForm(want: Want): formBindingData.FormBindingData
```

Called to notify the widget provider that a widget is being created.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onAddForm(want: Want): formBindingData.FormBindingData--><!--Device-FormExtensionAbility-onAddForm(want: Want): formBindingData.FormBindingData-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| formBindingData.FormBindingData |

## Examples

```TypeScript
import { formBindingData, FormExtensionAbility } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    console.info(`FormExtensionAbility onAddForm, want: ${want.abilityName}`);
    let temperatureData: Record<string, string> = {
      'temperature': '11°C',
      'time': '11:00'
    };

    let formBindingDataObj: formBindingData.FormBindingData = formBindingData.createFormBindingData(temperatureData);
    return formBindingDataObj;
  }
}
```

## onCastToNormalForm

```TypeScript
onCastToNormalForm(formId: string): void
```

Called to notify the widget provider that a temporary widget has been converted to a normal one. Temporary widgets and normal widgets are concepts of the widget host. Temporary widgets have a brief existence, appearing following particular events or user interactions and vanishing automatically upon task completion. Normal widgets maintain a lasting presence, continuing to exist unless explicitly removed or altered by the user. Function widgets developed in normal cases are normal widgets. Currently, the widget host does not use temporary widgets.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onCastToNormalForm(formId: string): void--><!--Device-FormExtensionAbility-onCastToNormalForm(formId: string): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

## Examples

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onCastToNormalForm(formId: string) {
    // Called to notify the widget provider that a temporary widget has been converted to a normal one. You need to perform operations as required.
    console.info(`FormExtensionAbility onCastToNormalForm, formId: ${formId}`);
  }
}
```

## onChangeFormVisibility

```TypeScript
onChangeFormVisibility(newStatus: Record<string, number>): void
```

Called to notify the widget provider that the widget visibility status is being changed. This API is valid only for system applications when **formVisibleNotify** is set to **true**.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormExtensionAbility-onChangeFormVisibility(newStatus: Record<string, int>): void--><!--Device-FormExtensionAbility-onChangeFormVisibility(newStatus: Record<string, int>): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [newStatus](../../apis-telephony-kit/arkts-apis/arkts-telephony-sms-updatesimmessageoptions-i-sys.md) | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, number&gt; | Yes |

## Examples

```TypeScript
import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

// According to the ArkTS specification, Object.keys and for..in... cannot be used in .ets files to obtain the key value of an object. Use the user-defined function getObjKeys instead.
// Extract this function to a .ts file and export it. Import this function to the required .ets file before using it.
function getObjKeys(obj: Object): string[] {
  let keys = Object.keys(obj);
  return keys;
}

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onChangeFormVisibility(newStatus: Record<string, number>) {
    console.info(`FormExtensionAbility onChangeFormVisibility, newStatus: ${newStatus}`);
    let param: Record<string, string> = {
      'temperature': '22°C',
      'time': '22:00'
    }
    let formBindingDataObj: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);

    let keys: string[] = getObjKeys(newStatus);

    for (let i: number = 0; i < keys.length; i++) {
      console.info(`FormExtensionAbility onChangeFormVisibility, key: ${keys[i]}, value= ${newStatus[keys[i]]}`);
      formProvider.updateForm(keys[i], formBindingDataObj).then(() => {
        console.info('FormExtensionAbility context updateForm');
      }).catch ((error: BusinessError) => {
        console.error(`Operation updateForm failed, code: ${error.code}, message: ${error.message}`);
      });
    }
  }
}
```

## onConfigurationUpdate

```TypeScript
onConfigurationUpdate(newConfig: Configuration): void
```

Called when system configuration items change. The **onConfigurationUpdate** callback is triggered only when the FormExtensionAbility is alive. &lt;!--Del--&gt;Since API version 20, for system applications, the **onConfigurationUpdate** callback within the FormExtensionAbility will be triggered when the system language changes.&lt;!--DelEnd--&gt;

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onConfigurationUpdate(newConfig: Configuration): void--><!--Device-FormExtensionAbility-onConfigurationUpdate(newConfig: Configuration): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| newConfig | [Configuration](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-configuration-configuration-i.md) | Yes |

## Examples

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';
import { Configuration } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onConfigurationUpdate(newConfig: Configuration) {
    // This lifecycle callback is triggered only when the configuration is updated while the FormExtensionAbility is alive.
    // If no operation is performed within 10 seconds after a FormExtensionAbility instance is created, the instance will be deleted.
    console.info(`onConfigurationUpdate, config: ${newConfig?.language}`);
  }
}
```

## onFormEvent

```TypeScript
onFormEvent(formId: string, message: string): void
```

Called to instruct the widget provider to process the widget event.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onFormEvent(formId: string, message: string): void--><!--Device-FormExtensionAbility-onFormEvent(formId: string, message: string): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| message | string | Yes |

## Examples

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onFormEvent(formId: string, message: string) {
    console.info(`FormExtensionAbility onFormEvent, formId: ${formId}, message: ${message}`);
  }
}
```

## onFormLocationChanged

```TypeScript
onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void
```

Called when the widget location changes.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FormExtensionAbility-onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void--><!--Device-FormExtensionAbility-onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| newFormLocation | formInfo.FormLocation | Yes |

## Examples

```TypeScript
import { formBindingData, FormExtensionAbility, formInfo } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class EntryFormAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    let formData: Record<string, string | Object> = {
      'data': 'addForm'
    };
    return formBindingData.createFormBindingData(formData);
  }
  onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation) {
    console.info('EntryFormAbility onFormLocationChanged current location: ' + newFormLocation);
  }
}
```

## onRemoveForm

```TypeScript
onRemoveForm(formId: string): void
```

Called to notify the widget provider that a widget is being destroyed.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onRemoveForm(formId: string): void--><!--Device-FormExtensionAbility-onRemoveForm(formId: string): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

## Examples

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onRemoveForm(formId: string) {
    console.info(`FormExtensionAbility onRemoveForm, formId: ${formId}`);
  }
}
```

## onSizeChanged

```TypeScript
onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void
```

Called when the widget size changes.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FormExtensionAbility-onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void--><!--Device-FormExtensionAbility-onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| newDimension | formInfo.FormDimension | Yes |
| newRect | formInfo.Rect | Yes |

## Examples

```TypeScript
import { FormExtensionAbility, formInfo } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect) {
    console.info(`FormExtensionAbility onSizeChanged, formId: ${formId}, newDimension: ${newDimension}`);
  }
}
```

## onStop

```TypeScript
onStop?(): void
```

Called when the widget process of the widget provider exits.

**Since:** 12

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FormExtensionAbility-onStop?(): void--><!--Device-FormExtensionAbility-onStop?(): void-End-->

**System capability:** SystemCapability.Ability.Form

## Examples

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onStop() {
    console.info(`FormExtensionAbility onStop`);
  }
}
```

## onUpdateForm

```TypeScript
onUpdateForm(formId: string, wantParams?: Record<string, Object>): void
```

Called to notify the widget provider that a widget is being updated, with update parameters carried. After obtaining the latest data, your application should call [updateForm](arkts-form-formprovider-updateform-f.md#updateForm) of **formProvider** to update the widget data.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onUpdateForm(formId: string, wantParams?: Record<string, Object>): void--><!--Device-FormExtensionAbility-onUpdateForm(formId: string, wantParams?: Record<string, Object>): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| wantParams | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; | No |

## Examples

```TypeScript
import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onUpdateForm(formId: string, wantParams?: Record<string, Object>) {
    console.info(`FormExtensionAbility onUpdateForm, formId: ${formId},
        wantPara: ${wantParams?.['ohos.extra.param.key.host_bg_inverse_color']}`);
    let param: Record<string, string> = {
      'temperature': '22c',
      'time': '22:00'
    }
    let obj2: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);
    formProvider.updateForm(formId, obj2).then(() => {
      console.info(`FormExtensionAbility context updateForm`);
    }).catch((error: BusinessError) => {
      console.error(`FormExtensionAbility context updateForm failed, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
    });
  }
}
```

## context

```TypeScript
context: FormExtensionContext
```

Context of the FormExtensionAbility. This context is inherited from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md#ExtensionContext). This API can be used in atomic services since API version 11.

**Type:** [FormExtensionContext](arkts-form-formextensioncontext-c-sys.md)

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-context: FormExtensionContext--><!--Device-FormExtensionAbility-context: FormExtensionContext-End-->

**System capability:** SystemCapability.Ability.Form

## onAcquireFormState

```TypeScript
onAcquireFormState?: OnAcquireFormStateFn
```

Called to return a FormState object. &lt;p&gt;You must override this callback if you want this ability to return the actual form state. Otherwise, this method returns DEFAULT by default.&lt;/p&gt;

**Type:** [OnAcquireFormStateFn](arkts-form-onacquireformstatefn-t.md)

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FormExtensionAbility-onAcquireFormState?: OnAcquireFormStateFn--><!--Device-FormExtensionAbility-onAcquireFormState?: OnAcquireFormStateFn-End-->

**System capability:** SystemCapability.Ability.Form

## onStop

```TypeScript
onStop?: OnStopFn
```

Called when this ability breaks the last link, notifying the provider that the provider process is about to stop.

**Type:** [OnStopFn](arkts-form-onstopfn-t.md)

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FormExtensionAbility-onStop?: OnStopFn--><!--Device-FormExtensionAbility-onStop?: OnStopFn-End-->

**System capability:** SystemCapability.Ability.Form
