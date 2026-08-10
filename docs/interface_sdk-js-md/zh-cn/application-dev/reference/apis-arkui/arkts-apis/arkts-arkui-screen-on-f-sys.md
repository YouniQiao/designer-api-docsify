# on（系统接口）

## 导入模块

```TypeScript
import { screen } from 'kits/@kit.ArkUI';
```

## on

```TypeScript
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void
```

开启屏幕状态变化的监听。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | 是 | 监听事件。&lt;br/&gt;-eventType为"connect"表示屏幕连接事件。&lt;br/&gt;-eventType为" disconnect"表示断开屏幕连接事件。&lt;br/&gt;-eventType为"change"表示屏幕状态改变事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 是 | 回调函数。返回屏幕的id，该参数为整数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## 示例

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in registering the callback for screen changes. Data: ${data}`);
};
// 开启屏幕连接事件的监听
screen.on('connect', callback);
```


## on

```TypeScript
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void
```

开启屏幕状态变化的监听。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | 是 | 监听事件。&lt;br/&gt;-eventType为"connect"表示屏幕连接事件。&lt;br/&gt;-eventType为" disconnect"表示断开屏幕连接事件。&lt;br/&gt;-eventType为"change"表示屏幕状态改变事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 是 | 回调函数。返回屏幕的id，该参数为整数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## 示例

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in registering the callback for screen changes. Data: ${data}`);
};
// 开启屏幕连接事件的监听
screen.on('connect', callback);
```


## on

```TypeScript
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void
```

开启屏幕状态变化的监听。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | 是 | 监听事件。&lt;br/&gt;-eventType为"connect"表示屏幕连接事件。&lt;br/&gt;-eventType为" disconnect"表示断开屏幕连接事件。&lt;br/&gt;-eventType为"change"表示屏幕状态改变事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 是 | 回调函数。返回屏幕的id，该参数为整数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| 202 | Permission verification failed. A non-system application calls a system API. |

## 示例

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in registering the callback for screen changes. Data: ${data}`);
};
// 开启屏幕连接事件的监听
screen.on('connect', callback);
```

