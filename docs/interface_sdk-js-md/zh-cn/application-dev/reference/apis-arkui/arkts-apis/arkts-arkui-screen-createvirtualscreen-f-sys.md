# createVirtualScreen（系统接口）

## 导入模块

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## createVirtualScreen

```TypeScript
function createVirtualScreen(options:VirtualScreenOption, callback: AsyncCallback<Screen>): void
```

创建虚拟屏幕，使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.CAPTURE_SCREEN

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [VirtualScreenOption](arkts-arkui-screen-virtualscreenoption-i-sys.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Screen](arkts-arkui-screen-screen-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |


## createVirtualScreen

```TypeScript
function createVirtualScreen(options:VirtualScreenOption): Promise<Screen>
```

创建虚拟屏幕，使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.CAPTURE_SCREEN

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [VirtualScreenOption](arkts-arkui-screen-virtualscreenoption-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Screen](arkts-arkui-screen-screen-i-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
