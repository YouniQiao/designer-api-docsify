# releaseForm (System API)

## releaseForm

```TypeScript
function releaseForm(formId: string, callback: AsyncCallback<void>): void
```

Releases a widget. After this API is called, the application can no longer use the widget, but the Widget Manager still retains the widget cache and storage information. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.app.form.formHost:formHost#releaseForm](arkts-form-formhost-releaseform-depr-f-sys.md#releaseform)

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function releaseForm(formId: string, callback: AsyncCallback<void>): void--><!--Device-formHost-function releaseForm(formId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## releaseForm

```TypeScript
function releaseForm(formId: string, isReleaseCache: boolean, callback: AsyncCallback<void>): void
```

Releases a widget. After this API is called, the application can no longer use the widget, but the Widget Manager retains the storage information about the widget and retains or releases the cache information based on the setting. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.app.form.formHost:formHost#releaseForm](arkts-form-formhost-releaseform-depr-f-sys.md#releaseform)

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function releaseForm(formId: string, isReleaseCache: boolean, callback: AsyncCallback<void>): void--><!--Device-formHost-function releaseForm(formId: string, isReleaseCache: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| isReleaseCache | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## releaseForm

```TypeScript
function releaseForm(formId: string, isReleaseCache?: boolean): Promise<void>
```

Releases a widget. After this API is called, the application can no longer use the widget, but the Widget Manager retains the storage information about the widget and retains or releases the cache information based on the setting. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [@ohos.app.form.formHost:formHost#releaseForm](arkts-form-formhost-releaseform-depr-f-sys.md#releaseform)

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function releaseForm(formId: string, isReleaseCache?: boolean): Promise<void>--><!--Device-formHost-function releaseForm(formId: string, isReleaseCache?: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| isReleaseCache | boolean | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |
