# ReportExecuteAbilityEvent

```TypeScript
type ReportExecuteAbilityEvent = (want: WantAgent) => void
```

通知音频模板控制方拉起指定媒体应用界面事件。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type ReportExecuteAbilityEvent = (want: WantAgent) => void--><!--Device-avMusicTemplate-type ReportExecuteAbilityEvent = (want: WantAgent) => void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [WantAgent](../../apis-ability-kit/arkts-apis/arkts-ability-wantagent-t.md) | Yes | 媒体应用页面启动信息。 |

