# ContactSyncInfo

调用应用程序相关的联系人同步的信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-contact-interface ContactSyncInfo--><!--Device-contact-interface ContactSyncInfo-End-->

**System capability:** SystemCapability.Applications.ContactsData

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## completedBatches

```TypeScript
completedBatches: Array<int>
```

表示已成功同步的联系人的批处理标识符数组。

值的范围是从1到totalBatches。

**Type:** Array&lt;int&gt;

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ContactSyncInfo-completedBatches: Array<int>--><!--Device-ContactSyncInfo-completedBatches: Array<int>-End-->

**System capability:** SystemCapability.Applications.ContactsData

## lastSyncTime

```TypeScript
lastSyncTime: int
```

指示联系人同步的最新时间戳（毫秒）。

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ContactSyncInfo-lastSyncTime: int--><!--Device-ContactSyncInfo-lastSyncTime: int-End-->

**System capability:** SystemCapability.Applications.ContactsData

## mode

```TypeScript
mode: ContactSyncMode
```

联系人同步模式。

**Type:** [ContactSyncMode](arkts-contacts-contact-contactsyncmode-e.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ContactSyncInfo-mode: ContactSyncMode--><!--Device-ContactSyncInfo-mode: ContactSyncMode-End-->

**System capability:** SystemCapability.Applications.ContactsData

## syncId

```TypeScript
syncId: int
```

表示用于同步所有联系人的同步标识符。

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ContactSyncInfo-syncId: int--><!--Device-ContactSyncInfo-syncId: int-End-->

**System capability:** SystemCapability.Applications.ContactsData

## totalBatches

```TypeScript
totalBatches: int
```

指示要同步的联系人批次总数。

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ContactSyncInfo-totalBatches: int--><!--Device-ContactSyncInfo-totalBatches: int-End-->

**System capability:** SystemCapability.Applications.ContactsData

