# openFormManager

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## openFormManager

```TypeScript
function openFormManager(want: Want): void
```

Opens the Widget Manager page of the current application.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-formProvider-function openFormManager(want: Want): void--><!--Device-formProvider-function openFormManager(want: Want): void-End-->

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | Parameter that must contain the following fields:&lt;br&gt;**bundleName**: bundle name of widget.&lt;br&gt; **abilityName**: ability name of the widget.&lt;br&gt;**parameters**:&lt;br&gt;- **ohos.extra.param.key.form_dimension**: [Widget dimension](arkts-form-forminfo-formdimension-e.md).&lt;br&gt;- **ohos.extra.param.key.form_name**: Widget name.&lt;br&gt;- **ohos.extra.param.key.module_name**: module name of the widget. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501000 | An internal functional error occurred. |
| 16500050 | IPC connection error. |
| 16500100 | Failed to obtain the configuration information. |

## 示例

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
  console.error(`catch error, code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
}
```

