# AccessedDLPFileInfo

表示被打开的DLP文件的信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-dlpPermission-export interface AccessedDLPFileInfo--><!--Device-dlpPermission-export interface AccessedDLPFileInfo-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## lastOpenTime

```TypeScript
lastOpenTime: number
```

表示DLP文件最近打开时间。单位：s。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-AccessedDLPFileInfo-lastOpenTime: number--><!--Device-AccessedDLPFileInfo-lastOpenTime: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## uri

```TypeScript
uri: string
```

表示DLP文件的uri。不超过4095字节。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-AccessedDLPFileInfo-uri: string--><!--Device-AccessedDLPFileInfo-uri: string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

