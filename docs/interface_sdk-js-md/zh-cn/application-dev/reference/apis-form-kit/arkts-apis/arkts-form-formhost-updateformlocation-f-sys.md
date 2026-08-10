# updateFormLocation（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## updateFormLocation

```TypeScript
function updateFormLocation(formId: string, location: formInfo.FormLocation): void
```

Updates the widget location.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.REQUIRE_FORM

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-formHost-function updateFormLocation(formId: string, location: formInfo.FormLocation): void--><!--Device-formHost-function updateFormLocation(formId: string, location: formInfo.FormLocation): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Widget ID. |
| location | formInfo.FormLocation | 是 | Widget location. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501003 | The form cannot be operated by the current application. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501001 | The ID of the form to be operated does not exist. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | caller is not system app. |

