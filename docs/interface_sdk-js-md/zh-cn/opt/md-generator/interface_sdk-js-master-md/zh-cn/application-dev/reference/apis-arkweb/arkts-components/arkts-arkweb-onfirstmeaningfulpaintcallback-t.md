# OnFirstMeaningfulPaintCallback

```TypeScript
type OnFirstMeaningfulPaintCallback = (firstMeaningfulPaint: FirstMeaningfulPaint) => void
```

网页绘制页面度量信息的回调，当网页加载完页面主要内容时会触发该回调。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-type OnFirstMeaningfulPaintCallback = (firstMeaningfulPaint: FirstMeaningfulPaint) => void--><!--Device-unnamed-type OnFirstMeaningfulPaintCallback = (firstMeaningfulPaint: FirstMeaningfulPaint) => void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| firstMeaningfulPaint | [FirstMeaningfulPaint](arkts-arkweb-firstmeaningfulpaint-i.md) | 是 |
