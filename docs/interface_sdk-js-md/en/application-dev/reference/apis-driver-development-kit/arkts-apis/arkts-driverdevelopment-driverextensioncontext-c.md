# DriverExtensionContext

DriverExtensionContext模块是DriverExtensionAbility的上下文环境，继承自ExtensionContext。DriverExtensionContext模块提供DriverExtensionAbility实现中需要主动发起的操作。

> **说明：**
> - 本模块接口仅可在Stage模型下使用。

**Inheritance/Implementation:** DriverExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-unnamed-declare class DriverExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class DriverExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

## updateDriverState

```TypeScript
updateDriverState(): void
```

驱动状态上报。预留接口，暂不提供具体功能。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DriverExtensionContext-updateDriverState(): void--><!--Device-DriverExtensionContext-updateDriverState(): void-End-->

**System capability:** SystemCapability.Driver.ExternalDevice

