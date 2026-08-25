# onApplicationFocusStateChange

## 导入模块

```TypeScript
import { window } from 'kits/@kit.ArkUI';
```

## onApplicationFocusStateChange

```TypeScript
function onApplicationFocusStateChange(callback: Callback<boolean>): void
```

开启应用进程获焦状态变化的监听。此监听针对应用间的获焦状态变化，若同应用内窗口间的获焦状态发生变化，则不会触发回调函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;boolean&gt; | 是 |
