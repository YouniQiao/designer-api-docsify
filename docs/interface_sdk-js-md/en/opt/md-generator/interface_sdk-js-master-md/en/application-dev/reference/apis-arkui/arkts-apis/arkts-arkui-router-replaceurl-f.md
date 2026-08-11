# replaceUrl

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## replaceUrl

```TypeScript
function replaceUrl(options: RouterOptions, callback: AsyncCallback<void>): void
```

Replaces the current page with another one in the application and destroys the current page.

> **NOTE：**
> 
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-uicontext.md) to obtain the [Router](arkts-arkui-uicontext.md) object associated
> with the current UI context.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#replaceUrl](arkts-arkui-arkui-uicontext-router-c.md#replaceurl)(options:

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function replaceUrl(options: RouterOptions, callback: AsyncCallback<void>): void--><!--Device-router-function replaceUrl(options: RouterOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [200002](../errorcode-router.md#200002-incorrect-uri-during-page-replacement) |

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, (err) => {
  if (err) {
    console.error(`replaceUrl failed. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('replaceUrl success');
})
```


## replaceUrl

```TypeScript
function replaceUrl(options: RouterOptions): Promise<void>
```

Replaces the current page with another one in the application and destroys the current page. This API cannot be used to configure page transition effects. To configure page transition effects, use the  
[Navigation](../../../ui/arkts-navigation-architecture.md) component.

> **NOTE：**
> 
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-uicontext.md) to obtain the [Router](arkts-arkui-uicontext.md) object associated
> with the current UI context.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#replaceUrl](arkts-arkui-arkui-uicontext-router-c.md#replaceurl)(options:

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function replaceUrl(options: RouterOptions): Promise<void>--><!--Device-router-function replaceUrl(options: RouterOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [200002](../errorcode-router.md#200002-incorrect-uri-during-page-replacement) |

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
})
  .then(() => {
    console.info(`replaceUrl finish`);
  })
  .catch((err: BusinessError) => {
    console.error(`replaceUrl failed. Code: ${err.code}, message: ${err.message}`);
  })
```


## replaceUrl

```TypeScript
function replaceUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void
```

Replaces the current page with another one in the application and destroys the current page.

> **NOTE：**
> 
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-uicontext.md) to obtain the [Router](arkts-arkui-uicontext.md) object associated
> with the current UI context.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#replaceUrl](arkts-arkui-arkui-uicontext-router-c.md#replaceurl)(options:

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function replaceUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void--><!--Device-router-function replaceUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |
| mode | [RouterMode](arkts-arkui-router-routermode-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [200002](../errorcode-router.md#200002-incorrect-uri-during-page-replacement) |

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(`replaceUrl failed. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('replaceUrl success');
});
```


## replaceUrl

```TypeScript
function replaceUrl(options: RouterOptions, mode: RouterMode): Promise<void>
```

Replaces the current page with another one in the application and destroys the current page.

> **NOTE：**
> 
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](arkts-arkui-uicontext.md) to obtain the [Router](arkts-arkui-uicontext.md) object associated
> with the current UI context.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#replaceUrl](arkts-arkui-arkui-uicontext-router-c.md#replaceurl)(options:

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function replaceUrl(options: RouterOptions, mode: RouterMode): Promise<void>--><!--Device-router-function replaceUrl(options: RouterOptions, mode: RouterMode): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes |
| mode | [RouterMode](arkts-arkui-router-routermode-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../errorcode-internal.md#100001-internal-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [200002](../errorcode-router.md#200002-incorrect-uri-during-page-replacement) |

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

import { BusinessError } from '@kit.BasicServicesKit';

class RouterParams {
  data1: string;

  constructor(str: string) {
    this.data1 = str;
  }
}

router.replaceUrl({
  url: 'pages/detail',
  params: new RouterParams('message')
}, router.RouterMode.Standard)
  .then(() => {
    console.info(`replaceUrl finish`);
  })
  .catch((err: BusinessError) => {
    console.error(`replaceUrl failed. Code: ${err.code}, message: ${err.message}`);
  })
```
