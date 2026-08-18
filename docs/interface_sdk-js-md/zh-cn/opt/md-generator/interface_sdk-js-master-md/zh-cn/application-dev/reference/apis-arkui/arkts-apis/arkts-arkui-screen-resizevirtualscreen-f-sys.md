# resizeVirtualScreen（系统接口）

## 导入模块

```TypeScript
```

## resizeVirtualScreen

```TypeScript
function resizeVirtualScreen(screenId:number, width: number, height: number): Promise<void>
```

修改指定虚拟屏的尺寸，使用Promise异步回调。

**起始版本：** 24

<!--Device-screen-function resizeVirtualScreen(screenId:long, width: long, height: long): Promise<void>--><!--Device-screen-function resizeVirtualScreen(screenId:long, width: long, height: long): Promise<void>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| screenId | number | 是 |
| width | number | 是 |
| height | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400004](../errorcode-display.md#1400004-参数异常) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// 虚拟屏ID需从createVirtualScreen()返回值获取
let screenId: number = 1000; // 虚拟屏ID
let width: number = 1920;
let height: number = 1080;
// 修改虚拟屏的尺寸
screen.resizeVirtualScreen(screenId, width, height).then(() => {
  console.info(`Succeeded in resizing virtual screen: screenId=${screenId}, width=${width}, height=${height}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to resize virtual screen. Code: ${err.code}, message: ${err.message}`);
});
```
