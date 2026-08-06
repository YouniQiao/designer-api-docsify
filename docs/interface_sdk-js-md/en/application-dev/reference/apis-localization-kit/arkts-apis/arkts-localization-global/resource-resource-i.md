# Resource

This module provides resource-related information, including the application package name, application module name,and resource ID.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Resource--><!--Device-unnamed-export interface Resource-End-->

**System capability:** SystemCapability.Global.ResourceManager

## bundleName

```TypeScript
bundleName: string
```

Application bundle name.

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

Resource ID. The value ranges are as follows:\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_- Application resource ranges: [0x01000000, 0x06FFFFFF] and [0x08000000, 0xFFFFFFFF], indicating the resource IDs of the application itself.\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- System resource range: [0x07000000, 0x07FFFFFF], indicating the resource IDs preset by the system.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Resource-id: long--><!--Device-Resource-id: long-End-->

**System capability:** SystemCapability.Global.ResourceManager

## moduleName

```TypeScript
moduleName: string
```

Application module name.

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

Resource parameters, including the resource name (string type), replacement values for formatting APIs (string or number types in the order of placeholders), and plural quantifier (number type, indicating the quantity). The replacement value of the formatting API is used for parameter substitution during string formatting, while the quantifier of the plural API is used to select the plural form in multilingual environments.

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

Resource type. The options are as follows:\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_- 10001: color\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_- 10002: float\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_- 10003: string\_\_\_HTML\_TAG\_DESC\_USD\_3\_\_\_- 10004: plural\_\_\_HTML\_TAG\_DESC\_USD\_4\_\_\_- 10005: boolean\_\_\_HTML\_TAG\_DESC\_USD\_5\_\_\_- 10006: intarray\_\_\_HTML\_TAG\_DESC\_USD\_6\_\_\_- 10007: integer\_\_\_HTML\_TAG\_DESC\_USD\_7\_\_\_- 10008: pattern\_\_\_HTML\_TAG\_DESC\_USD\_8\_\_\_- 10009: strarray\_\_\_HTML\_TAG\_DESC\_USD\_9\_\_\_- 20000: media\_\_\_HTML\_TAG\_DESC\_USD\_10\_\_\_- 30000: rawfile\_\_\_HTML\_TAG\_DESC\_USD\_11\_\_\_- 40000: symbol

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Resource-type?: int--><!--Device-Resource-type?: int-End-->

**System capability:** SystemCapability.Global.ResourceManager

