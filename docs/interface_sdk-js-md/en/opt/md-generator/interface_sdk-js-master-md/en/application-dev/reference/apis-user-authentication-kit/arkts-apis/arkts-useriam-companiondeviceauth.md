# @ohos.userIAM.companionDeviceAuth

The **companionDeviceAuth** module is an important part of the OpenHarmony user identity and access management ( UserIAM) system. It is dedicated to companion device authentication management. This module provides the system application with capabilities such as querying and subscribing to companion devices, and managing the service scope. This module applies to the following scenarios: - Managing the authentication relationship between a companion device and the primary device. - Querying and subscribing to the status changes of a companion device. - Managing the service scope supported by a companion device. - Implementing continuous authentication. - Processing device selection and registration.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace companionDeviceAuth--><!--Device-unnamed-declare namespace companionDeviceAuth-End-->

**System capability:** SystemCapability.UserIAM.UserAuth.CompanionDeviceAuth

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { companionDeviceAuth } from '@kit.UserAuthenticationKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getStatusMonitor](arkts-userauthentication-companiondeviceauth-getstatusmonitor-f-sys.md#getStatusMonitor-(System-API)) |
| [registerDeviceSelectCallback](arkts-userauthentication-companiondeviceauth-registerdeviceselectcallback-f-sys.md#registerDeviceSelectCallback-(System-API)) |
| [unregisterDeviceSelectCallback](arkts-userauthentication-companiondeviceauth-unregisterdeviceselectcallback-f-sys.md#unregisterDeviceSelectCallback-(System-API)) |
| [updateEnabledBusinessIds](arkts-userauthentication-companiondeviceauth-updateenabledbusinessids-f-sys.md#updateEnabledBusinessIds-(System-API)) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ContinuousAuthParam](arkts-userauthentication-companiondeviceauth-continuousauthparam-i-sys.md) |
| [DeviceKey](arkts-userauthentication-companiondeviceauth-devicekey-i-sys.md) |
| [DeviceSelectResult](arkts-userauthentication-companiondeviceauth-deviceselectresult-i-sys.md) |
| [DeviceStatus](arkts-userauthentication-companiondeviceauth-devicestatus-i-sys.md) |
| [StatusMonitor](arkts-userauthentication-companiondeviceauth-statusmonitor-i-sys.md) |
| [TemplateStatus](arkts-userauthentication-companiondeviceauth-templatestatus-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BusinessId](arkts-userauthentication-companiondeviceauth-businessid-e-sys.md) |
| [DeviceIdType](arkts-userauthentication-companiondeviceauth-deviceidtype-e-sys.md) |
| [SelectPurpose](arkts-userauthentication-companiondeviceauth-selectpurpose-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AvailableDeviceStatusCallback](arkts-userauthentication-companiondeviceauth-availabledevicestatuscallback-t-sys.md) |
| [ContinuousAuthStatusCallback](arkts-userauthentication-companiondeviceauth-continuousauthstatuscallback-t-sys.md) |
| [DeviceSelectCallback](arkts-userauthentication-companiondeviceauth-deviceselectcallback-t-sys.md) |
| [TemplateStatusCallback](arkts-userauthentication-companiondeviceauth-templatestatuscallback-t-sys.md) |
<!--DelEnd-->
