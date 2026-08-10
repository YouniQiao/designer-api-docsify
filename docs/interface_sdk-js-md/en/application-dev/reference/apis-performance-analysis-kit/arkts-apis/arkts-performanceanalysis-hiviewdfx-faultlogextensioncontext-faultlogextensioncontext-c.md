# FaultLogExtensionContext

FaultLogExtensionContext是  
[FaultLogExtensionAbility](arkts-performanceanalysis-hiviewdfx-faultlogextensionability-faultlogextensionability-c.md)的上下文环境，继承自[ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)。

FaultLogExtensionContext模块提供访问  
[FaultLogExtensionAbility](arkts-performanceanalysis-hiviewdfx-faultlogextensionability-faultlogextensionability-c.md)的资源的能力，对于扩展的ExtensionAbility，可直接将ExtensionContext作为上下文环境，或者定义一个继承自ExtensionContext的类型作为上下文环境。

> **说明：**
> 
> - 本模块接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**Inheritance/Implementation:** FaultLogExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn since version 21; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export default class FaultLogExtensionContext extends ExtensionContext--><!--Device-unnamed-export default class FaultLogExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

## Modules to Import

```TypeScript
import { FaultLogExtensionContext } from 'kits/@kit.PerformanceAnalysisKit';
```

