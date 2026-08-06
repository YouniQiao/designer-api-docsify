# @ohos.systemParameterEnhance

The **SystemParameter** module provides system services with easy access to key-value pairs. You can use the APIs provided by this module to describe the service status and change the service behavior. The basic operation primitives are **get** and **set**. You can obtain the values of system parameters through getter APIs and modify the values through setter APIs. For details about the system parameter design principles and definitions, see  
\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.
    **NOTE**  
    
    - The APIs provided by this module are system APIs.  
    
    - Third-party applications cannot use the APIs provided by this module because system parameters each require  
    specific discretionary access control (DAC) and mandatory access control (MAC) permissions.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace systemParameterEnhance--><!--Device-unnamed-declare namespace systemParameterEnhance-End-->

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [get](arkts-basicservices-systemparameterenhance-get-f-sys.md#get) | Obtains a value of the specified key. This API uses an asynchronous callback to return the result. |
| [get](arkts-basicservices-systemparameterenhance-get-f-sys.md#get-1) | Obtains a value of the specified key. This API uses an asynchronous callback to return the result. |
| [get](arkts-basicservices-systemparameterenhance-get-f-sys.md#get-2) | Obtains a value of the specified key. This API uses a promise to return the result. |
| [getSync](arkts-basicservices-systemparameterenhance-getsync-f-sys.md#getsync) | Obtains a value of the specified key. This API uses a promise to return the result. |
| [set](arkts-basicservices-systemparameterenhance-set-f-sys.md#set) | Sets a value of the specified key. This API uses an asynchronous callback to return the result. |
| [set](arkts-basicservices-systemparameterenhance-set-f-sys.md#set-1) | Sets a value of the specified key. This API uses a promise to return the result. |
| [setSync](arkts-basicservices-systemparameterenhance-setsync-f-sys.md#setsync) | Sets a value for the specified key. This API uses a promise to return the result. |
<!--DelEnd-->

