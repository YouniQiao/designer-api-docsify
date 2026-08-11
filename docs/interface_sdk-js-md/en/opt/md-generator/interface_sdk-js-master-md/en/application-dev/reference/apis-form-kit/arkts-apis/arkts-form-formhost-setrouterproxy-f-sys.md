# setRouterProxy (System API)

## Modules to Import

```TypeScript
import { formHost } from 'kits/@kit.FormKit';
```

## setRouterProxy

```TypeScript
function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>, callback: AsyncCallback<void>): void
```

Sets a router proxy for widgets and obtains the Want information required for redirection. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> Generally, for a widget added to the home screen, in the case of router-based redirection, the widget framework
> checks whether the destination is proper and whether the widget has the redirection permission, and then
> triggers redirection accordingly. For a widget that is added to a widget host and has a router proxy configured,
> in the case of router-based redirection, the widget framework does not trigger redirection for the widget.
> - Only one router proxy can be set for a widget. If multiple proxies are set, only the last proxy takes effect.

**Since:** 11

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>, callback: AsyncCallback<void>): void--><!--Device-formHost-function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array&lt;string&gt; | Yes |
| proxy | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt; | Yes |
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


## setRouterProxy

```TypeScript
function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>): Promise<void>
```

Sets a router proxy for widgets and obtains the Want information required for redirection. This API uses a promise to return the result. This API uses a promise to return the result.

> **NOTE：**
> 
> - Generally, for a widget added to the home screen, in the case of router-based redirection, the widget framework
> checks whether the destination is proper and whether the widget has the redirection permission, and then
> triggers redirection accordingly. For a widget that is added to a widget host and has a router proxy configured,
> in the case of router-based redirection, the widget framework does not trigger redirection for the widget.
> 
> - Only one router proxy can be set for a widget. If multiple proxies are set, only the last proxy takes effect.

**Since:** 11

**Required permissions:** ohos.permission.REQUIRE_FORM

<!--Device-formHost-function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>): Promise<void>--><!--Device-formHost-function setRouterProxy(formIds: Array<string>, proxy: Callback<Want>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| formIds | Array&lt;string&gt; | Yes |
| proxy | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt; | Yes |

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
