# TransitionContext（系统接口）

属性转换的上下文信息。

**起始版本：** 9

<!--Device-window-interface TransitionContext--><!--Device-window-interface TransitionContext-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

## completeTransition

```TypeScript
completeTransition(isCompleted: boolean): void
```

设置属性转换的最终完成状态。该函数需要在动画函数[animateTo()](../../apis-arkui/arkts-components/arkts-arkui-common-attribute.md)执行后设置。

**起始版本：** 9

<!--Device-TransitionContext-completeTransition(isCompleted: boolean): void--><!--Device-TransitionContext-completeTransition(isCompleted: boolean): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isCompleted | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
(context: window.TransitionContext) => {
  let toWindow: window.Window = context.toWindow;
  this.getUIContext()?.animateTo({
    duration: 1000, // 动画时长
    tempo: 0.5, // 播放速率
    curve: Curve.EaseInOut, // 动画曲线
    delay: 0, // 动画延迟
    iterations: 1, // 播放次数
    playMode: PlayMode.Normal, // 动画模式
  }, () => {
    let obj: window.TranslateOptions = {
      x: 100.0,
      y: 0.0,
      z: 0.0
    };
    toWindow?.translate(obj);
    console.info('toWindow translate end');
  }
  );
  try {
    context.completeTransition(true)
  } catch (exception) {
    console.error(`toWindow translate fail. Cause code: ${exception.code}, message: ${exception.message}`);
  }
  console.info('complete transition end');
};
```

## toWindow

```TypeScript
toWindow: Window
```

动画的目标窗口。

**类型：** [Window](arkts-arkui-window-window-i-sys.md)

**起始版本：** 9

<!--Device-TransitionContext-toWindow: Window--><!--Device-TransitionContext-toWindow: Window-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。
