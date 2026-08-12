# @ohos.resourceManager

This module provides the capabilities to access application resources and system resources. It allows applications to obtain the best-matching application or system resources based on the current   
[configuration](arkts-localization-resourcemanager-configuration-c.md#Configuration), supporting internationalization resource matching and multi-device adaptation. For details about the matching rules, see   
[Matching Resources](../../../quick-start/resource-categories-and-access.md#matching-resources).

The configuration includes language, script, country/region, orientation, color mode, Mobile Country Code (MCC), Mobile Network Code (MNC), device type, and screen density.

**Use scenarios**  
- Application internationalization: Automatically obtains matching string resources based on the user's language and   
region.  
- Multi-device adaptation: Obtains appropriate media resources based on device type and screen density.  
- Dynamic resource configuration: Obtains resources corresponding to the current device state, such as orientation   
and color mode.

**How to Use**  
- In the FA model, you need to import the module and then call   
[getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getResourceManager) to obtain a **ResourceManager** object.  
- Since API version 9, in the stage model, the stage model allows you to obtain the **resourceManager** object   
through context without importing any module. For details about the context, see   
[application context](../../../application-models/application-context-stage.md).

 ```ts  import { UIAbility } from '@kit.AbilityKit'; import { window } from '@kit.ArkUI';

 export default class EntryAbility extends UIAbility { onWindowStageCreate(windowStage: window.WindowStage) { let context = this.context; let resourceManager = context.resourceManager; } } ```

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace resourceManager--><!--Device-unnamed-declare namespace resourceManager-End-->

**System capability:** SystemCapability.Global.ResourceManager

## Modules to Import

```TypeScript
import { resourceManager } from '@kit.LocalizationKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager) | Obtains the **ResourceManager** object of the current application. This API uses an asynchronous callback to return the result. |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-1) | Obtains the **ResourceManager** object of the specified application. This API uses an asynchronous callback to return the result. |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-2) | Obtains the **ResourceManager** object of the current application. This API uses a promise to return the result. |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-3) | Obtains the **ResourceManager** object of the specified application. This API uses a promise to return the result. |
| [getSysResourceManager](arkts-localization-resourcemanager-getsysresourcemanager-f.md#getsysresourcemanager) | Obtains a system resource management object for accessing preset system resources. |
| [getSystemResourceManager](arkts-localization-resourcemanager-getsystemresourcemanager-f.md#getsystemresourcemanager) | Obtains a system resource management object for accessing preset system resources.  > **NOTE：** >  > The **Configuration** parameter in the **ResourceManager** object obtained via this API uses the default value. > The default value is > **{"locale": "", "direction": -1, "deviceType": -1, "screenDensity": 0, "colorMode": 1, "mcc": 0, "mnc": 0}**. |

### Classes

| Name | Description |
| --- | --- |
| [Configuration](arkts-localization-resourcemanager-configuration-c.md) | Defines the device configuration. |
| [DeviceCapability](arkts-localization-resourcemanager-devicecapability-c.md) | Defines the device capability. |

### Interfaces

| Name | Description |
| --- | --- |
| [AsyncCallback](arkts-localization-resourcemanager-asynccallback-i.md) | Asynchronous callback interface. |
| [ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md) | Provides the capability of accessing application resources and system resources. The accessible resources include the resources in the HAP/HSP module corresponding to the current context and all system resources.  > **NOTE：** >  > - The methods involved in **ResourceManager** are applicable only to the TypeScript-based declarative > development paradigm. >  > - Resource files are defined in the **resources** directory of the project. You can obtain resource values such > as strings, string arrays, and colors based on the specified **resName**, **resId**, or **Resource** object. > **resName** indicates the resource name, **resId** indicates the resource ID, which can be obtained through > `\\$r(*resource-address*).id`, for example, `\\$r('app.string.test').id`. >  > - No matter whether resources are in the same HAP or different HAPs or HSPs, you are advised to use the API with > **resName** or **resId** specified. Using the **Resource** object will take a longer time. If the resources are > in different HAPs or HSPs, you first need to use > [createModuleContext](../../apis-ability-kit/arkts-apis/arkts-ability-application-createmodulecontext-f.md#createModuleContext) to create the context > of the corresponding module and then call the API with **resName** or **resId** specified. For more information, > see [Accessing Resources](../../../quick-start/resource-categories-and-access.md#accessing-resources). >  > - In API version 22 and earlier versions, an exception is thrown due to an invalid ID when the intermediate-code > HAR or bytecode HAR accesses resources through resource ID-related APIs. From API version 23, the intermediate- > code HAR or bytecode HAR can properly access resources through resource ID-related APIs. For details, see > [Accessing Resources](../../../quick-start/resource-categories-and-access.md#accessing-resources). |

### Enums

| Name | Description |
| --- | --- |
| [ColorMode](arkts-localization-resourcemanager-colormode-e.md) | Defines the color mode of the current device. |
| [DeviceType](arkts-localization-resourcemanager-devicetype-e.md) | Enumerates the device types.  &lt;!--RP1--&gt;  &lt;!--RP1End--&gt; |
| [Direction](arkts-localization-resourcemanager-direction-e.md) | Enumerates the screen directions. |
| [ScreenDensity](arkts-localization-resourcemanager-screendensity-e.md) | Enumerates the screen density types. |

### Types

| Name | Description |
| --- | --- |
| [RawFileDescriptor](arkts-localization-resourcemanager-rawfiledescriptor-t.md) | Describes the file descriptor information of the HAP where the rawfile is located. |
| [Resource](arkts-localization-resourcemanager-resource-t.md) | Describes the resource information, including the application package name, application module name, resource ID,resource type, and formatting parameters. |

