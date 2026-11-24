# OnNeedSoftkeyboardCallback

```TypeScript
declare type OnNeedSoftkeyboardCallback = () => boolean
```

当绑定该方法的组件判断是否需要键盘时，将触发此回调。前提条件：组件需可获焦，否则本接口不生效。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务中使用。

<!--Device-unnamed-declare type OnNeedSoftkeyboardCallback = () => boolean--><!--Device-unnamed-declare type OnNeedSoftkeyboardCallback = () => boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否需要键盘。<br>若此回调的返回值为`true`，则表明该组件需要键盘；返回值为`false`，则表明该组件不需要键盘。 |
