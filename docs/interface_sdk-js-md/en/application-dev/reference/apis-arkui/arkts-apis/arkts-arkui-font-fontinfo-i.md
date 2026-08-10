# FontInfo

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-font-interface FontInfo--><!--Device-font-interface FontInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { font } from 'kits/@kit.ArkUI';
```

## family

```TypeScript
family: string
```

系统字体的字体家族。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontInfo-family: string--><!--Device-FontInfo-family: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fullName

```TypeScript
fullName: string
```

系统字体的名称。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontInfo-fullName: string--><!--Device-FontInfo-fullName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## italic

```TypeScript
italic: boolean
```

系统字体是否倾斜。

默认值：false

值为true，表示斜体字体，值为false，表示非斜体字体。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontInfo-italic: boolean--><!--Device-FontInfo-italic: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## monoSpace

```TypeScript
monoSpace: boolean
```

系统字体是否等宽。

默认值：false

值为true，表示等宽字体，值为false，表示非等宽字体。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontInfo-monoSpace: boolean--><!--Device-FontInfo-monoSpace: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path: string
```

系统字体的文件路径。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontInfo-path: string--><!--Device-FontInfo-path: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## postScriptName

```TypeScript
postScriptName: string
```

系统字体的postScript名称。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontInfo-postScriptName: string--><!--Device-FontInfo-postScriptName: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## subfamily

```TypeScript
subfamily: string
```

系统字体的子字体家族。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontInfo-subfamily: string--><!--Device-FontInfo-subfamily: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## symbolic

```TypeScript
symbolic: boolean
```

系统字体是否支持符号字体。

默认值：false

值为true，表示支持符号字体，值为false，表示不支持符号字体。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontInfo-symbolic: boolean--><!--Device-FontInfo-symbolic: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## weight

```TypeScript
weight: int
```

系统字体的字重。

取值范围：[100,900]，取值间隔为100，分别对应  
[FontWeight](../../../reference/apis-arkgraphics2d/js-apis-graphics-text.md#fontweight)枚举中的值。

默认值：100

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontInfo-weight: int--><!--Device-FontInfo-weight: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width: int
```

系统字体的宽度。

取值范围：[1,9]，取值间隔为1，分别对应[FontWidth](../../../reference/apis-arkgraphics2d/js-apis-graphics-text.md#fontwidth)枚举中的值。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontInfo-width: int--><!--Device-FontInfo-width: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

