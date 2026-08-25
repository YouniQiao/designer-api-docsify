# hasPrivateWindow（系统接口）

## 导入模块

```TypeScript
import { display } from '@kit.ArkUI';
```

## hasPrivateWindow

```TypeScript
function hasPrivateWindow(displayId: long): boolean
```

查询指定display对象上是否有可见的隐私窗口。可通过 [setWindowPrivacyMode()](../../../reference/apis-arkui/arkts-apis-window-Window.md#setwindowprivacymode9)接口设置隐私窗口。 隐私窗口内容将无法被截屏或录屏。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  // 获取默认Display对象
  displayClass = display.getDefaultDisplaySync();

  let hasPrivateWindow: boolean = false;
  try {
    // 查询默认屏幕上是否有隐私窗口
    hasPrivateWindow = display.hasPrivateWindow(displayClass.id);
  } catch (exception) {
    console.error(`Failed to check has privateWindow or not. Code: ${exception.code}, message: ${exception.message}`);
  }
  if (hasPrivateWindow) {
    console.info('There has privateWindow.');
  } else if (!hasPrivateWindow) {
    console.info('There has no privateWindow.');
  }
} catch (exception) {
  console.error(`Failed to obtain the default display object. Code: ${exception.code}, message: ${exception.message}`);
}
```

ArkTS-Sta示例：

```TypeScript
import { display } from '@kit.ArkUI';

let displayClass: display.Display | null = null;
try {
  displayClass = display.getDefaultDisplaySync();

  let ret: boolean = true;
  try {
    ret = display.hasPrivateWindow(displayClass.id);
  } catch (exception) {
    let error = exception as BusinessError;
    console.error(`Failed to check has privateWindow or not. Code: ${error.code} , message: ${error.message}`);
  }
  if (ret == undefined) {
    console.error("Failed to check has privateWindow or not.");
  }
  if (ret) {
    console.info("There has privateWindow.");
  } else if (!ret) {
    console.info("There has no privateWindow.");
  }
} catch (exception) {
  let error = exception as BusinessError;
  console.error(`Failed to obtain the default display object. Code: ${error.code} , message: ${error.message}`);
}
```
