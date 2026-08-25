# offFoldDisplayModeChange

## 导入模块

```TypeScript
import { display } from '@kit.ArkUI';
```

## offFoldDisplayModeChange

```TypeScript
function offFoldDisplayModeChange(callback?: Callback<FoldDisplayMode>): void
```

Unregister the callback for fold display mode changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[FoldDisplayMode](arkts-arkui-display-folddisplaymode-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

**示例**

```TypeScript
// 如果通过on注册多个callback，同时关闭所有callback监听
display.offFoldDisplayModeChange();

let callback: Callback<display.FoldDisplayMode> = (data: display.FoldDisplayMode) => {
  console.info(`unregistering FoldDisplayMode changes callback. Data: ${data}`);
};
// 关闭传入的callback监听
display.offFoldDisplayModeChange(callback);
```
