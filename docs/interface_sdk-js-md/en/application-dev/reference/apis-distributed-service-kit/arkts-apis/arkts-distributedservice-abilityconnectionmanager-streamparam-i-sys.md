# StreamParam (System API)

Streaming configuration parameters.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-abilityConnectionManager-interface StreamParam--><!--Device-abilityConnectionManager-interface StreamParam-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { abilityConnectionManager } from 'kits/@kit.DistributedServiceKit';
```

## bitrate

```TypeScript
bitrate?: int
```

视频码率，默认80(kbps)。仅在发送端有效。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StreamParam-bitrate?: int--><!--Device-StreamParam-bitrate?: int-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

## colorSpaceConversionTarget

```TypeScript
colorSpaceConversionTarget?: colorSpaceManager.ColorSpace
```

转换的目标色彩空间。目前仅支持BT709_LIMIT。如果发送端的视频格式为HDR且需要在传输时转换为SDR，则应设置此参数。

**Type:** colorSpaceManager.ColorSpace

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StreamParam-colorSpaceConversionTarget?: colorSpaceManager.ColorSpace--><!--Device-StreamParam-colorSpaceConversionTarget?: colorSpaceManager.ColorSpace-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

## name

```TypeScript
name: string
```

流名称，接收端必须与发送端保持一致。

**Type:** string

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StreamParam-name: string--><!--Device-StreamParam-name: string-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

## role

```TypeScript
role: StreamRole
```

流传输角色，可以是接收流或发送流。

**Type:** [StreamRole](arkts-distributedservice-abilityconnectionmanager-streamrole-e-sys.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-StreamParam-role: StreamRole--><!--Device-StreamParam-role: StreamRole-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**System API:** This is a system API.

