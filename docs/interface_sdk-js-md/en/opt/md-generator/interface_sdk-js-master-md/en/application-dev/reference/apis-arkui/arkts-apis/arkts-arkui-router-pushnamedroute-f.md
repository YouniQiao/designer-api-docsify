# pushNamedRoute

## Modules to Import

```TypeScript
import { router } from '@kit.ArkUI';
```

## pushNamedRoute

```TypeScript
function pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void
```

Navigates to a page using the named route. This API uses a promise to return the result.

> **NOTE：**
> 
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](@ohos.arkui.UIContext) to obtain the [Router](@ohos.arkui.UIContext) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [pushNamedRoute](@ohos.arkui.UIContext:Router#pushNamedRoute(options:)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void--><!--Device-router-function pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-internal.md#100001-internal-error) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |
| [100004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100004-incorrect-route-name) |

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

class InnerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: InnerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new InnerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
}, (err) => {
  if (err) {
    console.error(`pushNamedRoute failed. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('pushNamedRoute success');
})
```


## pushNamedRoute

```TypeScript
function pushNamedRoute(options: NamedRouterOptions): Promise<void>
```

Navigates to a page using the named route. This API uses a promise to return the result.

> **NOTE：**
> 
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](@ohos.arkui.UIContext) to obtain the [Router](@ohos.arkui.UIContext) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [pushNamedRoute](@ohos.arkui.UIContext:Router#pushNamedRoute(options:)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushNamedRoute(options: NamedRouterOptions): Promise<void>--><!--Device-router-function pushNamedRoute(options: NamedRouterOptions): Promise<void>-End-->

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
| [100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-internal.md#100001-internal-error) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |
| [100004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100004-incorrect-route-name) |

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

import { BusinessError } from '@kit.BasicServicesKit';

class InnerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: InnerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new InnerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
})
  .then(() => {
    console.info(`pushNamedRoute finish`);
  })
  .catch((err: BusinessError) => {
    console.error(`pushNamedRoute failed. Code: ${err.code}, message: ${err.message}`);
  })
```


## pushNamedRoute

```TypeScript
function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void
```

Navigates to a page using the named route. This API uses a promise to return the result.

> **NOTE：**
> 
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](@ohos.arkui.UIContext) to obtain the [Router](@ohos.arkui.UIContext) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [pushNamedRoute](@ohos.arkui.UIContext:Router#pushNamedRoute(options:)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void--><!--Device-router-function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) | Yes |
| mode | [RouterMode](arkts-arkui-router-routermode-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-internal.md#100001-internal-error) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |
| [100004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100004-incorrect-route-name) |

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

class InnerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: InnerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new InnerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(`pushNamedRoute failed. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('pushNamedRoute success');
})
```


## pushNamedRoute

```TypeScript
function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>
```

Navigates to a page using the named route. This API uses a promise to return the result.

> **NOTE：**
> 
> - Since API version 10, you can use the
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter) API in
> [UIContext](@ohos.arkui.UIContext) to obtain the [Router](@ohos.arkui.UIContext) object associated
> with the current UI context.

**Since:** 10

**Deprecated since:** 18

**Substitutes:** [pushNamedRoute](@ohos.arkui.UIContext:Router#pushNamedRoute(options:)

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>--><!--Device-router-function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>-End-->

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
| [100001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-internal.md#100001-internal-error) |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [100003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100003-too-many-pages-are-pushed-into-the-page-stack) |
| [100004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-router.md#100004-incorrect-route-name) |

## Examples

```TypeScript
import { router } from '@kit.ArkUI';

import { BusinessError } from '@kit.BasicServicesKit';

class InnerParams {
  data3: number[];

  constructor(tuple: number[]) {
    this.data3 = tuple;
  }
}

class RouterParams {
  data1: string;
  data2: InnerParams;

  constructor(str: string, tuple: number[]) {
    this.data1 = str;
    this.data2 = new InnerParams(tuple);
  }
}

router.pushNamedRoute({
  name: 'myPage',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard)
  .then(() => {
    console.info(`pushNamedRoute finish`);
  })
  .catch((err: BusinessError) => {
    console.error(`pushNamedRoute failed. Code: ${err.code}, message: ${err.message}`);
  })
```
