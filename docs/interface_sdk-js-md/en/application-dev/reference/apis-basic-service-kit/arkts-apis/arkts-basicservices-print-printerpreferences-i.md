# PrinterPreferences

定义打印机首选项的接口。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-print-interface PrinterPreferences--><!--Device-print-interface PrinterPreferences-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## borderless

```TypeScript
borderless?: boolean
```

表示是否无边距打印，true表示无边距，false表示有边距。默认值为false。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrinterPreferences-borderless?: boolean--><!--Device-PrinterPreferences-borderless?: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## defaultCollate

```TypeScript
defaultCollate?: boolean
```

表示默认出纸顺序。true表示逐份打印，false表示逐页打印。默认值为逐份。

**模型约束：** 此接口仅可在Stage模型下使用。

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrinterPreferences-defaultCollate?: boolean--><!--Device-PrinterPreferences-defaultCollate?: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## defaultColorMode

```TypeScript
defaultColorMode?: PrintColorMode
```

表示默认色彩模式。默认值为黑白。

**模型约束：** 此接口仅可在Stage模型下使用。

**Type:** [PrintColorMode](arkts-basicservices-print-printcolormode-e.md)

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrinterPreferences-defaultColorMode?: PrintColorMode--><!--Device-PrinterPreferences-defaultColorMode?: PrintColorMode-End-->

**System capability:** SystemCapability.Print.PrintFramework

## defaultDuplexMode

```TypeScript
defaultDuplexMode?: PrintDuplexMode
```

表示默认单双面模式。

**Type:** [PrintDuplexMode](arkts-basicservices-print-printduplexmode-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrinterPreferences-defaultDuplexMode?: PrintDuplexMode--><!--Device-PrinterPreferences-defaultDuplexMode?: PrintDuplexMode-End-->

**System capability:** SystemCapability.Print.PrintFramework

## defaultMediaType

```TypeScript
defaultMediaType?: string
```

表示默认纸张类型。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrinterPreferences-defaultMediaType?: string--><!--Device-PrinterPreferences-defaultMediaType?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## defaultOrientation

```TypeScript
defaultOrientation?: PrintOrientationMode
```

表示默认打印方向。

**Type:** [PrintOrientationMode](arkts-basicservices-print-printorientationmode-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrinterPreferences-defaultOrientation?: PrintOrientationMode--><!--Device-PrinterPreferences-defaultOrientation?: PrintOrientationMode-End-->

**System capability:** SystemCapability.Print.PrintFramework

## defaultPageSizeId

```TypeScript
defaultPageSizeId?: string
```

表示默认纸张尺寸的ID，其范围包含国际标准化组织定义的标准纸张尺寸，如ISO_A4，和系统中定义的非标准的纸张尺寸，如Custom.178x254mm，表示这种纸张尺寸为178毫米 x 254毫米。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrinterPreferences-defaultPageSizeId?: string--><!--Device-PrinterPreferences-defaultPageSizeId?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## defaultPrintQuality

```TypeScript
defaultPrintQuality?: PrintQuality
```

表示默认打印质量。

**Type:** [PrintQuality](arkts-basicservices-print-printquality-e.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrinterPreferences-defaultPrintQuality?: PrintQuality--><!--Device-PrinterPreferences-defaultPrintQuality?: PrintQuality-End-->

**System capability:** SystemCapability.Print.PrintFramework

## defaultReverse

```TypeScript
defaultReverse?: boolean
```

表示默认打印顺序。true表示逆序打印，false表示正序打印。默认值为正序打印。

**模型约束：** 此接口仅可在Stage模型下使用。

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PrinterPreferences-defaultReverse?: boolean--><!--Device-PrinterPreferences-defaultReverse?: boolean-End-->

**System capability:** SystemCapability.Print.PrintFramework

## options

```TypeScript
options?: string
```

表示打印机首选项中不在以上字段中的其他字段，查询打印机或者从打印机驱动获取，以json格式存储在string中。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-PrinterPreferences-options?: string--><!--Device-PrinterPreferences-options?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

