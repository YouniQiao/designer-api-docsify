# ChannelState

通道状态发生变化时，代理通道上报的通道连接状态。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-proxyChannelManager-enum ChannelState--><!--Device-proxyChannelManager-enum ChannelState-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## CHANNEL_WAIT_RESUME

```TypeScript
CHANNEL_WAIT_RESUME = 0
```

连接已断开，通道不可用。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelState-CHANNEL_WAIT_RESUME = 0--><!--Device-ChannelState-CHANNEL_WAIT_RESUME = 0-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## CHANNEL_RESUME

```TypeScript
CHANNEL_RESUME = 1
```

连接已恢复，通道可用。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelState-CHANNEL_RESUME = 1--><!--Device-ChannelState-CHANNEL_RESUME = 1-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## CHANNEL_EXCEPTION_SOFTWARE_FAILED

```TypeScript
CHANNEL_EXCEPTION_SOFTWARE_FAILED = 2
```

其他软件错误导致通道不可用。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelState-CHANNEL_EXCEPTION_SOFTWARE_FAILED = 2--><!--Device-ChannelState-CHANNEL_EXCEPTION_SOFTWARE_FAILED = 2-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

## CHANNEL_BR_NO_PAIRED

```TypeScript
CHANNEL_BR_NO_PAIRED = 3
```

蓝牙配对关系被删除，通道不可用。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ChannelState-CHANNEL_BR_NO_PAIRED = 3--><!--Device-ChannelState-CHANNEL_BR_NO_PAIRED = 3-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

