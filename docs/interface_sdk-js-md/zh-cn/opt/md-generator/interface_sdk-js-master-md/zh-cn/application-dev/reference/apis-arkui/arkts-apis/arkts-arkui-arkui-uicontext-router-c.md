# Router

class Router

**起始版本：** 10

<!--Device-unnamed-export class Router--><!--Device-unnamed-export class Router-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## back

```TypeScript
back(options?: router.RouterOptions): void
```

Returns to the previous page or a specified page.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-back(options?: router.RouterOptions): void--><!--Device-Router-back(options?: router.RouterOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.RouterOptions | 否 |

## back

```TypeScript
back(index: number, params?: Object): void
```

Returns to the specified page.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Router-back(index: number, params?: Object): void--><!--Device-Router-back(index: number, params?: Object): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| params | Object | 否 |

## clear

```TypeScript
clear(): void
```

Clears all historical pages and retains only the current page at the top of the stack.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-clear(): void--><!--Device-Router-clear(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## getLength

```TypeScript
getLength(): string
```

Obtains the number of pages in the current stack.

**起始版本：** 10

**废弃版本：** 23

**替代接口：** ohos.arkui.UIContext.Router#getStackSize

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-getLength(): string--><!--Device-Router-getLength(): string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| string |

## getParams

```TypeScript
getParams(): Object
```

Obtains information about the current page params.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-getParams(): Object--><!--Device-Router-getParams(): Object-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| Object |

## getStackSize

```TypeScript
getStackSize(): number
```

Obtains information about the current page state.

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-Router-getStackSize(): number--><!--Device-Router-getStackSize(): number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| number |

## getState

```TypeScript
getState(): router.RouterState
```

Obtains information about the current page state.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-getState(): router.RouterState--><!--Device-Router-getState(): router.RouterState-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| router.RouterState |

## getStateByIndex

```TypeScript
getStateByIndex(index: number): router.RouterState | undefined
```

Obtains page information by index.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Router-getStateByIndex(index: number): router.RouterState | undefined--><!--Device-Router-getStateByIndex(index: number): router.RouterState | undefined-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| router.RouterState |

## getStateByUrl

```TypeScript
getStateByUrl(url: string): Array<router.RouterState>
```

Obtains page information by url.

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-Router-getStateByUrl(url: string): Array<router.RouterState>--><!--Device-Router-getStateByUrl(url: string): Array<router.RouterState>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;router.RouterState&gt; |

## hideAlertBeforeBackPage

```TypeScript
hideAlertBeforeBackPage(): void
```

Hide alert before back page.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-hideAlertBeforeBackPage(): void--><!--Device-Router-hideAlertBeforeBackPage(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## pushNamedRoute

```TypeScript
pushNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void
```

Navigates to a page using the named route. This API uses a promise to return the result.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-pushNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void--><!--Device-Router-pushNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.NamedRouterOptions | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100003](../errorcode-router.md#100003-路由压入的page过多) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## pushNamedRoute

```TypeScript
pushNamedRoute(options: router.NamedRouterOptions): Promise<void>
```

Navigates to a page using the named route. This API uses a promise to return the result.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-pushNamedRoute(options: router.NamedRouterOptions): Promise<void>--><!--Device-Router-pushNamedRoute(options: router.NamedRouterOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.NamedRouterOptions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100003](../errorcode-router.md#100003-路由压入的page过多) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## pushNamedRoute

```TypeScript
pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void
```

Navigates to a page using the named route. This API uses a promise to return the result.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void--><!--Device-Router-pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.NamedRouterOptions | 是 |
| mode | router.RouterMode | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100003](../errorcode-router.md#100003-路由压入的page过多) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## pushNamedRoute

```TypeScript
pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>
```

Navigates to a page using the named route. This API uses a promise to return the result.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>--><!--Device-Router-pushNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.NamedRouterOptions | 是 |
| mode | router.RouterMode | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100003](../errorcode-router.md#100003-路由压入的page过多) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## pushUrl

```TypeScript
pushUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void
```

Navigates to a specified page in the application.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-pushUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void--><!--Device-Router-pushUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.RouterOptions | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100003](../errorcode-router.md#100003-路由压入的page过多) |
| [100002](../errorcode-router.md#100002-路由页面跳转时输入的uri错误) |

## pushUrl

```TypeScript
pushUrl(options: router.RouterOptions): Promise<void>
```

Navigates to a specified page in the application. This API uses a promise to return the result.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-pushUrl(options: router.RouterOptions): Promise<void>--><!--Device-Router-pushUrl(options: router.RouterOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.RouterOptions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100003](../errorcode-router.md#100003-路由压入的page过多) |
| [100002](../errorcode-router.md#100002-路由页面跳转时输入的uri错误) |

## pushUrl

```TypeScript
pushUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void
```

Navigates to a specified page in the application.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-pushUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void--><!--Device-Router-pushUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.RouterOptions | 是 |
| mode | router.RouterMode | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100003](../errorcode-router.md#100003-路由压入的page过多) |
| [100002](../errorcode-router.md#100002-路由页面跳转时输入的uri错误) |

## pushUrl

```TypeScript
pushUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>
```

Navigates to a specified page in the application. This API uses a promise to return the result.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-pushUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>--><!--Device-Router-pushUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.RouterOptions | 是 |
| mode | router.RouterMode | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100003](../errorcode-router.md#100003-路由压入的page过多) |
| [100002](../errorcode-router.md#100002-路由页面跳转时输入的uri错误) |

## replaceNamedRoute

```TypeScript
replaceNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void
```

Replaces the current page with another one in the application. The current page is destroyed after replacement.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-replaceNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void--><!--Device-Router-replaceNamedRoute(options: router.NamedRouterOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.NamedRouterOptions | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## replaceNamedRoute

```TypeScript
replaceNamedRoute(options: router.NamedRouterOptions): Promise<void>
```

Replaces the current page with another one in the application. The current page is destroyed after replacement.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-replaceNamedRoute(options: router.NamedRouterOptions): Promise<void>--><!--Device-Router-replaceNamedRoute(options: router.NamedRouterOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.NamedRouterOptions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## replaceNamedRoute

```TypeScript
replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void
```

Replaces the current page with another one in the application. The current page is destroyed after replacement.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void--><!--Device-Router-replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.NamedRouterOptions | 是 |
| mode | router.RouterMode | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## replaceNamedRoute

```TypeScript
replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>
```

用指定的命名路由页面替换当前页面，并销毁被替换的页面，使用Promise异步回调。与[replaceNamedRoute](arkts-arkui-arkui-uicontext-router-c.md#replacenamedroute)相比，新增了mode参数，即支持设置跳转页面使用的模式。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>--><!--Device-Router-replaceNamedRoute(options: router.NamedRouterOptions, mode: router.RouterMode): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.NamedRouterOptions | 是 |
| mode | router.RouterMode | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [100004](../errorcode-router.md#100004-命名路由页面跳转时输入的name错误) |

## replaceUrl

```TypeScript
replaceUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void
```

Replaces the current page with another one in the application. The current page is destroyed after replacement.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-replaceUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void--><!--Device-Router-replaceUrl(options: router.RouterOptions, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.RouterOptions | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [200002](../errorcode-router.md#200002-路由页面替换时输入的uri错误) |

## replaceUrl

```TypeScript
replaceUrl(options: router.RouterOptions): Promise<void>
```

Replaces the current page with another one in the application. The current page is destroyed after replacement.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-replaceUrl(options: router.RouterOptions): Promise<void>--><!--Device-Router-replaceUrl(options: router.RouterOptions): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.RouterOptions | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [200002](../errorcode-router.md#200002-路由页面替换时输入的uri错误) |

## replaceUrl

```TypeScript
replaceUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void
```

Replaces the current page with another one in the application. The current page is destroyed after replacement.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-replaceUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void--><!--Device-Router-replaceUrl(options: router.RouterOptions, mode: router.RouterMode, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.RouterOptions | 是 |
| mode | router.RouterMode | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [200002](../errorcode-router.md#200002-路由页面替换时输入的uri错误) |

## replaceUrl

```TypeScript
replaceUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>
```

Replaces the current page with another one in the application. The current page is destroyed after replacement.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-replaceUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>--><!--Device-Router-replaceUrl(options: router.RouterOptions, mode: router.RouterMode): Promise<void>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.RouterOptions | 是 |
| mode | router.RouterMode | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [200002](../errorcode-router.md#200002-路由页面替换时输入的uri错误) |

## showAlertBeforeBackPage

```TypeScript
showAlertBeforeBackPage(options: router.EnableAlertOptions): void
```

Pop up alert dialog to ask whether to back.

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-Router-showAlertBeforeBackPage(options: router.EnableAlertOptions): void--><!--Device-Router-showAlertBeforeBackPage(options: router.EnableAlertOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | router.EnableAlertOptions | 是 |

**错误码：**

| 错误码ID |
| --- |
| [100001](../errorcode-internal.md#100001-接口调用异常错误码) |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
