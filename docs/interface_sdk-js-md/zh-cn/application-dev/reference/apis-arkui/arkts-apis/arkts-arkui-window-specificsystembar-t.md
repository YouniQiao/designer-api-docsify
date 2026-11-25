# SpecificSystemBar

```TypeScript
type SpecificSystemBar = 'status' | 'navigation' | 'navigationIndicator'
```

当前支持显示或隐藏的系统栏类型。

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务中使用。

<!--Device-window-type SpecificSystemBar = 'status' | 'navigation'| 'navigationIndicator'--><!--Device-window-type SpecificSystemBar = 'status' | 'navigation'| 'navigationIndicator'-End-->

**系统能力：** SystemCapability.Window.SessionManager

| 类型 | 说明 |
| --- | --- |
| 'status' | 状态栏。 |
| 'navigation' | <!--RP13--><!--RP13End-->三键导航栏或工具栏。当前工具栏仅Car设备支持。 |
| 'navigationIndicator' | 底部导航。 <!--RP12-->OpenHarmony各设备不支持此能力。<!--RP12End--> |
