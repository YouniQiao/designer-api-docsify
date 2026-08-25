# wantAgent

The WantAgent module encapsulates a [Want](arkts-ability-app-ability-want-want-c.md) object, enabling an application to trigger a WantAgent object to perform specified operations (such as starting an ability or publishing a common event) at a future time.The module provides the APIs for creating a WantAgent object, obtaining the bundle name and UID of the application to which a WantAgent object belongs, proactively triggering a WantAgent object, and checking whether two WantAgent objects are the same. A typical use scenario of WantAgent is notification processing. For example, when a user touches a notification, the [trigger](arkts-ability-wantagent-trigger-f.md) API of WantAgent is triggered and the target application is started. For details, see [Notification](../../../notification/notification-with-wantagent.md).

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { wantAgent, WantAgent } from '@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getBundleName](arkts-ability-wantagent-getbundlename-f.md) |
| [getBundleName](arkts-ability-wantagent-getbundlename-f.md) |
| [getUid](arkts-ability-wantagent-getuid-f.md) |
| [getUid](arkts-ability-wantagent-getuid-f.md) |
| [cancel](arkts-ability-wantagent-cancel-f.md) |
| [cancel](arkts-ability-wantagent-cancel-f.md) |
| [trigger](arkts-ability-wantagent-trigger-f.md) |
| [equal](arkts-ability-wantagent-equal-f.md) |
| [equal](arkts-ability-wantagent-equal-f.md) |
| [getWantAgent](arkts-ability-wantagent-getwantagent-f.md) |
| [getWantAgent](arkts-ability-wantagent-getwantagent-f.md) |
| [getOperationType](arkts-ability-wantagent-getoperationtype-f.md) |
| [getOperationType](arkts-ability-wantagent-getoperationtype-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getWant](arkts-ability-wantagent-getwant-f-sys.md) |
| [getWant](arkts-ability-wantagent-getwant-f-sys.md) |
| [triggerAsync](arkts-ability-wantagent-triggerasync-f-sys.md) |
| [setWantAgentMultithreading](arkts-ability-wantagent-setwantagentmultithreading-f-sys.md) |
| [createLocalWantAgent](arkts-ability-wantagent-createlocalwantagent-f-sys.md) |
| [isLocalWantAgent](arkts-ability-wantagent-islocalwantagent-f-sys.md) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CompleteData](arkts-ability-wantagent-completedata-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [WantAgentFlags](arkts-ability-wantagent-wantagentflags-e.md) |
| [OperationType](arkts-ability-wantagent-operationtype-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [OperationType](arkts-ability-wantagent-operationtype-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [TriggerInfo](arkts-ability-wantagent-triggerinfo-t.md) |
| [WantAgentInfo](arkts-ability-wantagent-wantagentinfo-t.md) |

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LocalWantAgentInfo](arkts-ability-wantagent-localwantagentinfo-t-sys.md) |
<!--DelEnd-->
