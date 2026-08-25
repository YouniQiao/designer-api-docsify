# getWindowsByCoordinate

## 导入模块

```TypeScript
import { window } from '@kit.ArkUI';
```

## getWindowsByCoordinate

```TypeScript
function getWindowsByCoordinate(displayId: long, windowNumber?: int, x?: int, y?: int):
      Promise<Array<Window>>
```

查询本应用指定坐标下的可见窗口数组，按当前窗口层级排列，层级最高的窗口对应数组下标为0，使用Promise异步回调。

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| windowNumber | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| x | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |
| y | ArkTS-Dyn: number<br>ArkTS-Sta：int | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Window](arkts-arkui-window-window-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { UIAbility } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage): void {
    let windowClass: window.Window | undefined = undefined;
    try {
      let displayId = 0;
      window.getWindowsByCoordinate(displayId, 2, 500, 500).then((data) => {
        console.info(`Succeeded in getting windows. Data: ${data}`);
        for (let windowObject of data) {
          // do something with window
          windowClass = windowObject;
        }
      }).catch((err: BusinessError) => {
        console.error(`Failed to get window from point. Cause code: ${err.code}, message: ${err.message}`);
      });
    } catch (exception) {
      console.error(`Failed to get window from point. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let displayId = 0;
  window.getWindowsByCoordinate(displayId).then((data) => {
    console.info(`Succeeded in getting windows. Data: ${data}`);
  }).catch((err: Error) => {
    console.error(`Failed to get window from point. Cause code: ${err.code}, message: ${err.message}`);
  });
  window.getWindowsByCoordinate(displayId, 2, 500, 500).then((data) => {
    console.info(`Succeeded in getting windows. Data: ${data}`);
  }).catch((err: Error) => {
    console.error(`Failed to get window from point. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  let error = exception as BusinessError;
  console.error(`Failed to get window from point. Cause code: ${error.code}, message: ${error.message}`);
}
```
