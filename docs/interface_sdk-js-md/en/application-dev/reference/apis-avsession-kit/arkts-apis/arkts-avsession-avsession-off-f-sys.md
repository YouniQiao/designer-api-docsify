# off (System API)

## Modules to Import

```TypeScript
import { avSession } from 'kits/@kit.AVSessionKit';
```

## off('sessionCreate')

```TypeScript
function off(type: 'sessionCreate', callback?: (session: AVSessionDescriptor) => void): void
```

注销会话创建事件监听。注销后，不再接收该事件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-avSession-function off(type: 'sessionCreate', callback?: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function off(type: 'sessionCreate', callback?: (session: AVSessionDescriptor) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionCreate' | Yes | 事件回调类型，支持的事件为：`'sessionCreate'`。 |
| callback | (session: AVSessionDescriptor) =&gt; void | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 &lt;br&gt;该参数为会话相关描述，为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

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
            });
            avSession.off('sessionCreate');
          })
      }
    .width('100%')
    .height('100%')
  }
}
```


## off('sessionDestroy')

```TypeScript
function off(type: 'sessionDestroy', callback?: (session: AVSessionDescriptor) => void): void
```

注销会话销毁事件监听。注销后，不再监听该事件。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-avSession-function off(type: 'sessionDestroy', callback?: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function off(type: 'sessionDestroy', callback?: (session: AVSessionDescriptor) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionDestroy' | Yes | 事件回调类型，支持的事件为`'sessionDestroy'`。 |
| callback | (session: AVSessionDescriptor) =&gt; void | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 &lt;br&gt;该参数为会话相关描述，为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

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
            });
            avSession.off('sessionDestroy');
          })
      }
    .width('100%')
    .height('100%')
  }
}
```


## off('topSessionChange')

```TypeScript
function off(type: 'topSessionChange', callback?: (session: AVSessionDescriptor) => void): void
```

注销最新播放会话变更事件监听。注销后，不再进行该事件的监听。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-avSession-function off(type: 'topSessionChange', callback?: (session: AVSessionDescriptor) => void): void--><!--Device-avSession-function off(type: 'topSessionChange', callback?: (session: AVSessionDescriptor) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'topSessionChange' | Yes | 事件回调类型，支持的事件为`'topSessionChange'`。 |
| callback | (session: AVSessionDescriptor) =&gt; void | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 &lt;br&gt;该参数为会话相关描述，为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。 |

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
            });
            avSession.off('topSessionChange');
          })
      }
    .width('100%')
    .height('100%')
  }
}
```


## off('sessionServiceDie')

```TypeScript
function off(type: 'sessionServiceDie', callback?: () => void): void
```

取消会话服务死亡监听，取消后，不再进行服务死亡监听。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-avSession-function off(type: 'sessionServiceDie', callback?: () => void): void--><!--Device-avSession-function off(type: 'sessionServiceDie', callback?: () => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sessionServiceDie' | Yes | 事件回调类型，支持事件`'sessionServiceDie'`：会话服务死亡事件。 |
| callback | () =&gt; void | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。 &lt;br&gt;该参数为可选参数，若不填写该参数，则认为取消所有相关会话的服务死亡监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 6600101 | Session service exception. |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.off('sessionServiceDie');
```


## off('distributedSessionChange')

```TypeScript
function off(type: 'distributedSessionChange', distributedSessionType: DistributedSessionType, callback?: Callback<Array<AVSessionController>>): void
```

取消最新分布式远端会话变更的监听事件，取消后，不再进行该事件的监听。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-avSession-function off(type: 'distributedSessionChange', distributedSessionType: DistributedSessionType, callback?: Callback<Array<AVSessionController>>): void--><!--Device-avSession-function off(type: 'distributedSessionChange', distributedSessionType: DistributedSessionType, callback?: Callback<Array<AVSessionController>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'distributedSessionChange' | Yes | 事件回调类型，支持的事件为`'distributedSessionChange'`。 |
| distributedSessionType | [DistributedSessionType](arkts-avsession-avsession-distributedsessiontype-e-sys.md) | Yes | 远端会话类型。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;AVSessionController&gt;&gt; | No | 回调函数。参数为对应类型的会话控制器实例列表，可查看会话ID，并完成对会话发送命令及事件，获取元数据、播放状态信 息等操作。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 6600101 | Session service exception. |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.off('distributedSessionChange', avSession.DistributedSessionType.TYPE_SESSION_REMOTE);
```


## off('deviceAvailable')

```TypeScript
function off(type: 'deviceAvailable', callback?: (device: OutputDeviceInfo) => void): void
```

取消设备发现回调的监听。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-avSession-function off(type: 'deviceAvailable', callback?: (device: OutputDeviceInfo) => void): void--><!--Device-avSession-function off(type: 'deviceAvailable', callback?: (device: OutputDeviceInfo) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceAvailable' | Yes | 事件回调类型，支持事件`'deviceAvailable'`：设备发现回调。 |
| callback | (device: OutputDeviceInfo) =&gt; void | No | 用于返回设备信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.off('deviceAvailable');
```


## off('deviceOffline')

```TypeScript
function off(type: 'deviceOffline', callback?: (deviceId: string) => void): void
```

取消设备下线回调的监听。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-avSession-function off(type: 'deviceOffline', callback?: (deviceId: string) => void): void--><!--Device-avSession-function off(type: 'deviceOffline', callback?: (deviceId: string) => void): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceOffline' | Yes | 事件回调类型，支持事件`'deviceOffline'`：设备下线回调。 |
| callback | (deviceId: string) =&gt; void | No | 回调函数，参数deviceId是设备的ID。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的 事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.off('deviceOffline');
```


## off('deviceLogEvent')

```TypeScript
function off(type: 'deviceLogEvent', callback?: Callback<DeviceLogEventCode>): void
```

取消监听日志事件的回调。

**Since:** 13

**ArkTS mode:** ArkTS-Dyn only, since version 13.

<!--Device-avSession-function off(type: 'deviceLogEvent', callback?: Callback<DeviceLogEventCode>): void--><!--Device-avSession-function off(type: 'deviceLogEvent', callback?: Callback<DeviceLogEventCode>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceLogEvent' | Yes | 取消对应的监听事件，支持事件`'deviceLogEvent'`。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceLogEventCode&gt; | No | 回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关 会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 6600101 | Session service exception. |
| 6600102 | The session does not exist. |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.off('deviceLogEvent');
```


## off('deviceStateChanged')

```TypeScript
function off(type: 'deviceStateChanged', callback?: Callback<DeviceState>): void
```

取消投播设备连接状态的监听。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.MANAGE_MEDIA_RESOURCES

<!--Device-avSession-function off(type: 'deviceStateChanged', callback?: Callback<DeviceState>): void--><!--Device-avSession-function off(type: 'deviceStateChanged', callback?: Callback<DeviceState>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deviceStateChanged' | Yes | 取消对应的监听事件，支持事件`'deviceStateChanged'`，投播设备连接状态变化的回调。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DeviceState&gt; | No | 回调函数，当监听事件取消成功时，err为undefined；否则返回错误对象。该参数为可选参数，若未填写，则取消所有相关会话的事件监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not System App. |

## Examples

```TypeScript
avSession.off('deviceStateChanged');
```

