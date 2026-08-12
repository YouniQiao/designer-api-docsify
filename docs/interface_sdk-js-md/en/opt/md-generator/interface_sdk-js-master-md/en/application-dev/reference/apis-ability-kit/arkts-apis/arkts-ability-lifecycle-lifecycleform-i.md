# LifecycleForm

interface of form lifecycle.

**Since:** 7

<!--Device-unnamed-export declare interface LifecycleForm--><!--Device-unnamed-export declare interface LifecycleForm-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

## onAcquireFormState

```TypeScript
onAcquireFormState?(want: Want): formInfo.FormState
```

Called to return a [FormState](FormState) object.&lt;p&gt;You must override this callback if you want this ability to return the actual form state. Otherwise,this method returns [DEFAULT](FormState#DEFAULT) by default.&lt;/p&gt;

**Since:** 8

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onAcquireFormState?(want: Want): formInfo.FormState--><!--Device-LifecycleForm-onAcquireFormState?(want: Want): formInfo.FormState-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| formInfo.FormState |

## onCastToNormal

```TypeScript
onCastToNormal?(formId: string): void
```

Called when the form provider is notified that a temporary form is successfully converted to a normal form.

**Since:** 8

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onCastToNormal?(formId: string): void--><!--Device-LifecycleForm-onCastToNormal?(formId: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

## onCreate

```TypeScript
onCreate?(want: Want): formBindingData.FormBindingData
```

Called to return a [FormBindingData](formBindingData.FormBindingData) object.

**Since:** 8

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onCreate?(want: Want): formBindingData.FormBindingData--><!--Device-LifecycleForm-onCreate?(want: Want): formBindingData.FormBindingData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| formBindingData.FormBindingData |

## onDestroy

```TypeScript
onDestroy?(formId: string): void
```

Called to notify the form provider that a specified form has been deleted. Override this method if you want your application, as the form provider, to be notified of form deletion.

**Since:** 8

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onDestroy?(formId: string): void--><!--Device-LifecycleForm-onDestroy?(formId: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

## onEvent

```TypeScript
onEvent?(formId: string, message: string): void
```

Called when a specified message event defined by the form provider is triggered. This method is valid only for JS forms.

**Since:** 8

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onEvent?(formId: string, message: string): void--><!--Device-LifecycleForm-onEvent?(formId: string, message: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| message | string | Yes |

## onUpdate

```TypeScript
onUpdate?(formId: string): void
```

Called to notify the form provider to update a specified form.

**Since:** 8

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onUpdate?(formId: string): void--><!--Device-LifecycleForm-onUpdate?(formId: string): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

## onVisibilityChange

```TypeScript
onVisibilityChange?(newStatus: Record<string, number>): void
```

Called when the form provider receives form events from the system.

**Since:** 11

**Model restriction:** This API can be used only in the FA model.

<!--Device-LifecycleForm-onVisibilityChange?(newStatus: Record<string, number>): void--><!--Device-LifecycleForm-onVisibilityChange?(newStatus: Record<string, number>): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.FAModel

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [newStatus](../../apis-telephony-kit/arkts-apis/arkts-telephony-sms-updatesimmessageoptions-i-sys.md) | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, number&gt; | Yes |
