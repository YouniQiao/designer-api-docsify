# UrlCbFn

```TypeScript
type UrlCbFn = (value: string, key: string, searchParams: URLParams) => void
```

[forEach](arkts-arkts-url-urlparams-c.md#foreach)函数所需的回调函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-url-type UrlCbFn = (value: string, key: string, searchParams: URLParams) => void--><!--Device-url-type UrlCbFn = (value: string, key: string, searchParams: URLParams) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | 当前遍历到的键值。 |
| key | string | Yes | 当前遍历到的键名。 |
| searchParams | [URLParams](arkts-arkts-url-urlparams-c.md) | Yes | 当前调用[forEach](arkts-arkts-url-urlparams-c.md#foreach)方法的实例对象。 |

