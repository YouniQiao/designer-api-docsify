# SettingItem

设置项的定义。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-avMusicTemplate-interface SettingItem--><!--Device-avMusicTemplate-interface SettingItem-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## desc

```TypeScript
desc: string
```

设置项的描述。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SettingItem-desc: string--><!--Device-SettingItem-desc: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## id

```TypeScript
id: string
```

设置项的唯一ID。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SettingItem-id: string--><!--Device-SettingItem-id: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## mediaId

```TypeScript
mediaId: string
```

与当前设置关联的媒体ID。

如果设置与当前媒体信息相关联，需要设置mediaId；否则，不需要设置mediaId。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SettingItem-mediaId: string--><!--Device-SettingItem-mediaId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## settingType

```TypeScript
settingType?: SettingType
```

设置项的类型。

**Type:** [SettingType](arkts-avsession-avmusictemplate-settingtype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SettingItem-settingType?: SettingType--><!--Device-SettingItem-settingType?: SettingType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## settingValue

```TypeScript
settingValue?: string | boolean | SettingContent[] | WantAgent
```

设置项的值。

- 当settingType为SettingType.SWITCH时，该值为boolean类型。  
- 当settingType为SettingType.LIST时，该值为SettingContent数组。  
- 当settingType为SettingType.JUMP时，该值为string类型。

**Type:** string \| boolean \| SettingContent[] \| WantAgent

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SettingItem-settingValue?: string | boolean | SettingContent[] | WantAgent--><!--Device-SettingItem-settingValue?: string | boolean | SettingContent[] | WantAgent-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## title

```TypeScript
title: string
```

设置项的标题。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SettingItem-title: string--><!--Device-SettingItem-title: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

