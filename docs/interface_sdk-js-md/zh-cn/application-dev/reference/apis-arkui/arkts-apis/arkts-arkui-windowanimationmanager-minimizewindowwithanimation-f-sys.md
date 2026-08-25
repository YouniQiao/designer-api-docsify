# minimizeWindowWithAnimation（系统接口）

## 导入模块

```TypeScript
import { windowAnimationManager } from 'kits/@kit.ArkUI';
```

## minimizeWindowWithAnimation

```TypeScript
function minimizeWindowWithAnimation(windowTarget: WindowAnimationTarget,
    callback: AsyncCallback<WindowAnimationFinishedCallback>): void
```

最小化动画目标窗口，并返回动画完成的回调。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowTarget | [WindowAnimationTarget](../arkts-components/arkts-arkui-windowanimationtarget-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md)&gt; | 是 |


## minimizeWindowWithAnimation

```TypeScript
function minimizeWindowWithAnimation(windowTarget: WindowAnimationTarget): Promise<WindowAnimationFinishedCallback>
```

最小化动画目标窗口，并返回动画完成的回调。使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowTarget | [WindowAnimationTarget](../arkts-components/arkts-arkui-windowanimationtarget-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[WindowAnimationFinishedCallback](arkts-arkui-windowanimationmanager-windowanimationfinishedcallback-i-sys.md)&gt; |
