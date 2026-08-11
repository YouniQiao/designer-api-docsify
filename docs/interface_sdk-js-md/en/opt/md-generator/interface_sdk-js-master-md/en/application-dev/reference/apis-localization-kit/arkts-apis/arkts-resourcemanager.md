# @ohos.resourceManager

This module provides the capabilities to access application resources and system resources. It allows applications to obtain the best-matching application or system resources based on the current   
[configuration](arkts-localization-resourcemanager-configuration-c.md), supporting internationalization resource matching and multi-device adaptation. For details about the matching rules, see   
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
[getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager) to obtain a **ResourceManager** object.  
- Since API version 9, in the stage model, the stage model allows you to obtain the **resourceManager** object   
through context without importing any module. For details about the context, see   
[application context](../../../application-models/application-context-stage.md).

 ```ts  import { UIAbility } from '@kit.AbilityKit'; import { window } from '@kit.ArkUI';

 export default class EntryAbility extends UIAbility { onWindowStageCreate(windowStage: window.WindowStage) { let context = this.context; let resourceManager = context.resourceManager; } } ```

**Since:** 6

<!--Device-unnamed-declare namespace resourceManager--><!--Device-unnamed-declare namespace resourceManager-End-->

**System capability:** SystemCapability.Global.ResourceManager

## Modules to Import

```TypeScript
import { resourceManager } from 'kits/@kit.LocalizationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager) |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-1) |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-2) |
| [getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md#getresourcemanager-3) |
| [getSysResourceManager](arkts-localization-resourcemanager-getsysresourcemanager-f.md#getsysresourcemanager) |
| [getSystemResourceManager](arkts-localization-resourcemanager-getsystemresourcemanager-f.md#getsystemresourcemanager) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Configuration](arkts-localization-resourcemanager-configuration-c.md) |
| [DeviceCapability](arkts-localization-resourcemanager-devicecapability-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AsyncCallback](arkts-localization-resourcemanager-asynccallback-i.md) |
| [ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ColorMode](arkts-localization-resourcemanager-colormode-e.md) |
| [DeviceType](arkts-localization-resourcemanager-devicetype-e.md) |
| [Direction](arkts-localization-resourcemanager-direction-e.md) |
| [ScreenDensity](arkts-localization-resourcemanager-screendensity-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RawFileDescriptor](arkts-localization-resourcemanager-rawfiledescriptor-t.md) |
| [Resource](arkts-localization-resourcemanager-resource-t.md) |
