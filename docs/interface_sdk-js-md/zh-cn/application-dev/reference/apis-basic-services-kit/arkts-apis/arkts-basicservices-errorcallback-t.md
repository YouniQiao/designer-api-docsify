# ErrorCallback

```TypeScript
export type ErrorCallback<T extends Error = BusinessError> = (err: T) => void
```

通用回调函数，携带错误参数。回调返回的信息为[BusinessError](arkts-basicservices-base-businesserror-i.md)类型的信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| err | T | 是 |
