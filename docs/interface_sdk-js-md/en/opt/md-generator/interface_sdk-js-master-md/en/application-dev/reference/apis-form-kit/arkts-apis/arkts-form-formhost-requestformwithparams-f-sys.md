# requestFormWithParams (System API)

## Modules to Import

```TypeScript
```

## requestFormWithParams

```TypeScript
function requestFormWithParams(formId: string, wantParams?: Record<string, Object>): Promise<void>
```

Carries parameters to request a widget update. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function requestFormWithParams(formId: string, wantParams?: Record<string, Object>): Promise<void>--><!--Device-formHost-function requestFormWithParams(formId: string, wantParams?: Record<string, Object>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formId | string | Yes |
| wantParams | [Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16501003](../errorcode-form.md#16501003-widget-not-operatable) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16501001](../errorcode-form.md#16501001-widget-id-not-exist) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
