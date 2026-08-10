# DialogInfo

对话框信息的定义。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-avMusicTemplate-interface DialogInfo--><!--Device-avMusicTemplate-interface DialogInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## buttons

```TypeScript
buttons?: DialogButtonInfo[]
```

对话框按钮的数组。

**Type:** [DialogButtonInfo](arkts-avsession-avmusictemplate-dialogbuttoninfo-i.md)[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogInfo-buttons?: DialogButtonInfo[]--><!--Device-DialogInfo-buttons?: DialogButtonInfo[]-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## description

```TypeScript
description?: string
```

对话框的其他信息。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogInfo-description?: string--><!--Device-DialogInfo-description?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## dialogId

```TypeScript
dialogId: string
```

对话框的唯一ID。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogInfo-dialogId: string--><!--Device-DialogInfo-dialogId: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## dialogType

```TypeScript
dialogType: DialogType
```

对话框的类型。

**Type:** [DialogType](arkts-avsession-avmusictemplate-dialogtype-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogInfo-dialogType: DialogType--><!--Device-DialogInfo-dialogType: DialogType-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## qrCodes

```TypeScript
qrCodes?: QrCodeInfo[]
```

对话框二维码的数组。

当设置了二维码信息时，此对话框将被识别为二维码对话框，并将优先显示二维码信息。最多可以设置两个。

**Type:** [QrCodeInfo](arkts-avsession-avmusictemplate-qrcodeinfo-i.md)[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogInfo-qrCodes?: QrCodeInfo[]--><!--Device-DialogInfo-qrCodes?: QrCodeInfo[]-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## text

```TypeScript
text?: string
```

对话框的内容。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogInfo-text?: string--><!--Device-DialogInfo-text?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## title

```TypeScript
title?: string
```

对话框的标题。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DialogInfo-title?: string--><!--Device-DialogInfo-title?: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

