# @ohos.multimodalInput.infraredEmitter

The **infraredEmitter** module generates IR signals of the specified frequency and size, and queries the frequency range supported by the device.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace infraredEmitter--><!--Device-unnamed-declare namespace infraredEmitter-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InfraredEmitter

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getInfraredFrequencies](arkts-input-infraredemitter-getinfraredfrequencies-f.md#getinfraredfrequencies) | Queries the frequency range of IR signals supported by the device. |
| [hasIrEmitter](arkts-input-infraredemitter-hasiremitter-f.md#hasiremitter) | Checks whether the device has an infrared transmitter. This API uses a promise to return the result. |
| [transmitInfrared](arkts-input-infraredemitter-transmitinfrared-f.md#transmitinfrared) | Generates IR signals at the specified frequency and level. |

### Interfaces

| Name | Description |
| --- | --- |
| [InfraredFrequency](arkts-input-infraredemitter-infraredfrequency-i.md) | Defines the frequency range of IR signals. |

