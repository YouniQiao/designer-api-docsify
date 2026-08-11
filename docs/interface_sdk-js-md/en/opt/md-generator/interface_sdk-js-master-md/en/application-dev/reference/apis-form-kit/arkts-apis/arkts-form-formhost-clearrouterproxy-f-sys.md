# clearRouterProxy (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## clearRouterProxy

```TypeScript
function clearRouterProxy(formIds: Array<string>, callback: AsyncCallback<void>): void
```

Clears the router proxy set for widgets. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function clearRouterProxy(formIds: Array<string>, callback: AsyncCallback<void>): void--><!--Device-formHost-function clearRouterProxy(formIds: Array<string>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array&lt;string&gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [16501003](../errorcode-form.md#16501003-widget-not-operatable) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## clearRouterProxy

```TypeScript
function clearRouterProxy(formIds: Array<string>): Promise<void>
```

Clears the router proxy set for widgets. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function clearRouterProxy(formIds: Array<string>): Promise<void>--><!--Device-formHost-function clearRouterProxy(formIds: Array<string>): Promise<void>-End-->

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

**Error codes:**

| Error Code ID |
| --- |
| [16501003](../errorcode-form.md#16501003-widget-not-operatable) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [16501000](../errorcode-form.md#16501000-internal-function-error) |
| [16500060](../errorcode-form.md#16500060-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16500050](../errorcode-form.md#16500050-ipc-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
