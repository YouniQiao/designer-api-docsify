# offSystemBarTintChange（系统接口）

## 导入模块

```TypeScript
import { window } from '@kit.ArkUI';
```

## offSystemBarTintChange

```TypeScript
function offSystemBarTintChange(callback?: Callback<SystemBarTintState>): void
```

关闭状态栏、导航栏属性变化的监听。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-arkui-window-callback-i.md)&lt;[SystemBarTintState](arkts-arkui-window-systembartintstate-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
const callback = (systemBarTintState: window.SystemBarTintState) => {
  // ...
}
try {
  window.onSystemBarTintChange(callback);

  window.offSystemBarTintChange(callback);
  // 如果通过on开启多个callback进行监听，同时关闭所有监听：
  window.offSystemBarTintChange();
} catch (exception) {
  let error = exception as BusinessError;
  console.error(`Failed to enable or disable the listener for systemBarTint changes. Cause code: ${error.code}, message: ${error.message}`);
}
```
