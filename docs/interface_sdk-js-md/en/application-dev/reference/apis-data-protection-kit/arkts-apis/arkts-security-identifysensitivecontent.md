# @ohos.security.identifySensitiveContent(Identify sensitive file)

/*
 Copyright (c) 2025 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 21

<!--Device-unnamed-declare namespace identifySensitiveContent--><!--Device-unnamed-declare namespace identifySensitiveContent-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { identifySensitiveContent } from '@kit.DataProtectionKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [scanFile](arkts-dataprotection-identifysensitivecontent-scanfile-f.md#scanfile) | Identifies sensitive content in a specified file based on the configured policy and returns the identified result array, including the matched sensitivity labels, matched content, and number of matched items. This API uses a promise to return the result. |

### Interfaces

| Name | Description |
| --- | --- |
| [MatchResult](arkts-dataprotection-identifysensitivecontent-matchresult-i.md) | Displays the identification result of sensitive content. |
| [Policy](arkts-dataprotection-identifysensitivecontent-policy-i.md) | Defines the policy for sensitive content identification. In a single policy, keywords and regular expressions are combined in sequence, and two-level matching is performed. First, keyword matching is performed. If a keyword is matched, regular expression matching is performed within a scope of 100 bytes: from the position 50 bytes before the matched position of the keyword to that 50 bytes after the matched position. If only keywords are set, only keyword matching is performed. If only regular expressions are set, only regular expression matching is performed. Multiple policies are independent of each other, and each policy is applied separately during scanning. sensitiveLabel is used to mark the matching result to identify the specific policy matched. |

