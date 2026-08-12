# createCustomizedToneAttrs

## Modules to Import

```TypeScript
import { systemSoundManager } from '@kit.AudioKit';
```

## createCustomizedToneAttrs

```TypeScript
function createCustomizedToneAttrs(): ToneAttrs
```

Create customized tone attributes.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-systemSoundManager-function createCustomizedToneAttrs(): ToneAttrs--><!--Device-systemSoundManager-function createCustomizedToneAttrs(): ToneAttrs-End-->

**System capability:** SystemCapability.Multimedia.SystemSound.Core

**Return value:**

| Type | Description |
| --- | --- |
| [ToneAttrs](arkts-audio-systemsoundmanager-toneattrs-i.md) | Tone attributes created. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Caller is not a system application. |

## Examples

```TypeScript
let toneAttrs: systemSoundManager.ToneAttrs = systemSoundManager.createCustomizedToneAttrs();
```

