# AsyncCallback

```TypeScript
export type AsyncCallback<T, E = void> = (err: BusinessError<E> | null, data: T | undefined) => void
```

通用回调函数，携带错误参数和异步返回值。错误参数为[BusinessError](arkts-basicservices-base-businesserror-i.md)类型的信息。异步返回值的类型由开发者自定义，回调将返回对应类型的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export type AsyncCallback<T, E = void> = (err: BusinessError<E> | null, data: T | undefined) => void--><!--Device-unnamed-export type AsyncCallback<T, E = void> = (err: BusinessError<E> | null, data: T | undefined) => void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | [BusinessError](arkts-basicservices-base-businesserror-c.md)&lt;E&gt; \| null | Yes | 接口调用失败的公共错误信息。 |
| data | T \| undefined | Yes | 接口调用时的公共回调信息。 |

