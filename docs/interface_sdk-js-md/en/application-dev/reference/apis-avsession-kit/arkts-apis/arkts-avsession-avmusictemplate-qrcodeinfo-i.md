# QrCodeInfo

二维码信息的定义。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-avMusicTemplate-interface QrCodeInfo--><!--Device-avMusicTemplate-interface QrCodeInfo-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## Modules to Import

```TypeScript
import { avMusicTemplate } from 'kits/@kit.AVSessionKit';
```

## codeData

```TypeScript
codeData?: image.PixelMap
```

二维码图片。

**Type:** image.PixelMap

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QrCodeInfo-codeData?: image.PixelMap--><!--Device-QrCodeInfo-codeData?: image.PixelMap-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## content

```TypeScript
content: string
```

二维码的内容。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QrCodeInfo-content: string--><!--Device-QrCodeInfo-content: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## detailName

```TypeScript
detailName: string
```

详情名称。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QrCodeInfo-detailName: string--><!--Device-QrCodeInfo-detailName: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## icon

```TypeScript
icon?: image.PixelMap
```

与二维码关联的应用图标，用于应用登录的二维码应显示目标应用的图标。

**Type:** image.PixelMap

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QrCodeInfo-icon?: image.PixelMap--><!--Device-QrCodeInfo-icon?: image.PixelMap-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## id

```TypeScript
id: string
```

用于唯一标识用户登录的二维码会话。

当二维码过期时，MediaUI将使用此ID从媒体应用查询并更新新的二维码。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QrCodeInfo-id: string--><!--Device-QrCodeInfo-id: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## price

```TypeScript
price: string
```

购买价格。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QrCodeInfo-price: string--><!--Device-QrCodeInfo-price: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## tips

```TypeScript
tips: string
```

提示信息。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QrCodeInfo-tips: string--><!--Device-QrCodeInfo-tips: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## titleName

```TypeScript
titleName: string
```

标题名称。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QrCodeInfo-titleName: string--><!--Device-QrCodeInfo-titleName: string-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

## validPeriod

```TypeScript
validPeriod: int
```

二维码有效期（单位：秒）。

当二维码到期时，二维码ID将用于再次查询并获得新的二维码。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-QrCodeInfo-validPeriod: int--><!--Device-QrCodeInfo-validPeriod: int-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVMusicTemplate

