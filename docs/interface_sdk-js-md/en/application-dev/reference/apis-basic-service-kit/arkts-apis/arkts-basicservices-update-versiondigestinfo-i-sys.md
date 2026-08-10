# VersionDigestInfo (System API)

版本摘要。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface VersionDigestInfo--><!--Device-update-export interface VersionDigestInfo-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## versionDigest

```TypeScript
versionDigest: string
```

版本摘要。长度范围[1，128]，单位：字符。从版本检查结果中获取，用于标识具体版本。超出范围时抛出异常。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-VersionDigestInfo-versionDigest: string--><!--Device-VersionDigestInfo-versionDigest: string-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

