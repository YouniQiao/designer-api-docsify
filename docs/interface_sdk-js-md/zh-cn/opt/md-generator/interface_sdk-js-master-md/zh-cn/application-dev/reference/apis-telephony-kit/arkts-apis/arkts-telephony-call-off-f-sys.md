# off（系统接口）

## off('callDetailsChange')

```TypeScript
function off(type: 'callDetailsChange', callback?: Callback<CallAttributeOptions>): void
```

取消订阅callDetailsChange事件。使用callback异步回调。

**起始版本：** 7

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function off(type: 'callDetailsChange', callback?: Callback<CallAttributeOptions>): void--><!--Device-call-function off(type: 'callDetailsChange', callback?: Callback<CallAttributeOptions>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callDetailsChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallAttributeOptions](arkts-telephony-call-callattributeoptions-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
call.off('callDetailsChange', (data: call.CallAttributeOptions) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## off('callEventChange')

```TypeScript
function off(type: 'callEventChange', callback?: Callback<CallEventOptions>): void
```

取消订阅callEventChange事件。使用callback异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function off(type: 'callEventChange', callback?: Callback<CallEventOptions>): void--><!--Device-call-function off(type: 'callEventChange', callback?: Callback<CallEventOptions>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callEventChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallEventOptions](arkts-telephony-call-calleventoptions-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
call.off('callEventChange', (data: call.CallEventOptions) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## off('callDisconnectedCause')

```TypeScript
function off(type: 'callDisconnectedCause', callback?: Callback<DisconnectedDetails>): void
```

取消订阅callDisconnectedCause事件。使用callback异步回调。

**起始版本：** 8

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function off(type: 'callDisconnectedCause', callback?: Callback<DisconnectedDetails>): void--><!--Device-call-function off(type: 'callDisconnectedCause', callback?: Callback<DisconnectedDetails>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callDisconnectedCause' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DisconnectedDetails](arkts-telephony-call-disconnecteddetails-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
call.off('callDisconnectedCause', (data: call.DisconnectedDetails) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## off('mmiCodeResult')

```TypeScript
function off(type: 'mmiCodeResult', callback?: Callback<MmiCodeResults>): void
```

取消订阅mmiCodeResult事件。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function off(type: 'mmiCodeResult', callback?: Callback<MmiCodeResults>): void--><!--Device-call-function off(type: 'mmiCodeResult', callback?: Callback<MmiCodeResults>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'mmiCodeResult' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[MmiCodeResults](arkts-telephony-call-mmicoderesults-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
call.off('mmiCodeResult', (data: call.MmiCodeResults) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## off('audioDeviceChange')

```TypeScript
function off(type: 'audioDeviceChange', callback?: Callback<AudioDeviceCallbackInfo>): void
```

取消订阅audioDeviceChange事件。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function off(type: 'audioDeviceChange', callback?: Callback<AudioDeviceCallbackInfo>): void--><!--Device-call-function off(type: 'audioDeviceChange', callback?: Callback<AudioDeviceCallbackInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'audioDeviceChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AudioDeviceCallbackInfo](arkts-telephony-call-audiodevicecallbackinfo-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
call.off('audioDeviceChange', (data: call.AudioDeviceCallbackInfo) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## off('postDialDelay')

```TypeScript
function off(type: 'postDialDelay', callback?: Callback<string>): void
```

取消订阅拨号后延迟事件。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function off(type: 'postDialDelay', callback?: Callback<string>): void--><!--Device-call-function off(type: 'postDialDelay', callback?: Callback<string>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'postDialDelay' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
call.off('postDialDelay', (data: string) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## off('imsCallModeChange')

```TypeScript
function off(type: 'imsCallModeChange', callback?: Callback<ImsCallModeInfo>): void
```

取消订阅imsCallModeChange事件。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function off(type: 'imsCallModeChange', callback?: Callback<ImsCallModeInfo>): void--><!--Device-call-function off(type: 'imsCallModeChange', callback?: Callback<ImsCallModeInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'imsCallModeChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ImsCallModeInfo](arkts-telephony-call-imscallmodeinfo-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.off('imsCallModeChange', (data: call.ImsCallModeInfo) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## off('callSessionEvent')

```TypeScript
function off(type: 'callSessionEvent', callback?: Callback<CallSessionEvent>): void
```

取消订阅callSessionEvent事件。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function off(type: 'callSessionEvent', callback?: Callback<CallSessionEvent>): void--><!--Device-call-function off(type: 'callSessionEvent', callback?: Callback<CallSessionEvent>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callSessionEvent' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallSessionEvent](arkts-telephony-call-callsessionevent-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.off('callSessionEvent', (data: call.CallSessionEvent) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## off('peerDimensionsChange')

```TypeScript
function off(type: 'peerDimensionsChange', callback?: Callback<PeerDimensionsDetail>): void
```

取消订阅peerDimensionsChange事件。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function off(type: 'peerDimensionsChange', callback?: Callback<PeerDimensionsDetail>): void--><!--Device-call-function off(type: 'peerDimensionsChange', callback?: Callback<PeerDimensionsDetail>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'peerDimensionsChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[PeerDimensionsDetail](arkts-telephony-call-peerdimensionsdetail-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

call.off('peerDimensionsChange', (data: call.PeerDimensionsDetail) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```


## off('cameraCapabilitiesChange')

```TypeScript
function off(type: 'cameraCapabilitiesChange', callback?: Callback<CameraCapabilities>): void
```

取消订阅cameraCapabilitiesChange事件。使用callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function off(type: 'cameraCapabilitiesChange', callback?: Callback<CameraCapabilities>): void--><!--Device-call-function off(type: 'cameraCapabilitiesChange', callback?: Callback<CameraCapabilities>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cameraCapabilitiesChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CameraCapabilities](arkts-telephony-call-cameracapabilities-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
call.off('cameraCapabilitiesChange', (data: call.CameraCapabilities) => {
    console.info(`callback: data->${JSON.stringify(data)}`);
});
```
