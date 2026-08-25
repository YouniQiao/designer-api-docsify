# @ohos.systemparameter

The **SystemParameter** module provides system services with easy access to key-value pairs. You can use the APIs provided by this module to describe the service status and change the service behavior. The basic operation primitives are **get** and **set**. You can obtain the values of system parameters through getters and modify the values through setters.For details about the system parameter design principles and definitions, see [Parameter Management](../../../../device-dev/subsystems/subsys-boot-init-sysparam.md).

> **NOTE：**&gt;
> - The APIs of this module are no longer maintained since API version 9. You are advised to use
> [@ohos.systemParameterEnhance](arkts-systemparameterenhance.md) instead.&gt;
> - The APIs provided by this module are system APIs.&gt;
> - Third-party applications cannot use the APIs provided by this module because system parameters each require
> specific discretionary access control (DAC) and mandatory access control (MAC) permissions.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [systemParameterEnhance](arkts-systemparameterenhance.md)

**System capability:** SystemCapability.Startup.SystemInfo

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { systemParameter } from 'kits/@kit.BasicServicesKit';
```

## Summary

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [get](arkts-basicservices-systemparameter-get-f-sys.md) |
| [get](arkts-basicservices-systemparameter-get-f-sys.md) |
| [get](arkts-basicservices-systemparameter-get-f-sys.md) |
| [getSync](arkts-basicservices-systemparameter-getsync-f-sys.md) |
| [set](arkts-basicservices-systemparameter-set-f-sys.md) |
| [set](arkts-basicservices-systemparameter-set-f-sys.md) |
| [setSync](arkts-basicservices-systemparameter-setsync-f-sys.md) |
<!--DelEnd-->
