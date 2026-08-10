# setRouterProxy（系统接口）

## 导入模块

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## setRouterProxy

```TypeScript
function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>, callback: AsyncCallback<void>): void
```

Sets a router proxy for widgets and obtains the Want information required for redirection. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Generally, for a widget added to the home screen, in the case of router-based redirection, the widget framework
> checks whether the destination is proper and whether the widget has the redirection permission, and then
> triggers redirection accordingly. For a widget that is added to a widget host and has a router proxy configured,
> in the case of router-based redirection, the widget framework does not trigger redirection for the widget.
> - Only one router proxy can be set for a widget. If multiple proxies are set, only the last proxy takes effect.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>, callback: AsyncCallback<void>): void--><!--Device-formHost-function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formIds | Array&lt;string&gt; | 是 | Array of widget IDs. |
| proxy | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt; | 是 | Callback used to return the Want information required for redirection. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | Callback used to return the result. If the router proxy is set, **error** is **undefined**; otherwise, an exception is thrown. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501003 | The form cannot be operated by the current application. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |


## setRouterProxy

```TypeScript
function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>): Promise<void>
```

Sets a router proxy for widgets and obtains the Want information required for redirection. This API uses a promise to return the result. This API uses a promise to return the result.

> **NOTE：**
> 
> - Generally, for a widget added to the home screen, in the case of router-based redirection, the widget framework
> checks whether the destination is proper and whether the widget has the redirection permission, and then
> triggers redirection accordingly. For a widget that is added to a widget host and has a router proxy configured,
> in the case of router-based redirection, the widget framework does not trigger redirection for the widget.
> 
> - Only one router proxy can be set for a widget. If multiple proxies are set, only the last proxy takes effect.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>): Promise<void>--><!--Device-formHost-function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formIds | Array&lt;string&gt; | 是 | Array of widget IDs. |
| proxy | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt; | 是 | Callback used to return the Want information required for redirection. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 16501003 | The form cannot be operated by the current application. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| 16501000 | An internal functional error occurred. |
| 16500060 | Service connection error. |
| 201 | Permissions denied. |
| 16500050 | IPC connection error. |
| 202 | The application is not a system application. |

