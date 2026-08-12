# PrintPageRange

Defines the print range.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-print-interface PrintPageRange--><!--Device-print-interface PrintPageRange-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## endPage

```TypeScript
endPage?: int
```

End page. The default value is the maximum number of pages of the file to be printed.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PrintPageRange-endPage?: int--><!--Device-PrintPageRange-endPage?: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

## pages

```TypeScript
pages?: Array<int>
```

Page range set of the file to print. The default value is empty.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PrintPageRange-pages?: Array<int>--><!--Device-PrintPageRange-pages?: Array<int>-End-->

**System capability:** SystemCapability.Print.PrintFramework

## startPage

```TypeScript
startPage?: int
```

Start page. The default value is **1**.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-PrintPageRange-startPage?: int--><!--Device-PrintPageRange-startPage?: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

