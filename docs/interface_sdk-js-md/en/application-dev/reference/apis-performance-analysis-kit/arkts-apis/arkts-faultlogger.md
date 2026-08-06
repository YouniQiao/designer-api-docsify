# @ohos.faultLogger(FaultLogger)

The **faultLogger** APIs can be used to query fault logs of an application cached on the system. The APIs use the application bundle name and the UID allocated by the system as the unique key value.

The number of application fault logs stored in the system is limited by the system log pressure. You are advised to use [@ohos.hiviewdfx.hiAppEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ to subscribe to fault events such as  
**APP\_CRASH** and **APP\_FREEZE**.
    **NOTE**  
    
    The APIs of this module are no longer maintained since API version 18. You are advised to use  
    [@ohos.hiviewdfx.hiAppEvent]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ to subscribe to the **APP\_CRASH** and  
    **APP\_FREEZE** events in later versions.  
    
    For details about how to use HiAppEvent to subscribe to the **APP\_CRASH** event, see  
    \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_  
    .  
    
    For details about how to use HiAppEvent to subscribe to the **APP\_FREEZE** event, see  
    \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_  
    .

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 18

**Substitutes:** ohos.hiviewdfx.hiAppEvent

<!--Device-unnamed-declare namespace FaultLogger--><!--Device-unnamed-declare namespace FaultLogger-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

## Summary

### Functions

| Name | Description |
| --- | --- |
| [query](arkts-performanceanalysis-faultlogger-query-f.md#query) | Obtains the fault information about the current application. This API uses an asynchronous callback to return the fault information array obtained, which contains a maximum of 10 pieces of fault information. |
| [query](arkts-performanceanalysis-faultlogger-query-f.md#query-1) | Obtains the fault information about the current application. This API uses a promise to return the fault information array obtained, which contains a maximum of 10 pieces of fault information. |
| [querySelfFaultLog](arkts-performanceanalysis-faultlogger-queryselffaultlog-f.md#queryselffaultlog) | Obtains the fault information about the current application. This API uses an asynchronous callback to return the fault information array obtained, which contains a maximum of 10 pieces of fault information. |
| [querySelfFaultLog](arkts-performanceanalysis-faultlogger-queryselffaultlog-f.md#queryselffaultlog-1) | Obtains the fault information about the current application. This API uses a promise to return the fault information array obtained, which contains a maximum of 10 pieces of fault information. |

### Interfaces

| Name | Description |
| --- | --- |
| [FaultLogInfo](arkts-performanceanalysis-faultlogger-faultloginfo-i.md) | Defines the data structure of the fault log information. |

### Enums

| Name | Description |
| --- | --- |
| [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | Enumerates the fault types. |

