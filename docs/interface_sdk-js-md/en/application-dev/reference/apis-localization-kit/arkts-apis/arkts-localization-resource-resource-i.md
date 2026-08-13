# Resource

This module provides resource-related information, including the application package name, application module name, and resource ID.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface Resource--><!--Device-unnamed-export interface Resource-End-->

**System capability:** SystemCapability.Global.ResourceManager

## bundleName

```TypeScript
bundleName: string
```

Application bundle name.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Resource-bundleName: string--><!--Device-Resource-bundleName: string-End-->

**System capability:** SystemCapability.Global.ResourceManager

## id

```TypeScript
id: long
```

Resource ID. The value ranges are as follows: &lt;br&gt;- Application resource ranges: [0x01000000, 0x06FFFFFF] and [0x08000000, 0xFFFFFFFF], indicating the resource IDs of the application itself. &lt;br&gt;- System resource range: [0x07000000, 0x07FFFFFF], indicating the resource IDs preset by the system.

**Type:** long

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Resource-id: long--><!--Device-Resource-id: long-End-->

**System capability:** SystemCapability.Global.ResourceManager

## moduleName

```TypeScript
moduleName: string
```

Application module name.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Resource-moduleName: string--><!--Device-Resource-moduleName: string-End-->

**System capability:** SystemCapability.Global.ResourceManager

## params

```TypeScript
params?: Array<string | int | long | double | Resource>
```

Set params.

**Type:** Array&lt;string \| int \| long \| double \| [Resource](arkts-localization-resource-resource-i.md)&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-Resource-params?: Array<string | int | long | double | Resource>--><!--Device-Resource-params?: Array<string | int | long | double | Resource>-End-->

**System capability:** SystemCapability.Global.ResourceManager

## type

```TypeScript
type?: int
```

Resource type. The options are as follows: &lt;br&gt;- 10001: color &lt;br&gt;- 10002: float &lt;br&gt;- 10003: string &lt;br&gt;- 10004: plural &lt;br&gt;- 10005: boolean &lt;br&gt;- 10006: intarray &lt;br&gt;- 10007: integer &lt;br&gt;- 10008: pattern &lt;br&gt;- 10009: strarray &lt;br&gt;- 20000: media &lt;br&gt;- 30000: rawfile &lt;br&gt;- 40000: symbol

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Resource-type?: int--><!--Device-Resource-type?: int-End-->

**System capability:** SystemCapability.Global.ResourceManager

