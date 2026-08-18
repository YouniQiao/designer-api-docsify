# @ohos.multimodalInput.infraredEmitter(IR Management)

The **infraredEmitter** module generates IR signals of the specified frequency and size, and queries the frequency range supported by the device.

**Since:** 23

<!--Device-unnamed-declare namespace infraredEmitter--><!--Device-unnamed-declare namespace infraredEmitter-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InfraredEmitter

## Modules to Import

```TypeScript
import { infraredEmitter } from '@kit.InputKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [hasIrEmitter(IR Management)](arkts-input-infraredemitter-hasiremitter-f.md) | Checks whether the device has an infrared transmitter. This API uses a promise to return the result. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getInfraredFrequencies(IR Management)](arkts-input-infraredemitter-getinfraredfrequencies-f-sys.md) | Queries the frequency range of IR signals supported by the device. |
| [transmitInfrared(IR Management)](arkts-input-infraredemitter-transmitinfrared-f-sys.md) | Generates IR signals at the specified frequency and level. |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [InfraredFrequency(IR Management)](arkts-input-infraredemitter-infraredfrequency-i-sys.md) | Defines the frequency range of IR signals. |
<!--DelEnd-->

