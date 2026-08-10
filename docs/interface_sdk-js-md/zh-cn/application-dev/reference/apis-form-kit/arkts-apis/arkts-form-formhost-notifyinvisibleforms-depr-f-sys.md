# notifyInvisibleForms（系统接口）

## notifyInvisibleForms

```TypeScript
function notifyInvisibleForms(formIds: Array<string>, callback: AsyncCallback<void>): void
```

Instructs the widget framework to make a widget invisible. After this API is called, **onVisibilityChange** is invoked to notify the widget provider. This API uses an asynchronous callback to return the result.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** [@ohos.app.form.formHost:formHost#notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-depr-f-sys.md#notifyinvisibleforms)

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function notifyInvisibleForms(formIds: Array<string>, callback: AsyncCallback<void>): void--><!--Device-formHost-function notifyInvisibleForms(formIds: Array<string>, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formIds | Array&lt;string&gt; | 是 | List of widget IDs. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | Callback used to return the result. If a notification is sent to the widget framework to make the widget invisible, **error** is undefined; otherwise, **error** is an error object. |


## notifyInvisibleForms

```TypeScript
function notifyInvisibleForms(formIds: Array<string>): Promise<void>
```

Instructs the widget framework to make a widget invisible. After this API is called, **onVisibilityChange** is invoked to notify the widget provider. This API uses a promise to return the result.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** [@ohos.app.form.formHost:formHost#notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-depr-f-sys.md#notifyinvisibleforms)

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function notifyInvisibleForms(formIds: Array<string>): Promise<void>--><!--Device-formHost-function notifyInvisibleForms(formIds: Array<string>): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formIds | Array&lt;string&gt; | 是 | List of widget IDs. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

