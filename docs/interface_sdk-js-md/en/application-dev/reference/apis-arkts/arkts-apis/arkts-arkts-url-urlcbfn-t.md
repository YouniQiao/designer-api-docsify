# UrlCbFn

```TypeScript
type UrlCbFn = (value: string, key: string, searchParams: URLParams) => void
```

The type of URL callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-url-type UrlCbFn = (value: string, key: string, searchParams: URLParams) => void--><!--Device-url-type UrlCbFn = (value: string, key: string, searchParams: URLParams) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string | Yes | The value of the URL parameter.  |
| key | string | Yes | The key of the URL parameter.  |
| searchParams | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The URLParams object containing all parameters.  |

