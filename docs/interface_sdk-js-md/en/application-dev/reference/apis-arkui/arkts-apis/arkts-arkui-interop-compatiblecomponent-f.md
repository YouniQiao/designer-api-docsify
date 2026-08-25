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

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| init | [CompatibleInitCallback](arkts-arkui-compatibleinitcallback-t.md) | Yes |
| update | [CompatibleUpdateCallback](arkts-arkui-compatibleupdatecallback-t.md) | Yes |
| [component](arkts-arkui-interop-compatiblecomponentinfo-i.md) | [ExtendableComponent](arkts-arkui-extendablecomponent-extendablecomponent-c.md) | No |
