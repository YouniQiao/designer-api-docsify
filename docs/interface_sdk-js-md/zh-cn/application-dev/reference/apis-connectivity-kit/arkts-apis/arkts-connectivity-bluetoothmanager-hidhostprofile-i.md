# HidHostProfile

Manager hid host profile.

**继承/实现关系：** HidHostProfile extends [BaseProfile](arkts-connectivity-bluetoothmanager-baseprofile-i.md)

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.hid/hid.HidHostProfile

<!--Device-bluetoothManager-interface HidHostProfile extends BaseProfile--><!--Device-bluetoothManager-interface HidHostProfile extends BaseProfile-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

## 导入模块

```TypeScript
import { bluetoothManager } from 'kits/@kit.ConnectivityKit';
```

## off('connectionStateChange')

```TypeScript
off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void
```

Unsubscribe the event reported when the profile connection state changes.On API 10 and above, the permission required by this interface is changed to ACCESS_BLUETOOTH.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.hid/hid.HidHostProfile.off#event:connectionStateChange

**需要权限：** 
- API版本10+：ohos.permission.ACCESS_BLUETOOTH

<!--Device-HidHostProfile-off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void--><!--Device-HidHostProfile-off(type: 'connectionStateChange', callback?: Callback<StateChangeParam>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'connectionStateChange' | 是 | Type of the profile connection state changes event to listen for. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StateChangeParam&gt; | 否 | Callback used to listen for event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

## on('connectionStateChange')

```TypeScript
on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void
```

Subscribe the event reported when the profile connection state changes.On API 10 and above, the permission required by this interface is changed to ACCESS_BLUETOOTH.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 10

**替代接口：** ohos.bluetooth.hid/hid.HidHostProfile.on#event:connectionStateChange

**需要权限：** 
- API版本10+：ohos.permission.ACCESS_BLUETOOTH

<!--Device-HidHostProfile-on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void--><!--Device-HidHostProfile-on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'connectionStateChange' | 是 | Type of the profile connection state changes event to listen for . |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;StateChangeParam&gt; | 是 | Callback used to listen for event. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

