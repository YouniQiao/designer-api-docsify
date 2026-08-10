# requestPublishForm（系统接口）

## 导入模块

```TypeScript
import { formAgent } from 'kits/@kit.FormKit';
```

## requestPublishForm

```TypeScript
function requestPublishForm(want: Want, callback: AsyncCallback<string>): void
```

Requests to publish a widget to the widget host. This API uses an asynchronous callback to return the result. The widget host is usually the home screen.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.AGENT_REQUIRE_FORM

<!--Device-formAgent-function requestPublishForm(want: Want, callback: AsyncCallback<string>): void--><!--Device-formAgent-function requestPublishForm(want: Want, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | Publish request, which must contain the following fields: &lt;br&gt;**bundleName**: bundle name of the target widget. &lt;br&gt;**abilityName**: ability of the target widget. &lt;br&gt;parameters: &lt;br&gt;- **ohos.extra.param.key.form_dimension**: dimension of the target widget. &lt;br&gt;- **ohos.extra.param.key.form_name**: name of the target widget. &lt;br&gt;- **ohos.extra.param.key.module_name**: module name of the target widget. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 | Callback used to return the widget ID. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |
| 16501008 | Waiting for the form addition to the desktop timed out.<br>**适用版本：** 12+ |
| 16500100 | Failed to obtain the configuration information. |


## requestPublishForm

```TypeScript
function requestPublishForm(want: Want): Promise<string>
```

Requests to publish a widget to the widget host. This API uses a promise to return the result. The widget host is usually the home screen.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.AGENT_REQUIRE_FORM

<!--Device-formAgent-function requestPublishForm(want: Want): Promise<string>--><!--Device-formAgent-function requestPublishForm(want: Want): Promise<string>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | Publish request, which must contain the following fields: &lt;br&gt;**bundleName**: bundle name of the target widget. &lt;br&gt;**abilityName**: ability of the target widget. &lt;br&gt;parameters: &lt;br&gt;- **ohos.extra.param.key.form_dimension**: dimension of the target widget. &lt;br&gt;- **ohos.extra.param.key.form_name**: name of the target widget. &lt;br&gt;- **ohos.extra.param.key.module_name**: module name of the target widget. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the widget ID. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |
| 16501008 | Waiting for the form addition to the desktop timed out.<br>**适用版本：** 12+ |
| 16500100 | Failed to obtain the configuration information. |

