# AsyncCallback

异步回调接口

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md#asynccallback)

<!--Device-resourceManager-export interface AsyncCallback--><!--Device-resourceManager-export interface AsyncCallback-End-->

**系统能力：** SystemCapability.Global.ResourceManager

## 导入模块

```TypeScript
```

## constructor

```TypeScript
(err: Error, data: T): void
```

异步回调函数，携带错误参数和异步返回值。

**起始版本：** 6

**废弃版本：** 9

**替代接口：** [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md#asynccallback)

<!--Device-AsyncCallback-(err: Error, data: T): void--><!--Device-AsyncCallback-(err: Error, data: T): void-End-->

**系统能力：** SystemCapability.Global.ResourceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| err | Error | 是 |
| data | T | 是 |
