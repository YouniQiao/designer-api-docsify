# @ohos.annotation(Annotation)

The **annotation** module defines the annotation types of OpenHarmony ArkTS APIs, such as the minimum available
 version of the lifecycle.
 > **NOTE**
 >
 > - The initial APIs of this module are supported since API version 22. Newly added APIs will be marked with
 a superscript to indicate their earliest API version.


## Modules to Import

```TypeScript
import { SuppressWarnings, Available, SuppressWarningsType } from '@kit.BasicServicesKit';
```

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [Available](arkts-basicservices-annotation-available-i.md) | Annotates the minimum available version supported by an API. This annotation capability is provided by the system and can be used on classes, APIs, variables, types, modules, and enums. After the annotation is added to the source code, the compilation tool checks for potential compatibility issues. If the value of **minApiVersion** is greater than that of **compatibleSDKVersion** specified in **build-profile.json5**, a compatibility warning is reported. |

