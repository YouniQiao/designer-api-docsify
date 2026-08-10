# compatibleComponent

## compatibleComponent

```TypeScript
export declare function compatibleComponent(
    init: CompatibleInitCallback,
    update: CompatibleUpdateCallback,
    component?: ExtendableComponent
): void
```

在ArkTS-Sta中引用ArkTS-Dyn自定义组件的占位组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function compatibleComponent(    init: CompatibleInitCallback,    update: CompatibleUpdateCallback,    component?: ExtendableComponent): void--><!--Device-unnamed-export declare function compatibleComponent(    init: CompatibleInitCallback,    update: CompatibleUpdateCallback,    component?: ExtendableComponent): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| init | [CompatibleInitCallback](arkts-arkui-compatibleinitcallback-t.md) | Yes | 初始化占位组件的回调函数。 |
| update | [CompatibleUpdateCallback](arkts-arkui-compatibleupdatecallback-t.md) | Yes | 更新占位组件的回调函数。 |
| component | [ExtendableComponent](arkts-arkui-extendablecomponent-extendablecomponent-c.md) | No | 当前ArkTS-Sta自定义组件。 |

