# OnOverlayBackPressCallback

```TypeScript
export declare type OnOverlayBackPressCallback = () => boolean
```

定义拦截Overlay侧滑返回事件的回调类型。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务中使用。

<!--Device-unnamed-export declare type OnOverlayBackPressCallback = () => boolean--><!--Device-unnamed-export declare type OnOverlayBackPressCallback = () => boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | Whether to intercept the back-press event. If **true** is returned, the event is intercepted and is prevented from reaching the lower-layer component. If **false** is returned, the event is transparently transmitted to the lower-layer component. |
