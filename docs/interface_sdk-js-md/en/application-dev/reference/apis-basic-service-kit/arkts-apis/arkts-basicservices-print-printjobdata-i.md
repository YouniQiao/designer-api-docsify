# PrintJobData

定义打印任务的接口。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-print-interface PrintJobData--><!--Device-print-interface PrintJobData-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## binaryData

```TypeScript
binaryData?: Uint8Array
```

表示待打印二进制数据。

**Type:** Uint8Array

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-binaryData?: Uint8Array--><!--Device-PrintJobData-binaryData?: Uint8Array-End-->

**System capability:** SystemCapability.Print.PrintFramework

## colorMode

```TypeScript
colorMode: PrintColorMode
```

表示色彩模式。

**Type:** [PrintColorMode](arkts-basicservices-print-printcolormode-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-colorMode: PrintColorMode--><!--Device-PrintJobData-colorMode: PrintColorMode-End-->

**System capability:** SystemCapability.Print.PrintFramework

## copyNumber

```TypeScript
copyNumber: int
```

表示文件列表副本数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-copyNumber: int--><!--Device-PrintJobData-copyNumber: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## docFlavor

```TypeScript
docFlavor: DocFlavor
```

表示打印数据来源形式。

**Type:** [DocFlavor](arkts-basicservices-print-docflavor-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-docFlavor: DocFlavor--><!--Device-PrintJobData-docFlavor: DocFlavor-End-->

**System capability:** SystemCapability.Print.PrintFramework

## documentFormat

```TypeScript
documentFormat: PrintDocumentFormat
```

表示打印数据格式。

**Type:** [PrintDocumentFormat](arkts-basicservices-print-printdocumentformat-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-documentFormat: PrintDocumentFormat--><!--Device-PrintJobData-documentFormat: PrintDocumentFormat-End-->

**System capability:** SystemCapability.Print.PrintFramework

## duplexMode

```TypeScript
duplexMode: PrintDuplexMode
```

表示单双面打印模式。

**Type:** [PrintDuplexMode](arkts-basicservices-print-printduplexmode-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-duplexMode: PrintDuplexMode--><!--Device-PrintJobData-duplexMode: PrintDuplexMode-End-->

**System capability:** SystemCapability.Print.PrintFramework

## fdList

```TypeScript
fdList?: int[]
```

表示待打印文件fd列表。

**Type:** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-fdList?: int[]--><!--Device-PrintJobData-fdList?: int[]-End-->

**System capability:** SystemCapability.Print.PrintFramework

## isAutoRotate

```TypeScript
isAutoRotate?: boolean
```

表示是否自动旋转页面。true表示自动旋转页面，false表示不自动旋转页面。默认值为true。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-isAutoRotate?: boolean--><!--Device-PrintJobData-isAutoRotate?: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## isBorderless

```TypeScript
isBorderless?: boolean
```

表示是否无边框打印。true表示无边框打印，false表示有边框打印。默认值为true。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-isBorderless?: boolean--><!--Device-PrintJobData-isBorderless?: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## isCollate

```TypeScript
isCollate?: boolean
```

表示打印顺序方式。true表示逐页打印，false表示逐份打印。默认值为true。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-isCollate?: boolean--><!--Device-PrintJobData-isCollate?: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## isLandscape

```TypeScript
isLandscape: boolean
```

表示是否横向打印。true表示横向打印，false表示纵向打印。默认值为false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-isLandscape: boolean--><!--Device-PrintJobData-isLandscape: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## isReverse

```TypeScript
isReverse?: boolean
```

表示是否逆序打印。true表示逆序打印，false表示顺序打印。默认值为false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-isReverse?: boolean--><!--Device-PrintJobData-isReverse?: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## isSequential

```TypeScript
isSequential?: boolean
```

表示是否连续打印。true表示连续打印，false表示不连续打印。默认值为false。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-isSequential?: boolean--><!--Device-PrintJobData-isSequential?: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## jobId

```TypeScript
jobId?: string
```

表示打印任务的唯一标识符。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-jobId?: string--><!--Device-PrintJobData-jobId?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## jobName

```TypeScript
jobName: string
```

表示打印任务名称。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-jobName: string--><!--Device-PrintJobData-jobName: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## mediaType

```TypeScript
mediaType?: string
```

表示打印纸张类型。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-mediaType?: string--><!--Device-PrintJobData-mediaType?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## options

```TypeScript
options?: string
```

表示以JSON格式字符串化的对象。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-options?: string--><!--Device-PrintJobData-options?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## pageSize

```TypeScript
pageSize: PrintPageSize
```

表示选定的页面尺寸。

**Type:** [PrintPageSize](arkts-basicservices-print-printpagesize-i.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-pageSize: PrintPageSize--><!--Device-PrintJobData-pageSize: PrintPageSize-End-->

**System capability:** SystemCapability.Print.PrintFramework

## printQuality

```TypeScript
printQuality?: PrintQuality
```

表示打印质量。

**Type:** [PrintQuality](arkts-basicservices-print-printquality-e.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-printQuality?: PrintQuality--><!--Device-PrintJobData-printQuality?: PrintQuality-End-->

**System capability:** SystemCapability.Print.PrintFramework

## printerId

```TypeScript
printerId: string
```

表示打印机ID。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrintJobData-printerId: string--><!--Device-PrintJobData-printerId: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

