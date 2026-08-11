# @ohos.security.identifySensitiveContent(Identify sensitive file)

This module identifies sensitive information in a specified file based on the input [Policy](arkts-dataprotection-identifysensitivecontent-policy-i.md).The system matches the file content against the provided [Policy](arkts-dataprotection-identifysensitivecontent-policy-i.md) (including sensitive labels,keyword sets, and regular expressions) and returns the matched sensitive content.

**Since:** 21

<!--Device-unnamed-declare namespace identifySensitiveContent--><!--Device-unnamed-declare namespace identifySensitiveContent-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { identifySensitiveContent } from 'kits/@kit.DataProtectionKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [scanFile](arkts-dataprotection-identifysensitivecontent-scanfile-f.md#scanfile) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [MatchResult](arkts-dataprotection-identifysensitivecontent-matchresult-i.md) |
| [Policy](arkts-dataprotection-identifysensitivecontent-policy-i.md) |
