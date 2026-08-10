# requestPublishForm（系统接口）

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## requestPublishForm

```TypeScript
function requestPublishForm(
    want: Want,
    formBindingData: formBindingData.FormBindingData,
    callback: AsyncCallback<string>
  ): void
```

Requests to publish a widget to the widget host (usually the home screen). This API uses an asynchronous callback to return the result.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-formProvider-function requestPublishForm(    want: Want,    formBindingData: formBindingData.FormBindingData,    callback: AsyncCallback<string>  ): void--><!--Device-formProvider-function requestPublishForm(    want: Want,    formBindingData: formBindingData.FormBindingData,    callback: AsyncCallback<string>  ): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | Publish request, which must contain the following fields:&lt;br&gt;Information about the target widget. &lt;br&gt;**abilityName**: ability of the target widget.&lt;br&gt;**parameters**:&lt;br&gt;'ohos.extra.param.key.form_dimension'&lt;br&gt;' ohos.extra.param.key.form_name'&lt;br&gt;'ohos.extra.param.key.module_name' |
| formBindingData | formBindingData.FormBindingData | 是 | Data used for creating the widget. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 | Callback used to return the widget ID. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |
| 16500100 | Failed to obtain the configuration information. |


## requestPublishForm

```TypeScript
function requestPublishForm(want: Want, callback: AsyncCallback<string>): void
```

Requests to publish a widget to the widget host (usually the home screen). This API uses an asynchronous callback to return the result.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-formProvider-function requestPublishForm(want: Want, callback: AsyncCallback<string>): void--><!--Device-formProvider-function requestPublishForm(want: Want, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | Publish request, which must contain the following fields:&lt;br&gt;Information about the target widget. &lt;br&gt;**abilityName**: ability of the target widget.&lt;br&gt;**parameters**:&lt;br&gt;'ohos.extra.param.key.form_dimension'&lt;br&gt;' ohos.extra.param.key.form_name'&lt;br&gt;'ohos.extra.param.key.module_name' |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 | Callback used to return the widget ID. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |
| 16500100 | Failed to obtain the configuration information. |


## requestPublishForm

```TypeScript
function requestPublishForm(want: Want, formBindingData?: formBindingData.FormBindingData): Promise<string>
```

Requests to publish a widget to the widget host (usually the home screen). This API uses a promise to return the result.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-formProvider-function requestPublishForm(want: Want, formBindingData?: formBindingData.FormBindingData): Promise<string>--><!--Device-formProvider-function requestPublishForm(want: Want, formBindingData?: formBindingData.FormBindingData): Promise<string>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | Publish request, which must contain the following fields:&lt;br&gt;Information about the target widget. &lt;br&gt;**abilityName**: ability of the target widget.&lt;br&gt;**parameters**:&lt;br&gt;'ohos.extra.param.key.form_dimension'&lt;br&gt;' ohos.extra.param.key.form_name'&lt;br&gt;'ohos.extra.param.key.module_name' |
| formBindingData | formBindingData.FormBindingData | 否 | Data used for creating the widget. By default, no value is passed, indicating that no data is provided. |

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
| 16500100 | Failed to obtain the configuration information. |

