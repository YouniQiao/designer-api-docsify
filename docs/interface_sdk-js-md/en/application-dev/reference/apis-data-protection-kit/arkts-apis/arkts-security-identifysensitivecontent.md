# @ohos.security.identifySensitiveContent(Identify sensitive file)

This module identifies sensitive information in a specified file based on the input Policy. The system matches the file content against the provided Policy (including sensitive labels, keyword sets, and regular expressions) and returns the matched sensitive content.

**Since:** 21

**ArkTS mode:** Supports only ArkTS-Dyn, since version 21.

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { identifySensitiveContent } from '@kit.DataProtectionKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [scanFile(Identify sensitive file)](arkts-dataprotection-identifysensitivecontent-scanfile-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [MatchResult(Identify sensitive file)](arkts-dataprotection-identifysensitivecontent-matchresult-i.md) |
| [Policy(Identify sensitive file)](arkts-dataprotection-identifysensitivecontent-policy-i.md) |
