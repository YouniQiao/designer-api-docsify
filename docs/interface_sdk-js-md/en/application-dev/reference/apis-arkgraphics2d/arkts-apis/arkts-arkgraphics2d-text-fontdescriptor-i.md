# FontDescriptor

字体描述符信息。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-text-interface FontDescriptor--><!--Device-text-interface FontDescriptor-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { text } from 'kits/@kit.ArkGraphics2D';
```

## copyright

```TypeScript
copyright?: string
```

字体版权信息，可取任意字符串，默认为空字符串。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FontDescriptor-copyright?: string--><!--Device-FontDescriptor-copyright?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## fontFamily

```TypeScript
fontFamily?: string
```

字体家族，可取任意字符串，默认为空字符串。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontDescriptor-fontFamily?: string--><!--Device-FontDescriptor-fontFamily?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## fontFeatures

```TypeScript
fontFeatures?: Array<string>
```

字体支持的OpenType特性标签数组，默认为空数组。数组中每个元素为特性标签字符串（如'liga'表示标准连字、'kern'表示字距调整），表示该字体支持的字体特性。

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-FontDescriptor-fontFeatures?: Array<string>--><!--Device-FontDescriptor-fontFeatures?: Array<string>-End-->

**System capability:** SystemCapability.Graphics.Drawing

## fontSubfamily

```TypeScript
fontSubfamily?: string
```

子字体家族，可取任意字符串，默认为空字符串。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontDescriptor-fontSubfamily?: string--><!--Device-FontDescriptor-fontSubfamily?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## fullName

```TypeScript
fullName?: string
```

字体名称，可取任意字符串，默认为空字符串。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontDescriptor-fullName?: string--><!--Device-FontDescriptor-fullName?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## index

```TypeScript
index?: int
```

字体索引，字体文件为ttc类型时有效，ttf类型统一为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FontDescriptor-index?: int--><!--Device-FontDescriptor-index?: int-End-->

**System capability:** SystemCapability.Graphics.Drawing

## italic

```TypeScript
italic?: int
```

是否是斜体字体，0表示非斜体，1表示斜体，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontDescriptor-italic?: int--><!--Device-FontDescriptor-italic?: int-End-->

**System capability:** SystemCapability.Graphics.Drawing

## languages

```TypeScript
languages?: Array<string>
```

字体支持的语言列表，默认为空数组。数组中每个元素为BCP 47格式的语言标签字符串（如'en'、'zh-Hans'），表示该字体支持的书写语言。

**Type:** Array&lt;string&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-FontDescriptor-languages?: Array<string>--><!--Device-FontDescriptor-languages?: Array<string>-End-->

**System capability:** SystemCapability.Graphics.Drawing

## license

```TypeScript
license?: string
```

字体许可证信息，可取任意字符串，默认为空字符串。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FontDescriptor-license?: string--><!--Device-FontDescriptor-license?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## localFamilyName

```TypeScript
localFamilyName?: string
```

根据系统语言配置提取字体家族名称，字体文件中若无当前语言对应配置则取“en”对应信息。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FontDescriptor-localFamilyName?: string--><!--Device-FontDescriptor-localFamilyName?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## localFullName

```TypeScript
localFullName?: string
```

根据系统语言配置提取字体全名，字体文件中若无当前语言对应配置则取“en”对应信息。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FontDescriptor-localFullName?: string--><!--Device-FontDescriptor-localFullName?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## localPostscriptName

```TypeScript
localPostscriptName?: string
```

根据系统语言配置提取字体唯一标识，字体文件中若无当前语言对应配置则取“en”对应信息。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FontDescriptor-localPostscriptName?: string--><!--Device-FontDescriptor-localPostscriptName?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## localSubFamilyName

```TypeScript
localSubFamilyName?: string
```

根据系统语言配置提取子字体家族名称，字体文件中若无当前语言对应配置则取“en”对应信息。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FontDescriptor-localSubFamilyName?: string--><!--Device-FontDescriptor-localSubFamilyName?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## manufacture

```TypeScript
manufacture?: string
```

字体制造商信息，可取任意字符串，默认为空字符串。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FontDescriptor-manufacture?: string--><!--Device-FontDescriptor-manufacture?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## monoSpace

```TypeScript
monoSpace?: boolean
```

是否是等宽字体，true表示等宽，false表示非等宽，默认值为false。

**Type:** boolean

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontDescriptor-monoSpace?: boolean--><!--Device-FontDescriptor-monoSpace?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## path

```TypeScript
path?: string
```

字体绝对路径，可取遵循系统限制的任意字符串，默认为空字符串。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontDescriptor-path?: string--><!--Device-FontDescriptor-path?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## postScriptName

```TypeScript
postScriptName?: string
```

字体唯一标识名称，可取任意字符串，默认为空字符串。

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontDescriptor-postScriptName?: string--><!--Device-FontDescriptor-postScriptName?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## symbolic

```TypeScript
symbolic?: boolean
```

是否支持符号，true表示支持，false表示不支持，默认值为false。

**Type:** boolean

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontDescriptor-symbolic?: boolean--><!--Device-FontDescriptor-symbolic?: boolean-End-->

**System capability:** SystemCapability.Graphics.Drawing

## trademark

```TypeScript
trademark?: string
```

字体商标信息，可取任意字符串，默认为空字符串。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FontDescriptor-trademark?: string--><!--Device-FontDescriptor-trademark?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## variationAxisRecords

```TypeScript
variationAxisRecords?: Array<FontVariationAxis>
```

字体可变轴记录数组，用于描述字体支持的可变轴信息。非可变字体此字段为undefined。

**Type:** Array&lt;FontVariationAxis&gt;

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-FontDescriptor-variationAxisRecords?: Array<FontVariationAxis>--><!--Device-FontDescriptor-variationAxisRecords?: Array<FontVariationAxis>-End-->

**System capability:** SystemCapability.Graphics.Drawing

## variationInstanceRecords

```TypeScript
variationInstanceRecords?: Array<FontVariationInstance>
```

字体可变实例记录数组，用于描述字体支持的可变实例信息。非可变字体此字段为undefined。

**Type:** Array&lt;FontVariationInstance&gt;

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-FontDescriptor-variationInstanceRecords?: Array<FontVariationInstance>--><!--Device-FontDescriptor-variationInstanceRecords?: Array<FontVariationInstance>-End-->

**System capability:** SystemCapability.Graphics.Drawing

## version

```TypeScript
version?: string
```

字体版本，可取任意字符串，默认为空字符串。

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-FontDescriptor-version?: string--><!--Device-FontDescriptor-version?: string-End-->

**System capability:** SystemCapability.Graphics.Drawing

## weight

```TypeScript
weight?: FontWeight
```

字体字重，默认值为0。

**Type:** [FontWeight](../../apis-arkui/arkts-apis/arkts-arkui-fontweight-e.md)

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontDescriptor-weight?: FontWeight--><!--Device-FontDescriptor-weight?: FontWeight-End-->

**System capability:** SystemCapability.Graphics.Drawing

## width

```TypeScript
width?: int
```

字体宽度，取值范围1-9整数，默认值为0。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-FontDescriptor-width?: int--><!--Device-FontDescriptor-width?: int-End-->

**System capability:** SystemCapability.Graphics.Drawing

