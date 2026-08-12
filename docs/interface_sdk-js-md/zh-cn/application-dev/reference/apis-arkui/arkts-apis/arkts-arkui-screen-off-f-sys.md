# off（系统接口）

## off

```TypeScript
function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void
```

关闭屏幕状态变化的监听。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void--><!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | 是 | 监听事件。&lt;br/&gt;-eventType为"connect"表示屏幕连接事件。&lt;br/&gt;-eventType为" disconnect"表示断开屏幕连接事件。&lt;br/&gt;-eventType为"change"表示屏幕状态改变事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 否 | 回调函数。返回屏幕的id，该参数为整数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Permission verification failed. A non-system application calls a system API. |

## 示例

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in unregistering the callback for screen changes. Data: ${data}`);
};
// 关闭传入的callback监听
screen.off('connect', callback);
// 如果通过on注册多个callback，同时关闭所有callback监听
screen.off('connect');
```


## off

```TypeScript
function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void
```

关闭屏幕状态变化的监听。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void--><!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | 是 | 监听事件。&lt;br/&gt;-eventType为"connect"表示屏幕连接事件。&lt;br/&gt;-eventType为" disconnect"表示断开屏幕连接事件。&lt;br/&gt;-eventType为"change"表示屏幕状态改变事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 否 | 回调函数。返回屏幕的id，该参数为整数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Permission verification failed. A non-system application calls a system API. |

## 示例

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in unregistering the callback for screen changes. Data: ${data}`);
};
// 关闭传入的callback监听
screen.off('connect', callback);
// 如果通过on注册多个callback，同时关闭所有callback监听
screen.off('connect');
```


## off

```TypeScript
function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void
```

关闭屏幕状态变化的监听。

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void--><!--Device-screen-function off(eventType: 'connect' | 'disconnect' | 'change', callback?: Callback<long>): void-End-->

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| eventType | 'connect' \| 'disconnect' \| 'change' | 是 | 监听事件。&lt;br/&gt;-eventType为"connect"表示屏幕连接事件。&lt;br/&gt;-eventType为" disconnect"表示断开屏幕连接事件。&lt;br/&gt;-eventType为"change"表示屏幕状态改变事件。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;long&gt; | 否 | 回调函数。返回屏幕的id，该参数为整数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Permission verification failed. A non-system application calls a system API. |

## 示例

```TypeScript
let callback: Callback<number> = (data: number) => {
  console.info(`Succeeded in unregistering the callback for screen changes. Data: ${data}`);
};
// 关闭传入的callback监听
screen.off('connect', callback);
// 如果通过on注册多个callback，同时关闭所有callback监听
screen.off('connect');
```

