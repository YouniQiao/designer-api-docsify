# on（系统接口）

## on('sessionCreate')

```TypeScript
function on(type: 'sessionCreate', callback: (session: AVSessionDescriptor) => void): void
```

会话的创建事件监听。 使用callback异步回调。

**起始版本：** 9

<!--Device-avSession-function on(type: 'sessionCreate', callback: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function on(type: 'sessionCreate', callback: (session: AVSessionDescriptor) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sessionCreate' | 是 |
| callback | (session: AVSessionDescriptor) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            avSession.on('sessionCreate', (descriptor: avSession.AVSessionDescriptor) => {
              console.info(`on sessionCreate : isActive : ${descriptor.isActive}`);
              console.info(`on sessionCreate : type : ${descriptor.type}`);
              console.info(`on sessionCreate : sessionTag : ${descriptor.sessionTag}`);
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```


## on('sessionDestroy')

```TypeScript
function on(type: 'sessionDestroy', callback: (session: AVSessionDescriptor) => void): void
```

会话的销毁事件监听。使用callback异步回调。

**起始版本：** 9

<!--Device-avSession-function on(type: 'sessionDestroy', callback: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function on(type: 'sessionDestroy', callback: (session: AVSessionDescriptor) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sessionDestroy' | 是 |
| callback | (session: AVSessionDescriptor) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            avSession.on('sessionDestroy', (descriptor: avSession.AVSessionDescriptor) => {
              console.info(`on sessionDestroy : ${descriptor.sessionId}`);
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```


## on('topSessionChange')

```TypeScript
function on(type: 'topSessionChange', callback: (session: AVSessionDescriptor) => void): void
```

最新播放会话变更的事件监听。使用callback异步回调。

**起始版本：** 9

<!--Device-avSession-function on(type: 'topSessionChange', callback: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function on(type: 'topSessionChange', callback: (session: AVSessionDescriptor) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'topSessionChange' | 是 |
| callback | (session: AVSessionDescriptor) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            avSession.on('topSessionChange', (descriptor: avSession.AVSessionDescriptor) => {
              console.info(`on topSessionChange : isActive : ${descriptor.isActive}`);
              console.info(`on topSessionChange : type : ${descriptor.type}`);
              console.info(`on topSessionChange : sessionTag : ${descriptor.sessionTag}`);
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```


## on('sessionServiceDie')

```TypeScript
function on(type: 'sessionServiceDie', callback: () => void): void
```

监听会话的服务死亡事件。通知应用清理资源。

**起始版本：** 9

<!--Device-avSession-function on(type: 'sessionServiceDie', callback: () => void): void--><!--Device-avSession-function on(type: 'sessionServiceDie', callback: () => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'sessionServiceDie' | 是 |
| callback | () =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
avSession.on('sessionServiceDie', () => {
  console.info('on sessionServiceDie : session is dead ');
});
```


## on('distributedSessionChange')

```TypeScript
function on(type: 'distributedSessionChange', distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void
```

最新分布式远端会话变更的监听事件。

**起始版本：** 18

<!--Device-avSession-function on(type: 'distributedSessionChange', distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void--><!--Device-avSession-function on(type: 'distributedSessionChange', distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'distributedSessionChange' | 是 |
| distributedSessionType | [DistributedSessionType](arkts-avsession-avsession-distributedsessiontype-e-sys.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;AVSessionController&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
avSession.on('distributedSessionChange', avSession.DistributedSessionType.TYPE_SESSION_REMOTE, (sessionControllers: Array<avSession.AVSessionController>) => {
  console.info(`on distributedSessionChange size: ${sessionControllers.length}`);
});
```


## on('deviceAvailable')

```TypeScript
function on(type: 'deviceAvailable', callback: (device: OutputDeviceInfo) => void): void
```

设备发现回调监听。

**起始版本：** 10

<!--Device-avSession-function on(type: 'deviceAvailable', callback: (device: OutputDeviceInfo) => void): void--><!--Device-avSession-function on(type: 'deviceAvailable', callback: (device: OutputDeviceInfo) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceAvailable' | 是 |
| callback | (device: OutputDeviceInfo) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
let castDevice: avSession.OutputDeviceInfo;
avSession.on('deviceAvailable', (device: avSession.OutputDeviceInfo) => {
  castDevice = device;
  console.info(`on deviceAvailable  : ${device} `);
});
```


## on('deviceOffline')

```TypeScript
function on(type: 'deviceOffline', callback: (deviceId: string) => void): void
```

设备下线回调监听。

**起始版本：** 11

<!--Device-avSession-function on(type: 'deviceOffline', callback: (deviceId: string) => void): void--><!--Device-avSession-function on(type: 'deviceOffline', callback: (deviceId: string) => void): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceOffline' | 是 |
| callback | (deviceId: string) =&gt; void | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
let castDeviceId: string;
avSession.on('deviceOffline', (deviceId: string) => {
  castDeviceId = deviceId;
  console.info(`on deviceOffline  : ${deviceId} `);
});
```


## on('deviceLogEvent')

```TypeScript
function on(type: 'deviceLogEvent', callback: Callback<DeviceLogEventCode>): void
```

监听日志事件的回调。

**起始版本：** 13

<!--Device-avSession-function on(type: 'deviceLogEvent', callback: Callback<DeviceLogEventCode>): void--><!--Device-avSession-function on(type: 'deviceLogEvent', callback: Callback<DeviceLogEventCode>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceLogEvent' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceLogEventCode&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [6600102](../errorcode-avsession.md#6600102-会话不存在) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
avSession.on('deviceLogEvent', (eventCode: avSession.DeviceLogEventCode) => {
  console.info(`on deviceLogEvent code : ${eventCode}`);
});
```


## on('deviceStateChanged')

```TypeScript
function on(type: 'deviceStateChanged', callback: Callback<DeviceState>): void
```

投播设备连接状态的回调函数。

**起始版本：** 20

**需要权限：** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function on(type: 'deviceStateChanged', callback: Callback<DeviceState>): void--><!--Device-avSession-function on(type: 'deviceStateChanged', callback: Callback<DeviceState>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'deviceStateChanged' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
avSession.on('deviceStateChanged', (state: avSession.DeviceState) => {
  console.info(`on deviceStateChanged state, deviceId=${state.deviceId}, connect status=${state.deviceState},
    reasonCode=${state.reasonCode}, radarErrorCode=${state.radarErrorCode}`)
})
```
