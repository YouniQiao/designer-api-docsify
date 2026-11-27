# wantAgent(WantAgent Module)

```TypeScript
declare namespace wantAgent
```

The WantAgent module provides APIs for creating and comparing WantAgent objects, and obtaining the user ID and bundle name of a WantAgent object.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [wantAgent/wantAgent](arkts-ability-wantagent-n.md)

<!--Device-unnamed-declare namespace wantAgent--><!--Device-unnamed-declare namespace wantAgent-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import wantAgent from '@ohos.wantAgent';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [cancel](arkts-ability-wantagent-depr-cancel-f.md#cancel-1) | Cancels a WantAgent object. This API uses an asynchronous callback to return the result. |
| [cancel](arkts-ability-wantagent-depr-cancel-f.md#cancel-2) | Cancels a WantAgent object. This API uses a promise to return the result. |
| [equal](arkts-ability-wantagent-depr-equal-f.md#equal-1) | Checks whether two WantAgent objects are equal to determine whether the same operation is from the same application. This API uses an asynchronous callback to return the result. |
| [equal](arkts-ability-wantagent-depr-equal-f.md#equal-2) | Checks whether two WantAgent objects are equal to determine whether the same operation is from the same application. This API uses a promise to return the result. |
| [getBundleName](arkts-ability-wantagent-depr-getbundlename-f.md#getbundlename-1) | Obtains the bundle name of a WantAgent. |
| [getBundleName](arkts-ability-wantagent-depr-getbundlename-f.md#getbundlename-2) | Obtains the bundle name of a WantAgent. |
| [getUid](arkts-ability-wantagent-depr-getuid-f.md#getuid-1) | Obtains the user ID of a WantAgent object. This API uses an asynchronous callback to return the result. |
| [getUid](arkts-ability-wantagent-depr-getuid-f.md#getuid-2) | Obtains the user ID of a WantAgent object. This API uses a promise to return the result. |
| [getWantAgent](arkts-ability-wantagent-depr-getwantagent-f.md#getwantagent-1) | Creates a WantAgent object. If the creation fails, a null WantAgent object is returned. This API uses an asynchronous callback to return the result. |
| [getWantAgent](arkts-ability-wantagent-depr-getwantagent-f.md#getwantagent-2) | Creates a WantAgent object. If the creation fails, a null WantAgent object is returned. This API uses a promise to return the result. |
| [trigger](arkts-ability-wantagent-depr-trigger-f.md#trigger-1) | Triggers a WantAgent object. This API uses an asynchronous callback to return the result. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [getWant](arkts-ability-wantagent-depr-getwant-f-sys.md#getwant-1) | Obtains the Want in a WantAgent object. This API uses an asynchronous callback to return the result. |
| [getWant](arkts-ability-wantagent-depr-getwant-f-sys.md#getwant-2) | Obtains the Want in a WantAgent object. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [CompleteData](arkts-ability-wantagent-depr-completedata-i.md) | Describes the data returned by after wantAgent.trigger is called. |

### Enums

| Name | Description |
| --- | --- |
| [OperationType](arkts-ability-wantagent-depr-operationtype-e.md) | Identifies the operation for using a WantAgent, such as starting an ability or sending a common event. |
| [WantAgentFlags](arkts-ability-wantagent-depr-wantagentflags-e.md) | Enumerates flags for using a WantAgent. |
