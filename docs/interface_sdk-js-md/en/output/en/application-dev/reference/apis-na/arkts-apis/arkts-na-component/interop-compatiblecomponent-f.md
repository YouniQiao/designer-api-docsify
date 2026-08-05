# compatibleComponent

## compatibleComponent

```TypeScript
export declare function compatibleComponent(
    init: CompatibleInitCallback,
    update: CompatibleUpdateCallback,
    component?: ExtendableComponent
): void
```

Obtains the compatible custom component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function compatibleComponent(    init: CompatibleInitCallback,    update: CompatibleUpdateCallback,    component?: ExtendableComponent): void--><!--Device-unnamed-export declare function compatibleComponent(    init: CompatibleInitCallback,    update: CompatibleUpdateCallback,    component?: ExtendableComponent): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| init | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the callback for initializing compatible custom component |
| update | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the callback for updating compatible custom component |
| component | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | the custom component |

