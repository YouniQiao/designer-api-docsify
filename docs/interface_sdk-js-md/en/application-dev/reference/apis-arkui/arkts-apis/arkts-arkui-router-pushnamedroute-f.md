# pushNamedRoute

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## pushNamedRoute

```TypeScript
function pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void
```

Navigates to a page using the named route. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)(options: router.NamedRouterOptions, callback: AsyncCallback&lt;void&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [100003](../errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |


## pushNamedRoute

```TypeScript
function pushNamedRoute(options: NamedRouterOptions): Promise<void>
```

Navigates to a page using the named route. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)(options: router.NamedRouterOptions)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [100003](../errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |


## pushNamedRoute

```TypeScript
function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void
```

Navigates to a page using the named route. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback&lt;void&gt;)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) | Yes |
| mode | [RouterMode](arkts-arkui-router-routermode-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [100003](../errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |


## pushNamedRoute

```TypeScript
function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>
```

Navigates to a page using the named route. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)(options: router.NamedRouterOptions, mode: router.RouterMode)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) | Yes |
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
| [100003](../errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |
| [100004](../errorcode-router.md#100004-incorrect-route-name) |
