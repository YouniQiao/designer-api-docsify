# requestForm (System API)

## requestForm

```TypeScript
function requestForm(formId: string, callback: AsyncCallback<void>): void
```

Requests a widget update. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [requestForm](arkts-form-formhost-requestform-f-sys.md#requestForm)

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function requestForm(formId: string, callback: AsyncCallback<void>): void--><!--Device-formHost-function requestForm(formId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## requestForm

```TypeScript
function requestForm(formId: string): Promise<void>
```

Requests a widget update. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [requestForm](arkts-form-formhost-requestform-f-sys.md#requestForm)

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function requestForm(formId: string): Promise<void>--><!--Device-formHost-function requestForm(formId: string): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
