# enableFormsUpdate (System API)

## enableFormsUpdate

```TypeScript
function enableFormsUpdate(formIds: Array<string>, callback: AsyncCallback<void>): void
```

Instructs the widget framework to make a widget updatable. After this API is called, the widget is in the enabled state and can receive updates from the widget provider. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.app.form.formHost:formHost#enableFormsUpdate](arkts-form-formhost-enableformsupdate-depr-f-sys.md#enableformsupdate)

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function enableFormsUpdate(formIds: Array<string>, callback: AsyncCallback<void>): void--><!--Device-formHost-function enableFormsUpdate(formIds: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array&lt;string&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## enableFormsUpdate

```TypeScript
function enableFormsUpdate(formIds: Array<string>): Promise<void>
```

Instructs the widget framework to make a widget updatable. After this API is called, the widget is in the enabled state and can receive updates from the widget provider. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.app.form.formHost:formHost#enableFormsUpdate](arkts-form-formhost-enableformsupdate-depr-f-sys.md#enableformsupdate)

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function enableFormsUpdate(formIds: Array<string>): Promise<void>--><!--Device-formHost-function enableFormsUpdate(formIds: Array<string>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |
