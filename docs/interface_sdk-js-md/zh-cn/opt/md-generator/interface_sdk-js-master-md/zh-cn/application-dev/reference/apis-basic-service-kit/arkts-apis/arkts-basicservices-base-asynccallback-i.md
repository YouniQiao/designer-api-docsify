# AsyncCallback

通用回调函数，携带错误参数和异步返回值，用于在异步操作完成时同时回传错误信息或成功数据。

错误参数为[BusinessError](arkts-basicservices-base-businesserror-i.md#BusinessError)类型。

异步返回值的类型由开发者自定义，回调将返回对应类型的信息。

**起始版本：** 6

<!--Device-unnamed-export interface AsyncCallback<T, E = void>--><!--Device-unnamed-export interface AsyncCallback<T, E = void>-End-->

**系统能力：** SystemCapability.Base

## [[Call]]

```TypeScript
(err: BusinessError<E>, data: T): void
```

**起始版本：** 6

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

<!--Device-AsyncCallback-(err: BusinessError<E>, data: T): void--><!--Device-AsyncCallback-(err: BusinessError<E>, data: T): void-End-->

**系统能力：** SystemCapability.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| err | [BusinessError](arkts-basicservices-base-businesserror-i.md)&lt;E&gt; | 是 |
| data | T | 是 |
