# AsyncCallback

```TypeScript
export type AsyncCallback<T, E = void> = (err: BusinessError<E> | null, data: T | undefined) => void
```

通用回调函数，携带错误参数和异步返回值。错误参数为[BusinessError](arkts-basicservices-base-businesserror-i.md)类型的信息。异步返回值的类型由开发者自定义，回调将返回对应类型的信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| err | [BusinessError](arkts-basicservices-base-businesserror-i.md)&lt;E&gt; \| null | 是 |
| data | T \| undefined | 是 |
