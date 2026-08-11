# off

## off('add' | 'remove' | 'change')

```TypeScript
function off(type: 'add' | 'remove' | 'change', callback?: Callback<number>): void
```

关闭显示设备变化的监听。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function off(type: 'add' | 'remove' | 'change', callback?: Callback<long>): void--><!--Device-display-function off(type: 'add' | 'remove' | 'change', callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'add' \| 'remove' \| 'change' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
// 如果通过on注册多个callback，同时关闭所有callback监听
display.off('remove');

let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in unregistering the callback for display remove. Data: ${data}`)
};
// 关闭传入的callback监听
display.off('remove', callback);
```


## off('add' | 'remove' | 'change')

```TypeScript
function off(type: 'add' | 'remove' | 'change', callback?: Callback<number>): void
```

关闭显示设备变化的监听。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function off(type: 'add' | 'remove' | 'change', callback?: Callback<long>): void--><!--Device-display-function off(type: 'add' | 'remove' | 'change', callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'add' \| 'remove' \| 'change' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
// 如果通过on注册多个callback，同时关闭所有callback监听
display.off('remove');

let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in unregistering the callback for display remove. Data: ${data}`)
};
// 关闭传入的callback监听
display.off('remove', callback);
```


## off('add' | 'remove' | 'change')

```TypeScript
function off(type: 'add' | 'remove' | 'change', callback?: Callback<number>): void
```

关闭显示设备变化的监听。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function off(type: 'add' | 'remove' | 'change', callback?: Callback<long>): void--><!--Device-display-function off(type: 'add' | 'remove' | 'change', callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'add' \| 'remove' \| 'change' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
// 如果通过on注册多个callback，同时关闭所有callback监听
display.off('remove');

let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in unregistering the callback for display remove. Data: ${data}`)
};
// 关闭传入的callback监听
display.off('remove', callback);
```


## off('foldStatusChange')

```TypeScript
function off(type: 'foldStatusChange', callback?: Callback<FoldStatus>): void
```

关闭折叠设备折叠状态变化的监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function off(type: 'foldStatusChange', callback?: Callback<FoldStatus>): void--><!--Device-display-function off(type: 'foldStatusChange', callback?: Callback<FoldStatus>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'foldStatusChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FoldStatus&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
// 如果通过on注册多个callback，同时关闭所有callback监听
display.off('foldStatusChange');

let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
  console.info(`unregistering FoldStatus changes callback. Data: ${data}`);
};
// 关闭传入的callback监听
display.off('foldStatusChange', callback);
```


## off('foldAngleChange')

```TypeScript
function off(type: 'foldAngleChange', callback?: Callback<Array<number>>): void
```

关闭折叠设备折叠角度变化的监听。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function off(type: 'foldAngleChange', callback?: Callback<Array<double>>): void--><!--Device-display-function off(type: 'foldAngleChange', callback?: Callback<Array<double>>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'foldAngleChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;number&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

// 如果通过on注册多个callback，同时关闭所有callback监听
display.off('foldAngleChange');

let callback: Callback<Array<number>> = (angles: Array<number>) => {
  console.info('Listening fold angles length: ' + angles.length);
};
// 关闭传入的callback监听
display.off('foldAngleChange', callback);
```


## off('captureStatusChange')

```TypeScript
function off(type: 'captureStatusChange', callback?: Callback<boolean>): void
```

关闭设备的屏幕显示信息是否被获取的监听。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function off(type: 'captureStatusChange', callback?: Callback<boolean>): void--><!--Device-display-function off(type: 'captureStatusChange', callback?: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'captureStatusChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

// 如果通过on注册多个callback，同时关闭所有callback监听
display.off('captureStatusChange');

let callback: Callback<boolean> = (captureStatus: boolean) => {
  console.info('Listening capture status: ' + captureStatus);
};
// 关闭传入的callback监听
display.off('captureStatusChange', callback);
```


## off('foldDisplayModeChange')

```TypeScript
function off(type: 'foldDisplayModeChange', callback?: Callback<FoldDisplayMode>): void
```

关闭折叠设备屏幕显示模式变化的监听。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function off(type: 'foldDisplayModeChange', callback?: Callback<FoldDisplayMode>): void--><!--Device-display-function off(type: 'foldDisplayModeChange', callback?: Callback<FoldDisplayMode>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'foldDisplayModeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FoldDisplayMode&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

// 如果通过on注册多个callback，同时关闭所有callback监听
display.off('foldDisplayModeChange');

let callback: Callback<display.FoldDisplayMode> = (data: display.FoldDisplayMode) => {
  console.info(`unregistering FoldDisplayMode changes callback. Data: ${data}`);
};
// 关闭传入的callback监听
display.off('foldDisplayModeChange', callback);
```


## off('brightnessInfoChange')

```TypeScript
function off(type: 'brightnessInfoChange', callback?: BrightnessCallback<number, BrightnessInfo>): void
```

关闭所有屏幕亮度信息状态变化的监听。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-display-function off(type: 'brightnessInfoChange', callback?: BrightnessCallback<long, BrightnessInfo>): void--><!--Device-display-function off(type: 'brightnessInfoChange', callback?: BrightnessCallback<long, BrightnessInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'brightnessInfoChange' | 是 |
| callback | [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md)&lt;number, BrightnessInfo&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400004](../errorcode-display.md#1400004-参数异常) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
let callback: display.BrightnessCallback<number, display.BrightnessInfo> = (id: number, data: display.BrightnessInfo) => {
  console.info(`Listening enabled ${id}. Data: ${JSON.stringify(data)}`);
};
try {
  display.off('brightnessInfoChange', callback);
} catch (error) {
  console.error(`Failed to unregister brightnessInfoChange listener. Code ${error.code}, message: ${error.message}`);
}
```
