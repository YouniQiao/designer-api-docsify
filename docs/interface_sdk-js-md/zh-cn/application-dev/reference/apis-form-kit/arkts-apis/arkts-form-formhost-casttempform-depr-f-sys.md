# castTempForm（系统接口）

## castTempForm

```TypeScript
function castTempForm(formId: string, callback: AsyncCallback<void>): void
```

Converts a temporary widget to a normal one. This API uses an asynchronous callback to return the result.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** [@ohos.app.form.formHost:formHost#castTempForm](arkts-form-formhost-casttempform-depr-f-sys.md#casttempform)

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function castTempForm(formId: string, callback: AsyncCallback<void>): void--><!--Device-formHost-function castTempForm(formId: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| formId | string | 是 | Widget ID. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 | Callback used to return the result. If the widget is converted to a normal one, **error** is undefined; otherwise, **error** is an error object. |


## castTempForm

```TypeScript
function castTempForm(formId: string): Promise<void>
```

Converts a temporary widget to a normal one. This API uses a promise to return the result.

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为8。

**废弃版本：** 9

**替代接口：** [@ohos.app.form.formHost:formHost#castTempForm](arkts-form-formhost-casttempform-depr-f-sys.md#casttempform)

**需要权限：** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function castTempForm(formId: string): Promise<void>--><!--Device-formHost-function castTempForm(formId: string): Promise<void>-End-->

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

