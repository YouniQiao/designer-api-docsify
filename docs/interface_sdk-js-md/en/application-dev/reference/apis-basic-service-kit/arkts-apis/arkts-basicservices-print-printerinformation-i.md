# PrinterInformation

定义打印机信息的接口。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-print-interface PrinterInformation--><!--Device-print-interface PrinterInformation-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## alias

```TypeScript
alias?: string
```

表示打印机别名。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrinterInformation-alias?: string--><!--Device-PrinterInformation-alias?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## capability

```TypeScript
capability?: PrinterCapabilities
```

表示打印机能力。

**Type:** [PrinterCapabilities](arkts-basicservices-print-printercapabilities-i.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrinterInformation-capability?: PrinterCapabilities--><!--Device-PrinterInformation-capability?: PrinterCapabilities-End-->

**System capability:** SystemCapability.Print.PrintFramework

## description

```TypeScript
description?: string
```

表示打印机说明。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrinterInformation-description?: string--><!--Device-PrinterInformation-description?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## options

```TypeScript
options?: string
```

表示打印机详细信息。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrinterInformation-options?: string--><!--Device-PrinterInformation-options?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## preferences

```TypeScript
preferences?: PrinterPreferences
```

表示打印机首选项。

**Type:** [PrinterPreferences](arkts-basicservices-print-printerpreferences-i.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrinterInformation-preferences?: PrinterPreferences--><!--Device-PrinterInformation-preferences?: PrinterPreferences-End-->

**System capability:** SystemCapability.Print.PrintFramework

## printerId

```TypeScript
printerId: string
```

表示打印机ID。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrinterInformation-printerId: string--><!--Device-PrinterInformation-printerId: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## printerMake

```TypeScript
printerMake?: string
```

表示打印机型号。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrinterInformation-printerMake?: string--><!--Device-PrinterInformation-printerMake?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## printerName

```TypeScript
printerName: string
```

表示打印机名称。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrinterInformation-printerName: string--><!--Device-PrinterInformation-printerName: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## printerStatus

```TypeScript
printerStatus: PrinterStatus
```

表示当前打印机状态。

**Type:** [PrinterStatus](arkts-basicservices-print-printerstatus-e.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrinterInformation-printerStatus: PrinterStatus--><!--Device-PrinterInformation-printerStatus: PrinterStatus-End-->

**System capability:** SystemCapability.Print.PrintFramework

## selectedDriver

```TypeScript
selectedDriver?: PpdInfo
```

表示添加打印机时选择的驱动的信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**Type:** [PpdInfo](arkts-basicservices-print-ppdinfo-i.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrinterInformation-selectedDriver?: PpdInfo--><!--Device-PrinterInformation-selectedDriver?: PpdInfo-End-->

**System capability:** SystemCapability.Print.PrintFramework

## selectedProtocol

```TypeScript
selectedProtocol?: string
```

表示添加打印机时使用的协议。

**模型约束：** 此接口仅可在Stage模型下使用。

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrinterInformation-selectedProtocol?: string--><!--Device-PrinterInformation-selectedProtocol?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## uri

```TypeScript
uri?: string
```

表示打印机uri。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-PrinterInformation-uri?: string--><!--Device-PrinterInformation-uri?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

