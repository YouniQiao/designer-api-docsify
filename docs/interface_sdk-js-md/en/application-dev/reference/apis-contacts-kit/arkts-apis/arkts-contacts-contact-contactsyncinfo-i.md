# ContactSyncInfo

Information about contact synchronization for the calling application.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-contact-interface ContactSyncInfo--><!--Device-contact-interface ContactSyncInfo-End-->

**System capability:** SystemCapability.Applications.ContactsData

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## completedBatches

```TypeScript
completedBatches: Array<int>
```

Indicates the array of batch identifiers for contacts that have been synchronized successfully.

The range of values is from 1 to totalBatches.

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

Indicates the latest timestamp the contacts were synchronized in milliseconds.

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

The contact synchronization mode.

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

Indicates the sync identifier used for synchronizing all contacts.

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

Indicates the total number of batches of contacts to be synchronized.

**Type:** int

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ContactSyncInfo-totalBatches: int--><!--Device-ContactSyncInfo-totalBatches: int-End-->

**System capability:** SystemCapability.Applications.ContactsData

