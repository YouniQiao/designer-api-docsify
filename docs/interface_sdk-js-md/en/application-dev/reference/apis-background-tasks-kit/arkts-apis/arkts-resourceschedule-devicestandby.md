# @ohos.resourceschedule.deviceStandby

Provides methods for managing device standby, including the methods for querying standby status and exemption list.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace deviceStandby--><!--Device-unnamed-declare namespace deviceStandby-End-->

**System capability:** SystemCapability.ResourceSchedule.DeviceStandby

## Modules to Import

```TypeScript
import { deviceStandby } from 'deviceStandby';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [getExemptedApps](arkts-backgroundtasks-devicestandby-getexemptedapps-f-sys.md#getExemptedApps) | Returns the information about the specified exempted application. |
| [getExemptedApps](arkts-backgroundtasks-devicestandby-getexemptedapps-f-sys.md#getExemptedApps-(System-API)) | Returns the information about the specified exempted application. |
| [releaseExemptionResource](arkts-backgroundtasks-devicestandby-releaseexemptionresource-f-sys.md#releaseExemptionResource) | Releases exemption resources. |
| [requestExemptionResource](arkts-backgroundtasks-devicestandby-requestexemptionresource-f-sys.md#requestExemptionResource) | Requests exemption resources. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ExemptedAppInfo](arkts-backgroundtasks-devicestandby-exemptedappinfo-i-sys.md) | Information about an exempted application. |
| [ResourceRequest](arkts-backgroundtasks-devicestandby-resourcerequest-i-sys.md) | The request of standby resources. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ResourceType](arkts-backgroundtasks-devicestandby-resourcetype-e-sys.md) | The type of exemption resources requested by the application. |
<!--DelEnd-->

