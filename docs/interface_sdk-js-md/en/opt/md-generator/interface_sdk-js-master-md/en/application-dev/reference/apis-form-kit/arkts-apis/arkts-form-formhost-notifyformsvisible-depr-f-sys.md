# notifyFormsVisible (System API)

## notifyFormsVisible

```TypeScript
function notifyFormsVisible(formIds: Array<string>, isVisible: boolean, callback: AsyncCallback<void>): void
```

Instructs the widgets to make themselves visible. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md#notifyFormsVisible-(System-API))

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function notifyFormsVisible(formIds: Array<string>, isVisible: boolean, callback: AsyncCallback<void>): void--><!--Device-formHost-function notifyFormsVisible(formIds: Array<string>, isVisible: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | Yes |
| isVisible | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## notifyFormsVisible

```TypeScript
function notifyFormsVisible(formIds: Array<string>, isVisible: boolean): Promise<void>
```

Instructs the widgets to make themselves visible. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md#notifyFormsVisible-(System-API))

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function notifyFormsVisible(formIds: Array<string>, isVisible: boolean): Promise<void>--><!--Device-formHost-function notifyFormsVisible(formIds: Array<string>, isVisible: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array & lt;string & gt; | Yes |
| isVisible | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
