# PrinterRange

Defines the print range.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-print-interface PrinterRange--><!--Device-print-interface PrinterRange-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## endPage

```TypeScript
endPage?: int
```

End page. The default value is the maximum number of pages of the file to be printed.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterRange-endPage?: int--><!--Device-PrinterRange-endPage?: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## pages

```TypeScript
pages?: Array<int>
```

Page range set of the file to print. The default value is empty.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterRange-pages?: Array<int>--><!--Device-PrinterRange-pages?: Array<int>-End-->

**System capability:** SystemCapability.Print.PrintFramework

## startPage

```TypeScript
startPage?: int
```

Start page. The default value is **1**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-PrinterRange-startPage?: int--><!--Device-PrinterRange-startPage?: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

