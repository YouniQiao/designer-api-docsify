# @ohos.userIAM.companionDeviceAuth(Companion Device Authentication)

The **companionDeviceAuth** module is an important part of the OpenHarmony user identity and access management (UserIAM) system. It is dedicated to companion device authentication management. This module provides the system application with capabilities such as querying and subscribing to companion devices, and managing the service scope.This module applies to the following scenarios:  
- Managing the authentication relationship between a companion device and the primary device.  
- Querying and subscribing to the status changes of a companion device.  
- Managing the service scope supported by a companion device.  
- Implementing continuous authentication.  
- Processing device selection and registration.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { companionDeviceAuth } from 'kits/@kit.UserAuthenticationKit';
```

## Summary

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getStatusMonitor(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-getstatusmonitor-f-sys.md) |
| [registerDeviceSelectCallback(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-registerdeviceselectcallback-f-sys.md) |
| [registerPasscodePromptCallback(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-registerpasscodepromptcallback-f-sys.md) |
| [unregisterDeviceSelectCallback(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-unregisterdeviceselectcallback-f-sys.md) |
| [unregisterPasscodePromptCallback(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-unregisterpasscodepromptcallback-f-sys.md) |
| [updateEnabledBusinessIds(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-updateenabledbusinessids-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ContinuousAuthParam(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-continuousauthparam-i-sys.md) |
| [DeviceKey(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-devicekey-i-sys.md) |
| [DeviceSelectResult(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-deviceselectresult-i-sys.md) |
| [DeviceStatus(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-devicestatus-i-sys.md) |
| [PasscodePromptParams(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-passcodepromptparams-i-sys.md) |
| [StatusMonitor(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-statusmonitor-i-sys.md) |
| [TemplateStatus(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-templatestatus-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BusinessId(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-businessid-e-sys.md) |
| [DeviceIdType(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-deviceidtype-e-sys.md) |
| [SelectPurpose(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-selectpurpose-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AvailableDeviceStatusCallback(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-availabledevicestatuscallback-t-sys.md) |
| [ContinuousAuthStatusCallback(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-continuousauthstatuscallback-t-sys.md) |
| [DeviceSelectCallback(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-deviceselectcallback-t-sys.md) |
| [PasscodePromptCallback(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-passcodepromptcallback-t-sys.md) |
| [PasscodeSubmitCallback(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-passcodesubmitcallback-t-sys.md) |
| [TemplateStatusCallback(Companion Device Authentication)](arkts-userauthentication-companiondeviceauth-templatestatuscallback-t-sys.md) |
<!--DelEnd-->
