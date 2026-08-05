# DeathRecipient

Subscribes to death notifications of a remote object. When the remote object is dead, the local end will receive a notification and **[onRemoteDied]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_** will be called. A remote object is dead when the process holding the object is terminated or the device of the remote object is shut down or restarted. If the local and remote objects belong to different devices, the remote object is dead when the device holding the remote object is detached from the network.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-rpc-interface DeathRecipient--><!--Device-rpc-interface DeathRecipient-End-->

**System capability:** SystemCapability.Communication.IPC.Core

## onRemoteDied

```TypeScript
onRemoteDied(): void
```

Called to perform subsequent operations when a death notification of the remote object is received.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-DeathRecipient-onRemoteDied(): void--><!--Device-DeathRecipient-onRemoteDied(): void-End-->

**System capability:** SystemCapability.Communication.IPC.Core

**Example**

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

**Type:** OnRemoteDiedFunc

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-DeathRecipient-onRemoteDied: OnRemoteDiedFunc--><!--Device-DeathRecipient-onRemoteDied: OnRemoteDiedFunc-End-->

**System capability:** SystemCapability.Communication.IPC.Core

