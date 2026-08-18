# PrinterRange (System API)

Defines the print range.

**Since:** 23

<!--Device-print-interface PrinterRange--><!--Device-print-interface PrinterRange-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { print } from '@kit.BasicServicesKit';
```

## endPage

```TypeScript
endPage?: int
```

End page. The default value is the maximum number of pages of the file to be printed.

**Type:** int

**Since:** 23

<!--Device-PrinterRange-endPage?: int--><!--Device-PrinterRange-endPage?: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

## pages

```TypeScript
pages?: Array<int>
```

Page range set of the file to print. The default value is empty.

**Type:** Array&lt;int&gt;

**Since:** 23

<!--Device-PrinterRange-pages?: Array<int>--><!--Device-PrinterRange-pages?: Array<int>-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

## startPage

```TypeScript
startPage?: int
```

Start page. The default value is **1**.

**Type:** int

**Since:** 23

<!--Device-PrinterRange-startPage?: int--><!--Device-PrinterRange-startPage?: int-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

