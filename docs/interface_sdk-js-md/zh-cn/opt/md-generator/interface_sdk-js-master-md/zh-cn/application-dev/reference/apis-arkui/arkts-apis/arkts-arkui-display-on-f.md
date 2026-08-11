# on

## on('add' | 'remove' | 'change')

```TypeScript
function on(type: 'add' | 'remove' | 'change', callback: Callback<number>): void
```

开启显示设备变化的监听。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function on(type: 'add' | 'remove' | 'change', callback: Callback<long>): void--><!--Device-display-function on(type: 'add' | 'remove' | 'change', callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'add' \| 'remove' \| 'change' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<number> = (data: number) => {
  console.info(`Listening enabled. Data: ${data}`);
};

display.on('add', callback);
```


## on('add' | 'remove' | 'change')

```TypeScript
function on(type: 'add' | 'remove' | 'change', callback: Callback<number>): void
```

开启显示设备变化的监听。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function on(type: 'add' | 'remove' | 'change', callback: Callback<long>): void--><!--Device-display-function on(type: 'add' | 'remove' | 'change', callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'add' \| 'remove' \| 'change' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<number> = (data: number) => {
  console.info(`Listening enabled. Data: ${data}`);
};

display.on('add', callback);
```


## on('add' | 'remove' | 'change')

```TypeScript
function on(type: 'add' | 'remove' | 'change', callback: Callback<number>): void
```

开启显示设备变化的监听。

**起始版本：** 7

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function on(type: 'add' | 'remove' | 'change', callback: Callback<long>): void--><!--Device-display-function on(type: 'add' | 'remove' | 'change', callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'add' \| 'remove' \| 'change' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<number> = (data: number) => {
  console.info(`Listening enabled. Data: ${data}`);
};

display.on('add', callback);
```


## on('foldStatusChange')

```TypeScript
function on(type: 'foldStatusChange', callback: Callback<FoldStatus>): void
```

开启折叠设备折叠状态变化的监听。

本接口监听设备物理折叠状态的变化，如果要监听屏幕显示模式的变化，需要使用  
[display.on('foldDisplayModeChange')](display.on(type: 'foldDisplayModeChange', callback: Callback&lt;FoldDisplayMode&gt;))接口。

两者存在差异，时序上物理折叠状态变化在前，底层会根据物理折叠状态匹配屏幕显示模式状态。

若需监听当前显示内容是显示在折叠设备的内屏还是外屏，请使用  
[display.on('foldDisplayModeChange')](display.on(type: 'foldDisplayModeChange', callback: Callback&lt;FoldDisplayMode&gt;))。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function on(type: 'foldStatusChange', callback: Callback<FoldStatus>): void--><!--Device-display-function on(type: 'foldStatusChange', callback: Callback<FoldStatus>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'foldStatusChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FoldStatus&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

/**
 * 注册监听的callback参数要采用对象传递。
 * 若使用匿名函数注册，每次调用会创建一个新的底层对象，引起内存泄漏问题。
 */
let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
  console.info(`Listening enabled. Data: ${data}`);
};
display.on('foldStatusChange', callback);
```


## on('foldAngleChange')

```TypeScript
function on(type: 'foldAngleChange', callback: Callback<Array<number>>): void
```

开启折叠设备折叠角度变化的监听。如果是双折轴设备，则有两个角度值；在充电口朝下的状态下，从右到左分别是折轴一和折轴二。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function on(type: 'foldAngleChange', callback: Callback<Array<double>>): void--><!--Device-display-function on(type: 'foldAngleChange', callback: Callback<Array<double>>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'foldAngleChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;number&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<Array<number>> = (angles: Array<number>) => {
  console.info('Listening fold angles length: ' + angles.length);
};
display.on('foldAngleChange', callback);
```


## on('captureStatusChange')

```TypeScript
function on(type: 'captureStatusChange', callback: Callback<boolean>): void
```

开启设备的屏幕显示信息是否被获取的监听。

**起始版本：** 12

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function on(type: 'captureStatusChange', callback: Callback<boolean>): void--><!--Device-display-function on(type: 'captureStatusChange', callback: Callback<boolean>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'captureStatusChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<boolean> = (captureStatus: boolean) => {
  console.info('Listening capture status: ' + captureStatus);
};
display.on('captureStatusChange', callback);
```


## on('foldDisplayModeChange')

```TypeScript
function on(type: 'foldDisplayModeChange', callback: Callback<FoldDisplayMode>): void
```

开启折叠设备屏幕显示模式变化的监听。

本接口监听设备屏幕显示模式的变化，如果要监听设备物理折叠状态的变化，需要使用  
[display.on('foldStatusChange')](display.on(type: 'foldStatusChange', callback: Callback&lt;FoldStatus&gt;))接口。

两者存在差异，时序上物理折叠状态变化在前，底层会根据物理折叠状态匹配屏幕显示模式状态。

**起始版本：** 10

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-display-function on(type: 'foldDisplayModeChange', callback: Callback<FoldDisplayMode>): void--><!--Device-display-function on(type: 'foldDisplayModeChange', callback: Callback<FoldDisplayMode>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'foldDisplayModeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FoldDisplayMode&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |

## 示例

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

/**
 * 注册监听的callback参数要采用对象传递。
 * 若使用匿名函数注册，每次调用会创建一个新的底层对象，引起内存泄漏问题。
 */
let callback: Callback<display.FoldDisplayMode> = (data: display.FoldDisplayMode) => {
  console.info(`Listening enabled. Data: ${data}`);
}; 
display.on('foldDisplayModeChange', callback);
```


## on('brightnessInfoChange')

```TypeScript
function on(type: 'brightnessInfoChange', callback: BrightnessCallback<number, BrightnessInfo>): void
```

开启所有屏幕亮度信息变化的监听。如果屏幕不支持HDR，监听到的[BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md)对象中的currentHeadroom和maxHeadroom为默认值。虚拟屏的BrightnessInfo对象中sdrNits为默认值。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-display-function on(type: 'brightnessInfoChange', callback: BrightnessCallback<long, BrightnessInfo>): void--><!--Device-display-function on(type: 'brightnessInfoChange', callback: BrightnessCallback<long, BrightnessInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'brightnessInfoChange' | 是 |
| callback | [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md)&lt;number, BrightnessInfo&gt; | 是 |

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
  display.on('brightnessInfoChange', callback);
} catch (error) {
  console.error(`Failed to register brightnessInfoChange listener. Code ${error.code}, message: ${error.message}`);
}
```
