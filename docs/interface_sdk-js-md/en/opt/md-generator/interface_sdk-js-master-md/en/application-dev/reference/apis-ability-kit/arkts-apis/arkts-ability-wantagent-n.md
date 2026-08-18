# wantAgent

The WantAgent module encapsulates a [Want](arkts-ability-app-ability-want-want-c.md#want) object, enabling an application to trigger a WantAgent object to perform specified operations (such as starting an ability or publishing a common event) at a future time. The module provides the APIs for creating a WantAgent object, obtaining the bundle name and UID of the application to which a WantAgent object belongs, proactively triggering a WantAgent object, and checking whether two WantAgent objects are the same. A typical use scenario of WantAgent is notification processing. For example, when a user touches a notification, the [trigger](arkts-ability-wantagent-trigger-f.md#trigger) API of WantAgent is triggered and the target application is started. For details, see [Notification](../../../notification/notification-with-wantagent.md).

**Since:** 23

<!--Device-unnamed-declare namespace wantAgent--><!--Device-unnamed-declare namespace wantAgent-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getBundleName](arkts-ability-wantagent-getbundlename-f.md#getbundlename) |
| [getBundleName](arkts-ability-wantagent-getbundlename-f.md#getbundlename) |
| [getUid](arkts-ability-wantagent-getuid-f.md#getuid) |
| [getUid](arkts-ability-wantagent-getuid-f.md#getuid) |
| [cancel](arkts-ability-wantagent-cancel-f.md#cancel) |
| [cancel](arkts-ability-wantagent-cancel-f.md#cancel) |
| [trigger](arkts-ability-wantagent-trigger-f.md#trigger) |
| [equal](arkts-ability-wantagent-equal-f.md#equal) |
| [equal](arkts-ability-wantagent-equal-f.md#equal) |
| [getWantAgent](arkts-ability-wantagent-getwantagent-f.md#getwantagent) |
| [getWantAgent](arkts-ability-wantagent-getwantagent-f.md#getwantagent) |
| [getOperationType](arkts-ability-wantagent-getoperationtype-f.md#getoperationtype) |
| [getOperationType](arkts-ability-wantagent-getoperationtype-f.md#getoperationtype) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getWant](arkts-ability-wantagent-getwant-f-sys.md#getwant-system-api) |
| [getWant](arkts-ability-wantagent-getwant-f-sys.md#getwant-system-api) |
| [triggerAsync](arkts-ability-wantagent-triggerasync-f-sys.md#triggerasync-system-api) |
| [setWantAgentMultithreading](arkts-ability-wantagent-setwantagentmultithreading-f-sys.md#setwantagentmultithreading-system-api) |
| [createLocalWantAgent](arkts-ability-wantagent-createlocalwantagent-f-sys.md#createlocalwantagent-system-api) |
| [isLocalWantAgent](arkts-ability-wantagent-islocalwantagent-f-sys.md#islocalwantagent-system-api) |
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
### Enums（系统接口）

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
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [LocalWantAgentInfo](arkts-ability-wantagent-localwantagentinfo-t-sys.md) |
<!--DelEnd-->
