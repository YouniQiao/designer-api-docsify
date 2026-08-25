# OnOverrideErrorPageCallback

```TypeScript
type OnOverrideErrorPageCallback = (errorPageEvent: OnErrorReceiveEvent) => string
```

onOverrideErrorPage的回调函数，网页加载失败时触发。

**起始版本：** 20

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| errorPageEvent | [OnErrorReceiveEvent](arkts-arkweb-onerrorreceiveevent-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| string |
