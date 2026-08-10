# ErrorCallback

```TypeScript
export type ErrorCallback<T extends Error = BusinessError> = (err: T) => void
```

通用回调函数，携带错误参数。回调返回的信息为[BusinessError](arkts-basicservices-base-businesserror-i.md)类型的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export type ErrorCallback<T extends Error = BusinessError> = (err: T) => void--><!--Device-unnamed-export type ErrorCallback<T extends Error = BusinessError> = (err: T) => void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| err | T | Yes | 接口调用失败的公共错误信息。 |

