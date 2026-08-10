# SettingsChangeEvent

```TypeScript
type SettingsChangeEvent = (settingItem: SettingItem) => Promise<SettingItem>
```

设置变更事件类型。使用Promise异步回调。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-avMusicTemplate-type SettingsChangeEvent = (settingItem: SettingItem) => Promise<SettingItem>--><!--Device-avMusicTemplate-type SettingsChangeEvent = (settingItem: SettingItem) => Promise<SettingItem>-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| settingItem | [SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md) | Yes | 设置项。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;SettingItem&gt; | Promise对象，返回变更过的设置项。 |

