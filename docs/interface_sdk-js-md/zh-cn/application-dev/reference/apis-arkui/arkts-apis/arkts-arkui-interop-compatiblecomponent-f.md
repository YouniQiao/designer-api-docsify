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

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| init | [CompatibleInitCallback](arkts-arkui-compatibleinitcallback-t.md) | 是 |
| update | [CompatibleUpdateCallback](arkts-arkui-compatibleupdatecallback-t.md) | 是 |
| [component](arkts-arkui-interop-compatiblecomponentinfo-i.md) | [ExtendableComponent](arkts-arkui-extendablecomponent-extendablecomponent-c.md) | 否 |
