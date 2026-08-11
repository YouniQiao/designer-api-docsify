# on（系统接口）

## on

```TypeScript
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<number>): void
```

开启屏幕状态变化的监听。

**起始版本：** 9

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

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
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<number>): void
```

开启屏幕状态变化的监听。

**起始版本：** 9

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

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
function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<number>): void
```

开启屏幕状态变化的监听。

**起始版本：** 9

<!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void--><!--Device-screen-function on(eventType: 'connect' | 'disconnect' | 'change', callback: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in registering the callback for screen changes. Data: ${data}`);
};
// 开启屏幕连接事件的监听
screen.on('connect', callback);
```
