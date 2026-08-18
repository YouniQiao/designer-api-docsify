# getAllWindowLayoutInfo

## 导入模块

```TypeScript
```

## getAllWindowLayoutInfo

```TypeScript
function getAllWindowLayoutInfo(displayId: number): Promise<Array<WindowLayoutInfo>>
```

获取指定屏幕上可见的窗口布局信息数组，其中返回的每个Rect的宽、高是已经过缩放计算后的值，按当前窗口层级排列，层级最高的对应数组index为0，使用Promise异步回调。

**起始版本：** 23

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

<!--Device-window-function getAllWindowLayoutInfo(displayId: long): Promise<Array<WindowLayoutInfo>>--><!--Device-window-function getAllWindowLayoutInfo(displayId: long): Promise<Array<WindowLayoutInfo>>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[WindowLayoutInfo](arkts-arkui-window-windowlayoutinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300002](../errorcode-window.md#1300002-窗口状态异常) |

**示例**

```TypeScript
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let displayId = 0;
  let promise = window.getAllWindowLayoutInfo(displayId);
  promise.then((data) => {
    console.info('Succeeded in obtaining all window layout info. Data: ' + JSON.stringify(data));
  }).catch((err: BusinessError) => {
    console.error(`Failed to obtain all window layout info. Cause code: ${err.code}, message: ${err.message}`);
  });
} catch (exception) {
  console.error(`Failed to obtain all window layout info. Cause code: ${exception.code}, message: ${exception.message}`);
}
```


## getAllWindowLayoutInfo

```TypeScript
function getAllWindowLayoutInfo(displayId: number, option?: WindowInfoOptions): Promise<Array<WindowLayoutInfo>>
```

根据option指定的过滤条件获取指定屏幕上可见的窗口布局信息数组，其中返回的每个Rect的宽、高是已经过缩放计算后的值，按当前窗口层级排列，层级最高的对应数组index为0，使用Promise异步回调。当未传入option或其中 的字段都为默认值时，当前接口与[getAllWindowLayoutInfo](#getallwindowlayoutinfo)等价。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-window-function getAllWindowLayoutInfo(displayId: long, option?: WindowInfoOptions): Promise<Array<WindowLayoutInfo>>--><!--Device-window-function getAllWindowLayoutInfo(displayId: long, option?: WindowInfoOptions): Promise<Array<WindowLayoutInfo>>-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| displayId | number | 是 |
| option | [WindowInfoOptions](arkts-arkui-window-windowinfooptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[WindowLayoutInfo](arkts-arkui-window-windowlayoutinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [1300003](../errorcode-window.md#1300003-系统服务工作异常) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1300016](../errorcode-window.md#1300016-参数校验错误) |
