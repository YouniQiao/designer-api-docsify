# pushUrl

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## pushUrl

```TypeScript
function pushUrl(options: RouterOptions, callback: AsyncCallback<void>): void
```

跳转到应用内的指定页面。

> **说明：**
> 
> - 从API version 9开始支持，从API version 18开始废弃，建议使用
> [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)
> 替代。pushUrl需先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)(options:

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushUrl(options: RouterOptions, callback: AsyncCallback<void>): void--><!--Device-router-function pushUrl(options: RouterOptions, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes | 跳转页面描述信息。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 异常响应回调。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist |

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

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
}, (err) => {
  if (err) {
    console.error(`pushUrl failed. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('pushUrl success');
});
```


## pushUrl

```TypeScript
function pushUrl(options: RouterOptions): Promise<void>
```

跳转到应用内的指定页面。

> **说明：**
> 
> - 从API version 9开始支持，从API version 18开始废弃，建议使用
> [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)替代。pushUrl需先通过
> [UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)(options:

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushUrl(options: RouterOptions): Promise<void>--><!--Device-router-function pushUrl(options: RouterOptions): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes | 跳转页面描述信息。 |

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
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist |

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

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
})
  .then(() => {
    console.info(`pushUrl finish`);
  })
  .catch((err: BusinessError) => {
    console.error(`pushUrl failed. Code: ${err.code}, message: ${err.message}`);
  });
```


## pushUrl

```TypeScript
function pushUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void
```

跳转到应用内的指定页面。

> **说明：**
> 
> - 从API version 9开始支持，从API version 18开始废弃，建议使用
> [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)
> 替代。pushUrl需先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)(options:

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void--><!--Device-router-function pushUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes | 跳转页面描述信息。 |
| mode | [RouterMode](arkts-arkui-router-routermode-e.md) | Yes | 跳转页面使用的模式。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 页面跳转结果回调函数。&lt;br/&gt;当页面跳转成功时，error为undefined。当页面跳转失败时，error为系统返回的错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | Internal error. |
| 401 | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |
| 100003 | Page stack error. Too many pages are pushed. |
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist |

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

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard, (err) => {
  if (err) {
    console.error(`pushUrl failed. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('pushUrl success');
})
```


## pushUrl

```TypeScript
function pushUrl(options: RouterOptions, mode: RouterMode): Promise<void>
```

跳转到应用内的指定页面。

> **说明：**
> 
> - 从API version 9开始支持，从API version 18开始废弃，建议使用
> [pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)替代。
> pushUrl需先通过[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](arkts-arkui-uicontext.md)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](arkts-arkui-uicontext.md)对象。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** [@ohos.arkui.UIContext:Router#pushUrl](arkts-arkui-arkui-uicontext-router-c.md#pushurl)(options:

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-router-function pushUrl(options: RouterOptions, mode: RouterMode): Promise<void>--><!--Device-router-function pushUrl(options: RouterOptions, mode: RouterMode): Promise<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | Yes | 跳转页面描述信息。 |
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
| 100002 | Uri error. The URI of the page to redirect is incorrect or does not exist |

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

router.pushUrl({
  url: 'pages/routerpage2',
  params: new RouterParams('message', [123, 456, 789])
}, router.RouterMode.Standard)
  .then(() => {
    console.info(`pushUrl finish`);
  })
  .catch((err: BusinessError) => {
    console.error(`pushUrl failed. Code: ${err.code}, message: ${err.message}`);
  })
```

