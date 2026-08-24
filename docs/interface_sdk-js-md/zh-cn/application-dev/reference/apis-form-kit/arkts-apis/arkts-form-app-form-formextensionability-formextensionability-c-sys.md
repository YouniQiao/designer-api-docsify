# FormExtensionAbility

Widget extension class. It provides APIs to notify the widget provider that a widget is being created or the widget visibility status is being changed.

**起始版本：** 23

<!--Device-unnamed-declare class FormExtensionAbility--><!--Device-unnamed-declare class FormExtensionAbility-End-->

**系统能力：** SystemCapability.Ability.Form

## 导入模块

```TypeScript
import { FormExtensionAbility } from '@kit.FormKit';
```

## onAcquireFormData

```TypeScript
onAcquireFormData?(formId: string): Record<string, Object>
```

Called when the system acquire the form data.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FormExtensionAbility-onAcquireFormData?(formId: string): Record<string, Object>--><!--Device-FormExtensionAbility-onAcquireFormData?(formId: string): Record<string, Object>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Indicates the ID of the form. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| object | Returns the wantParams object.<br>**适用版本：** 10 |
| Record&lt;string, Object&gt; | Returns the wantParams object.<br>**适用版本：** 11+ |

**示例**

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
}
```

## onShareForm

```TypeScript
onShareForm?(formId: string): Record<string, Object>
```

Called when the system shares the form.

**起始版本：** 9

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FormExtensionAbility-onShareForm?(formId: string): Record<string, Object>--><!--Device-FormExtensionAbility-onShareForm?(formId: string): Record<string, Object>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Indicates the ID of the form. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| object | Returns the wantParams object.<br>**适用版本：** 9 - 10 |
| Record&lt;string, Object&gt; | Returns the wantParams object.<br>**适用版本：** 11+ |

**示例**

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
}
```

## onAcquireFormData

```TypeScript
onAcquireFormData?: OnAcquireFormDataFn
```

Called when the system acquire the form data.

**类型：** [OnAcquireFormDataFn](arkts-form-onacquireformdatafn-t-sys.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FormExtensionAbility-onAcquireFormData?: OnAcquireFormDataFn--><!--Device-FormExtensionAbility-onAcquireFormData?: OnAcquireFormDataFn-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## onShareForm

```TypeScript
onShareForm?: OnShareFormFn
```

Called when the system shares the form.

**类型：** [OnShareFormFn](arkts-form-onshareformfn-t-sys.md)

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FormExtensionAbility-onShareForm?: OnShareFormFn--><!--Device-FormExtensionAbility-onShareForm?: OnShareFormFn-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

