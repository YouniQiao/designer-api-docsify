# AsyncCallback

异步回调接口

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md#AsyncCallback)

<!--Device-resourceManager-export interface AsyncCallback<T>--><!--Device-resourceManager-export interface AsyncCallback<T>-End-->

**系统能力：** SystemCapability.Global.ResourceManager

## [[Call]]

```TypeScript
(err: Error, data: T): void
```

异步回调函数，携带错误参数和异步返回值。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md#AsyncCallback)

<!--Device-AsyncCallback-(err: Error, data: T): void--><!--Device-AsyncCallback-(err: Error, data: T): void-End-->

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| err | Error | 是 |
| data | T | 是 |
