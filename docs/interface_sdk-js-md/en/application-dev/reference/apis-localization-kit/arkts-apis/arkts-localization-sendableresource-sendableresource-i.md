# SendableResource

本模块提供SendableResource资源相关信息，包括应用包名、应用模块名、资源类型等。SendableResource实现了  
[ISendable](../../../arkts-utils/arkts-sendable.md#isendable)接口，支持跨线程传输，用于在多线程场景下访问应用资源。

**Inheritance/Implementation:** SendableResource extends [lang.ISendable](../../apis-arkts/arkts-apis/arkts-arkts-lang-isendable-i.md/arkts-arkts-lang-isendable-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface SendableResource extends lang.ISendable--><!--Device-unnamed-interface SendableResource extends lang.ISendable-End-->

**System capability:** SystemCapability.Global.ResourceManager

## bundleName

```TypeScript
bundleName: string
```

应用包名。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SendableResource-bundleName: string--><!--Device-SendableResource-bundleName: string-End-->

**System capability:** SystemCapability.Global.ResourceManager

## id

```TypeScript
id: number
```

资源ID，取值如下：  
- 应用资源区间：[0x01000000, 0x06FFFFFF] 和 [0x08000000, 0xFFFFFFFF]，表示应用自身的资源ID。  
- 系统资源区间：[0x07000000, 0x07FFFFFF]，表示系统预置的资源ID。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SendableResource-id: number--><!--Device-SendableResource-id: number-End-->

**System capability:** SystemCapability.Global.ResourceManager

## moduleName

```TypeScript
moduleName: string
```

应用模块名。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SendableResource-moduleName: string--><!--Device-SendableResource-moduleName: string-End-->

**System capability:** SystemCapability.Global.ResourceManager

## params

```TypeScript
params?: collections.Array <string | number>
```

资源参数，包括：资源名（string类型）、格式化接口替换值（按占位符顺序提供string或number）、复数接口量词（number类型，表示数量）。格式化接口的替换值用于字符串格式化时的参数替换，复数接口的量词用于选择多语言环境下的复数形式。

**Type:** collections.Array &lt;string \| number&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SendableResource-params?: collections.Array <string | number>--><!--Device-SendableResource-params?: collections.Array <string | number>-End-->

**System capability:** SystemCapability.Global.ResourceManager

## type

```TypeScript
type?: number
```

资源类型，取值如下：  
- 10001：color  
- 10002：float  
- 10003：string  
- 10004：plural  
- 10005：boolean  
- 10006：intarray  
- 10007：integer  
- 10008：pattern  
- 10009：strarray  
- 20000：media  
- 30000：rawfile  
- 40000：symbol

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SendableResource-type?: number--><!--Device-SendableResource-type?: number-End-->

**System capability:** SystemCapability.Global.ResourceManager

