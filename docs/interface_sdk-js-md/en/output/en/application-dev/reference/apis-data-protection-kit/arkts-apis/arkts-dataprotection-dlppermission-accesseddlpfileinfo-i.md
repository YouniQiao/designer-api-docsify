# AccessedDLPFileInfo

Represents the information about a DLP file opened.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-dlpPermission-export interface AccessedDLPFileInfo--><!--Device-dlpPermission-export interface AccessedDLPFileInfo-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## lastOpenTime

```TypeScript
lastOpenTime: number
```

Time when the file was last opened. The value must be greater than or equal to 0. Unit: s.

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-AccessedDLPFileInfo-lastOpenTime: number--><!--Device-AccessedDLPFileInfo-lastOpenTime: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## uri

```TypeScript
uri: string
```

URI of the DLP file. The value contains a maximum of 4095 bytes. If the value is out of range, error code 19100001 is thrown.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-AccessedDLPFileInfo-uri: string--><!--Device-AccessedDLPFileInfo-uri: string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

