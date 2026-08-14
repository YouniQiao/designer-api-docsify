# DLPProperty (System API)

Represents the authorization information.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-dlpPermission-export interface DLPProperty--><!--Device-dlpPermission-export interface DLPProperty-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { dlpPermission } from 'dlpPermission';
```

## allowedOpenCount

```TypeScript
allowedOpenCount?: number
```

Number of allowed opening times. The default value is **0**. No value range restriction is specified.

**Type:** number

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

<!--Device-DLPProperty-allowedOpenCount?: number--><!--Device-DLPProperty-allowedOpenCount?: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## countdown

```TypeScript
countdown?: number
```

Validity period for file viewing, in seconds. The default value is 0. After the validity period expires, the file is automatically closed. The value range is [-2&lt;sup&gt;31&lt;/sup&gt;, 2&lt;sup&gt;31&lt;/sup&gt;-1].

**Type:** number

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DLPProperty-countdown?: number--><!--Device-DLPProperty-countdown?: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## extensionFields

```TypeScript
extensionFields?: Record<string, Object>
```

Extended attribute of a DLP file. This parameter is left empty by default.

**Type:** Record&lt;string, Object&gt;

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DLPProperty-extensionFields?: Record<string, Object>--><!--Device-DLPProperty-extensionFields?: Record<string, Object>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## fileId

```TypeScript
fileId?: string
```

System account ID. This parameter is left empty by default. The value contains a maximum of 255 bytes. If the value is out of range, error code 401 is thrown.

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Deprecated since:** -1

<!--Device-DLPProperty-fileId?: string--><!--Device-DLPProperty-fileId?: string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## waterMarkConfig

```TypeScript
waterMarkConfig?: boolean
```

Whether watermarks are required. **true**: yes; **false**: no. This parameter is left empty by default.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-DLPProperty-waterMarkConfig?: boolean--><!--Device-DLPProperty-waterMarkConfig?: boolean-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

