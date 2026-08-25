# updateForm

## Modules to Import

```TypeScript
```

## updateForm

```TypeScript
function updateForm(
    formId: string,
    formBindingData: formBindingData.FormBindingData,
    callback: AsyncCallback<void>
  ): void
```

Updates a widget. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [updateForm](arkts-form-formprovider-updateform-f.md)

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| [formBindingData](arkts-application-formbindingdata.md) | formBindingData.FormBindingData | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## updateForm

```TypeScript
function updateForm(formId: string, formBindingData: formBindingData.FormBindingData): Promise<void>
```

Updates a widget. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [updateForm](arkts-form-formprovider-updateform-f.md)

**System capability:** SystemCapability.Ability.Form

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| [formBindingData](arkts-application-formbindingdata.md) | formBindingData.FormBindingData | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
