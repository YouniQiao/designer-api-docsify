# offFoldDisplayModeChange

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## offFoldDisplayModeChange

```TypeScript
function offFoldDisplayModeChange(callback?: Callback<FoldDisplayMode>): void
```

Unregister the callback for fold display mode changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-display-function offFoldDisplayModeChange(callback?: Callback<FoldDisplayMode>): void--><!--Device-display-function offFoldDisplayModeChange(callback?: Callback<FoldDisplayMode>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FoldDisplayMode&gt; | 否 | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 1400003 | This display manager service works abnormally. |

