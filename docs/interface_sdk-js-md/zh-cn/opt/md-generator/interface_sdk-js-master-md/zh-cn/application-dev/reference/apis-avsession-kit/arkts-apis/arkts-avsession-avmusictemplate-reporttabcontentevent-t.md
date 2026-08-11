# ReportTabContentEvent

```TypeScript
type ReportTabContentEvent = (tabId: string, tabContent: MediaTabContent) => void
```

标签页内容上报事件。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-avMusicTemplate-type ReportTabContentEvent = (tabId: string, tabContent: MediaTabContent) => void--><!--Device-avMusicTemplate-type ReportTabContentEvent = (tabId: string, tabContent: MediaTabContent) => void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tabId | string | 是 |
| tabContent | [MediaTabContent](arkts-avsession-avmusictemplate-mediatabcontent-i.md) | 是 |
