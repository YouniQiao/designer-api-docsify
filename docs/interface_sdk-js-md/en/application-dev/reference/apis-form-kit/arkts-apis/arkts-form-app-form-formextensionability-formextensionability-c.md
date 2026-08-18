# FormExtensionAbility

Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed.

**Since:** 23

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

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onAcquireFormState?(want: Want): formInfo.FormState--><!--Device-FormExtensionAbility-onAcquireFormState?(want: Want): formInfo.FormState-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Description of the widget state, including the bundle name, ability name, module name, and widget name. |

**Return value:**

| Type | Description |
| --- | --- |
| formInfo.FormState | Enumerated values of the current widget status. |

**Examples**

```TypeScript
import { FormExtensionAbility, formInfo } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAcquireFormState(want: Want) {
    console.info(`FormExtensionAbility onAcquireFormState, want: ${want}`);
    return formInfo.FormState.UNKNOWN;
  }
};
```

## onAddForm

```TypeScript
onAddForm(want: Want): formBindingData.FormBindingData
```

Called to notify the widget provider that a widget is being created.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onAddForm(want: Want): formBindingData.FormBindingData--><!--Device-FormExtensionAbility-onAddForm(want: Want): formBindingData.FormBindingData-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Want information of the widget. You can set the **parameters** field to one or more values enumerated in [widget parameters](arkts-form-forminfo-formparam-e.md), such as widget ID, widget name, and widget style. The information must be managed as persistent data to facilitate subsequent widget update and deletion. |

**Return value:**

| Type | Description |
| --- | --- |
| formBindingData.FormBindingData | A **formBindingData.FormBindingData** object containing the data to be displayed on the widget. |

**Examples**

```TypeScript
import { formBindingData, FormExtensionAbility } from '@kit.FormKit';
import { Want } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onAddForm(want: Want) {
    console.info(`FormExtensionAbility onAddForm, want: ${want.abilityName}`);
    let dataObj1: Record<string, string> = {
      'temperature': '11c',
      'time': '11:00'
    };

    let obj1: formBindingData.FormBindingData = formBindingData.createFormBindingData(dataObj1);
    return obj1;
  }
}
```

## onCastToNormalForm

```TypeScript
onCastToNormalForm(formId: string): void
```

Called to notify the widget provider that a temporary widget has been converted to a normal one. Temporary widgets and normal widgets are concepts of the widget host. Temporary widgets have a brief existence, appearing following particular events or user interactions and vanishing automatically upon task completion. Normal widgets maintain a lasting presence, continuing to exist unless explicitly removed or altered by the user. Function widgets developed in normal cases are normal widgets. Currently, the widget host does not use temporary widgets.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onCastToNormalForm(formId: string): void--><!--Device-FormExtensionAbility-onCastToNormalForm(formId: string): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | ID of the widget that requests to be converted to a normal one. |

**Examples**

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onCastToNormalForm(formId: string) {
    // Called to notify the widget provider that a temporary widget has been converted to a normal one. You need to perform operations as required.
    console.info(`FormExtensionAbility onCastToNormalForm, formId: ${formId}`);
  }
};
```

## onChangeFormVisibility

```TypeScript
onChangeFormVisibility(newStatus: Record<string, int>): void
```

Called to notify the widget provider that the widget visibility status is being changed. This API is valid only for system applications when **formVisibleNotify** is set to **true**.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormExtensionAbility-onChangeFormVisibility(newStatus: Record<string, int>): void--><!--Device-FormExtensionAbility-onChangeFormVisibility(newStatus: Record<string, int>): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newStatus | Record&lt;string, int&gt; | Yes | ID and visibility status of the widget to be changed.<br>**Since:** 11 |

**Examples**

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
      'temperature': '22c',
      'time': '22:00'
    }
    let obj2: formBindingData.FormBindingData = formBindingData.createFormBindingData(param);

    let keys: string[] = getObjKeys(newStatus);

    for (let i: number = 0; i < keys.length; i++) {
      console.info(`FormExtensionAbility onChangeFormVisibility, key: ${keys[i]}, value= ${newStatus[keys[i]]}`);
      formProvider.updateForm(keys[i], obj2).then(() => {
        console.info('FormExtensionAbility context updateForm');
      }).catch((error: BusinessError) => {
        console.error(`Operation updateForm failed. , code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message})`);
      });
    }
  }
};
```

## onConfigurationUpdate

```TypeScript
onConfigurationUpdate(newConfig: Configuration): void
```

Called when system configuration items change. The **onConfigurationUpdate** callback is triggered only when the FormExtensionAbility is alive. <!--Del-->Since API version 20, for system applications, the **onConfigurationUpdate** callback within the FormExtensionAbility will be triggered when the system language changes.<!--DelEnd-->

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onConfigurationUpdate(newConfig: Configuration): void--><!--Device-FormExtensionAbility-onConfigurationUpdate(newConfig: Configuration): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newConfig | [Configuration](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-configuration-configuration-i.md) | Yes | New configuration. |

**Examples**

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';
import { Configuration } from '@kit.AbilityKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onConfigurationUpdate(newConfig: Configuration) {
    // This lifecycle callback is triggered only when the configuration is updated while the FormExtensionAbility is alive.
    // If no operation is performed within 10 seconds after a FormExtensionAbility instance is created, the instance will be deleted.
    console.info(`onConfigurationUpdate, config: ${newConfig?.language}`);
  }
};
```

## onFormEvent

```TypeScript
onFormEvent(formId: string, message: string): void
```

Called to instruct the widget provider to process the widget event.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onFormEvent(formId: string, message: string): void--><!--Device-FormExtensionAbility-onFormEvent(formId: string, message: string): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | ID of the widget that requests the event. |
| message | string | Yes | Event message. |

**Examples**

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onFormEvent(formId: string, message: string) {
    console.info(`FormExtensionAbility onFormEvent, formId: ${formId}, message: ${message}`);
  }
};
```

## onFormLocationChanged

```TypeScript
onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void
```

Called when the widget location changes.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FormExtensionAbility-onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void--><!--Device-FormExtensionAbility-onFormLocationChanged(formId: string, newFormLocation: formInfo.FormLocation): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Widget ID. |
| newFormLocation | formInfo.FormLocation | Yes | Enumerated value of the latest widget location. |

**Examples**

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
    console.info("EntryFormAbility onFormLocationChanged current location: " + newFormLocation);
  }
}
```

## onRemoveForm

```TypeScript
onRemoveForm(formId: string): void
```

Called to notify the widget provider that a widget is being destroyed.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onRemoveForm(formId: string): void--><!--Device-FormExtensionAbility-onRemoveForm(formId: string): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | ID of the widget to be destroyed. |

**Examples**

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';

export default class MyFormExtensionAbility extends FormExtensionAbility {
  onRemoveForm(formId: string) {
    console.info(`FormExtensionAbility onRemoveForm, formId: ${formId}`);
  }
};
```

## onSizeChanged

```TypeScript
onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void
```

Called when the widget size changes.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FormExtensionAbility-onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void--><!--Device-FormExtensionAbility-onSizeChanged(formId: string, newDimension: formInfo.FormDimension, newRect: formInfo.Rect): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Widget ID. |
| newDimension | formInfo.FormDimension | Yes | Widget dimension. For example, **Dimension_1_2** indicates a 1 x 2 widget. |
| newRect | formInfo.Rect | Yes | Widget position information, including the X and Y coordinates of the widget's top- left corner, as well as its width and height. |

**Examples**

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

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FormExtensionAbility-onStop?(): void--><!--Device-FormExtensionAbility-onStop?(): void-End-->

**System capability:** SystemCapability.Ability.Form

**Examples**

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

Called to notify the widget provider that a widget is being updated, with update parameters carried. After obtaining the latest data, your application should call [updateForm](arkts-form-formprovider-updateform-f.md) of **formProvider** to update the widget data.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FormExtensionAbility-onUpdateForm(formId: string, wantParams?: Record<string, Object>): void--><!--Device-FormExtensionAbility-onUpdateForm(formId: string, wantParams?: Record<string, Object>): void-End-->

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | ID of the widget that requests to be updated. |
| wantParams | Record&lt;string, Object&gt; | No | Parameters used for the update. |

**Examples**

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
};
```

## context

```TypeScript
context: FormExtensionContext
```

Context of the FormExtensionAbility. This context is inherited from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md). This API can be used in atomic services since API version 11.

**Type:** [FormExtensionContext](arkts-form-formextensioncontext-c-sys.md)

**Since:** 23

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

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FormExtensionAbility-onStop?: OnStopFn--><!--Device-FormExtensionAbility-onStop?: OnStopFn-End-->

**System capability:** SystemCapability.Ability.Form

