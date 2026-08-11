# FloatingBallController

闪控球控制器实例，用于启动、更新、停止闪控球以及注册回调等操作。

下列API示例中都需先使用[floatingBall.create()](arkts-arkui-floatingball-create-f.md#create)方法获取到闪控球控制器实例（即floatingBallController），再通过此实例调用对应方法。

**起始版本：** 20

<!--Device-floatingBall-interface FloatingBallController--><!--Device-floatingBall-interface FloatingBallController-End-->

**系统能力：** SystemCapability.Window.SessionManager

## getFloatingBallWindowInfo

```TypeScript
getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>
```

获得闪控球窗口信息，使用Promise异步回调。

**起始版本：** 20

<!--Device-FloatingBallController-getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>--><!--Device-FloatingBallController-getFloatingBallWindowInfo(): Promise<FloatingBallWindowInfo>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise&lt;FloatingBallWindowInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300025](../errorcode-window.md#1300025-闪控球状态不支持该操作) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 获取闪控球窗口信息
floatingBallController.getFloatingBallWindowInfo().then((data: floatingBall.FloatingBallWindowInfo) => {
  console.info('Succeeded in getting floating ball window info. Info: ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(`Failed to get floating ball window info. Cause code: ${err.code}, message: ${err.message}`);
});
```

## off('stateChange')

```TypeScript
off(type: 'stateChange', callback?: Callback<FloatingBallState>): void
```

取消闪控球生命周期状态变化的监听事件。

**起始版本：** 20

<!--Device-FloatingBallController-off(type: 'stateChange', callback?: Callback<FloatingBallState>): void--><!--Device-FloatingBallController-off(type: 'stateChange', callback?: Callback<FloatingBallState>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'stateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FloatingBallState&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |

## 示例

```TypeScript
// 定义状态变化回调函数（需与注册时的回调一致）
let onStateChange = (state: floatingBall.FloatingBallState) => {
  console.info('Floating ball stateChange: ' + state);
};
try {
  // 取消闪控球状态变化监听
  floatingBallController.off('stateChange', onStateChange);
} catch (e) {
  console.error(`Failed to off stateChange floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## off('click')

```TypeScript
off(type: 'click', callback?: Callback<void>): void
```

取消闪控球点击的监听事件。

**起始版本：** 20

<!--Device-FloatingBallController-off(type: 'click', callback?: Callback<void>): void--><!--Device-FloatingBallController-off(type: 'click', callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'click' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |

## 示例

```TypeScript
// 定义点击事件回调函数（需与注册时的回调一致）
let onClick = () => {
  console.info('Floating ball onClick');
};
try {
  // 取消闪控球点击监听
  floatingBallController.off('click', onClick);
} catch (e) {
  console.error(`Failed to off click floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## offDestroy

```TypeScript
offDestroy(callback?: Callback<string>): void
```

取消闪控球销毁事件的监听。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatingBallController-offDestroy(callback?: Callback<string>): void--><!--Device-FloatingBallController-offDestroy(callback?: Callback<string>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |

## 示例

```TypeScript
// 定义销毁事件回调函数（需与注册时的回调一致）
let onDestroy = (reason: string) => {
  console.info('Floating ball has destroyed, reason: ' + reason);
};
try {
  // 取消闪控球销毁事件监听
  floatingBallController?.offDestroy(onDestroy);
} catch (e) {
  console.error(`Failed to offDestroy floating ball. Cause:${e.code}, message:${e.message}`);
}
// 取消所有监听
try {
  floatingBallController?.offDestroy();
} catch (e) {
  console.error(`Failed to offDestroy all listeners. Cause:${e.code}, message:${e.message}`);
}
```

## on('stateChange')

```TypeScript
on(type: 'stateChange', callback: Callback<FloatingBallState>): void
```

注册闪控球生命周期状态变化的监听事件。不再使用时，取消监听以避免内存泄漏。

**起始版本：** 20

<!--Device-FloatingBallController-on(type: 'stateChange', callback: Callback<FloatingBallState>): void--><!--Device-FloatingBallController-on(type: 'stateChange', callback: Callback<FloatingBallState>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'stateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FloatingBallState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300022](../errorcode-window.md#1300022-重复操作闪控球) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |

## 示例

```TypeScript
// 定义状态变化回调函数
let onStateChange = (state: floatingBall.FloatingBallState) => {
  console.info('Floating ball stateChange: ' + state);
};
try {
  // 注册闪控球状态变化监听
  floatingBallController.on('stateChange', onStateChange);
} catch (e) {
  console.error(`Failed to on stateChange floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## on('click')

```TypeScript
on(type: 'click', callback: Callback<void>): void
```

注册闪控球的点击监听事件，不使用时，取消监听以避免内存泄漏。

**起始版本：** 20

<!--Device-FloatingBallController-on(type: 'click', callback: Callback<void>): void--><!--Device-FloatingBallController-on(type: 'click', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'click' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300022](../errorcode-window.md#1300022-重复操作闪控球) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |

## 示例

```TypeScript
// 定义点击事件回调函数
let onClick = () => {
  console.info('Floating ball onClick');
};
try {
  // 注册闪控球点击监听
  floatingBallController.on('click', onClick);
} catch (e) {
  console.error(`Failed to on click floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## onDestroy

```TypeScript
onDestroy(callback: Callback<string>): void
```

注册闪控球销毁事件的监听。当闪控球销毁时，回调函数会接收到销毁原因的字符串。不再使用时，调用[offDestroy](#offdestroy)接口取消监听以避免内存泄漏。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatingBallController-onDestroy(callback: Callback<string>): void--><!--Device-FloatingBallController-onDestroy(callback: Callback<string>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300022](../errorcode-window.md#1300022-重复操作闪控球) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |

## 示例

```TypeScript
// 定义销毁事件回调函数
let onDestroy = (reason: string) => {
  console.info('Floating ball has destroyed, reason: ' + reason);
};
try {
  // 注册闪控球销毁事件监听
  floatingBallController?.onDestroy(onDestroy);
} catch (e) {
  console.error(`Failed to onDestroy floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## restoreMainWindow

```TypeScript
restoreMainWindow(want: Want): Promise<void>
```

恢复应用主窗口并加载指定页面。使用Promise异步回调。仅支持在点击闪控球后调用；若应用拥有`ohos.permission.AUTO_RESTORE_MAIN_WINDOW`权限，可以无需点击直接调用该接口。

**起始版本：** 20

**需要权限：** ohos.permission.USE_FLOAT_BALL

<!--Device-FloatingBallController-restoreMainWindow(want: Want): Promise<void>--><!--Device-FloatingBallController-restoreMainWindow(want: Want): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1300026](../errorcode-window.md#1300026-闪控球拉起应用窗口失败) |
| [1300025](../errorcode-window.md#1300025-闪控球状态不支持该操作) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { Want } from '@kit.AbilityKit';

// 配置要恢复的主窗口Want参数
let want: Want = {
  bundleName: 'xxx.xxx.xxx',
  abilityName: 'EntryAbility'
};
try {
  // 恢复应用主窗口并加载指定页面
  floatingBallController.restoreMainWindow(want).then(() => {
    console.info('Succeeded in restoring floating ball main window.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to restore floating ball main window. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (e) {
  console.error(`Failed to restore floating ball main window. Cause:${e.code}, message:${e.message}`);
}
```

## setFloatingBallVisibilityInApp

```TypeScript
setFloatingBallVisibilityInApp(isVisible: boolean): Promise<void>
```

设置闪控球在应用内是否可见。使用Promise异步回调。

- 当应用处于多任务界面时（[生命周期状态](../../../windowmanager/window-overview.md#生命周期状态)为PAUSED），闪控球不可见。  
- 默认情况（即未调用此接口设置时）和调用此接口传入true时：除多任务界面外，闪控球均可见。  
- 调用此接口传入false时：当应用处于前台（[生命周期状态](../../../windowmanager/window-overview.md#生命周期状态)为SHOWN或者RESUMED）时，闪控球不可见；当应用处于  
 后台（[生命周期状态](../../../windowmanager/window-overview.md#生命周期状态)为HIDDEN）时，闪控球可见。

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FloatingBallController-setFloatingBallVisibilityInApp(isVisible: boolean): Promise<void>--><!--Device-FloatingBallController-setFloatingBallVisibilityInApp(isVisible: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isVisible | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 设置闪控球在应用内不可见
floatingBallController?.setFloatingBallVisibilityInApp(false).then(() => {
  console.info('Succeeded in setting floating ball visibility.');
}).catch((err: BusinessError) => {
  console.error(`Failed to set floating ball visibility. Cause code: ${err.code}, message: ${err.message}`);
});
```

## startFloatingBall

```TypeScript
startFloatingBall(params: FloatingBallParams): Promise<void>
```

启动闪控球，使用Promise异步回调。

**起始版本：** 20

**需要权限：** ohos.permission.USE_FLOAT_BALL

<!--Device-FloatingBallController-startFloatingBall(params: FloatingBallParams): Promise<void>--><!--Device-FloatingBallController-startFloatingBall(params: FloatingBallParams): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [FloatingBallParams](arkts-arkui-floatingball-floatingballparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [1300034](../errorcode-window.md#1300034-闪控窗与其他悬浮窗口操作冲突) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300022](../errorcode-window.md#1300022-重复操作闪控球) |
| [1300021](../errorcode-window.md#1300021-启动多个闪控球失败) |
| [1300020](../errorcode-window.md#1300020-创建闪控球窗口失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [1300025](../errorcode-window.md#1300025-闪控球状态不支持该操作) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 配置闪控球启动参数
let startParams: floatingBall.FloatingBallParams = {
  template: floatingBall.FloatingBallTemplate.EMPHATIC,
  title: 'title',
  content: 'content'
};
try {
  // 启动闪控球
  floatingBallController.startFloatingBall(startParams).then(() => {
    console.info('Succeeded in starting floating ball.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to start floating ball. Cause:${err.code}, message:${err.message}`);
  });
} catch (e) {
  console.error(`Failed to start floating ball. Cause:${e.code}, message:${e.message}`);
}
```

## stopFloatingBall

```TypeScript
stopFloatingBall(): Promise<void>
```

停止闪控球，使用Promise异步回调。

**起始版本：** 20

<!--Device-FloatingBallController-stopFloatingBall(): Promise<void>--><!--Device-FloatingBallController-stopFloatingBall(): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300022](../errorcode-window.md#1300022-重复操作闪控球) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 停止闪控球
floatingBallController.stopFloatingBall().then(() => {
  console.info('Succeeded in stopping floating ball.');
}).catch((err: BusinessError) => {
  console.error(`Failed to stop floating ball. Cause:${err.code}, message:${err.message}`);
});
```

## updateFloatingBall

```TypeScript
updateFloatingBall(params: FloatingBallParams): Promise<void>
```

更新闪控球，使用Promise异步回调。

**起始版本：** 20

<!--Device-FloatingBallController-updateFloatingBall(params: FloatingBallParams): Promise<void>--><!--Device-FloatingBallController-updateFloatingBall(params: FloatingBallParams): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [FloatingBallParams](arkts-arkui-floatingball-floatingballparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [1300019](../errorcode-window.md#1300019-闪控球参数校验错误) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |
| [1300023](../errorcode-window.md#1300023-闪控球内部错误) |
| [1300004](../errorcode-window.md#1300004-无权限操作) |
| [1300027](../errorcode-window.md#1300027-更新闪控球时不能改变模板类型) |
| [1300025](../errorcode-window.md#1300025-闪控球状态不支持该操作) |
| [1300024](../errorcode-window.md#1300024-闪控球窗口状态异常) |
| [1300028](../errorcode-window.md#1300028-不支持更新静态模板类型闪控球) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 配置闪控球更新参数
let updateParams: floatingBall.FloatingBallParams = {
  template: floatingBall.FloatingBallTemplate.EMPHATIC,
  title: 'title2',
  content: 'content2'
};
try {
  // 更新闪控球
  floatingBallController.updateFloatingBall(updateParams).then(() => {
    console.info('Succeeded in updating floating ball.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to update floating ball. Cause:${err.code}, message:${err.message}`);
  });
} catch (e) {
  console.error(`Failed to update floating ball. Cause:${e.code}, message:${e.message}`);
}
```
