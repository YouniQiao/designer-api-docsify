# pushUrl

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## pushUrl

```TypeScript
function pushUrl(options: RouterOptions, callback: AsyncCallback<void>): void
```

Navigates to a specified page in the application.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)(options: router.RouterOptions, callback: AsyncCallback&lt;void&gt;)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [100002](../errorcode-router.md#100002-incorrect-uri-during-page-redirection) |
| [100003](../errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |


## pushUrl

```TypeScript
function pushUrl(options: RouterOptions): Promise<void>
```

Navigates to a specified page in the application.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)(options: router.RouterOptions)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [100002](../errorcode-router.md#100002-incorrect-uri-during-page-redirection) |
| [100003](../errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |


## pushUrl

```TypeScript
function pushUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void
```

Navigates to a specified page in the application.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback&lt;void&gt;)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |
| mode | [RouterMode](arkts-arkui-router-routermode-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [100002](../errorcode-router.md#100002-incorrect-uri-during-page-redirection) |
| [100003](../errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |


## pushUrl

```TypeScript
function pushUrl(options: RouterOptions, mode: RouterMode): Promise<void>
```

Navigates to a specified page in the application.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)(options: router.RouterOptions, mode: router.RouterMode)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |
| mode | [RouterMode](arkts-arkui-router-routermode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [100002](../errorcode-router.md#100002-incorrect-uri-during-page-redirection) |
| [100003](../errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |
