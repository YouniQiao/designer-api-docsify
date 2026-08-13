# FingerprintEvent (System API)

Provides fingerprint gesture event types and the offset of the fingerprint sensor relative to the side edge.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface FingerprintEvent--><!--Device-unnamed-export declare interface FingerprintEvent-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { shortKey } from '@kit.InputKit';
```

## action

```TypeScript
action: FingerprintAction
```

Enumeration of fingerprint gesture event types.

**Type:** [FingerprintAction](arkts-input-multimodalinput-shortkey-fingerprintaction-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-FingerprintEvent-action: FingerprintAction--><!--Device-FingerprintEvent-action: FingerprintAction-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## distanceX

```TypeScript
distanceX: double
```

Offset relative to the short axis of the side fingerprint device (positive values indicate movement to the right, and negative values indicate movement to the left).

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-FingerprintEvent-distanceX: double--><!--Device-FingerprintEvent-distanceX: double-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

## distanceY

```TypeScript
distanceY: double
```

Offset relative to the long axis of the side fingerprint device (positive values indicate upward movement, and negative values indicate downward movement).

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-FingerprintEvent-distanceY: double--><!--Device-FingerprintEvent-distanceY: double-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Core

**System API:** This is a system API.

