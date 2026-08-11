# createCustomizedToneAttrs

## Modules to Import

```TypeScript
import { systemSoundManager } from 'kits/@kit.AudioKit';
```

## createCustomizedToneAttrs

```TypeScript
function createCustomizedToneAttrs(): ToneAttrs
```

Create customized tone attributes.

**Since:** 12

<!--Device-systemSoundManager-function createCustomizedToneAttrs(): ToneAttrs--><!--Device-systemSoundManager-function createCustomizedToneAttrs(): ToneAttrs-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
let toneAttrs: systemSoundManager.ToneAttrs = systemSoundManager.createCustomizedToneAttrs();
```
