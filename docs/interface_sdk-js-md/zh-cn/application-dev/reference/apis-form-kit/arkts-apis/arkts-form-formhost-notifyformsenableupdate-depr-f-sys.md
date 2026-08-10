# notifyFormsEnableUpdate（系统接口）

## notifyFormsEnableUpdate

```TypeScript
function notifyFormsEnableUpdate(
    formIds: Array<string>,
    isEnableUpdate: boolean,
    callback: AsyncCallback<void>
  ): void
```

Instructs the widgets to enable or disable updates. This API uses an asynchronous callback to return the result.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** [@ohos.app.form.formHost:formHost#notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-depr-f-sys.md#notifyformsenableupdate)

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function notifyFormsEnableUpdate(    formIds: Array<string>,    isEnableUpdate: boolean,    callback: AsyncCallback<void>  ): void--><!--Device-formHost-function notifyFormsEnableUpdate(    formIds: Array<string>,    isEnableUpdate: boolean,    callback: AsyncCallback<void>  ): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formIds | Array&lt;string&gt; | 是 | List of widget IDs. |
| isEnableUpdate | boolean | 是 | Whether to make the widgets updatable. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | Callback used to return the result. If the notification is sent, **error** is undefined; otherwise, **error** is an error object. |


## notifyFormsEnableUpdate

```TypeScript
function notifyFormsEnableUpdate(formIds: Array<string>, isEnableUpdate: boolean): Promise<void>
```

Instructs the widgets to enable or disable updates. This API uses a promise to return the result.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** [@ohos.app.form.formHost:formHost#notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-depr-f-sys.md#notifyformsenableupdate)

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function notifyFormsEnableUpdate(formIds: Array<string>, isEnableUpdate: boolean): Promise<void>--><!--Device-formHost-function notifyFormsEnableUpdate(formIds: Array<string>, isEnableUpdate: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formIds | Array&lt;string&gt; | 是 | List of widget IDs. |
| isEnableUpdate | boolean | 是 | Whether to make the widgets updatable. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

