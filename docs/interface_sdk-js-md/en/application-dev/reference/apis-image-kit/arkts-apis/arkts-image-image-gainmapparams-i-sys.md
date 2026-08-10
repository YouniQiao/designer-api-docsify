# GainmapParams (System API)

Gainmap（增益图）参数设置选项。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-image-interface GainmapParams--><!--Device-image-interface GainmapParams-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## isFullSizeGainmap

```TypeScript
isFullSizeGainmap: boolean
```

返回Picture中的Gainmap（增益图）是否使用全尺寸图。

true表示使用全尺寸图，宽高和主图一致；false表示不使用全尺寸图，宽高均为主图的一半。默认值为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GainmapParams-isFullSizeGainmap: boolean--><!--Device-GainmapParams-isFullSizeGainmap: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

**System API:** This is a system API.

