# updateFormCrossBundle（系统接口）

## 导入模块

```TypeScript
import { formAgent } from 'kits/@kit.FormKit';
```

## updateFormCrossBundle

```TypeScript
function updateFormCrossBundle(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>
```

Updates a widget by cross bundle. This API uses a promise to return the result.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.UPDATE_FORM_CROSS_BUNDLE

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-formAgent-function updateFormCrossBundle(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>--><!--Device-formAgent-function updateFormCrossBundle(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | ID of the widget to update. |
| formBindingData | formBindingData.FormBindingData | 是 | Data to be used for the update. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501003 | The form to be operated has been deleted already. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501000 | Possible cause internal functional error. Such as virtualization failed. |
| 16501007 | The form to be operated is not trusted. |
| 16500060 | Possible cause Service State error. Such as the form is recovering. |
| 201 | Permissions denied. |
| 16500050 | Possible cause IPC connection error. Such as the remote object dose not exist. |
| 202 | The application is not a system application. |

