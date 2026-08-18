# PictureScanProgress

Defines the progress of scanning pictures.

**Since:** 23

<!--Device-scan-interface PictureScanProgress--><!--Device-scan-interface PictureScanProgress-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { scan } from '@kit.BasicServicesKit';
```

## isFinal

```TypeScript
isFinal: boolean
```

Whether the picture is the last one to be scanned. The value **true** indicates that the picture is the last one to be scanned, and **false** indicates that the picture is not the last one.

**Type:** boolean

**Since:** 23

<!--Device-PictureScanProgress-isFinal: boolean--><!--Device-PictureScanProgress-isFinal: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## pictureFd

```TypeScript
pictureFd: int
```

File descriptor of the scanned picture.

**Type:** int

**Since:** 23

<!--Device-PictureScanProgress-pictureFd: int--><!--Device-PictureScanProgress-pictureFd: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## progress

```TypeScript
progress: int
```

Progress percentage, whose value ranges from 0 to 100. Unit: %

**Type:** int

**Since:** 23

<!--Device-PictureScanProgress-progress: int--><!--Device-PictureScanProgress-progress: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

