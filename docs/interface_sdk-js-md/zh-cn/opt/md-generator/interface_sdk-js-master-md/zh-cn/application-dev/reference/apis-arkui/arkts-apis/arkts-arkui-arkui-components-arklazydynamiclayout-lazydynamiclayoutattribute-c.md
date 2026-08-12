# LazyDynamicLayoutAttribute

定义LazyDynamicLayout组件。

**继承/实现关系：** LazyDynamicLayoutAttribute extends [CommonMethod<LazyDynamicLayoutAttribute>](CommonMethod<LazyDynamicLayoutAttribute>)

**起始版本：** 26.0.0

<!--Device-unnamed-export declare class LazyDynamicLayoutAttribute extends CommonMethod<LazyDynamicLayoutAttribute>--><!--Device-unnamed-export declare class LazyDynamicLayoutAttribute extends CommonMethod<LazyDynamicLayoutAttribute>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## onVisibleIndexesChange

```TypeScript
onVisibleIndexesChange(callback: Callback<number[]> | undefined): LazyDynamicLayoutAttribute
```

当可见索引更改时调用。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-LazyDynamicLayoutAttribute-onVisibleIndexesChange(callback: Callback<int[]> | undefined): LazyDynamicLayoutAttribute--><!--Device-LazyDynamicLayoutAttribute-onVisibleIndexesChange(callback: Callback<int[]> | undefined): LazyDynamicLayoutAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-callback-t.md) & lt;number[] & gt; \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [LazyDynamicLayoutAttribute](arkts-arkui-arkui-components-arklazydynamiclayout-lazydynamiclayoutattribute-c.md) |
