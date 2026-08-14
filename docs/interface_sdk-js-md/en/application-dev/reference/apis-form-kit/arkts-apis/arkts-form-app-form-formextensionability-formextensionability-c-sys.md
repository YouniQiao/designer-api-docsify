# FormExtensionAbility

Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare class FormExtensionAbility--><!--Device-unnamed-declare class FormExtensionAbility-End-->

**System capability:** SystemCapability.Ability.Form

## Modules to Import

```TypeScript
import { FormExtensionAbility } from 'FormExtensionAbility';
```

## onAcquireFormData

```TypeScript
onAcquireFormData?(formId: string): Record<string, Object>
```

Called when the system acquire the form data.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

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
| object | Returns the wantParams object.<br>**Applicable version:** 10 and later |
| Record&lt;string, Object&gt; | Returns the wantParams object.<br>**Applicable version:** 11 and later |

## onShareForm

```TypeScript
onShareForm?(formId: string): Record<string, Object>
```

Called when the system shares the form.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** -1

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

## onAcquireFormData

```TypeScript
onAcquireFormData?: OnAcquireFormDataFn
```

Called when the system acquire the form data.

**Type:** [OnAcquireFormDataFn](arkts-form-onacquireformdatafn-t-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

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

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormExtensionAbility-onShareForm?: OnShareFormFn--><!--Device-FormExtensionAbility-onShareForm?: OnShareFormFn-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

