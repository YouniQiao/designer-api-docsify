# replaceUrl

## replaceUrl

```TypeScript
function replaceUrl(options: RouterOptions, callback: AsyncCallback<void>): void
```

用应用内的某个页面替换当前页面，并销毁被替换的页面。不支持设置页面转场动效，如需设置，推荐使用[Navigation组件](../../ui/arkts-navigation-architecture.md)。

> **说明：**
> 
> - 从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用
> [replaceUrl](arkts-arkui-arkui-uicontext-router-c.md#replaceUrl)
> 替代。replaceUrl需先通过[UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](@ohos.arkui.UIContext)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](@ohos.arkui.UIContext)对象。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [replaceUrl](@ohos.arkui.UIContext:Router#replaceUrl(options:)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-router-function replaceUrl(options: RouterOptions, callback: AsyncCallback<void>): void--><!--Device-router-function replaceUrl(options: RouterOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [200002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#200002-路由页面替换时输入的uri错误) |

## 示例

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

用应用内的某个页面替换当前页面，并销毁被替换的页面。不支持设置页面转场动效，如需设置，推荐使用[Navigation组件](../../../ui/arkts-navigation-architecture.md)。

> **说明：**
> 
> - 从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用
> [replaceUrl](arkts-arkui-arkui-uicontext-router-c.md#replaceUrl-1)替代。replaceUrl需先通过
> [UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](@ohos.arkui.UIContext)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](@ohos.arkui.UIContext)对象。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [replaceUrl](@ohos.arkui.UIContext:Router#replaceUrl(options:)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-router-function replaceUrl(options: RouterOptions): Promise<void>--><!--Device-router-function replaceUrl(options: RouterOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [200002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#200002-路由页面替换时输入的uri错误) |

## 示例

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

用应用内的某个页面替换当前页面，并销毁被替换的页面。不支持设置页面转场动效，如需设置，推荐使用[Navigation组件](../../ui/arkts-navigation-architecture.md)。

> **说明：**
> 
> - 从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用
> [replaceUrl](arkts-arkui-arkui-uicontext-router-c.md#replaceUrl)
> 替代。replaceUrl需先通过[UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](@ohos.arkui.UIContext)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](@ohos.arkui.UIContext)对象。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [replaceUrl](@ohos.arkui.UIContext:Router#replaceUrl(options:)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-router-function replaceUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void--><!--Device-router-function replaceUrl(options: RouterOptions, mode: RouterMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | 是 |
| mode | [RouterMode](arkts-arkui-router-routermode-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [200002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#200002-路由页面替换时输入的uri错误) |

## 示例

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

用应用内的某个页面替换当前页面，并销毁被替换的页面。不支持设置页面转场动效，如需设置，推荐使用[Navigation组件](../../ui/arkts-navigation-architecture.md)。

> **说明：**
> 
> - 从API version 9开始支持，除Lite Wearable外，从API version 18开始废弃，建议使用
> [replaceUrl](arkts-arkui-arkui-uicontext-router-c.md#replaceUrl-3)
> 替代。replaceUrl需先通过[UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)获取
> [Router](@ohos.arkui.UIContext)实例，然后通过该实例进行调用。
> 
> - 从API version 10开始，可以通过使用[UIContext](@ohos.arkui.UIContext)中的
> [getRouter](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#getrouter)方法获取当前UI上下文关联的
> [Router](@ohos.arkui.UIContext)对象。

**起始版本：** 9

**废弃版本：** 18

**替代接口：** [replaceUrl](@ohos.arkui.UIContext:Router#replaceUrl(options:)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-router-function replaceUrl(options: RouterOptions, mode: RouterMode): Promise<void>--><!--Device-router-function replaceUrl(options: RouterOptions, mode: RouterMode): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RouterOptions](arkts-arkui-system-router-routeroptions-i.md) | 是 |
| mode | [RouterMode](arkts-arkui-router-routermode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [200002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkui/errorcode-router.md#200002-路由页面替换时输入的uri错误) |

## 示例

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
