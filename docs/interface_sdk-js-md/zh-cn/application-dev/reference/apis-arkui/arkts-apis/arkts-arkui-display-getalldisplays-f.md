# getAllDisplays

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## getAllDisplays

```TypeScript
function getAllDisplays(callback: AsyncCallback<Array<Display>>): void
```

获取当前所有的Display对象，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Display](arkts-arkui-display-display-i.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |


## getAllDisplays

```TypeScript
function getAllDisplays(): Promise<Array<Display>>
```

获取当前所有的Display对象，使用Promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Display](arkts-arkui-display-display-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1400001](../errorcode-display.md#1400001-无效的显示设备) |
