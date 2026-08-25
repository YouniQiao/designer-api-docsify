# stopMirror（系统接口）

## 导入模块

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## stopMirror

```TypeScript
function stopMirror(mirrorScreen:Array<number>, callback: AsyncCallback<void>): void
```

停止屏幕的镜像模式，使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mirrorScreen | Array & lt;number & gt; | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |


## stopMirror

```TypeScript
function stopMirror(mirrorScreen:Array<number>): Promise<void>
```

停止屏幕的镜像模式，使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mirrorScreen | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
