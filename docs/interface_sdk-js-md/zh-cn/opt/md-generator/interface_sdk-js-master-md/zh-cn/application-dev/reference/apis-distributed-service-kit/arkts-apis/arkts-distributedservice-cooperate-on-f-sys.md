# on（系统接口）

## on('cooperate')

```TypeScript
function on(type: 'cooperate', callback: Callback<{ networkId: string, msg: CooperateMsg }>): void
```

注册监听键鼠穿越状态。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [on](../../apis-test-kit/arkts-apis/arkts-test-uitest-on-c.md/arkts-test-uitest-on-c.md)(type:

<!--Device-cooperate-function on(type: 'cooperate', callback: Callback<{ networkId: string, msg: CooperateMsg }>): void--><!--Device-cooperate-function on(type: 'cooperate', callback: Callback<{ networkId: string, msg: CooperateMsg }>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cooperate' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;{ networkId: string, msg: CooperateMsg }&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { cooperate } from '@kit.DistributedServiceKit';
class Data {
  networkId: string = "networkId";
  msg: cooperate.CooperateMsg = 0;
}

try {
  cooperate.on('cooperate', (data: Data) => {
    console.info(`Keyboard mouse crossing event: ${JSON.stringify(data)}`);
  });
} catch (error) {
  console.error(`Register failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```


## on('cooperateMessage')

```TypeScript
function on(type: 'cooperateMessage', callback: Callback<CooperateMessage>): void
```

注册监听键鼠穿越状态。

**起始版本：** 11

**需要权限：** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function on(type: 'cooperateMessage', callback: Callback<CooperateMessage>): void--><!--Device-cooperate-function on(type: 'cooperateMessage', callback: Callback<CooperateMessage>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cooperateMessage' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CooperateMessage&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function callback(msg: cooperate.CooperateMessage) {
  console.info(`Keyboard mouse crossing event: ${JSON.stringify(msg)}`);
  return false;
}

try {
  cooperate.on('cooperateMessage', callback);
} catch (error) {
  console.error(`Register failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```


## on('cooperateMouse')

```TypeScript
function on(type: 'cooperateMouse', networkId: string, callback: Callback<MouseLocation>): void
```

注册监听指定设备鼠标光标位置。

**起始版本：** 12

**需要权限：** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function on(type: 'cooperateMouse', networkId: string, callback: Callback<MouseLocation>): void--><!--Device-cooperate-function on(type: 'cooperateMouse', networkId: string, callback: Callback<MouseLocation>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cooperateMouse' | 是 |
| networkId | string | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MouseLocation&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function callback(data: cooperate.MouseLocation) {
  console.info('displayX:' + data.displayX + 'displayY:' + data.displayY + 'displayWidth:' +
  data.displayWidth + 'displayHeight:' + data.displayHeight);
}

try {
  let networkId: string = 'Default';
  cooperate.on('cooperateMouse', networkId, callback);
} catch (error) {
  console.error(`Register failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
}
```
