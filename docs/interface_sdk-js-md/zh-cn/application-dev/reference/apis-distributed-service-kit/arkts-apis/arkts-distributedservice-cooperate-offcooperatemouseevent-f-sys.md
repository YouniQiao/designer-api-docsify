# offCooperateMouseEvent（系统接口）

## offCooperateMouseEvent

```TypeScript
function offCooperateMouseEvent(networkId: string, callback?: Callback<MouseLocation>): void
```

Disables listening for mouse pointer position information on the specified device for cooperation.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function offCooperateMouseEvent(networkId: string, callback?: Callback<MouseLocation>): void--><!--Device-cooperate-function offCooperateMouseEvent(networkId: string, callback?: Callback<MouseLocation>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | Specified device. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MouseLocation](arkts-distributedservice-cooperate-mouselocation-i-sys.md)&gt; | 否 | Callback for receiving reported events. &lt;br&gt; If no callback is specified, listening will be disabled for all **cooperateMouse**. &lt;br&gt; events of the device specified by **networkId**. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified. &lt;br&gt;2. Incorrect parameter types. &lt;br&gt;3. Parameter verification failed. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Permission verification failed. A non-system application calls a system API. |

## 示例

```TypeScript
function callbackOn(data: cooperate.MouseLocation): void {
  console.info('Register mouse location listener');
}

function callbackOff(data: cooperate.MouseLocation): void {
  console.info('Unregister mouse location listener');
}

try {
  let networkId: string = 'Default';
  cooperate.onCooperateMouseEvent(networkId, callbackOn);
  cooperate.offCooperateMouseEvent(networkId, callbackOff);
} catch (error) {
  console.error(`Execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```

```TypeScript
function callbackOn(data: cooperate.MouseLocation): void {
  console.info('Register mouse location listener');
}

try {
  let networkId: string = 'Default';
  cooperate.onCooperateMouseEvent(networkId, callbackOn);
  cooperate.offCooperateMouseEvent(networkId);
} catch (error) {
  console.error(`Execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```

