# Callback

```TypeScript
export type Callback<T> = (data: T) => void
```

通用回调函数。开发者在使用时，可自定义data的类型，回调将返回对应类型的信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export type Callback<T> = (data: T) => void--><!--Device-unnamed-export type Callback<T> = (data: T) => void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | T | Yes | 接口调用时的公共回调信息。 |

