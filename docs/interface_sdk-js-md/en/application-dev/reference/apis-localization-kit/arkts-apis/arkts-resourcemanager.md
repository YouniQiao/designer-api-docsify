# @ohos.resourceManager(Resource Management)

This module provides the capabilities to access application resources and system resources. It allows applications to obtain the best-matching application or system resources based on the current [configuration](arkts-localization-resourcemanager-configuration-c.md), supporting internationalization resource matching and multi- device adaptation. For details about the matching rules, see [Matching Resources](../../../quick-start/resource-categories-and-access.md#matching-resources).The configuration includes language, script, country/region, orientation, color mode, Mobile Country Code (MCC), Mobile Network Code (MNC), device type, and screen density.  
**Use scenarios**  
- Application internationalization: Automatically obtains matching string resources based on the user's language and  
region.  
- Multi-device adaptation: Obtains appropriate media resources based on device type and screen density.  
- Dynamic resource configuration: Obtains resources corresponding to the current device state, such as orientation  
and color mode.  
**How to Use**  
- In the FA model, you need to import the module and then call  
[getResourceManager](arkts-localization-resourcemanager-getresourcemanager-f.md) to obtain a **ResourceManager** object.  
- Since API version 9, in the stage model, the stage model allows you to obtain the **resourceManager** object  
through context without importing any module. For details about the context, see [application context](../../../application-models/application-context-stage.md).  
 ```ts
 import { UIAbility } from '@kit.AbilityKit';
 import { window } from '@kit.ArkUI';

 export default class EntryAbility extends UIAbility {
 onWindowStageCreate(windowStage: window.WindowStage) {
 let context = this.context;
 let resourceManager = context.resourceManager;
 }
 }
 ```

**Since:** 6

**System capability:** SystemCapability.Global.ResourceManager

## Modules to Import

```TypeScript
import { resourceManager } from 'kits/@kit.LocalizationKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getResourceManager(Resource Management)](arkts-localization-resourcemanager-getresourcemanager-f.md) |
| [getResourceManager(Resource Management)](arkts-localization-resourcemanager-getresourcemanager-f.md) |
| [getResourceManager(Resource Management)](arkts-localization-resourcemanager-getresourcemanager-f.md) |
| [getResourceManager(Resource Management)](arkts-localization-resourcemanager-getresourcemanager-f.md) |
| [getSysResourceManager(Resource Management)](arkts-localization-resourcemanager-getsysresourcemanager-f.md) |
| [getSystemResourceManager(Resource Management)](arkts-localization-resourcemanager-getsystemresourcemanager-f.md) |

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Configuration(Resource Management)](arkts-localization-resourcemanager-configuration-c.md) |
| [DeviceCapability(Resource Management)](arkts-localization-resourcemanager-devicecapability-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AsyncCallback(Resource Management)](arkts-localization-resourcemanager-asynccallback-i.md) |
| [ResourceManager(Resource Management)](arkts-localization-resourcemanager-resourcemanager-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ColorMode(Resource Management)](arkts-localization-resourcemanager-colormode-e.md) |
| [DeviceType(Resource Management)](arkts-localization-resourcemanager-devicetype-e.md) |
| [Direction(Resource Management)](arkts-localization-resourcemanager-direction-e.md) |
| [ScreenDensity(Resource Management)](arkts-localization-resourcemanager-screendensity-e.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RawFileDescriptor(Resource Management)](arkts-localization-resourcemanager-rawfiledescriptor-t.md) |
| [Resource(Resource Management)](arkts-localization-resourcemanager-resource-t.md) |
