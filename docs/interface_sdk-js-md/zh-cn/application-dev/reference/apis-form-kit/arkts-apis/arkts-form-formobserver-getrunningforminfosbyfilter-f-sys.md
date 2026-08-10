# getRunningFormInfosByFilter（系统接口）

## 导入模块

```TypeScript
import { formObserver } from 'kits/@kit.FormKit';
```

## getRunningFormInfosByFilter

```TypeScript
function getRunningFormInfosByFilter(
    formProviderFilter: formInfo.FormProviderFilter
  ): Promise<Array<formInfo.RunningFormInfo>>
```

Obtains the RunningFormInfo objects by FormProviderFilter.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter  ): Promise<Array<formInfo.RunningFormInfo>>--><!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter  ): Promise<Array<formInfo.RunningFormInfo>>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formProviderFilter | formInfo.FormProviderFilter | 是 | Indicates the form provider app info. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | The promise returned by the function. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |
| 16500100 | Failed to obtain the configuration information. |


## getRunningFormInfosByFilter

```TypeScript
function getRunningFormInfosByFilter(
    formProviderFilter: formInfo.FormProviderFilter,
    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>
  ): void
```

Obtains the RunningFormInfo objects by FormProviderFilter.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.OBSERVE_FORM_RUNNING

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter,    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>  ): void--><!--Device-formObserver-function getRunningFormInfosByFilter(    formProviderFilter: formInfo.FormProviderFilter,    callback: AsyncCallback<Array<formInfo.RunningFormInfo>>  ): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formProviderFilter | formInfo.FormProviderFilter | 是 | Indicates the form provider app info. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;formInfo.RunningFormInfo&gt;&gt; | 是 | The callback of getFormInstancesByFilter. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |
| 16500100 | Failed to obtain the configuration information. |

