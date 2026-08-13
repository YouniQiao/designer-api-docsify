# Action

```TypeScript
type Action = 'accessibilityFocus' | 'clearAccessibilityFocus' | 'focus' | 'clearFocus' | 'clearSelection' |
  'click' | 'longClick' | 'cut' | 'copy' | 'paste' | 'select' | 'setText' | 'delete' |
  'scrollForward' | 'scrollBackward' | 'setSelection' | 'setCursorPosition' | 'home' |
  'back' | 'recentTask' | 'notificationCenter' | 'controlCenter' | 'common' | 'injectAction' | 'executeCustomAction'
```

应用所支持的目标动作，需要配置参数的目标动作已在描述中标明。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

<!--Device-accessibility-type Action = 'accessibilityFocus' | 'clearAccessibilityFocus' | 'focus' | 'clearFocus' | 'clearSelection' |  'click' | 'longClick' | 'cut' | 'copy' | 'paste' | 'select' | 'setText' | 'delete' |  'scrollForward' | 'scrollBackward' | 'setSelection' | 'setCursorPosition' | 'home' |  'back' | 'recentTask' | 'notificationCenter' | 'controlCenter' | 'common' | 'injectAction' | 'executeCustomAction'--><!--Device-accessibility-type Action = 'accessibilityFocus' | 'clearAccessibilityFocus' | 'focus' | 'clearFocus' | 'clearSelection' |  'click' | 'longClick' | 'cut' | 'copy' | 'paste' | 'select' | 'setText' | 'delete' |  'scrollForward' | 'scrollBackward' | 'setSelection' | 'setCursorPosition' | 'home' |  'back' | 'recentTask' | 'notificationCenter' | 'controlCenter' | 'common' | 'injectAction' | 'executeCustomAction'-End-->

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

| 类型 |
| --- |
| 'accessibilityFocus' |
| 'clearAccessibilityFocus' |
| 'focus' |
| 'clearFocus' |
| 'clearSelection' |
| 'click' |
| 'longClick' |
| 'cut' |
| 'copy' |
| 'paste' |
| 'select' |
| 'setText' |
| 'delete' |
| 'scrollForward' |
| 'scrollBackward' |
| 'setSelection' |
| 'setCursorPosition' |
| 'home' |
| 'back' |
| 'recentTask' |
| 'notificationCenter' |
| 'controlCenter' |
| 'common' |
| 'injectAction' |
| 'executeCustomAction' |
