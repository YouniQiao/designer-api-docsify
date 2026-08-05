# @ohos.resourceManager

This module provides the capabilities to access application resources and system resources. It allows applications to obtain the best-matching application or system resources based on the current [configuration]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_, supporting internationalization resource matching and multi- device adaptation. For details about the matching rules, see \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_. The configuration includes language, script, country/region, orientation, color mode, Mobile Country Code (MCC), Mobile Network Code (MNC), device type, and screen density. **Use scenarios** - Application internationalization: Automatically obtains matching string resources based on the user's language and region. - Multi-device adaptation: Obtains appropriate media resources based on device type and screen density. - Dynamic resource configuration: Obtains resources corresponding to the current device state, such as orientation and color mode. **How to Use** - In the FA model, you need to import the module and then call [getResourceManager]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_ to obtain a **ResourceManager** object. - Since API version 9, in the stage model, the stage model allows you to obtain the **resourceManager** object through context without importing any module. For details about the context, see \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_. \_\_\_CODE\_BLOCK\_DESC\_USD\_0\_\_\_

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace resourceManager--><!--Device-unnamed-declare namespace resourceManager-End-->

**System capability:** SystemCapability.Global.ResourceManager

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager) | Obtains the **ResourceManager** object of the current application. This API uses an asynchronous callback to return the result. |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-1) | Obtains the **ResourceManager** object of the specified application. This API uses an asynchronous callback to return the result. |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-2) | Obtains the **ResourceManager** object of the current application. This API uses a promise to return the result. |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-3) | Obtains the **ResourceManager** object of the specified application. This API uses a promise to return the result. |
| [getSysResourceManager](arkts-localization-resourcemanager-getsysresourcemanager-f.md#getsysresourcemanager) | Obtains a system resource management object for accessing preset system resources. |
| [getSystemResourceManager](arkts-localization-resourcemanager-getsystemresourcemanager-f.md#getsystemresourcemanager) | Obtains a system resource management object for accessing preset system resources. |

### Classes

| Name | Description |
| --- | --- |
| [Configuration](arkts-localization-resourcemanager-configuration-c.md) | Defines the device configuration. |
| [DeviceCapability](arkts-localization-resourcemanager-devicecapability-c.md) | Defines the device capability. |

### Interfaces

| Name | Description |
| --- | --- |
| [AsyncCallback](arkts-localization-resourcemanager-asynccallback-i.md) | Asynchronous callback interface. |
| [ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md) | Provides the capability of accessing application resources and system resources. The accessible resources include the resources in the HAP/HSP module corresponding to the current context and all system resources. |

### Enums

| Name | Description |
| --- | --- |
| [ColorMode](arkts-localization-resourcemanager-colormode-e.md) | Defines the color mode of the current device. |
| [DeviceType](arkts-localization-resourcemanager-devicetype-e.md) | Enumerates the device types. \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_COMMENT\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_COMMENT\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ |
| [Direction](arkts-localization-resourcemanager-direction-e.md) | Enumerates the screen directions. |
| [ScreenDensity](arkts-localization-resourcemanager-screendensity-e.md) | Enumerates the screen density types. |

### Types

| Name | Description |
| --- | --- |
| [RawFileDescriptor](arkts-localization-resourcemanager-rawfiledescriptor-t.md) | Describes the file descriptor information of the HAP where the rawfile is located. |
| [Resource](arkts-localization-resourcemanager-resource-t.md) | Describes the resource information, including the application package name, application module name, resource ID, resource type, and formatting parameters. |

