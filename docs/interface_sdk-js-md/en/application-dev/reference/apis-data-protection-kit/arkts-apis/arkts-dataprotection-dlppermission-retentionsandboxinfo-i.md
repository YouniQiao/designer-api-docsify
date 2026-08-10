# RetentionSandboxInfo

保留沙箱的沙箱信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-dlpPermission-export interface RetentionSandboxInfo--><!--Device-dlpPermission-export interface RetentionSandboxInfo-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## appIndex

```TypeScript
appIndex: number
```

表示DLP沙箱应用索引。取值范围为1001到1100。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RetentionSandboxInfo-appIndex: number--><!--Device-RetentionSandboxInfo-appIndex: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## bundleName

```TypeScript
bundleName: string
```

表示应用包名。最小7字节，最大128字节。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RetentionSandboxInfo-bundleName: string--><!--Device-RetentionSandboxInfo-bundleName: string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## docUris

```TypeScript
docUris: Array<string>
```

表示DLP文件的URI列表。不对Array长度进行限制，每个string长度不超过4095字节。

**Type:** Array&lt;string&gt;

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-RetentionSandboxInfo-docUris: Array<string>--><!--Device-RetentionSandboxInfo-docUris: Array<string>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

