# requestFormWithParams（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## requestFormWithParams

```TypeScript
function requestFormWithParams(formId: string, wantParams?: Record<string, Object>): Promise<void>
```

Carries parameters to request a widget update. This API uses a promise to return the result.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function requestFormWithParams(formId: string, wantParams?: Record<string, Object>): Promise<void>--><!--Device-formHost-function requestFormWithParams(formId: string, wantParams?: Record<string, Object>): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Widget ID. |
| wantParams | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | 否 | Parameters used for the update. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

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
| 202 | The application is not a system application. |

