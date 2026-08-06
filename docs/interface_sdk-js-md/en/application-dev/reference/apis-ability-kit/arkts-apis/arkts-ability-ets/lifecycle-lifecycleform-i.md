# LifecycleForm

interface of form lifecycle.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-export declare interface LifecycleForm--><!--Device-unnamed-export declare interface LifecycleForm-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

## onAcquireFormState

```TypeScript
onAcquireFormState?(want: Want): formInfo.FormState
```

Called to return a \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ object.\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_You must override this callback if you want this ability to return the actual form state. Otherwise,this method returns \_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ by default.\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onAcquireFormState?(want: Want): formInfo.FormState--><!--Device-LifecycleForm-onAcquireFormState?(want: Want): formInfo.FormState-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the description of the form for which the \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is obtained. The description covers the bundle name, ability name, module name, form name, form dimensions. |

**Return value:**

| Type | Description |
| --- | --- |
| formInfo.FormState | Returns the { |

## onCastToNormal

```TypeScript
onCastToNormal?(formId: string): void
```

Called when the form provider is notified that a temporary form is successfully converted to a normal form.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onCastToNormal?(formId: string): void--><!--Device-LifecycleForm-onCastToNormal?(formId: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Indicates the ID of the form. |

## onCreate

```TypeScript
onCreate?(want: Want): formBindingData.FormBindingData
```

Called to return a \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ object.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onCreate?(want: Want): formBindingData.FormBindingData--><!--Device-LifecycleForm-onCreate?(want: Want): formBindingData.FormBindingData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the detailed information for creating a \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. The {@code Want} object must include the form ID, form name, and grid style of the form, which can be obtained from \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_2\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, and \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_3\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, respectively. Such form information must be managed as persistent data for further form acquisition, update, and deletion. |

**Return value:**

| Type | Description |
| --- | --- |
| formBindingData.FormBindingData | Returns the created { |

## onDestroy

```TypeScript
onDestroy?(formId: string): void
```

Called to notify the form provider that a specified form has been deleted. Override this method if you want your application, as the form provider, to be notified of form deletion.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onDestroy?(formId: string): void--><!--Device-LifecycleForm-onDestroy?(formId: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Indicates the ID of the deleted form. |

## onEvent

```TypeScript
onEvent?(formId: string, message: string): void
```

Called when a specified message event defined by the form provider is triggered. This method is valid only for JS forms.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onEvent?(formId: string, message: string): void--><!--Device-LifecycleForm-onEvent?(formId: string, message: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Indicates the ID of the form on which the message event is triggered, which is provided by the client to the form provider. |
| message | string | Yes | Indicates the value of the {@code params} field of the message event. This parameter is used to identify the specific component on which the event is triggered. |

## onUpdate

```TypeScript
onUpdate?(formId: string): void
```

Called to notify the form provider to update a specified form.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onUpdate?(formId: string): void--><!--Device-LifecycleForm-onUpdate?(formId: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| formId | string | Yes | Indicates the ID of the form to update. |

## onVisibilityChange

```TypeScript
onVisibilityChange?(newStatus: Record<string, number>): void
```

Called when the form provider receives form events from the system.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onVisibilityChange?(newStatus: Record<string, number>): void--><!--Device-LifecycleForm-onVisibilityChange?(newStatus: Record<string, number>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| newStatus | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;string, number&gt; | Yes | Indicates the form events occurred. The key in the {@code Map} object indicates form ID,and the value indicates the event type, which can be either \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ or \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_2\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ means that the form becomes visible, and \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_3\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ means that the form becomes invisible. |

