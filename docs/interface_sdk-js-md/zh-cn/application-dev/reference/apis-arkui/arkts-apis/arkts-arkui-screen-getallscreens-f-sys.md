# getAllScreens（系统接口）

## 导入模块

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## getAllScreens

```TypeScript
function getAllScreens(callback: AsyncCallback<Array<Screen>>): void
```

获取所有的屏幕，使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Screen](arkts-arkui-screen-screen-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |


## getAllScreens

```TypeScript
function getAllScreens(): Promise<Array<Screen>>
```

获取所有的屏幕，使用Promise异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Screen](arkts-arkui-screen-screen-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
