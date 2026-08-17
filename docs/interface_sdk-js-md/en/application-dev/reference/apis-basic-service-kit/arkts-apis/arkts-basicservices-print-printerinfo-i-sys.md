# PrinterInfo (System API)

Provides the printer information.

**Since:** 23

<!--Device-print-interface PrinterInfo--><!--Device-print-interface PrinterInfo-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { print } from 'print';
```

## capability

```TypeScript
capability?: PrinterCapability
```

Printer capability.

**Type:** [PrinterCapability](arkts-basicservices-print-printercapability-i-sys.md)

**Since:** 23

<!--Device-PrinterInfo-capability?: PrinterCapability--><!--Device-PrinterInfo-capability?: PrinterCapability-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

## description

```TypeScript
description?: string
```

Printer description.

**Type:** string

**Since:** 23

<!--Device-PrinterInfo-description?: string--><!--Device-PrinterInfo-description?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

## options

```TypeScript
options?: Object
```

Printer options. The value is a JSON object string.

**Type:** Object

**Since:** 23

<!--Device-PrinterInfo-options?: Object--><!--Device-PrinterInfo-options?: Object-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

## printerIcon

```TypeScript
printerIcon?: int
```

Resource ID of the printer icon. The default value is **-1**.

**Type:** int

**Since:** 23

<!--Device-PrinterInfo-printerIcon?: int--><!--Device-PrinterInfo-printerIcon?: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

## printerId

```TypeScript
printerId: string
```

Printer ID.

**Type:** string

**Since:** 23

<!--Device-PrinterInfo-printerId: string--><!--Device-PrinterInfo-printerId: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

## printerName

```TypeScript
printerName: string
```

Printer name.

**Type:** string

**Since:** 23

<!--Device-PrinterInfo-printerName: string--><!--Device-PrinterInfo-printerName: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

## printerState

```TypeScript
printerState: PrinterState
```

Printer state.

**Type:** [PrinterState](arkts-basicservices-print-printerstate-e.md)

**Since:** 23

<!--Device-PrinterInfo-printerState: PrinterState--><!--Device-PrinterInfo-printerState: PrinterState-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

