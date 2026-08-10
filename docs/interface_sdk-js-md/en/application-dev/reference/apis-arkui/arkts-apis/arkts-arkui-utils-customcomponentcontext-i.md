# CustomComponentContext

自定义组件的上下文信息。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface CustomComponentContext--><!--Device-unnamed-export declare interface CustomComponentContext-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getReusePool

```TypeScript
getReusePool(): IReusePool | undefined
```

从当前自定义组件获取全局重用池。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentContext-getReusePool(): IReusePool | undefined--><!--Device-CustomComponentContext-getReusePool(): IReusePool | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [IReusePool](arkts-arkui-utils-ireusepool-i.md) | Returns the recyclepool instance. |

## registerActiveAndInactiveCallback

```TypeScript
registerActiveAndInactiveCallback(active?: ActiveAndInactiveCallbackType,
    inactive?: ActiveAndInactiveCallbackType): void
```

注册激活和非激活回调。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-CustomComponentContext-registerActiveAndInactiveCallback(active?: ActiveAndInactiveCallbackType,    inactive?: ActiveAndInactiveCallbackType): void--><!--Device-CustomComponentContext-registerActiveAndInactiveCallback(active?: ActiveAndInactiveCallbackType,    inactive?: ActiveAndInactiveCallbackType): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| active | [ActiveAndInactiveCallbackType](arkts-arkui-activeandinactivecallbacktype-t.md) | No | 激活函数回调 默认值： 默认值：undefined。 |
| inactive | [ActiveAndInactiveCallbackType](arkts-arkui-activeandinactivecallbacktype-t.md) | No | in激活函数回调 默认值： 默认值：undefined。 |

