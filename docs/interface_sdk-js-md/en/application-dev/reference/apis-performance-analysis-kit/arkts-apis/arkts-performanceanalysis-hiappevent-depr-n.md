# hiAppEvent(Application Event Logging)

The **hiAppEvent** module provides the application event logging functions, such as writing application events to the event file and managing the event logging configuration.

> **NOTE：**
> 
> - The APIs provided by this module are deprecated since API version 9. You are advised to use
> [@ohos.hiviewdfx.hiAppEvent](arkts-performanceanalysis-hiappevent-n.md).

**Since:** 7

**Deprecated since:** 9

**Substitutes:** hiAppEvent

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
```

## Summary

### Namespaces

| Name | Description |
| --- | --- |
| [Event(Application Event Logging)](arkts-performanceanalysis-hiappevent-event-depr-n.md) | Provides constants that define the names of all predefined events.  \| Name \| Type \| Readable\| Writable\| Description \| \| ------------------------- \| ------ \| ---- \| ---- \| -------------------- \| \| USER_LOGIN \| string \| Yes \| No \| User login event. \| \| USER_LOGOUT \| string \| Yes \| No \| User logout event. \| \| DISTRIBUTED_SERVICE_START \| string \| Yes \| No \| Distributed service startup event.\| |
| [Param(Application Event Logging)](arkts-performanceanalysis-hiappevent-param-depr-n.md) | Provides constants that define the names of all predefined event parameters.  \| Name \| Type \| Readable\| Writable\| Description \| \| ------------------------------- \| ------ \| ---- \| ---- \| ------------------ \| \| USER_ID \| string \| Yes \| No \| Custom user ID. \| \| DISTRIBUTED_SERVICE_NAME \| string \| Yes \| No \| Distributed service name. \| \| DISTRIBUTED_SERVICE_INSTANCE_ID \| string \| Yes \| No \| Distributed service instance ID.\| |

### Functions

| Name | Description |
| --- | --- |
| [write(Application Event Logging)](arkts-performanceanalysis-hiappevent-write-depr-f.md#write) | Writes event information to the event file of the current day. This API uses a promise to return the result. |
| [write(Application Event Logging)](arkts-performanceanalysis-hiappevent-write-depr-f.md#write) | Writes event information to the event file of the current day. This API uses an asynchronous callback to return the result. |
| [configure(Application Event Logging)](arkts-performanceanalysis-hiappevent-configure-depr-f.md#configure) | Configures the application event logging function, such as setting the event logging switch and maximum size of the directory that stores the event logging files. |

### Interfaces

| Name | Description |
| --- | --- |
| [ConfigOption(Application Event Logging)](arkts-performanceanalysis-hiappevent-configoption-depr-i.md) | Provides the configuration items for application event logging. |

### Enums

| Name | Description |
| --- | --- |
| [EventType(Application Event Logging)](arkts-performanceanalysis-hiappevent-eventtype-depr-e.md) | Enumerates the event types. |
