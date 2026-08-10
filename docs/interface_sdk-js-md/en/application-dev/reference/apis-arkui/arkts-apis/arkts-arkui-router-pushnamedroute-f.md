# pushNamedRoute

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## pushNamedRoute

```TypeScript
function pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void
```

跳转到指定的命名路由页面。

> **说明：**
> 
> - 从API version 10开始支持，从API version 18开始废弃，建议使用
> [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)
> 替代。pushNamedRoute需先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)(options:

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void--><!--Device-router-function pushNamedRoute(options: NamedRouterOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) | Yes | 跳转页面描述信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异常响应回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

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

跳转到指定的命名路由页面。

> **说明：**
> 
> - 从API version 10开始支持，从API version 18开始废弃，建议使用
> [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)替代。
> pushNamedRoute需先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)(options:

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushNamedRoute(options: NamedRouterOptions): Promise<void>--><!--Device-router-function pushNamedRoute(options: NamedRouterOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) | Yes | 跳转页面描述信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 异常返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

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

跳转到指定的命名路由页面。

> **说明：**
> 
> - 从API version 10开始支持，从API version 18开始废弃，建议使用
> [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)
> 替代。pushNamedRoute需先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)(options:

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void--><!--Device-router-function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) | Yes | 跳转页面描述信息。 |
| mode | [RouterMode](arkts-arkui-router-routermode-e.md) | Yes | 跳转页面使用的模式。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异常响应回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

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

跳转到指定的命名路由页面。

> **说明：**
> 
> - 从API version 10开始支持，从API version 18开始废弃，建议使用
> [pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)
> 替代。pushNamedRoute需先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#pushNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#pushnamedroute)(options:

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>--><!--Device-router-function pushNamedRoute(options: NamedRouterOptions, mode: RouterMode): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [NamedRouterOptions](arkts-arkui-router-namedrouteroptions-i.md) | Yes | 跳转页面描述信息。 |
| mode | [RouterMode](arkts-arkui-router-routermode-e.md) | Yes | 跳转页面使用的模式。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 异常返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100004 | Named route error. The named route does not exist. |

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

