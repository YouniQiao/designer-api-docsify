# DataInfo

存放接收的数据信息，包括通道Id和数据。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-proxyChannelManager-interface DataInfo--><!--Device-proxyChannelManager-interface DataInfo-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## Modules to Import

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## channelId

```TypeScript
channelId: int
```

代理通道的channelId。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataInfo-channelId: int--><!--Device-DataInfo-channelId: int-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## data

```TypeScript
data: ArrayBuffer
```

接收到的字节数据。

**Type:** ArrayBuffer

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataInfo-data: ArrayBuffer--><!--Device-DataInfo-data: ArrayBuffer-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

