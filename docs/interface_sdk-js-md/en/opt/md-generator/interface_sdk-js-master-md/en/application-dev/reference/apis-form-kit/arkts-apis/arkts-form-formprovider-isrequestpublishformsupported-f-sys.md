# isRequestPublishFormSupported (System API)

## Modules to Import

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## isRequestPublishFormSupported

```TypeScript
function isRequestPublishFormSupported(callback: AsyncCallback<boolean>): void
```

Checks whether a widget can be added to the widget host. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-formProvider-function isRequestPublishFormSupported(callback: AsyncCallback<boolean>): void--><!--Device-formProvider-function isRequestPublishFormSupported(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## isRequestPublishFormSupported

```TypeScript
function isRequestPublishFormSupported(): Promise<boolean>
```

Checks whether a widget can be added to the widget host. This API uses a promise to return the result.

**Since:** 9

<!--Device-formProvider-function isRequestPublishFormSupported(): Promise<boolean>--><!--Device-formProvider-function isRequestPublishFormSupported(): Promise<boolean>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
