# notifyFormsEnableUpdate (System API)

## notifyFormsEnableUpdate

```TypeScript
function notifyFormsEnableUpdate(
    formIds: Array<string>,
    isEnableUpdate: boolean,
    callback: AsyncCallback<void>
  ): void
```

Instructs the widgets to enable or disable updates. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.app.form.formHost:formHost#notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-depr-f-sys.md#notifyformsenableupdate)

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function notifyFormsEnableUpdate(    formIds: Array<string>,    isEnableUpdate: boolean,    callback: AsyncCallback<void>  ): void--><!--Device-formHost-function notifyFormsEnableUpdate(    formIds: Array<string>,    isEnableUpdate: boolean,    callback: AsyncCallback<void>  ): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array&lt;string&gt; | Yes |
| isEnableUpdate | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## notifyFormsEnableUpdate

```TypeScript
function notifyFormsEnableUpdate(formIds: Array<string>, isEnableUpdate: boolean): Promise<void>
```

Instructs the widgets to enable or disable updates. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.app.form.formHost:formHost#notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-depr-f-sys.md#notifyformsenableupdate)

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function notifyFormsEnableUpdate(formIds: Array<string>, isEnableUpdate: boolean): Promise<void>--><!--Device-formHost-function notifyFormsEnableUpdate(formIds: Array<string>, isEnableUpdate: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array&lt;string&gt; | Yes |
| isEnableUpdate | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |
