# Resource

本模块提供资源相关信息，包括应用包名、应用模块名、资源ID等。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Resource--><!--Device-unnamed-export interface Resource-End-->

**System capability:** SystemCapability.Global.ResourceManager

## bundleName

```TypeScript
bundleName: string
```

应用包名。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Resource-bundleName: string--><!--Device-Resource-bundleName: string-End-->

**System capability:** SystemCapability.Global.ResourceManager

## id

```TypeScript
id: long
```

资源ID，取值如下：

- 应用资源区间：[0x01000000, 0x06FFFFFF] 和 [0x08000000, 0xFFFFFFFF]，表示应用自身的资源ID。  
- 系统资源区间：[0x07000000, 0x07FFFFFF]，表示系统预置的资源ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Resource-id: long--><!--Device-Resource-id: long-End-->

**System capability:** SystemCapability.Global.ResourceManager

## moduleName

```TypeScript
moduleName: string
```

应用模块名。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Resource-moduleName: string--><!--Device-Resource-moduleName: string-End-->

**System capability:** SystemCapability.Global.ResourceManager

## params

```TypeScript
params?: any[]
```

资源参数，包括：资源名（string类型）、格式化接口替换值（按占位符顺序提供string或number）、复数接口量词（number类型，表示数量）。格式化接口的替换值用于字符串格式化时的参数替换，复数接口的量词用于选择多语言环境下的复数形式。

**Type:** any[]

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Resource-params?: any[]--><!--Device-Resource-params?: any[]-End-->

**System capability:** SystemCapability.Global.ResourceManager

## type

```TypeScript
type?: int
```

资源类型，取值如下：&lt;br&gt;- 10001: color&lt;br&gt;- 10002: float&lt;br&gt;- 10003: string&lt;br&gt;- 10004: plural&lt;br&gt;- 10005: boolean&lt;br&gt;- 10006: intarray&lt;br&gt;- 10007: integer&lt;br&gt;- 10008: pattern&lt;br&gt;- 10009: strarray&lt;br&gt;- 20000: media&lt;br&gt;- 30000: rawfile&lt;br&gt;- 40000: symbol

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Resource-type?: int--><!--Device-Resource-type?: int-End-->

**System capability:** SystemCapability.Global.ResourceManager

