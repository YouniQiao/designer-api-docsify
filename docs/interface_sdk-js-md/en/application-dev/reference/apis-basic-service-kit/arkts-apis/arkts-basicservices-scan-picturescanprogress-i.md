# PictureScanProgress

定义图片扫描进度的接口。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-scan-interface PictureScanProgress--><!--Device-scan-interface PictureScanProgress-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## isFinal

```TypeScript
isFinal: boolean
```

是否是本次扫描的最后一张图片。true表示是最后一张图片，false表示不是最后一张图片。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PictureScanProgress-isFinal: boolean--><!--Device-PictureScanProgress-isFinal: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## pictureFd

```TypeScript
pictureFd: int
```

扫描图片的文件描述符。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PictureScanProgress-pictureFd: int--><!--Device-PictureScanProgress-pictureFd: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## progress

```TypeScript
progress: int
```

当前进度百分比，范围从0~100。单位：百分比。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-PictureScanProgress-progress: int--><!--Device-PictureScanProgress-progress: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

