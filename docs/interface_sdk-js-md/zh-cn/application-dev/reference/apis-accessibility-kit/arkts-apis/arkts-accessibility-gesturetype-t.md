# GestureType

```TypeScript
type GestureType = 'left' | 'leftThenRight' | 'leftThenUp' | 'leftThenDown' |
  'right' | 'rightThenLeft' | 'rightThenUp' | 'rightThenDown' |
  'up' | 'upThenLeft' | 'upThenRight' | 'upThenDown' |
  'down' | 'downThenLeft' | 'downThenRight' | 'downThenUp' |
  'twoFingerSingleTap' | 'twoFingerDoubleTap' | 'twoFingerDoubleTapAndHold' | 'twoFingerTripleTap' |
  'twoFingerTripleTapAndHold' | 'threeFingerSingleTap' | 'threeFingerDoubleTap' | 'threeFingerDoubleTapAndHold' |
  'threeFingerTripleTap' | 'threeFingerTripleTapAndHold' | 'fourFingerSingleTap' | 'fourFingerDoubleTap' |
  'fourFingerDoubleTapAndHold' | 'fourFingerTripleTap' | 'fourFingerTripleTapAndHold' |
  'threeFingerSwipeUp' | 'threeFingerSwipeDown' | 'threeFingerSwipeLeft' | 'threeFingerSwipeRight' |
  'fourFingerSwipeUp' | 'fourFingerSwipeDown' | 'fourFingerSwipeLeft' | 'fourFingerSwipeRight' | 'oneFingerDoubleTap'
```

手势事件类型。手势事件在用户执行特定手势操作时由无障碍服务触发，辅助功能扩展可通过onAccessibilityEvent回调接收并处理对应的手势事件。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为9。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

| 类型 |
| --- |
| 'left' |
| 'leftThenRight' |
| 'leftThenUp' |
| 'leftThenDown' |
| 'right' |
| 'rightThenLeft' |
| 'rightThenUp' |
| 'rightThenDown' |
| 'up' |
| 'upThenLeft' |
| 'upThenRight' |
| 'upThenDown' |
| 'down' |
| 'downThenLeft' |
| 'downThenRight' |
| 'downThenUp' |
| 'twoFingerSingleTap' |
| 'twoFingerDoubleTap' |
| 'twoFingerDoubleTapAndHold' |
| 'twoFingerTripleTap' |
| 'twoFingerTripleTapAndHold' |
| 'threeFingerSingleTap' |
| 'threeFingerDoubleTap' |
| 'threeFingerDoubleTapAndHold' |
| 'threeFingerTripleTap' |
| 'threeFingerTripleTapAndHold' |
| 'fourFingerSingleTap' |
| 'fourFingerDoubleTap' |
| 'fourFingerDoubleTapAndHold' |
| 'fourFingerTripleTap' |
| 'fourFingerTripleTapAndHold' |
| 'threeFingerSwipeUp' |
| 'threeFingerSwipeDown' |
| 'threeFingerSwipeLeft' |
| 'threeFingerSwipeRight' |
| 'fourFingerSwipeUp' |
| 'fourFingerSwipeDown' |
| 'fourFingerSwipeLeft' |
| 'fourFingerSwipeRight' |
| 'oneFingerDoubleTap' |
