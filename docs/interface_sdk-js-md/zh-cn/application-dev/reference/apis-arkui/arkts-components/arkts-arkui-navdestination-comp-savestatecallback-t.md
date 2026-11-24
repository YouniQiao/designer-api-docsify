# SaveStateCallback

```TypeScript
declare type SaveStateCallback = () => Record<string, Object> | null
```

自定义页面状态保存回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务中使用。

<!--Device-unnamed-declare type SaveStateCallback = () => Record<string, Object> | null--><!--Device-unnamed-declare type SaveStateCallback = () => Record<string, Object> | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record&lt;string, Object&gt; &#124; null | Custom page state. |
