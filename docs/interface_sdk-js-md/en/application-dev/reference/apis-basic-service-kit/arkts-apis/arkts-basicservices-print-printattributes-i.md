# PrintAttributes

定义打印参数的接口。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-print-interface PrintAttributes--><!--Device-print-interface PrintAttributes-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## colorMode

```TypeScript
colorMode?: PrintColorMode
```

表示待打印文件的色彩模式。

**Type:** [PrintColorMode](arkts-basicservices-print-printcolormode-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PrintAttributes-colorMode?: PrintColorMode--><!--Device-PrintAttributes-colorMode?: PrintColorMode-End-->

**System capability:** SystemCapability.Print.PrintFramework

## copyNumber

```TypeScript
copyNumber?: int
```

表示文件打印份数。默认值为1。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PrintAttributes-copyNumber?: int--><!--Device-PrintAttributes-copyNumber?: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## directionMode

```TypeScript
directionMode?: PrintDirectionMode
```

表示待打印文件的方向。

**Type:** [PrintDirectionMode](arkts-basicservices-print-printdirectionmode-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PrintAttributes-directionMode?: PrintDirectionMode--><!--Device-PrintAttributes-directionMode?: PrintDirectionMode-End-->

**System capability:** SystemCapability.Print.PrintFramework

## duplexMode

```TypeScript
duplexMode?: PrintDuplexMode
```

表示待打印文件的单双面模式。

**Type:** [PrintDuplexMode](arkts-basicservices-print-printduplexmode-e.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PrintAttributes-duplexMode?: PrintDuplexMode--><!--Device-PrintAttributes-duplexMode?: PrintDuplexMode-End-->

**System capability:** SystemCapability.Print.PrintFramework

## pageRange

```TypeScript
pageRange?: PrintPageRange
```

表示待打印文件的页面范围。

**Type:** [PrintPageRange](arkts-basicservices-print-printpagerange-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PrintAttributes-pageRange?: PrintPageRange--><!--Device-PrintAttributes-pageRange?: PrintPageRange-End-->

**System capability:** SystemCapability.Print.PrintFramework

## pageSize

```TypeScript
pageSize?: PrintPageSize | PrintPageType
```

表示待打印文件的纸张类型。

**Type:** [PrintPageSize](arkts-basicservices-print-printpagesize-i.md) \| PrintPageType

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PrintAttributes-pageSize?: PrintPageSize | PrintPageType--><!--Device-PrintAttributes-pageSize?: PrintPageSize | PrintPageType-End-->

**System capability:** SystemCapability.Print.PrintFramework

