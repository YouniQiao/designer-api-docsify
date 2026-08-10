# PrintJob

定义打印任务的接口。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-print-interface PrintJob--><!--Device-print-interface PrintJob-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## colorMode

```TypeScript
colorMode: int
```

表示色彩模式。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-colorMode: int--><!--Device-PrintJob-colorMode: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## copyNumber

```TypeScript
copyNumber: int
```

表示文件列表副本。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-copyNumber: int--><!--Device-PrintJob-copyNumber: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## duplexMode

```TypeScript
duplexMode: int
```

表示单双面打印模式。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-duplexMode: int--><!--Device-PrintJob-duplexMode: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## fdList

```TypeScript
fdList: Array<int>
```

表示待打印文件fd列表。

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-fdList: Array<int>--><!--Device-PrintJob-fdList: Array<int>-End-->

**System capability:** SystemCapability.Print.PrintFramework

## isLandscape

```TypeScript
isLandscape: boolean
```

表示是否横向打印。true表示横向打印，false表示纵向打印。默认值为false。

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-isLandscape: boolean--><!--Device-PrintJob-isLandscape: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## isSequential

```TypeScript
isSequential: boolean
```

表示是否连续打印。true表示连续打印，false表示不连续打印。默认值为false。

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-isSequential: boolean--><!--Device-PrintJob-isSequential: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## jobId

```TypeScript
jobId: string
```

表示打印任务ID。

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-jobId: string--><!--Device-PrintJob-jobId: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## jobState

```TypeScript
jobState: PrintJobState
```

表示当前打印任务状态。

**Type:** [PrintJobState](arkts-basicservices-print-printjobstate-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-jobState: PrintJobState--><!--Device-PrintJob-jobState: PrintJobState-End-->

**System capability:** SystemCapability.Print.PrintFramework

## jobSubstate

```TypeScript
jobSubstate: PrintJobSubState
```

表示当前打印任务子状态。

**Type:** [PrintJobSubState](arkts-basicservices-print-printjobsubstate-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PrintJob-jobSubstate: PrintJobSubState--><!--Device-PrintJob-jobSubstate: PrintJobSubState-End-->

**System capability:** SystemCapability.Print.PrintFramework

## margin

```TypeScript
margin?: PrintMargin
```

表示当前页边距设置。

**Type:** [PrintMargin](arkts-basicservices-print-printmargin-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-margin?: PrintMargin--><!--Device-PrintJob-margin?: PrintMargin-End-->

**System capability:** SystemCapability.Print.PrintFramework

## options

```TypeScript
options?: Object
```

表示JSON对象字符串。

**Type:** Object

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-options?: Object--><!--Device-PrintJob-options?: Object-End-->

**System capability:** SystemCapability.Print.PrintFramework

## pageRange

```TypeScript
pageRange: PrinterRange
```

表示打印范围大小。

**Type:** [PrinterRange](arkts-basicservices-print-printerrange-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-pageRange: PrinterRange--><!--Device-PrintJob-pageRange: PrinterRange-End-->

**System capability:** SystemCapability.Print.PrintFramework

## pageSize

```TypeScript
pageSize: PrintPageSize
```

表示选定的页面尺寸。

**Type:** [PrintPageSize](arkts-basicservices-print-printpagesize-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-pageSize: PrintPageSize--><!--Device-PrintJob-pageSize: PrintPageSize-End-->

**System capability:** SystemCapability.Print.PrintFramework

## preview

```TypeScript
preview?: PreviewAttribute
```

表示预览设置。

**Type:** [PreviewAttribute](arkts-basicservices-print-previewattribute-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-preview?: PreviewAttribute--><!--Device-PrintJob-preview?: PreviewAttribute-End-->

**System capability:** SystemCapability.Print.PrintFramework

## printerId

```TypeScript
printerId: string
```

表示负责打印的打印机ID。

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrintJob-printerId: string--><!--Device-PrintJob-printerId: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

