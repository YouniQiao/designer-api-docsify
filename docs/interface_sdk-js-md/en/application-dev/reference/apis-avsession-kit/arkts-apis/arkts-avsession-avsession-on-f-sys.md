# on (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## on('sessionCreate')

```TypeScript
function on(type: 'sessionCreate', callback: (session: AVSessionDescriptor) => void): void
```

会话的创建事件监听。 使用callback异步回调。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-avSession-function on(type: 'sessionCreate', callback: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function on(type: 'sessionCreate', callback: (session: AVSessionDescriptor) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionCreate' | Yes | 事件回调类型，支持的事件是'sessionCreate'：会话创建事件，检测到会话创建时触发。 |
| callback | (session: AVSessionDescriptor) =&gt; void | Yes | 回调函数。参数为会话相关描述。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 202 | Not System App. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-avSession-function on(type: 'sessionDestroy', callback: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function on(type: 'sessionDestroy', callback: (session: AVSessionDescriptor) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionDestroy' | Yes | 事件回调类型，支持的事件是`'sessionDestroy'`：会话销毁事件，检测到会话销毁时触发。 |
| callback | (session: AVSessionDescriptor) =&gt; void | Yes | 回调函数。参数为会话相关描述。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 202 | Not System App. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-avSession-function on(type: 'topSessionChange', callback: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function on(type: 'topSessionChange', callback: (session: AVSessionDescriptor) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'topSessionChange' | Yes | 事件回调类型，支持的事件是 `'topSessionChange'`：最新播放会话的变化事件，检测到最新的会话改变时触发。 |
| callback | (session: AVSessionDescriptor) =&gt; void | Yes | 回调函数。参数为会话相关描述。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 202 | Not System App. |

## Examples

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

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-avSession-function on(type: 'sessionServiceDie', callback: () => void): void--><!--Device-avSession-function on(type: 'sessionServiceDie', callback: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionServiceDie' | Yes | 事件回调类型，支持事件`'sessionServiceDie'`：会话服务死亡事件，检测到会话的服务死亡时触发。 |
| callback | () =&gt; void | Yes | 回调函数。当监听事件注册成功，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.on('sessionServiceDie', () => {
  console.info('on sessionServiceDie  : session is  Died ');
});
```


## on('distributedSessionChange')

```TypeScript
function on(type: 'distributedSessionChange', distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void
```

最新分布式远端会话变更的监听事件。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-avSession-function on(type: 'distributedSessionChange', distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void--><!--Device-avSession-function on(type: 'distributedSessionChange', distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'distributedSessionChange' | Yes | 事件回调类型，支持的事件为 `'distributedSessionChange'`：最新远端分布式会话的变化事件，检测到最新的会话改变时触 发。 |
| distributedSessionType | [DistributedSessionType](arkts-avsession-avsession-distributedsessiontype-e-sys.md) | Yes | 远端会话类型。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;AVSessionController&gt;&gt; | Yes | 回调函数。参数为对应类型的会话控制器实例列表，可查看会话ID，并完成对会话发送命令及事件，获取元数据、播放状态信 息等操作。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |
| 202 | Not System App. |

## Examples

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

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-avSession-function on(type: 'deviceAvailable', callback: (device: OutputDeviceInfo) => void): void--><!--Device-avSession-function on(type: 'deviceAvailable', callback: (device: OutputDeviceInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceAvailable' | Yes | 事件回调类型，支持事件`'deviceAvailable'`，有设备被发现时触发回调。 |
| callback | (device: OutputDeviceInfo) =&gt; void | Yes | 回调函数。当监听事件注册成功，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 202 | Not System App. |

## Examples

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

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-avSession-function on(type: 'deviceOffline', callback: (deviceId: string) => void): void--><!--Device-avSession-function on(type: 'deviceOffline', callback: (deviceId: string) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceOffline' | Yes | 事件回调类型，支持事件`'deviceOffline'`，有设备下线时触发回调。 |
| callback | (deviceId: string) =&gt; void | Yes | 回调函数，参数deviceId是设备的ID。当监听事件注册成功，err为undefined，否则返回错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 202 | Not System App. |

## Examples

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

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

<!--Device-avSession-function on(type: 'deviceLogEvent', callback: Callback<DeviceLogEventCode>): void--><!--Device-avSession-function on(type: 'deviceLogEvent', callback: Callback<DeviceLogEventCode>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceLogEvent' | Yes | 事件回调类型，支持事件`'deviceLogEvent'`。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceLogEventCode&gt; | Yes | 回调函数，参数DeviceLogEventCode是当前设备日志返回值。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 202 | Not System App. |

## Examples

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

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function on(type: 'deviceStateChanged', callback: Callback<DeviceState>): void--><!--Device-avSession-function on(type: 'deviceStateChanged', callback: Callback<DeviceState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceStateChanged' | Yes | 事件回调类型，支持事件`'deviceStateChanged'`，投播设备连接状态发生变化时触发回调。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceState&gt; | Yes | 回调函数，参数DeviceState包含投播设备ID、连接状态码、连接错误码和系统雷达错误码。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.on('deviceStateChanged', (state: avSession.DeviceState) => {
  console.info(`on deviceStateChanged state, deviceId=${state.deviceId}, connect status=${state.deviceState},
    reasonCode=${state.reasonCode}, radarErrorCode=${state.radarErrorCode}`)
})
```

