# @ohos.app.ability.autoStartupManager

The autoStartupManager module provides APIs for an application to query whether it is configured to start automatically at boot time.

**Since:** 23

<!--Device-unnamed-declare namespace autoStartupManager--><!--Device-unnamed-declare namespace autoStartupManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { autoStartupManager } from '@kit.AbilityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAutoStartupStatusForSelf](arkts-ability-autostartupmanager-getautostartupstatusforself-f.md) | Checks whether the current application is enabled for automatic startup at boot time. This API uses a promise to return the result. This API can be properly called only on phones, PC/2-in-1 devices, tablets, and wearables. On other devices, it returns the error code 801. |
| [isAutoStartupSupported](arkts-ability-autostartupmanager-isautostartupsupported-f.md) | Check whether the current device supports auto startup on this device. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [cancelApplicationAutoStartup](arkts-ability-autostartupmanager-cancelapplicationautostartup-f-sys.md) | Cancels the auto-startup setting for an application component. This API uses an asynchronous callback to return the result. Starting from API version 18, this API can be properly called on 2-in-1 devices and wearables. If it is called on other device types, error code 16000050 is returned. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000050 is returned. |
| [cancelApplicationAutoStartup](arkts-ability-autostartupmanager-cancelapplicationautostartup-f-sys.md) | Cancels the auto-startup setting for an application component. This API uses a promise to return the result. Starting from API version 18, this API can be properly called on 2-in-1 devices and wearables. If it is called on other device types, error code 16000050 is returned. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000050 is returned. |
| [offSystemAutoStartup](arkts-ability-autostartupmanager-offsystemautostartup-f-sys.md) | Unregister listener that watches for all applications auto startup state. |
| off_systemAutoStartup | Unregisters the callback used to listen for auto-startup status changes of an application component. Starting from API version 18, this API can be properly called on 2-in-1 devices and wearables. If it is called on other device types, error code 16000050 is returned. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000050 is returned. |
| [onSystemAutoStartup](arkts-ability-autostartupmanager-onsystemautostartup-f-sys.md) | Register the listener that watches for all applications auto startup state. |
| on_systemAutoStartup | Registers a callback to listen for auto-startup status changes of an application component. Starting from API version 18, this API can be properly called on 2-in-1 devices and wearables. If it is called on other device types, error code 16000050 is returned. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000050 is returned. |
| [queryAllAutoStartupApplications](arkts-ability-autostartupmanager-queryallautostartupapplications-f-sys.md) | Obtains information about all auto-startup application components. This API uses an asynchronous callback to return the result. Starting from API version 18, this API can be properly called on 2-in-1 devices and wearables. If it is called on other device types, error code 16000050 is returned. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000050 is returned. |
| [queryAllAutoStartupApplications](arkts-ability-autostartupmanager-queryallautostartupapplications-f-sys.md) | Obtains information about all auto-startup application components. This API uses a promise to return the result. Starting from API version 18, this API can be properly called on 2-in-1 devices and wearables. If it is called on other device types, error code 16000050 is returned. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000050 is returned. |
| [setApplicationAutoStartup](arkts-ability-autostartupmanager-setapplicationautostartup-f-sys.md) | Sets an application component to automatically start upon system boot. This API uses an asynchronous callback to return the result. Starting from API version 18, this API can be properly called on 2-in-1 devices and wearables. If it is called on other device types, error code 16000050 is returned. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000050 is returned. |
| [setApplicationAutoStartup](arkts-ability-autostartupmanager-setapplicationautostartup-f-sys.md) | Sets an application component to automatically start upon system boot. This API uses a promise to return the result. Starting from API version 18, this API can be properly called on 2-in-1 devices and wearables. If it is called on other device types, error code 16000050 is returned. For versions earlier than API version 18, this API can be properly called only on 2-in-1 devices. If it is called on other device types, error code 16000050 is returned. |
<!--DelEnd-->

