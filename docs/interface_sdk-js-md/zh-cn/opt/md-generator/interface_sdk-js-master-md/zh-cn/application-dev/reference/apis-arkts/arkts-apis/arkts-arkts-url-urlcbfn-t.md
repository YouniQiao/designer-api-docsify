# UrlCbFn

```TypeScript
type UrlCbFn = (value: string, key: string, searchParams: URLParams) => void
```

[forEach](arkts-arkts-url-urlparams-c.md#forEach)函数所需的回调函数。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-url-type UrlCbFn = (value: string, key: string, searchParams: URLParams) => void--><!--Device-url-type UrlCbFn = (value: string, key: string, searchParams: URLParams) => void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string | 是 |
| key | string | 是 |
| [searchParams](arkts-arkts-url-url-c.md) | [URLParams](arkts-arkts-url-urlparams-c.md) | 是 |
