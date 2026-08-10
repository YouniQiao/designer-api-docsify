# DeathRecipient

用于订阅远端对象的死亡通知。当被订阅该通知的远端对象死亡时，本端可收到消息，调用[onRemoteDied](arkts-ipc-rpc-deathrecipient-i.md#onremotedied)接口。远端对象死亡可以为远端对象所在进程死亡，远端对象所在设备关机或重启，当远端对象与本端对象属于不同设备时，也可为远端对象离开组网时。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-rpc-interface DeathRecipient--><!--Device-rpc-interface DeathRecipient-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Modules to Import

```TypeScript
import { rpc } from 'kits/@kit.IPCKit';
```

## onRemoteDied

```TypeScript
onRemoteDied(): void
```

在成功添加死亡通知订阅后，当远端对象死亡时，将自动调用本方法。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-DeathRecipient-onRemoteDied(): void--><!--Device-DeathRecipient-onRemoteDied(): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## Examples

```TypeScript
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

class MyDeathRecipient implements rpc.DeathRecipient {
  onRemoteDied() {
    hilog.info(0x0000, 'testTag', 'server died');
  }
}
```

## onRemoteDied

```TypeScript
onRemoteDied: OnRemoteDiedFunc
```

Called to perform subsequent operations when a death notification of the remote object is received.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DeathRecipient-onRemoteDied: OnRemoteDiedFunc--><!--Device-DeathRecipient-onRemoteDied: OnRemoteDiedFunc-End-->

**System capability:** SystemCapability.Communication.IPC.Core

