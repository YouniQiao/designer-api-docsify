# Single

单曲的定义。继承自[MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)。

**Inheritance/Implementation:** Single extends [MediaEntity](arkts-avsession-avmusictemplate-mediaentity-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-avMusicTemplate-interface Single extends MediaEntity--><!--Device-avMusicTemplate-interface Single extends MediaEntity-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## downloadProgress

```TypeScript
downloadProgress?: int
```

歌曲下载进度。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Single-downloadProgress?: int--><!--Device-Single-downloadProgress?: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## downloadStatus

```TypeScript
downloadStatus?: DownloadStatus
```

歌曲下载状态。

**Type:** [DownloadStatus](arkts-avsession-avmusictemplate-downloadstatus-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Single-downloadStatus?: DownloadStatus--><!--Device-Single-downloadStatus?: DownloadStatus-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## favSubscribeData

```TypeScript
favSubscribeData: FavoriteData
```

收藏或订阅的信息。

**Type:** [FavoriteData](arkts-avsession-avmusictemplate-favoritedata-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Single-favSubscribeData: FavoriteData--><!--Device-Single-favSubscribeData: FavoriteData-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## isVip

```TypeScript
isVip: boolean
```

是否是VIP歌曲。true表示是，false表示不是。无默认值。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Single-isVip: boolean--><!--Device-Single-isVip: boolean-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## playInfo

```TypeScript
playInfo: PlayInfo
```

播放歌曲信息。

**Type:** [PlayInfo](arkts-avsession-avmusictemplate-playinfo-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Single-playInfo: PlayInfo--><!--Device-Single-playInfo: PlayInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## settings

```TypeScript
settings?: SettingItem[]
```

歌曲设置项的数组。

**Type:** [SettingItem](arkts-avsession-avmusictemplate-settingitem-i.md)[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Single-settings?: SettingItem[]--><!--Device-Single-settings?: SettingItem[]-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## singer

```TypeScript
singer: string
```

歌手名。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Single-singer: string--><!--Device-Single-singer: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## tags

```TypeScript
tags?: string[]
```

歌曲标签信息的数组。

**Type:** string[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Single-tags?: string[]--><!--Device-Single-tags?: string[]-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

