# Available

Annotates the minimum available version supported by an API. This annotation capability is provided by the system and can be used on classes, APIs, variables, types, modules, and enums. After the annotation is added to the source code, the compilation tool checks for potential compatibility issues. If the value of **minApiVersion** is greater than that of **compatibleSDKVersion** specified in **build-profile.json5**, a compatibility warning is reported.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export @interface Available--><!--Device-unnamed-export @interface Available-End-->

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
import { SuppressWarnings, Available, SuppressWarningsType } from 'kits/@kit.BasicServicesKit';
```

## minApiVersion

```TypeScript
minApiVersion: string = ''
```

Minimum available version, which consists of two parts: system type and version number. The system type can be omitted only when it is OpenHarmony, for example, **'OpenHarmony 20'** or **'20'**.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Available-minApiVersion: string = ''--><!--Device-Available-minApiVersion: string = ''-End-->

**System capability:** SystemCapability.Base

