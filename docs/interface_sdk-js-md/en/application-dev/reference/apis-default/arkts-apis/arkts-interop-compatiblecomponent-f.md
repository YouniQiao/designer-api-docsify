# compatibleComponent

## compatibleComponent

```TypeScript
@Builder
export declare function compatibleComponent(
    init: CompatibleInitCallback,
    update: CompatibleUpdateCallback,
    component?: ExtendableComponent
): void
```

Obtains the compatible custom component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function compatibleComponent(    init: CompatibleInitCallback,    update: CompatibleUpdateCallback,    component?: ExtendableComponent): void--><!--Device-unnamed-@Builderexport declare function compatibleComponent(    init: CompatibleInitCallback,    update: CompatibleUpdateCallback,    component?: ExtendableComponent): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| init | [CompatibleInitCallback](arkts-compatibleinitcallback-t.md) | Yes | the callback for initializing compatible custom component |
| update | [CompatibleUpdateCallback](arkts-compatibleupdatecallback-t.md) | Yes | the callback for updating compatible custom component |
| component | [ExtendableComponent](arkts-extendablecomponent-extendablecomponent-c.md) | No | the custom component |

