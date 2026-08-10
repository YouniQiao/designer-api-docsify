# OtaMode (System API)

升级模式。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-update-export enum OtaMode--><!--Device-update-export enum OtaMode-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## REGULAR_OTA

```TypeScript
REGULAR_OTA = 0
```

正常升级，先下载完整升级包到本地，再执行安装升级，适用于大多数常规升级场景。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-OtaMode-REGULAR_OTA = 0--><!--Device-OtaMode-REGULAR_OTA = 0-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## STREAM_OTA

```TypeScript
STREAM_OTA = 1
```

流式升级，边下载边升级，无需等待完整下载，适用于存储空间受限或需要快速升级的场景。详见[术语](../../../basic-services/update/update-kit-term.md)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-OtaMode-STREAM_OTA = 1--><!--Device-OtaMode-STREAM_OTA = 1-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## AB_REGULAR_OTA

```TypeScript
AB_REGULAR_OTA = 2
```

AB正常升级，适用于A/B分区设备。详见[术语](../../../basic-services/update/update-kit-term.md)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-OtaMode-AB_REGULAR_OTA = 2--><!--Device-OtaMode-AB_REGULAR_OTA = 2-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## AB_STREAM_OTA

```TypeScript
AB_STREAM_OTA = 3
```

AB流式升级，适用于A/B分区设备。详见[术语](../../../basic-services/update/update-kit-term.md)。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-OtaMode-AB_STREAM_OTA = 3--><!--Device-OtaMode-AB_STREAM_OTA = 3-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

