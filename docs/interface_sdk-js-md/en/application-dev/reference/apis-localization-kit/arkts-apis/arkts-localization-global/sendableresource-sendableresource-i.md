# SendableResource

This module provides information related to \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_, including the application bundle package name,application module name, and resource type. \_\_\_INLINE\_CODE\_DESC\_USD\_1\_\_\_ implements the  
\_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ API and supports cross-thread transmission, enabling access to application resources in multi-thread scenarios.

**Inheritance/Implementation:** SendableResource extends [lang.ISendable](../../../apis-arkts/arkts-apis/arkts-arkts-lang-isendable-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-interface SendableResource extends lang.ISendable--><!--Device-unnamed-interface SendableResource extends lang.ISendable-End-->

**System capability:** SystemCapability.Global.ResourceManager

## bundleName

```TypeScript
bundleName: string
```

Application bundle name.

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

Resource ID. The value ranges are as follows:\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_- Application resource ranges: [0x01000000, 0x06FFFFFF] and [0x08000000, 0xFFFFFFFF], indicating the resource IDs of the application itself.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- System resource range: [0x07000000, 0x07FFFFFF], indicating the resource IDs preset by the system.

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

Application module name.

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

Resource parameters, including the resource name (string type), replacement values for formatting APIs (string or number in the order of placeholders), and plural quantifier (number type, indicating the quantity). The replacement value of the formatting API is used for parameter substitution during string formatting, while the quantifier of the plural API is used to select the plural form in multilingual environments.

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

Resource type. The options are as follows:\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_- 10001: color\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- 10002: float\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- 10003: string\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_- 10004: plural\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_- 10005: boolean\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_- 10006: intarray\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_- 10007: integer\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_- 10008: pattern\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_- 10009: strarray\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_- 20000: media\_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_- 30000: rawfile\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_- 40000: symbol

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-SendableResource-type?: number--><!--Device-SendableResource-type?: number-End-->

**System capability:** SystemCapability.Global.ResourceManager

