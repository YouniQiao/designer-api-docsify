# TransitionContext (System API)

Provides the context for the transition animation.

**Since:** 9

<!--Device-window-interface TransitionContext--><!--Device-window-interface TransitionContext-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## completeTransition

```TypeScript
completeTransition(isCompleted: boolean): void
```

Completes the transition. This API can be called only after [animateTo()](../arkts-components/arkts-arkui-common-animateto-f.md/arkts-arkui-common-animateto-f.md#animateto)is executed.

**Since:** 9

<!--Device-TransitionContext-completeTransition(isCompleted: boolean): void--><!--Device-TransitionContext-completeTransition(isCompleted: boolean): void-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isCompleted | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
(context: window.TransitionContext) => {
  let toWindow: window.Window = context.toWindow;
  this.getUIContext()?.animateTo({
    duration: 1000, // Animation duration.
    tempo: 0.5, // Playback speed.
    curve: Curve.EaseInOut, // Animation curve.
    delay: 0, // Animation delay.
    iterations: 1, // Number of playback times.
    playMode: PlayMode.Normal // Animation playback mode.
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

The target window with animation

**Type:** [Window](arkts-arkui-window-window-i-sys.md)

**Since:** 9

<!--Device-TransitionContext-toWindow: Window--><!--Device-TransitionContext-toWindow: Window-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**System API:** This is a system API.
