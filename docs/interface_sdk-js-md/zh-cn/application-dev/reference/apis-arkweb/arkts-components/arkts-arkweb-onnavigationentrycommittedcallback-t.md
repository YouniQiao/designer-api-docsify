# OnNavigationEntryCommittedCallback

```TypeScript
type OnNavigationEntryCommittedCallback = (loadCommittedDetails: LoadCommittedDetails) => void
```

导航条目提交时触发的回调。

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| loadCommittedDetails | [LoadCommittedDetails](arkts-arkweb-loadcommitteddetails-i.md) | 是 |
