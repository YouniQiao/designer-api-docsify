# WaitingReason

枚举，定义任务等待的原因。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-agent-enum WaitingReason--><!--Device-agent-enum WaitingReason-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## TASK_QUEUE_FULL

```TypeScript
TASK_QUEUE_FULL = 0x00
```

表示任务因任务队列已满而进入等待状态。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-WaitingReason-TASK_QUEUE_FULL = 0x00--><!--Device-WaitingReason-TASK_QUEUE_FULL = 0x00-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## NETWORK_NOT_MATCH

```TypeScript
NETWORK_NOT_MATCH = 0x01
```

表示任务因所需网络条件不满足而进入等待状态。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-WaitingReason-NETWORK_NOT_MATCH = 0x01--><!--Device-WaitingReason-NETWORK_NOT_MATCH = 0x01-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## APP_BACKGROUND

```TypeScript
APP_BACKGROUND = 0x02
```

表示任务因应用长时间处于后台而进入等待状态。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-WaitingReason-APP_BACKGROUND = 0x02--><!--Device-WaitingReason-APP_BACKGROUND = 0x02-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

## USER_INACTIVATED

```TypeScript
USER_INACTIVATED = 0x03
```

表示任务因所属用户处于非激活状态而进入等待状态。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-WaitingReason-USER_INACTIVATED = 0x03--><!--Device-WaitingReason-USER_INACTIVATED = 0x03-End-->

**System capability:** SystemCapability.Request.FileTransferAgent

