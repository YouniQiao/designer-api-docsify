# deleteForm（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## deleteForm

```TypeScript
function deleteForm(formId: string, callback: AsyncCallback<void>): void
```

Deletes a widget. After this API is called, the application can no longer use the widget, and the Widget Manager will not retain the widget information. This API uses an asynchronous callback to return the result.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function deleteForm(formId: string, callback: AsyncCallback<void>): void--><!--Device-formHost-function deleteForm(formId: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Widget ID. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | Callback used to return the result. If the widget is deleted, **error** is undefined; otherwise, **error** is an error object. |

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


## deleteForm

```TypeScript
function deleteForm(formId: string): Promise<void>
```

Deletes a widget. After this API is called, the application can no longer use the widget, and the Widget Manager will not retain the widget information. This API uses a promise to return the result.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function deleteForm(formId: string): Promise<void>--><!--Device-formHost-function deleteForm(formId: string): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Widget ID. |

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

