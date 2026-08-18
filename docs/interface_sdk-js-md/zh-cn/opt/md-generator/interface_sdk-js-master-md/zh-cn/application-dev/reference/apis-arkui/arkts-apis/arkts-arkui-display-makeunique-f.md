# makeUnique

## 导入模块

```TypeScript
```

## makeUnique

```TypeScript
function makeUnique(screenId: number): Promise<void>
```

将屏幕设置为异源模式，使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.ACCESS_VIRTUAL_SCREEN

<!--Device-display-function makeUnique(screenId: long): Promise<void>--><!--Device-display-function makeUnique(screenId: long): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| screenId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let screenId: number = 0;
// 将屏幕设置为异源模式
display.makeUnique(screenId).then(() => {
  console.info('Succeeded in making unique screens.');
}).catch((err: BusinessError) => {
  console.error(`Failed to make unique screens. Code: ${err.code}, message: ${err.message}`);
});
```
