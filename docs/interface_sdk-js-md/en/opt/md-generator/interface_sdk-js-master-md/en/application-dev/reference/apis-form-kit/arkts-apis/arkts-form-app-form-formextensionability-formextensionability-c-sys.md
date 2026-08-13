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

## onAcquireFormData

```TypeScript
onAcquireFormData?(formId: string): Record<string, Object>
```

Called when the system acquire the form data.

**Since:** 10

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormExtensionAbility-onAcquireFormData?(formId: string): Record<string, Object>--><!--Device-FormExtensionAbility-onAcquireFormData?(formId: string): Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| object |
| [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; |

## onShareForm

```TypeScript
onShareForm?(formId: string): Record<string, Object>
```

Called when the system shares the form.

**Since:** 9

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormExtensionAbility-onShareForm?(formId: string): Record<string, Object>--><!--Device-FormExtensionAbility-onShareForm?(formId: string): Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| object |
| [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; |

## onAcquireFormData

```TypeScript
onAcquireFormData?: OnAcquireFormDataFn
```

Called when the system acquire the form data.

**Type:** [OnAcquireFormDataFn](arkts-form-onacquireformdatafn-t-sys.md)

**Since:** 23

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

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-FormExtensionAbility-onShareForm?: OnShareFormFn--><!--Device-FormExtensionAbility-onShareForm?: OnShareFormFn-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.
