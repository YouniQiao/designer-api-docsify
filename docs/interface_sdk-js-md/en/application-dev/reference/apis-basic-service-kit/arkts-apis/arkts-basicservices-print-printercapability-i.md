# PrinterCapability

Defines the printer capabilities.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-print-interface PrinterCapability--><!--Device-print-interface PrinterCapability-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## colorMode

```TypeScript
colorMode: int
```

Color mode.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterCapability-colorMode: int--><!--Device-PrinterCapability-colorMode: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## duplexMode

```TypeScript
duplexMode: int
```

Simplex or duplex mode.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterCapability-duplexMode: int--><!--Device-PrinterCapability-duplexMode: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## minMargin

```TypeScript
minMargin?: PrintMargin
```

Minimum margin of the printer.

**Type:** [PrintMargin](arkts-basicservices-print-printmargin-i.md)

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterCapability-minMargin?: PrintMargin--><!--Device-PrinterCapability-minMargin?: PrintMargin-End-->

**System capability:** SystemCapability.Print.PrintFramework

## options

```TypeScript
options?: Object
```

Printer options. The value is a JSON object string.

**Type:** Object

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PrinterCapability-options?: Object--><!--Device-PrinterCapability-options?: Object-End-->

**System capability:** SystemCapability.Print.PrintFramework

## pageSize

```TypeScript
pageSize: Array<PrintPageSize>
```

List of page sizes supported by the printer.

**Type:** Array&lt;PrintPageSize&gt;

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterCapability-pageSize: Array<PrintPageSize>--><!--Device-PrinterCapability-pageSize: Array<PrintPageSize>-End-->

**System capability:** SystemCapability.Print.PrintFramework

## resolution

```TypeScript
resolution?: Array<PrintResolution>
```

List of resolutions supported by the printer.

**Type:** Array&lt;PrintResolution&gt;

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterCapability-resolution?: Array<PrintResolution>--><!--Device-PrinterCapability-resolution?: Array<PrintResolution>-End-->

**System capability:** SystemCapability.Print.PrintFramework

