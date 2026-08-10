# @ohos.multimodalInput.infraredEmitter(IR Management)

红外管理模块提供产生特定频率和大小的红外信号，以及查询设备支持的频率范围等功能。

> **说明：**

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace infraredEmitter--><!--Device-unnamed-declare namespace infraredEmitter-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InfraredEmitter

## Modules to Import

```TypeScript
import { infraredEmitter } from 'kits/@kit.InputKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getInfraredFrequencies](arkts-input-infraredemitter-getinfraredfrequencies-f.md#getinfraredfrequencies) | 查询设备支持的红外信号的频率范围。 |
| [hasIrEmitter](arkts-input-infraredemitter-hasiremitter-f.md#hasiremitter) | 查询设备是否配备红外发射器。使用Promise异步回调。 |
| [transmitInfrared](arkts-input-infraredemitter-transmitinfrared-f.md#transmitinfrared) | 产生特定频率和特定电平大小的红外信号。 |

### Interfaces

| Name | Description |
| --- | --- |
| [InfraredFrequency](arkts-input-infraredemitter-infraredfrequency-i.md) | 红外信号的频率范围。 |

