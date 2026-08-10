# PrinterInfo

定义打印信息的接口。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-print-interface PrinterInfo--><!--Device-print-interface PrinterInfo-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## capability

```TypeScript
capability?: PrinterCapability
```

表示打印机功能。

**Type:** [PrinterCapability](arkts-basicservices-print-printercapability-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterInfo-capability?: PrinterCapability--><!--Device-PrinterInfo-capability?: PrinterCapability-End-->

**System capability:** SystemCapability.Print.PrintFramework

## description

```TypeScript
description?: string
```

表示打印机说明。

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterInfo-description?: string--><!--Device-PrinterInfo-description?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## options

```TypeScript
options?: Object
```

表示JSON对象字符串。

**Type:** Object

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterInfo-options?: Object--><!--Device-PrinterInfo-options?: Object-End-->

**System capability:** SystemCapability.Print.PrintFramework

## printerIcon

```TypeScript
printerIcon?: int
```

表示打印机图标的资源ID。默认值为-1。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterInfo-printerIcon?: int--><!--Device-PrinterInfo-printerIcon?: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## printerId

```TypeScript
printerId: string
```

表示打印机ID。

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterInfo-printerId: string--><!--Device-PrinterInfo-printerId: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## printerName

```TypeScript
printerName: string
```

表示打印机名称。

**Type:** string

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterInfo-printerName: string--><!--Device-PrinterInfo-printerName: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## printerState

```TypeScript
printerState: PrinterState
```

表示当前打印机状态。

**Type:** [PrinterState](arkts-basicservices-print-printerstate-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterInfo-printerState: PrinterState--><!--Device-PrinterInfo-printerState: PrinterState-End-->

**System capability:** SystemCapability.Print.PrintFramework

