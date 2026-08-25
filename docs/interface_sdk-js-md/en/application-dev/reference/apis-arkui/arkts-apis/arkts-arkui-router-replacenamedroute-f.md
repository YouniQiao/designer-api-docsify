# replaceNamedRoute

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## replaceNamedRoute

```TypeScript
function replaceNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void
```

Replaces the current page with another one using the named route and destroys the current page.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [replaceNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#replacenamedroute)(options: router.NamedRouterOptions, callback: AsyncCallback&lt;void&gt;)

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
| [100004](../errorcode-router.md#100004-incorrect-route-name) |


## replaceNamedRoute

```TypeScript
function replaceNamedRoute(options: NamedRouterOptions): Promise<void>
```

Replaces the current page with another one using the named route and destroys the current page.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [replaceNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#replacenamedroute)(options: router.NamedRouterOptions)

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
| [100004](../errorcode-router.md#100004-incorrect-route-name) |


## replaceNamedRoute

```TypeScript
function replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void
```

Replaces the current page with another one using the named route and destroys the current page.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [replaceNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#replacenamedroute)(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback&lt;void&gt;)

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
| [100004](../errorcode-router.md#100004-incorrect-route-name) |


## replaceNamedRoute

```TypeScript
function replaceNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>
```

Replaces the current page with another one using the named route and destroys the current page.

> **NOTE：**&gt;
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) to obtain the [Router](arkts-arkui-arkui-uicontext-uicontext-c.md) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [replaceNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#replacenamedroute)(options: router.NamedRouterOptions, mode: router.RouterMode)

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
| [100004](../errorcode-router.md#100004-incorrect-route-name) |
