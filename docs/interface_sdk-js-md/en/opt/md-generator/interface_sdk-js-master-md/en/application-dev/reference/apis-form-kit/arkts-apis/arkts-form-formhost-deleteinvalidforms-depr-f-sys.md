# deleteInvalidForms (System API)

## deleteInvalidForms

```TypeScript
function deleteInvalidForms(formIds: Array<string>, callback: AsyncCallback<number>): void
```

Deletes invalid widgets from the list. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.app.form.formHost:formHost#deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-depr-f-sys.md#deleteinvalidforms)

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function deleteInvalidForms(formIds: Array<string>, callback: AsyncCallback<number>): void--><!--Device-formHost-function deleteInvalidForms(formIds: Array<string>, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array&lt;string&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |


## deleteInvalidForms

```TypeScript
function deleteInvalidForms(formIds: Array<string>): Promise<number>
```

Deletes invalid widgets from the list. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.app.form.formHost:formHost#deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-depr-f-sys.md#deleteinvalidforms)

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function deleteInvalidForms(formIds: Array<string>): Promise<number>--><!--Device-formHost-function deleteInvalidForms(formIds: Array<string>): Promise<number>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array&lt;string&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |
